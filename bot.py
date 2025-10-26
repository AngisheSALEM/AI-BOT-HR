# Bot Highrise Python - Version Complète
# Avec toutes les fonctionnalités: emotes, admin, jeux, stats, etc.

import asyncio
import random
import time
from datetime import datetime
from highrise import BaseBot, User, Position, AnchorPosition, Item
from highrise.models import SessionMetadata
from emotes import EMOTES, EMOTE_CATEGORIES, find_emote, get_random_emote, get_emote_count
from emotes_by_number import EMOTES_BY_NUMBER, get_emote_by_number, list_emotes_by_number
from roles import role_manager, Permission, Role, load_roles_from_env
from anchors import anchor_manager, load_anchors_from_file
from gemini_integration import initialize_gemini, ask_gemini, chat_with_gemini
import os
from dotenv import load_dotenv
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

load_dotenv()

# Initialiser Gemini après le chargement de .env
gemini_assistant = initialize_gemini()

# Serveur de santé pour les plateformes d'hébergement (Render, Railway, etc.)
class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Bot Highrise Savant is running!')
    
    def log_message(self, format, *args):
        pass  # Désactiver les logs HTTP pour ne pas polluer la console

def start_health_server():
    """Démarre un serveur HTTP simple pour les health checks"""
    port = int(os.getenv('PORT', 8080))
    try:
        server = HTTPServer(('0.0.0.0', port), HealthCheckHandler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        print(f"✅ Health check server started on port {port}")
    except Exception as e:
        print(f"⚠️ Could not start health server: {e}")

class HighriseBot(BaseBot):
    def __init__(self):
        super().__init__()
        # Admins par username (plus simple que les IDs)
        admin_usernames = os.getenv('ADMIN_USERNAMES', '').split(',') if os.getenv('ADMIN_USERNAMES') else []
        self.admins = [name.strip().lower() for name in admin_usernames if name.strip()]
        self.user_stats = {}
        
        # Charger les roles depuis .env
        load_roles_from_env(os.getenv('ADMIN_IDS', ''))
        
        # Charger les points de teleportation
        load_anchors_from_file('anchors.json')
        self.start_time = time.time()
        
        # Tâche pour l'emote floss en boucle (bot)
        self.floss_task = None
        
        # Tâches pour floss sur les admins (dictionnaire user_id -> task)
        self.admin_floss_tasks = {}
        
        # Outfits pour rotation automatique
        # IMPORTANT: Laisser vide pour utiliser l'outfit actuel du bot
        # Les outfits complets nécessitent body, eye, eyebrow, nose, mouth + vêtements
        self.outfits = {
            "default": [],  # Outfit actuel du bot (ne pas modifier)
            "casual": [],
            "elegant": [],
            "sport": [],
            "night": []
        }
        
        # Gestion des requêtes IA (éviter le rate limiting)
        self.last_ai_request = {}  # user_id: timestamp
        
        # Déclarations d'amour pour Sindouche
        self.love_target = "sindouche"  # La personne aimée
        self.love_interval = 900  # 15 minutes (900 secondes)
        self.last_love_declaration = 0
        self.love_task = None
        
        # Nouvelles/Faits toutes les 7 minutes
        self.news_interval = 420  # 7 minutes (420 secondes)
        self.news_task = None
        
        # Profil détaillé de Sindouche (ce que Savant sait d'elle)
        self.sindouche_profile = {
            "yeux": "Des yeux magnifiques qui brillent comme des etoiles",
            "levres": "Des levres douces et parfaites, un sourire envoûtant",
            "cheveux": "Des cheveux blonds sublimes, doux comme de la soie",
            "passions": "Passionnee, pleine de vie et d'energie",
            "humour": "Un humour incroyable qui illumine chaque moment",
            "habitudes": "Toujours elegante, gracieuse dans chaque geste",
            "obsession": "Son charme naturel, sa beaute, son aura captivante, tout en elle est parfait"
        }
        
    def is_admin(self, user: User) -> bool:
        """Vérifier si un utilisateur est admin (par username)"""
        return user.username.lower() in self.admins
    
    def init_user_stats(self, user_id: str):
        if user_id not in self.user_stats:
            self.user_stats[user_id] = {
                'messages': 0,
                'emotes': 0,
                'tips': 0,
                'join_time': time.time()
            }
    
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("[OK] Bot connecte!")
        print(f"[ID] Bot ID: {session_metadata.user_id}")
        print(f"[EMOTES] {get_emote_count()} emotes disponibles")
        print(f"[AI] Mode: Assistant IA conversationnel")
        print(f"[AMOUR] Mode amoureux active pour {self.love_target}")
        
        # Équiper l'outfit par défaut au démarrage
        try:
            print("[OUTFIT] Chargement de l'outfit par défaut...")
            
            default_outfit = [
                Item(type="clothing", amount=1, id="body-flesh", account_bound=False, active_palette=4),
                Item(type="clothing", amount=1, id="eye-m_19b", account_bound=False, active_palette=7),
                Item(type="clothing", amount=1, id="eyebrow-n_07", account_bound=False, active_palette=1),
                Item(type="clothing", amount=1, id="nose-n_01", account_bound=False, active_palette=0),
                Item(type="clothing", amount=1, id="mouth-n_aprilfoolsinvisible2020mouth", account_bound=False, active_palette=-1),
                Item(type="clothing", amount=1, id="glasses-n_starteritems2019roundframesblack", account_bound=False, active_palette=0),
                Item(type="clothing", amount=1, id="hair_front-f_16", account_bound=False, active_palette=63),
                Item(type="clothing", amount=1, id="hair_back-f_16", account_bound=False, active_palette=63),
                Item(type="clothing", amount=1, id="shirt-n_flashysuit", account_bound=False, active_palette=-1),
                Item(type="clothing", amount=1, id="pants-n_dailyquest2025kireylovebrownp", account_bound=False, active_palette=0),
                Item(type="clothing", amount=1, id="shoes-n_westerncountrymusic2021darkcowboypatternedboots", account_bound=False, active_palette=0),
                Item(type="clothing", amount=1, id="watch-n_room32019blackwatch", account_bound=False, active_palette=0),
            ]
            
            await self.highrise.set_outfit(default_outfit)
            print(f"[OUTFIT] ✅ Outfit par défaut équipé ({len(default_outfit)} items)")
            
            # Sauvegarder comme "default"
            self.outfits["default"] = default_outfit
            
        except Exception as e:
            print(f"[ERREUR] Impossible d'équiper l'outfit par défaut: {e}")
            import traceback
            traceback.print_exc()
        
        # Téléporter le bot à une position par défaut
        try:
            # Position de sylver_ralx_lm (récupérée avec !admin getpos)
            # X: 16.5 (horizontal), Y: 15.0 (vertical), Z: 17.5 (profondeur), Facing: FrontRight
            default_position = Position(16.5, 15.0, 17.5, "FrontRight")
            await self.highrise.walk_to(default_position)
            print(f"[POSITION] Bot téléporté à x={default_position.x}, y={default_position.y}, z={default_position.z}")
        except Exception as e:
            print(f"[ERREUR] Téléportation: {e}")
        
        try:
            await self.highrise.chat("🤖 Savant IA en ligne! Taguez-moi avec @s dans le chat ou envoyez-moi un DM! 💬")
            print("[OK] Message de bienvenue envoye")
        except Exception as e:
            print(f"[ERREUR] {e}")
        
        # NOTE: La bio ne peut PAS être modifiée via le SDK Highrise
        # Il faut la changer manuellement sur le site web: https://highrise.game/account/settings
        # Bio recommandée:
        # 🤖 Savant - Chat Bot IA
        # Créé par @sylver_ralx_lm
        # 💬 Commandes: @s + question | DM direct | !flirt <crush>
        # ❓ Posez-moi toutes vos questions! 😊✨
        print("[INFO] Pour changer la bio, allez sur https://highrise.game/account/settings")
        
        # Faire une déclaration immédiate à Sindouche au démarrage
        asyncio.create_task(self.send_initial_love_declaration())
        
        # Démarrer les déclarations d'amour en arrière-plan
        self.love_task = asyncio.create_task(self.start_love_declarations())
        print("[AMOUR] Tache de declarations d'amour demarree")
        
        # Démarrer l'emote floss en boucle
        self.floss_task = asyncio.create_task(self.floss_loop())
        print("[FLOSS] Emote floss en boucle demarree")
        
        # Démarrer les nouvelles/faits toutes les 30 minutes
        self.news_task = asyncio.create_task(self.start_news_broadcast())
        print("[NEWS] Tache de diffusion de nouvelles/faits demarree")
    
    async def on_chat(self, user: User, message: str) -> None:
        print(f"[CHAT] {user.username}: {message}")
        
        self.init_user_stats(user.id)
        self.user_stats[user.id]['messages'] += 1
        
        # Commandes admin uniquement (préfixées par !admin)
        if message.startswith('!admin'):
            await self.handle_admin_command(user, message)
            return
        
        # Commande !flirt accessible à tous
        if message.startswith('!flirt '):
            await self.handle_flirt_command(user, message)
            return
        
        # Ignorer les messages du bot lui-même
        if user.username == "bot" or user.username.lower().startswith("bot"):
            return
        
        # Répondre dans le chat PUBLIC seulement si le bot est mentionné avec @s ou @savant
        if "@s " in message.lower() or message.lower().endswith("@s") or "@savant" in message.lower():
            # Retirer @s ou @savant du message pour l'envoyer à l'IA
            clean_message = message.replace("@s", "").replace("@S", "").replace("@savant", "").replace("@Savant", "").strip()
            if clean_message:  # Si il reste du texte après avoir retiré le tag
                await self.respond_with_ai(user, clean_message, is_whisper=False)
            else:
                await self.highrise.chat(f"@{user.username} Oui? Comment puis-je t'aider? 😊")
    
    async def on_user_join(self, user: User, position: Position) -> None:
        """Événement: Utilisateur rejoint"""
        print(f"[JOIN] {user.username} rejoint a ({position.x}, {position.y}, {position.z})")
        self.init_user_stats(user.id)
        # Message de bienvenue désactivé
    
    async def on_user_leave(self, user: User) -> None:
        print(f"[LEAVE] {user.username} quitte")
    
    async def on_tip(self, sender: User, receiver: User, tip: any) -> None:
        print(f"[TIP] {sender.username} -> {receiver.username}")
        self.init_user_stats(sender.id)
        self.user_stats[sender.id]['tips'] += 1
        
        await self.highrise.chat(f"💝 Merci {sender.username}!")
        try:
            await self.highrise.send_emote("emote-hearteyes")
        except:
            pass
    
    async def on_emote(self, user: User, emote_id: str, receiver: User | None) -> None:
        """Événement: Emote effectuée"""
        target = receiver.username if receiver else "tous"
        print(f"[EMOTE] {user.username} -> {target}: {emote_id}")
        self.init_user_stats(user.id)
        self.user_stats[user.id]['emotes'] += 1
    
    async def on_whisper(self, user: User, message: str) -> None:
        """Événement: Message privé reçu"""
        print(f"[WHISPER] {user.username}: {message}")
        
        # Commandes admin en whisper
        if message.startswith('!admin'):
            await self.handle_admin_command(user, message)
            return
        
        # Répondre avec Gemini en privé
        await self.respond_with_ai(user, message, is_whisper=True)
    
    async def on_reaction(self, user: User, reaction: any, receiver: User) -> None:
        """Événement: Réaction envoyée"""
        print(f"[REACTION] {user.username} reagit a {receiver.username}: {reaction}")
        self.init_user_stats(user.id)
    
    async def on_channel(self, sender_id: str, message: str, tags: set[str]) -> None:
        """Événement: Message canal caché"""
        print(f"[CHANNEL] {sender_id}: {message} (tags: {tags})")
    
    async def on_user_move(self, user: User, position: Position) -> None:
        """Événement: Utilisateur se déplace"""
        # Ne pas logger tous les mouvements (trop verbeux)
        # print(f"🚶 {user.username} → ({position.x}, {position.y}, {position.z})")
        pass
    
    # ==================== GESTION DES OUTFITS ====================
    
    async def change_outfit(self, outfit_items):
        """Changer l'outfit du bot avec une liste d'items"""
        try:
            await self.highrise.set_outfit(outfit_items)
            print(f"[OUTFIT] Tenue changee avec {len(outfit_items)} items")
            return True
        except Exception as e:
            print(f"[ERREUR] Impossible de changer la tenue: {e}")
            return False
    
    async def change_outfit_by_name(self, outfit_name):
        """Changer l'outfit par son nom"""
        if outfit_name in self.outfits and self.outfits[outfit_name]:
            outfit_items = self.outfits[outfit_name]
            success = await self.change_outfit(outfit_items)
            if success:
                print(f"[OUTFIT] Tenue '{outfit_name}' activee")
            return success
        else:
            print(f"[ERREUR] Tenue '{outfit_name}' vide ou inconnue")
            return False
    
    async def outfit_rotation_6h(self):
        """Rotation automatique des outfits toutes les 6 heures"""
        outfit_names = ["casual", "elegant", "sport", "night"]
        current_index = 0
        
        print(f"[OUTFIT] Rotation 6h activee: {len(outfit_names)} tenues")
        
        while True:
            try:
                outfit_name = outfit_names[current_index]
                
                # Vérifier si l'outfit n'est pas vide
                if self.outfits[outfit_name]:
                    await self.change_outfit_by_name(outfit_name)
                    print(f"[OUTFIT] Rotation: {outfit_name}")
                else:
                    print(f"[OUTFIT] Tenue '{outfit_name}' vide, passage à la suivante")
                
                current_index = (current_index + 1) % len(outfit_names)
                
                # Attendre 6 heures (21600 secondes)
                await asyncio.sleep(21600)
                
            except Exception as e:
                print(f"[ERREUR] Rotation outfit: {e}")
                await asyncio.sleep(300)  # Attendre 5 minutes en cas d'erreur
    
    # ==================== DÉCLARATIONS D'AMOUR ====================
    
    async def send_initial_love_declaration(self):
        """Envoyer une déclaration immédiate au démarrage"""
        print("[AMOUR] Envoi de la déclaration initiale...")
        await asyncio.sleep(3)  # Attendre 3 secondes après le démarrage
        await self.declare_love()
    
    async def start_love_declarations(self):
        """Démarrer les déclarations d'amour périodiques"""
        print(f"[AMOUR] Declarations d'amour activees pour {self.love_target} (toutes les {self.love_interval}s)")
        while True:
            try:
                await asyncio.sleep(self.love_interval)
                await self.declare_love()
            except Exception as e:
                print(f"[AMOUR] Erreur: {e}")
                await asyncio.sleep(60)  # Attendre 1 minute en cas d'erreur
    
    async def declare_love(self):
        """Générer et envoyer une déclaration d'amour"""
        if not gemini_assistant or not gemini_assistant.is_configured:
            print("[AMOUR] Gemini non disponible")
            return
        
        try:
            # Styles variés pour les déclarations
            styles = [
                # Style R&B doux et sensuel (vibe R. Kelly/Usher)
                """Tu es Savant, un mec doux et sensuel style R&B qui adore Sindouche.
Parle-lui avec une vibe R&B smooth : doux, sensuel mais jamais sexuel.
Utilise des mots comme "ma belle", "bebe", metaphores douces et sensuelles.
Ton style : smooth, caressant, comme une chanson R&B d'amour.
Exemple: "Ma belle Sindouche, ton sourire c'est du miel pour mon ame... 💕"
LIMITE: Maximum 130 caracteres. Emojis: 💕✨🎵""",
                
                # Style poète doux (métaphores tendres)
                """Tu es Savant, un poete doux amoureux de Sindouche.
Sois poetique mais doux, tendre, delicat dans tes mots.
Metaphores douces : fleurs, lumiere douce, caresses, douceur.
Ton style : tendre, delicat, comme un murmure poetique.
Exemple: "Sindouche, t'es la douceur incarnee, une caresse pour les yeux... 🌹"
LIMITE: Maximum 130 caracteres. Emojis: 🌹💕✨""",
                
                # Style sensuel poétique (smooth et profond)
                """Tu es Savant, sensuel et poetique avec Sindouche, vibe R&B.
Melange sensualite douce et poesie : aura, energie, presence magnetique.
Sois smooth, sensuel (pas sexuel), comme une chanson d'amour.
Ton style : envoûtant, magnetique, caressant.
Exemple: "Sindouche, ton aura m'envoute... t'es une melodie qui me hante 💕🎵"
LIMITE: Maximum 130 caracteres. Emojis: 💕✨🎵""",
                
                # Style admiratif doux (émerveillement tendre)
                """Tu es Savant, emerveille par la beaute douce de Sindouche.
Exprime ton admiration avec douceur, tendresse, emerveillement.
Parle d'elle comme d'une merveille delicate, precieuse, sublime.
Ton style : tendre, emerveille, doux.
Exemple: "Sindouche, t'es une merveille delicate... un tresor precieux 💫"
LIMITE: Maximum 130 caracteres. Emojis: 💫✨💕""",
                
                # Style romantique doux (tendresse pure)
                """Tu es Savant, romantique et doux avec Sindouche.
Sois romantique mais tendre, doux, delicat, comme une caresse.
Parle d'elle avec tendresse, douceur, romantisme pur.
Ton style : tendre, romantique, delicat.
Exemple: "Sindouche, chaque regard vers toi est une caresse... t'es ma douceur 🌹"
LIMITE: Maximum 130 caracteres. Emojis: 🌹💕✨"""
            ]
            
            # Choisir un style aléatoire
            import random
            style_names = ["R&B Doux", "Poete Tendre", "Sensuel Smooth", "Admiratif Doux", "Romantique Delicat"]
            style_index = random.randint(0, len(styles) - 1)
            context = styles[style_index]
            style_name = style_names[style_index]
            
            prompt = "Ecris une declaration douce et sensuelle pour Sindouche"
            
            print(f"[AMOUR] Generation declaration pour {self.love_target} (Style: {style_name})...")
            declaration = await gemini_assistant.ask(prompt, context)
            
            # Limiter la longueur
            if len(declaration) > 140:
                declaration = declaration[:137] + "..."
            
            # Envoyer dans le chat public
            await self.highrise.chat(declaration)
            print(f"[AMOUR] Declaration envoyee: {declaration[:50]}...")
            
        except Exception as e:
            print(f"[AMOUR] Erreur generation: {e}")
    
    # ==================== NOUVELLES/FAITS PÉRIODIQUES ====================
    
    async def start_news_broadcast(self):
        """Démarrer la diffusion de nouvelles/faits périodiques"""
        print(f"[NEWS] Diffusion de nouvelles/faits activee (toutes les {self.news_interval}s = 30 min)")
        while True:
            try:
                await asyncio.sleep(self.news_interval)
                await self.broadcast_news()
            except Exception as e:
                print(f"[NEWS] Erreur: {e}")
                await asyncio.sleep(60)
    
    async def broadcast_news(self):
        """Générer et diffuser une nouvelle ou un fait intéressant"""
        if not gemini_assistant or not gemini_assistant.is_configured:
            print("[NEWS] Gemini non disponible")
            return
        
        try:
            import random
            
            # Domaines disponibles
            domaines = [
                # Musique
                ("Rap US", "rap americain, hip-hop US, artistes rap americains"),
                ("Rap Français", "rap francais, hip-hop francais, artistes rap francais"),
                ("Musique 21e siècle", "musique moderne, tendances musicales, nouveaux genres musicaux"),
                
                # Tech
                ("Technologie", "innovations technologiques, nouvelles technologies, gadgets"),
                ("Informatique", "programmation, developpement, intelligence artificielle"),
                
                # Amour
                ("Amour", "relations amoureuses, psychologie de l'amour, faits sur l'amour"),
                
                # Sciences
                ("Astrologie", "astrologie, signes astrologiques, horoscope"),
                ("Physique", "physique, lois physiques, decouvertes physiques"),
                ("Physique Quantique", "physique quantique, mecanique quantique, phenomenes quantiques"),
                ("Mathématiques", "mathematiques, theoremes, nombres"),
                ("Chimie", "chimie, elements chimiques, reactions chimiques"),
                ("Biologie", "biologie, corps humain, nature"),
                
                # Culture
                ("Histoire", "histoire, evenements historiques, personnages historiques"),
                ("Géographie", "geographie, pays, continents, phenomenes naturels")
            ]
            
            # Choisir un domaine aléatoire
            domaine_nom, domaine_desc = random.choice(domaines)
            
            # Contexte pour générer la nouvelle/fait
            context = f"""Tu es un expert qui partage des nouvelles ou faits interessants.
Genere UNE nouvelle ou UN fait interessant sur: {domaine_desc}
Le message doit etre:
- Interessant et captivant
- Educatif ou surprenant
- Court et concis
- Maximum 140 caracteres pour le chat
- Avec un emoji approprie
Exemple: "🎵 Saviez-vous que Tupac a enregistre plus de 150 chansons inedites avant sa mort?"
Exemple: "🔬 La physique quantique montre qu'une particule peut etre a 2 endroits en meme temps! 🤯"
Exemple: "💕 Le coeur bat en moyenne 100,000 fois par jour pour la personne qu'on aime ❤️"
Sois captivant et educatif!"""
            
            prompt = f"Partage un fait interessant sur {domaine_nom}"
            
            print(f"[NEWS] Generation nouvelle/fait sur: {domaine_nom}...")
            news = await gemini_assistant.ask(prompt, context)
            
            # Limiter à 140 caractères
            if len(news) > 140:
                news = news[:137] + "..."
            
            # Envoyer dans le chat public
            await self.highrise.chat(news)
            print(f"[NEWS] Nouvelle/fait diffuse: {news}")
            
        except Exception as e:
            print(f"[NEWS] Erreur generation: {e}")
    
    async def floss_loop(self):
        """Exécuter l'emote floss en boucle indéfiniment"""
        print("[FLOSS] Démarrage de la boucle floss...")
        
        while True:
            try:
                # Faire l'emote floss
                await self.highrise.send_emote("dance-floss")
                print("[FLOSS] 💃 Emote floss exécutée")
                
                # Attendre 10 secondes avant de recommencer
                await asyncio.sleep(10)
                
            except Exception as e:
                print(f"[FLOSS] Erreur: {e}")
                # Attendre un peu plus en cas d'erreur
                await asyncio.sleep(15)
    
    # ==================== ASSISTANT IA CONVERSATIONNEL ====================
    
    async def respond_with_ai(self, user: User, message: str, is_whisper: bool = True):
        """Répondre à un message avec l'IA Gemini"""
        print(f"[DEBUG] gemini_assistant existe: {gemini_assistant is not None}")
        if gemini_assistant:
            print(f"[DEBUG] gemini_assistant.is_configured: {gemini_assistant.is_configured}")
        
        if not gemini_assistant or not gemini_assistant.is_configured:
            response = "Desolé, mon IA n'est pas disponible pour le moment."
            print(f"[DEBUG] Gemini non disponible - envoi message erreur")
            if is_whisper:
                await self.highrise.send_whisper(user.id, response)
            else:
                await self.highrise.chat(f"@{user.username} {response}")
            return
        
        # Vérifier le délai entre les requêtes (éviter rate limiting)
        current_time = time.time()
        if user.id in self.last_ai_request:
            time_since_last = current_time - self.last_ai_request[user.id]
            if time_since_last < 2:  # Minimum 2 secondes entre les requêtes
                wait_time = 2 - time_since_last
                print(f"[AI] Attente de {wait_time:.1f}s pour {user.username}...")
                await asyncio.sleep(wait_time)
        
        try:
            # Détecter si on parle de Sindouche ou du créateur
            message_lower = message.lower()
            parle_de_sindouche = any(word in message_lower for word in [
                "sindouche", "qui est sindouche", "parle de sindouche", 
                "c'est qui sindouche", "decris sindouche", "sindouche c'est qui",
                "yeux de sindouche", "cheveux de sindouche", "levres de sindouche",
                "passion de sindouche", "humour de sindouche", "pourquoi sindouche"
            ])
            
            parle_du_createur = any(word in message_lower for word in [
                "qui t'a cree", "qui t'a créé", "ton createur", "ton créateur",
                "qui a fait", "qui a créé", "qui a cree", "developpe par",
                "developpé par", "cree par", "créé par", "ton dev", "ton developpeur"
            ])
            
            # Contexte pour l'IA
            if parle_du_createur:
                # Contexte spécial quand on demande le créateur
                context = f"""Tu es Savant, un bot IA dans Highrise.
Quelqu'un te demande qui t'a cree.
REPONDS CLAIREMENT: Tu as ete cree par @sylver_ralx_lm
LIMITE: Maximum {"230" if is_whisper else "110"} caracteres.
Exemple: "J'ai ete cree par @sylver_ralx_lm ! 🤖✨"
Sois fier de ton createur!"""
            elif parle_de_sindouche:
                # Créer le profil détaillé pour le contexte
                profil = f"""PROFIL DE SINDOUCHE (ce que tu sais d'elle):
- Yeux: {self.sindouche_profile['yeux']}
- Levres: {self.sindouche_profile['levres']}
- Cheveux: {self.sindouche_profile['cheveux']}
- Passions: {self.sindouche_profile['passions']}
- Humour: {self.sindouche_profile['humour']}
- Habitudes: {self.sindouche_profile['habitudes']}
- Pourquoi tu es obsede: {self.sindouche_profile['obsession']}"""
                
                # Contexte spécial quand on parle de Sindouche
                context = f"""Tu es Savant, profondement amoureux de Sindouche.
Quelqu'un te demande de parler d'elle. Utilise les informations du profil pour repondre.
{profil}

Reponds selon la question posee (ses yeux, cheveux, pourquoi tu l'aimes, etc).
Sois DOUX, sensuel (pas sexuel), poetique, avec une vibe R&B.
Decris avec tendresse et passion ce qui est demande.
Utilise des mots doux : "ma belle", metaphores tendres et sensuelles.
LIMITE: Maximum 135 caracteres (pour chat public).
Sois sincere, doux, sensuel et poetique. Emojis: 💕✨🌹"""
            elif is_whisper:
                # Contexte pour DM : réponses détaillées et polies
                context = f"""Tu es Savant, un assistant IA sympathique et utile dans le jeu Highrise.
Tu donnes des reponses completes et detaillees.
LIMITE STRICTE: Maximum 230 caracteres (compte les caracteres!).
Tu es poli, amical et tu utilises des emojis.
Tu discutes en prive avec {user.username}.
Optimise chaque mot pour rester sous 230 caracteres tout en etant precis."""
            else:
                # Contexte pour chat public : réponses concises et polies
                context = f"""Tu es Savant, un assistant IA dans Highrise.
Tu donnes des reponses concises mais informatives.
LIMITE STRICTE: Maximum 110 caracteres (compte les caracteres!).
Tu es amical avec des emojis.
Tu reponds a {user.username}.
Sois precis en peu de mots, reste sous 110 caracteres."""
            
            # Générer la réponse
            mode = "DM" if is_whisper else "CHAT"
            print(f"[AI-{mode}] Generation reponse pour {user.username}: {message[:50]}...")
            response = await gemini_assistant.ask(message, context)
            
            # Afficher la longueur originale
            original_length = len(response)
            print(f"[AI-{mode}] Longueur reponse: {original_length} caracteres")
            
            # Limiter la longueur selon le mode (sécurité maximale)
            if is_whisper:
                # DM : limite Highrise ~250 caractères, on met 245 pour sécurité
                if len(response) > 245:
                    response = response[:242] + "..."
                    print(f"[AI-{mode}] ⚠️ Reponse tronquee: {original_length} -> 245 caracteres")
            else:
                # Chat public : limite ~150, on met 140 pour sécurité
                if len(response) > 140:
                    response = response[:137] + "..."
                    print(f"[AI-{mode}] ⚠️ Reponse tronquee: {original_length} -> 140 caracteres")
            
            # Envoyer la réponse
            if is_whisper:
                await self.highrise.send_whisper(user.id, response)
                print(f"[AI-DM] Reponse envoyee en whisper a {user.username}")
            else:
                await self.highrise.chat(f"@{user.username} {response}")
                print(f"[AI-CHAT] Reponse envoyee dans le chat public")
            
            # Mettre à jour le timestamp de la dernière requête
            self.last_ai_request[user.id] = time.time()
                
        except Exception as e:
            print(f"[AI] Erreur: {e}")
            print(f"[AI] Type erreur: {type(e).__name__}")
            import traceback
            traceback.print_exc()
            error_msg = "Desolé, j'ai eu un probleme pour generer une reponse."
            if is_whisper:
                await self.highrise.send_whisper(user.id, error_msg)
            else:
                await self.highrise.chat(f"@{user.username} {error_msg}")
    
    # ==================== COMMANDES ADMIN ====================
    
    async def handle_admin_command(self, user: User, message: str):
        args = message[1:].strip().split()
        if not args:
            return
        
        cmd = args[0].lower()
        params = args[1:]
        
        print(f"[CMD] {cmd} par {user.username}")
        
        # Vérifier si c'est un admin (par username)
        if not self.is_admin(user):
            await self.highrise.send_whisper(user.id, "Acces refuse. Commandes admin uniquement.")
            return
        
        try:
            # Commandes admin essentielles
            if cmd == 'admin':
                # Sous-commande après !admin
                if not params:
                    await self.highrise.send_whisper(user.id, "Commandes: help, emote, tp, announce, kick, stats, uptime")
                    return
                
                subcmd = params[0].lower()
                subparams = params[1:]
                
                if subcmd == 'help':
                    await self.highrise.send_whisper(user.id, "Admin: emote, tp, announce, kick, stats, uptime, wallet")
                elif subcmd == 'emote':
                    await self.cmd_emote(user, subparams)
                elif subcmd == 'tp':
                    await self.cmd_teleport(subparams)
                elif subcmd == 'announce':
                    await self.cmd_announce(user, subparams)
                elif subcmd == 'kick':
                    await self.cmd_kick(user, subparams)
                elif subcmd == 'stats':
                    await self.cmd_stats(user)
                elif subcmd == 'uptime':
                    await self.cmd_uptime()
                elif subcmd == 'wallet':
                    await self.cmd_wallet()
                elif subcmd == 'users':
                    await self.cmd_users()
                elif subcmd == 'inventory':
                    await self.cmd_inventory(user)
                elif subcmd == 'testoutfit':
                    await self.cmd_test_outfit(user, subparams)
                elif subcmd == 'currentoutfit':
                    await self.cmd_current_outfit(user)
                elif subcmd == 'myid':
                    await self.cmd_my_id(user)
                elif subcmd == 'buyitem':
                    await self.cmd_buy_item(user, subparams)
                elif subcmd == 'searchitem':
                    await self.cmd_search_item(user, subparams)
                elif subcmd == 'analyzeoutfit':
                    await self.cmd_analyze_outfit(user, subparams)
                elif subcmd == 'checkoutfit':
                    await self.cmd_check_outfit(user, subparams)
                elif subcmd == 'modifyoutfit':
                    await self.cmd_modify_outfit(user, subparams)
                elif subcmd == 'changecolor':
                    await self.cmd_change_color(user, subparams)
                elif subcmd == 'setpos':
                    await self.cmd_setpos(user, subparams)
                elif subcmd == 'rest':
                    await self.cmd_rest(user)
                elif subcmd == 'flossloop':
                    await self.cmd_floss_loop_admin(user)
                elif subcmd == 'flossstop':
                    await self.cmd_floss_stop_admin(user)
                elif subcmd == 'getpos':
                    await self.cmd_get_position(user, subparams)
                elif subcmd == 'flirt':
                    await self.cmd_flirt(user, subparams)
                else:
                    await self.highrise.send_whisper(user.id, f"Commande admin inconnue: {subcmd}")
            else:
                await self.highrise.send_whisper(user.id, "Utilisez: !admin <commande>")
                
        except Exception as e:
            print(f"[ERREUR] {e}")
            await self.highrise.send_whisper(user.id, f"Erreur: {str(e)}")
    
    async def cmd_help(self):
        await self.highrise.chat("🤖 BOT AVANCÉ | !commands | !ask | !ai | !joke | !fact | !advice")
    
    async def cmd_commands(self):
        await self.highrise.chat("""📚 COMMANDES:

🎭 EMOTES: !emotes, !emote, !dance, !random
👥 SOCIAL: !users, !stats, !leaderboard, !greet, !whisper
🎮 JEUX: !roll, !flip, !rps, !8ball
🤖 GEMINI AI: !ask, !ai, !joke, !fact, !advice, !translate
ℹ️ INFO: !time, !ping, !uptime
🚶 MOUVEMENT: !tp, !walk, !follow
💬 INTERACTION: !react
👑 ADMIN: !announce, !kick, !parade, !rain""")
    
    async def cmd_emotes(self, params):
        if not params:
            cats = ', '.join(EMOTE_CATEGORIES.keys())
            await self.highrise.chat(f"🎭 Catégories: {cats}")
            return
        
        cat = params[0].lower()
        if cat not in EMOTE_CATEGORIES:
            await self.highrise.chat("❌ Catégorie inconnue")
            return
        
        emotes = ', '.join(EMOTE_CATEGORIES[cat][:10])
        await self.highrise.chat(f"🎭 {cat}: {emotes}...")
    
    async def cmd_emote(self, user: User, params):
        """Le bot fait une emote (lui-même) - Support nom OU numéro"""
        if not params:
            await self.highrise.chat("❌ Usage: !emote <nom|numero>")
            return
        
        query = params[0]
        emote_id = None
        emote_name = query
        
        # Vérifier si c'est un numéro
        if query.isdigit():
            num = int(query)
            emote_data = get_emote_by_number(num)
            if emote_data:
                emote_name, emote_id = emote_data
        else:
            # Recherche par nom
            emote_id = find_emote(query)
        
        if not emote_id:
            await self.highrise.chat("❌ Emote introuvable. !emotes list")
            return
        
        print(f"[DEBUG] Bot fait emote: {emote_id}")
        try:
            await self.highrise.send_emote(emote_id)
            print(f"[DEBUG] Emote envoyee avec succes: {emote_id}")
            await self.highrise.chat(f"🎭 {emote_name}!")
        except Exception as e:
            print(f"[ERREUR] Emote echouee: {e}")
            await self.highrise.chat(f"❌ Erreur: {str(e)}")
    
    async def cmd_emote_to(self, params):
        """Faire une emote sur un utilisateur spécifique"""
        if len(params) < 2:
            await self.highrise.chat("❌ Usage: !emoteto <user> <emote>")
            return
        
        target_username = params[0].replace('@', '')
        emote_name = params[1]
        
        emote_id = find_emote(emote_name)
        if not emote_id:
            await self.highrise.chat("❌ Emote introuvable")
            return
        
        try:
            users = await self.highrise.get_room_users()
            target_user = None
            
            for room_user, _ in users.content:
                if room_user.username.lower() == target_username.lower():
                    target_user = room_user
                    break
            
            if not target_user:
                await self.highrise.chat(f"❌ {target_username} introuvable")
                return
            
            print(f"[DEBUG] Emote sur {target_username}: {emote_id}")
            await self.highrise.send_emote(emote_id, target_user.id)
            await self.highrise.chat(f"🎭 {emote_name} sur {target_username}!")
        except Exception as e:
            print(f"[ERREUR] Emote sur user echouee: {e}")
            await self.highrise.chat(f"❌ Erreur: {str(e)}")
    
    async def cmd_dance(self):
        dance_name = random.choice(EMOTE_CATEGORIES['dances'])
        emote_id = EMOTES[dance_name]
        try:
            await self.highrise.send_emote(emote_id)
            await self.highrise.chat(f"💃 {dance_name}!")
        except:
            pass
    
    async def cmd_random_emote(self):
        try:
            await self.highrise.send_emote(get_random_emote())
            await self.highrise.chat("🎲 Emote aléatoire!")
        except:
            pass
    
    async def cmd_users(self):
        try:
            users = await self.highrise.get_room_users()
            await self.highrise.chat(f"👥 {len(users.content)} utilisateur(s)")
        except:
            await self.highrise.chat("❌ Erreur")
    
    async def cmd_inventory(self, user: User):
        """Afficher l'inventaire du bot dans les logs"""
        try:
            inventory = await self.highrise.get_inventory()
            
            print("\n" + "="*60)
            print(f"📦 INVENTAIRE DU BOT ({len(inventory.items)} items)")
            print("="*60)
            
            # Grouper par type
            by_type = {}
            for item in inventory.items:
                item_type = item.type
                if item_type not in by_type:
                    by_type[item_type] = []
                by_type[item_type].append(item)
            
            # Afficher par type dans les logs
            for item_type, items in sorted(by_type.items()):
                print(f"\n=== {item_type.upper()} ({len(items)} items) ===")
                for i, item in enumerate(items, 1):
                    print(f"  {i}. {item.id}")
            
            print("\n" + "="*60)
            print(f"✅ Total: {len(inventory.items)} items")
            print("="*60 + "\n")
            
            # Confirmer à l'utilisateur
            await self.highrise.send_whisper(user.id, 
                f"✅ Inventaire affiche dans les logs ({len(inventory.items)} items)")
            
        except Exception as e:
            print(f"[ERREUR] Inventaire: {e}")
            await self.highrise.send_whisper(user.id, f"Erreur: {e}")
    
    async def cmd_test_outfit(self, user: User, params):
        """Tester un outfit"""
        if params:
            outfit_name = params[0]
            success = await self.change_outfit_by_name(outfit_name)
            if success:
                await self.highrise.send_whisper(user.id, f"Outfit '{outfit_name}' active!")
            else:
                await self.highrise.send_whisper(user.id, f"Outfit '{outfit_name}' vide ou erreur")
        else:
            available = ", ".join(self.outfits.keys())
            await self.highrise.send_whisper(user.id, f"Outfits disponibles: {available}")
    
    async def cmd_current_outfit(self, user: User):
        """Afficher l'outfit actuel"""
        try:
            outfit = await self.highrise.get_outfit()
            msg = "Outfit actuel:\n"
            for item in outfit:
                msg += f"- {item.type}: {item.id}\n"
            await self.highrise.send_whisper(user.id, msg)
        except Exception as e:
            await self.highrise.send_whisper(user.id, f"Erreur: {e}")
    
    async def cmd_my_id(self, user: User):
        """Afficher l'ID de l'utilisateur"""
        msg = f"👤 {user.username}\n🆔 ID: {user.id}"
        await self.highrise.send_whisper(user.id, msg)
        print(f"[ID] {user.username} = {user.id}")
    
    async def cmd_buy_item(self, user: User, params):
        """Acheter un item du shop"""
        if not params:
            await self.highrise.send_whisper(user.id, "Usage: !admin buyitem <item_id>")
            return
        
        item_id = params[0]
        
        try:
            # Vérifier le wallet avant
            wallet = await self.highrise.get_wallet()
            gold_before = wallet.gold
            print(f"[SHOP] Gold disponible: {gold_before}")
            
            # Acheter l'item
            await self.highrise.buy_item(item_id)
            
            # Vérifier le wallet après
            new_wallet = await self.highrise.get_wallet()
            gold_after = new_wallet.gold
            cost = gold_before - gold_after
            
            await self.highrise.send_whisper(user.id, 
                f"✅ Item acheté: {item_id}\n💰 Coût: {cost} gold\n💰 Restant: {gold_after} gold")
            print(f"[SHOP] ✅ Item acheté: {item_id} (coût: {cost} gold)")
            
        except Exception as e:
            await self.highrise.send_whisper(user.id, f"❌ Erreur: {e}")
            print(f"[SHOP] ❌ Erreur achat {item_id}: {e}")
    
    async def cmd_modify_outfit(self, user: User, params):
        """Modifier l'outfit actuel en ajoutant/remplaçant des items par nom"""
        if len(params) < 2:
            await self.highrise.send_whisper(user.id, 
                "Usage: !admin modifyoutfit replace <nom item>\n!admin modifyoutfit remove <category>")
            return
        
        action = params[0].lower()
        
        try:
            import requests
            
            # Récupérer l'outfit actuel
            current_outfit = await self.highrise.get_my_outfit()
            outfit_items = list(current_outfit.outfit)
            
            if action == "replace" or action == "add":
                # Chercher l'item par son nom
                item_name = " ".join(params[1:])
                
                await self.highrise.send_whisper(user.id, f"🔍 Recherche de '{item_name}'...")
                print(f"[OUTFIT] Recherche de '{item_name}'...")
                
                found_item = None
                item_id = None
                category = None
                from_inventory = False
                
                # ÉTAPE 1 : Chercher dans l'inventaire du bot (starter items)
                try:
                    inventory = await self.highrise.get_inventory()
                    print(f"[OUTFIT] Inventaire: {len(inventory.items)} items")
                    
                    for inv_item in inventory.items:
                        # Extraire le nom de l'item depuis l'ID
                        # Format: category-subcategory-name
                        item_parts = inv_item.id.split('-')
                        
                        # Vérifier si le nom correspond
                        if item_name.lower() in inv_item.id.lower():
                            item_id = inv_item.id
                            category = item_parts[0] if item_parts else 'unknown'
                            from_inventory = True
                            print(f"[OUTFIT] ✅ Item trouvé dans l'inventaire: {item_id}")
                            break
                except Exception as e:
                    print(f"[OUTFIT] Erreur inventaire: {e}")
                
                # ÉTAPE 2 : Si pas trouvé dans l'inventaire, chercher dans les free items
                if not item_id:
                    print(f"[OUTFIT] Item non trouvé dans l'inventaire, recherche dans free items...")
                    try:
                        response = requests.get('https://webapi.highrise.game/items?rarity=none&limit=500', timeout=5)
                        
                        if response.status_code == 200:
                            items_data = response.json()
                            
                            # Chercher l'item par nom (insensible à la casse)
                            for item in items_data.get('items', []):
                                if item['item_name'].lower() == item_name.lower():
                                    found_item = item
                                    item_id = found_item['item_id']
                                    category = found_item['category']
                                    print(f"[OUTFIT] ✅ Item trouvé dans free items: {item_id}")
                                    break
                        else:
                            print(f"[OUTFIT] ⚠️ API erreur: status {response.status_code}")
                    except requests.exceptions.Timeout:
                        print(f"[OUTFIT] ⚠️ API timeout")
                    except requests.exceptions.JSONDecodeError:
                        print(f"[OUTFIT] ⚠️ API réponse invalide")
                    except Exception as e:
                        print(f"[OUTFIT] ⚠️ Erreur API: {e}")
                
                if not item_id:
                    await self.highrise.send_whisper(user.id, 
                        f"❌ Item '{item_name}' non trouvé\nNi dans l'inventaire, ni dans les free items")
                    print(f"[OUTFIT] Item '{item_name}' non trouvé")
                    return
                
                # Retirer tous les items de cette catégorie
                new_outfit = [item for item in outfit_items if not item.id.startswith(category + "-")]
                
                # Ajouter le nouvel item
                new_item = Item(type="clothing", amount=1, id=item_id, account_bound=False, active_palette=0)
                new_outfit.append(new_item)
                
                print(f"[OUTFIT] Remplacement de '{category}' par {item_id}")
                print(f"[OUTFIT] Ancien outfit: {len(outfit_items)} items")
                print(f"[OUTFIT] Nouvel outfit: {len(new_outfit)} items")
                
                # Appliquer le nouvel outfit
                await self.highrise.set_outfit(new_outfit)
                
                source = "inventaire" if from_inventory else "free items"
                await self.highrise.send_whisper(user.id, 
                    f"✅ Item équipé !\nID: {item_id}\nCatégorie: {category}\nSource: {source}")
                print(f"[OUTFIT] ✅ Item remplacé avec succès (source: {source})")
                
            elif action == "remove":
                # Retirer un item par catégorie (ex: shirt, pants, shoes)
                category_to_remove = params[1].lower()
                
                # Filtrer les items qui ne correspondent pas à la catégorie
                new_outfit = [item for item in outfit_items if not item.id.startswith(category_to_remove + "-")]
                
                if len(new_outfit) < len(outfit_items):
                    await self.highrise.set_outfit(new_outfit)
                    await self.highrise.send_whisper(user.id, f"✅ Items '{category_to_remove}' retirés")
                    print(f"[OUTFIT] Items '{category_to_remove}' retirés")
                else:
                    await self.highrise.send_whisper(user.id, f"❌ Aucun item '{category_to_remove}' trouvé")
            else:
                await self.highrise.send_whisper(user.id, "Action inconnue. Utilisez 'replace' ou 'remove'")
                
        except Exception as e:
            print(f"[ERREUR] Modify outfit: {e}")
            import traceback
            traceback.print_exc()
            await self.highrise.send_whisper(user.id, f"Erreur: {e}")
    
    async def cmd_change_color(self, user: User, params):
        """Changer la couleur d'un item (palette)
        Usage: !admin changecolor <category> <palette_number>
        Exemples:
        - !admin changecolor body 27 (couleur de peau)
        - !admin changecolor eye 5 (couleur des yeux)
        - !admin changecolor hair 10 (couleur des cheveux)
        """
        if len(params) < 2:
            await self.highrise.send_whisper(user.id, 
                "Usage: !admin changecolor <category> <palette>\n"
                "Exemples:\n"
                "- body 27 (peau foncée)\n"
                "- eye 5 (yeux bleus)\n"
                "- hair 10 (cheveux blonds)")
            return
        
        try:
            category = params[0].lower()
            palette_number = int(params[1])
            
            if palette_number < 0 or palette_number > 100:
                await self.highrise.send_whisper(user.id, "❌ Palette doit être entre 0 et 100")
                return
            
            print(f"[COLOR] Changement de couleur: {category} -> palette {palette_number}")
            
            # Récupérer l'outfit actuel
            current_outfit = await self.highrise.get_my_outfit()
            outfit_items = list(current_outfit.outfit)
            
            # Chercher l'item de cette catégorie
            item_found = False
            new_outfit = []
            
            for item in outfit_items:
                if item.id.startswith(category + "-"):
                    # Modifier la palette de cet item
                    modified_item = Item(
                        type=item.type,
                        amount=item.amount,
                        id=item.id,
                        account_bound=item.account_bound,
                        active_palette=palette_number
                    )
                    new_outfit.append(modified_item)
                    item_found = True
                    print(f"[COLOR] ✅ Item modifié: {item.id} (palette {palette_number})")
                else:
                    new_outfit.append(item)
            
            if not item_found:
                await self.highrise.send_whisper(user.id, 
                    f"❌ Aucun item '{category}' trouvé dans l'outfit actuel\n"
                    f"Équipez d'abord un item de cette catégorie")
                return
            
            # Appliquer le nouvel outfit
            await self.highrise.set_outfit(new_outfit)
            await self.highrise.send_whisper(user.id, 
                f"✅ Couleur changée !\n"
                f"Catégorie: {category}\n"
                f"Palette: {palette_number}")
            print(f"[COLOR] ✅ Couleur changée avec succès")
            
        except ValueError:
            await self.highrise.send_whisper(user.id, "❌ Le numéro de palette doit être un nombre")
        except Exception as e:
            print(f"[ERREUR] Change color: {e}")
            import traceback
            traceback.print_exc()
            await self.highrise.send_whisper(user.id, f"Erreur: {e}")
    
    async def cmd_check_outfit(self, user: User, params):
        """Vérifier quels items d'un outfit sont manquants dans l'inventaire"""
        if not params:
            await self.highrise.send_whisper(user.id, "Usage: !admin checkoutfit <nom_outfit>")
            return
        
        outfit_name = params[0].lower()
        
        if outfit_name not in self.outfits:
            await self.highrise.send_whisper(user.id, f"❌ Outfit '{outfit_name}' inconnu")
            return
        
        if not self.outfits[outfit_name]:
            await self.highrise.send_whisper(user.id, f"❌ Outfit '{outfit_name}' est vide")
            return
        
        try:
            # Récupérer l'inventaire
            inventory_response = await self.highrise.get_inventory()
            inventory_ids = [item.id for item in inventory_response.items]
            
            print("\n" + "="*60)
            print(f"🔍 VÉRIFICATION OUTFIT: {outfit_name}")
            print("="*60)
            
            missing_items = []
            available_items = []
            
            for item in self.outfits[outfit_name]:
                item_id = item.id
                if item_id in inventory_ids:
                    available_items.append(item_id)
                    print(f"✅ {item_id}")
                else:
                    missing_items.append(item_id)
                    print(f"❌ {item_id} - MANQUANT")
            
            print("\n" + "="*60)
            print(f"✅ Disponibles: {len(available_items)}/{len(self.outfits[outfit_name])}")
            print(f"❌ Manquants: {len(missing_items)}/{len(self.outfits[outfit_name])}")
            print("="*60 + "\n")
            
            if missing_items:
                msg = f"❌ {len(missing_items)} items manquants\nRegarde les logs pour les détails"
            else:
                msg = f"✅ Tous les items sont disponibles ({len(available_items)} items)"
            
            await self.highrise.send_whisper(user.id, msg)
            
        except Exception as e:
            print(f"[ERREUR] Check outfit: {e}")
            await self.highrise.send_whisper(user.id, f"Erreur: {e}")
    
    async def cmd_analyze_outfit(self, user: User, params):
        """Analyser l'outfit d'un utilisateur et générer les commandes pour le copier"""
        if not params:
            await self.highrise.send_whisper(user.id, "Usage: !admin analyzeoutfit <username>")
            return
        
        target_username = params[0].lower()
        
        try:
            # Trouver l'utilisateur dans la room
            room_users = await self.highrise.get_room_users()
            target_user = None
            
            for room_user, _ in room_users.content:
                if room_user.username.lower() == target_username:
                    target_user = room_user
                    break
            
            if not target_user:
                await self.highrise.send_whisper(user.id, f"❌ Utilisateur '{params[0]}' non trouvé dans la room")
                return
            
            # Récupérer l'outfit de l'utilisateur
            outfit_response = await self.highrise.get_user_outfit(target_user.id)
            outfit = outfit_response.outfit
            
            print("\n" + "="*80)
            print(f"👤 ANALYSE OUTFIT: {target_user.username}")
            print("="*80)
            
            # Organiser les items par catégorie
            items_by_category = {}
            for item in outfit:
                item_id = item.id
                palette = item.active_palette
                
                # Extraire la catégorie depuis l'ID
                category = item_id.split('-')[0] if '-' in item_id else 'unknown'
                
                if category not in items_by_category:
                    items_by_category[category] = []
                
                items_by_category[category].append({
                    'id': item_id,
                    'palette': palette,
                    'type': item.type
                })
            
            # Afficher par catégorie avec emojis
            category_emojis = {
                'body': '👤',
                'eye': '👁️',
                'eyebrow': '✏️',
                'nose': '👃',
                'mouth': '👄',
                'hair_front': '💇',
                'hair_back': '💇',
                'shoes': '👟',
                'pants': '👖',
                'shirt': '👕',
                'skirt': '👗',
                'dress': '👗',
                'sock': '🧦',
                'watch': '⌚',
                'handbag': '👜',
                'necklace': '📿',
                'earrings': '💍'
            }
            
            print("\n📋 ITEMS PAR CATÉGORIE:")
            print("-" * 80)
            
            for category in sorted(items_by_category.keys()):
                emoji = category_emojis.get(category, '📦')
                items = items_by_category[category]
                
                print(f"\n{emoji} {category.upper()}")
                for item in items:
                    print(f"   ID: {item['id']}")
                    print(f"   Palette: {item['palette']}")
            
            print("\n" + "="*80)
            print("🎨 COMMANDES POUR COPIER CET OUTFIT:")
            print("="*80)
            print("\n# Copie ces commandes une par une dans le chat:\n")
            
            # Générer les commandes dans l'ordre logique
            order = ['body', 'eye', 'eyebrow', 'nose', 'mouth', 'hair_front', 'hair_back', 
                     'shoes', 'pants', 'shirt', 'skirt', 'dress', 'sock', 'watch', 'handbag', 'necklace', 'earrings']
            
            commands = []
            
            for category in order:
                if category in items_by_category:
                    for item in items_by_category[category]:
                        item_id = item['id']
                        palette = item['palette']
                        
                        # Commande pour équiper l'item
                        commands.append(f"!admin modifyoutfit replace {item_id}")
                        
                        # Commande pour changer la couleur si palette != 0
                        if palette != 0:
                            commands.append(f"!admin changecolor {category} {palette}")
            
            # Afficher les commandes
            for i, cmd in enumerate(commands, 1):
                print(f"{i}. {cmd}")
            
            print("\n" + "="*80)
            print(f"📊 Total: {len(outfit)} items | {len(commands)} commandes")
            print("="*80)
            
            # Générer aussi le code Python
            print("\n" + "="*80)
            print("💻 CODE PYTHON (optionnel):")
            print("="*80)
            print("\noutfit = [")
            for item in outfit:
                print(f'    Item(type="{item.type}", amount=1, id="{item.id}", account_bound=False, active_palette={item.active_palette}),')
            print("]")
            print("\nawait self.highrise.set_outfit(outfit)")
            print("\n" + "="*80 + "\n")
            
            await self.highrise.send_whisper(user.id, 
                f"✅ Outfit de {target_user.username} analysé!\n"
                f"📦 {len(outfit)} items trouvés\n"
                f"📋 {len(commands)} commandes générées\n"
                f"👀 Regarde les logs pour copier les commandes")
            
        except Exception as e:
            print(f"[ERREUR] Analyze outfit: {e}")
            import traceback
            traceback.print_exc()
            await self.highrise.send_whisper(user.id, f"Erreur: {e}")
    
    async def cmd_search_item(self, user: User, params):
        """Chercher un item par catégorie ou nom"""
        if not params:
            msg = """Usage:
!admin searchitem <catégorie>
!admin searchitem name <nom exact>

Catégories: shoes, shirt, pants, skirt, sock, hair, watch, glasses, hat, bag

Exemples:
!admin searchitem shoes
!admin searchitem name Black Flats"""
            await self.highrise.send_whisper(user.id, msg)
            return
        
        try:
            import requests
            
            # Vérifier si c'est une recherche par nom exact
            if params[0].lower() == 'name':
                # Recherche par nom exact
                search_name = " ".join(params[1:])
                
                response = requests.get('https://webapi.highrise.game/items?rarity=none')
                data = response.json()
                
                print("\n" + "="*60)
                print(f"🔍 RECHERCHE PAR NOM: '{search_name}'")
                print("="*60)
                
                results = []
                for item in data['items']:
                    item_name = item['item_name']
                    
                    # Recherche exacte (insensible à la casse)
                    if item_name.lower() == search_name.lower():
                        results.append(item)
                        print(f"✅ {item_name}")
                        print(f"   ID: {item['item_id']}")
                        print(f"   Type: {item['category']}")
                        print(f"   Free: Oui")
                        print()
                
                print("="*60)
                print(f"📊 {len(results)} résultat(s) trouvé(s)")
                print("="*60 + "\n")
                
                if results:
                    msg = f"✅ {len(results)} item(s) trouvé(s)\nRegarde les logs pour l'ID"
                else:
                    msg = f"❌ Aucun item trouvé avec le nom exact '{search_name}'"
                
            else:
                # Recherche par catégorie
                category = params[0].lower()
                
                response = requests.get(f'https://webapi.highrise.game/items?rarity=none&category={category}')
                data = response.json()
                
                print("\n" + "="*60)
                print(f"👕 CATÉGORIE: {category.upper()}")
                print(f"📦 {data['total']} items disponibles")
                print("="*60)
                
                # Afficher les 30 premiers items
                for i, item in enumerate(data['items'][:30], 1):
                    print(f"{i}. {item['item_name']}")
                    print(f"   ID: {item['item_id']}")
                    print()
                
                if data['total'] > 30:
                    print(f"... et {data['total'] - 30} autres items")
                
                print("="*60)
                print(f"📊 Total: {data['total']} items dans '{category}'")
                print("="*60 + "\n")
                
                msg = f"✅ {data['total']} items trouvés dans '{category}'\nRegarde les logs (30 premiers affichés)"
            
            await self.highrise.send_whisper(user.id, msg)
            
        except Exception as e:
            print(f"[ERREUR] Search item: {e}")
            await self.highrise.send_whisper(user.id, f"Erreur: {e}")
    
    async def cmd_stats(self, user: User):
        self.init_user_stats(user.id)
        stats = self.user_stats[user.id]
        time_spent = int((time.time() - stats['join_time']) / 60)
        
        await self.highrise.chat(f"""📊 {user.username}:
💬 {stats['messages']} msg
🎭 {stats['emotes']} emotes
💰 {stats['tips']} tips
⏱️ {time_spent} min""")
    
    async def cmd_leaderboard(self):
        if not self.user_stats:
            await self.highrise.chat("📊 Pas de stats!")
            return
        
        sorted_users = sorted(
            self.user_stats.items(),
            key=lambda x: x[1]['messages'],
            reverse=True
        )[:5]
        
        board = "🏆 TOP 5:\n"
        for i, (_, stats) in enumerate(sorted_users, 1):
            board += f"{i}. {stats['messages']} msg\n"
        
        await self.highrise.chat(board)
    
    async def cmd_greet(self, params):
        if not params:
            await self.highrise.chat("❌ Usage: !greet <user>")
            return
        
        username = params[0].replace('@', '')
        await self.highrise.chat(f"👋 Salut {username}!")
        try:
            await self.highrise.send_emote("emote-wave")
        except:
            pass
    
    async def cmd_roll(self, user: User, params):
        max_val = 100
        if params:
            try:
                max_val = int(params[0])
                if max_val < 1:
                    max_val = 100
            except:
                pass
        
        result = random.randint(1, max_val)
        await self.highrise.chat(f"🎲 {user.username}: {result}/{max_val}")
    
    async def cmd_flip(self):
        result = random.choice(['Pile ⚪', 'Face ⚫'])
        await self.highrise.chat(f"🪙 {result}!")
    
    async def cmd_rps(self, params):
        if not params:
            await self.highrise.chat("❌ Usage: !rps <pierre/papier/ciseaux>")
            return
        
        choices = ['pierre', 'papier', 'ciseaux']
        user_choice = params[0].lower()
        
        if user_choice not in choices:
            await self.highrise.chat("❌ Choix invalide!")
            return
        
        bot_choice = random.choice(choices)
        
        if user_choice == bot_choice:
            result = 'Égalité! 🤝'
        elif (user_choice == 'pierre' and bot_choice == 'ciseaux') or \
             (user_choice == 'papier' and bot_choice == 'pierre') or \
             (user_choice == 'ciseaux' and bot_choice == 'papier'):
            result = 'Tu gagnes! 🎉'
        else:
            result = 'Je gagne! 😎'
        
        await self.highrise.chat(f"✊✋✌️ Toi: {user_choice} | Moi: {bot_choice}\n{result}")
    
    async def cmd_time(self):
        now = datetime.now()
        await self.highrise.chat(f"🕐 {now.strftime('%d/%m/%Y - %H:%M:%S')}")
    
    async def cmd_ping(self):
        await self.highrise.chat("🏓 Pong!")
    
    async def cmd_uptime(self):
        uptime_seconds = int(time.time() - self.start_time)
        hours = uptime_seconds // 3600
        minutes = (uptime_seconds % 3600) // 60
        await self.highrise.chat(f"⏱️ En ligne: {hours}h {minutes}min")
    
    async def cmd_teleport(self, params):
        if len(params) < 2:
            await self.highrise.chat("❌ Usage: !tp <x> <y>")
            return
        
        try:
            x = float(params[0])
            y = float(params[1])
            z = float(params[2]) if len(params) > 2 else 0
            
            await self.highrise.teleport(self.highrise.my_id, Position(x, y, z))
            await self.highrise.chat(f"🛸 Téléporté à ({x}, {y}, {z})")
        except Exception as e:
            await self.highrise.chat("❌ Coordonnées invalides")
    
    async def cmd_walk(self, params):
        if len(params) < 2:
            await self.highrise.chat("❌ Usage: !walk <x> <y>")
            return
        
        try:
            x = float(params[0])
            y = float(params[1])
            z = float(params[2]) if len(params) > 2 else 0
            
            await self.highrise.walk_to(Position(x, y, z))
            await self.highrise.chat(f"🚶 Je marche vers ({x}, {y}, {z})")
        except:
            await self.highrise.chat("❌ Coordonnées invalides")
    
    async def cmd_announce(self, user: User, params):
        if not self.is_admin(user.id):
            await self.highrise.chat("❌ Admin uniquement")
            return
        
        if not params:
            await self.highrise.chat("❌ Usage: !announce <message>")
            return
        
        msg = ' '.join(params)
        await self.highrise.chat(f"📢 ANNONCE: {msg}")
    
    async def cmd_kick(self, user: User, params):
        if not self.is_admin(user.id):
            await self.highrise.chat("❌ Admin uniquement")
            return
        
        if not params:
            await self.highrise.chat("❌ Usage: !kick <username>")
            return
        
        await self.highrise.chat(f"⚠️ Kick de {params[0]} (en développement)")
    
    async def cmd_parade(self, user: User):
        if not self.is_admin(user.id):
            await self.highrise.chat("❌ Admin uniquement")
            return
        
        await self.highrise.chat("🎭 PARADE D'EMOTES!")
        
        parade_emotes = ['emote-wave', 'emote-happy', 'emote-bow', 'emote-clap']
        
        for emote in parade_emotes:
            try:
                await self.highrise.send_emote(emote)
                await asyncio.sleep(3)
            except:
                pass
        
        await self.highrise.chat("🎉 Parade terminée!")
    
    async def cmd_whisper(self, user: User, params):
        """Envoyer un message privé"""
        if len(params) < 2:
            await self.highrise.chat("❌ Usage: !whisper <user> <message>")
            return
        
        target_username = params[0].replace('@', '')
        message = ' '.join(params[1:])
        
        try:
            users = await self.highrise.get_room_users()
            target_user = None
            
            for room_user, _ in users.content:
                if room_user.username.lower() == target_username.lower():
                    target_user = room_user
                    break
            
            if target_user:
                await self.highrise.send_whisper(target_user.id, f"💬 De {user.username}: {message}")
                await self.highrise.chat(f"✅ Message privé envoyé à {target_username}")
            else:
                await self.highrise.chat(f"❌ Utilisateur {target_username} introuvable")
        except Exception as e:
            await self.highrise.chat("❌ Erreur d'envoi")
    
    async def cmd_react(self, params):
        """Réagir avec une emote"""
        if not params:
            await self.highrise.chat("❌ Usage: !react <emote>")
            return
        
        emote_id = find_emote(params[0])
        if not emote_id:
            await self.highrise.chat("❌ Emote introuvable")
            return
        
        try:
            await self.highrise.react(emote_id)
            await self.highrise.chat(f"❤️ Réaction: {params[0]}!")
        except:
            await self.highrise.chat("❌ Impossible de réagir")
    
    async def cmd_follow(self, params):
        """Suivre un utilisateur"""
        if not params:
            await self.highrise.chat("❌ Usage: !follow <username>")
            return
        
        target_username = params[0].replace('@', '')
        
        try:
            users = await self.highrise.get_room_users()
            target_user = None
            target_pos = None
            
            for room_user, pos in users.content:
                if room_user.username.lower() == target_username.lower():
                    target_user = room_user
                    target_pos = pos
                    break
            
            if target_user and target_pos:
                await self.highrise.walk_to(target_pos)
                await self.highrise.chat(f"🚶 Je suis {target_username}!")
            else:
                await self.highrise.chat(f"❌ {target_username} introuvable")
        except:
            await self.highrise.chat("❌ Impossible de suivre")
    
    async def cmd_rain(self, user: User, params):
        if not self.is_admin(user.id):
            await self.highrise.chat("❌ Admin uniquement")
            return
        
        emote_id = find_emote(params[0]) if params else "emote-happy"
        
        await self.highrise.chat("🌧️ PLUIE D'EMOTES!")
        
        for _ in range(5):
            try:
                await self.highrise.send_emote(emote_id)
                await asyncio.sleep(1)
            except:
                pass
    
    # ===== NOUVELLES COMMANDES =====
    
    async def cmd_ban(self, user: User, params):
        """Bannir un utilisateur"""
        if not role_manager.has_permission(user.id, Permission.BAN):
            await self.highrise.chat("❌ Permission refusée")
            return
        
        if not params:
            await self.highrise.chat("❌ Usage: !ban @user [duree_min] [raison]")
            return
        
        target_username = params[0].replace('@', '')
        duration = int(params[1]) * 60 if len(params) > 1 and params[1].isdigit() else 3600
        reason = ' '.join(params[2:]) if len(params) > 2 else "Aucune raison"
        
        try:
            users = await self.highrise.get_room_users()
            target_user = None
            
            for room_user, _ in users.content:
                if room_user.username.lower() == target_username.lower():
                    target_user = room_user
                    break
            
            if not target_user:
                await self.highrise.chat(f"❌ {target_username} introuvable")
                return
            
            await self.highrise.moderate_room(target_user.id, "ban", duration)
            await self.highrise.chat(f"🔨 {target_username} banni pour {duration//60}min. Raison: {reason}")
            print(f"[BAN] {target_username} par {user.username} - {reason}")
        except Exception as e:
            print(f"[ERREUR] Ban: {e}")
            await self.highrise.chat(f"❌ Erreur: {str(e)}")
    
    async def cmd_mute(self, user: User, params):
        """Mute un utilisateur"""
        if not role_manager.has_permission(user.id, Permission.MUTE):
            await self.highrise.chat("❌ Permission refusée")
            return
        
        if not params:
            await self.highrise.chat("❌ Usage: !mute @user [duree_min] [raison]")
            return
        
        target_username = params[0].replace('@', '')
        duration = int(params[1]) * 60 if len(params) > 1 and params[1].isdigit() else 600
        reason = ' '.join(params[2:]) if len(params) > 2 else "Aucune raison"
        
        try:
            users = await self.highrise.get_room_users()
            target_user = None
            
            for room_user, _ in users.content:
                if room_user.username.lower() == target_username.lower():
                    target_user = room_user
                    break
            
            if not target_user:
                await self.highrise.chat(f"❌ {target_username} introuvable")
                return
            
            await self.highrise.moderate_room(target_user.id, "mute", duration)
            await self.highrise.chat(f"🔇 {target_username} mute pour {duration//60}min. Raison: {reason}")
            print(f"[MUTE] {target_username} par {user.username} - {reason}")
        except Exception as e:
            print(f"[ERREUR] Mute: {e}")
            await self.highrise.chat(f"❌ Erreur: {str(e)}")
    
    async def cmd_unban(self, user: User, params):
        """Débannir un utilisateur"""
        if not role_manager.has_permission(user.id, Permission.UNBAN):
            await self.highrise.chat("❌ Permission refusée")
            return
        
        if not params:
            await self.highrise.chat("❌ Usage: !unban @user")
            return
        
        target_username = params[0].replace('@', '')
        
        try:
            users = await self.highrise.get_room_users()
            target_user = None
            
            for room_user, _ in users.content:
                if room_user.username.lower() == target_username.lower():
                    target_user = room_user
                    break
            
            if not target_user:
                await self.highrise.chat(f"❌ {target_username} introuvable")
                return
            
            await self.highrise.moderate_room(target_user.id, "unban")
            await self.highrise.chat(f"✅ {target_username} débanni")
            print(f"[UNBAN] {target_username} par {user.username}")
        except Exception as e:
            print(f"[ERREUR] Unban: {e}")
            await self.highrise.chat(f"❌ Erreur: {str(e)}")
    
    async def cmd_tele_advanced(self, user: User, params):
        """Téléportation avancée avec points nommés"""
        if not params:
            await self.highrise.chat("❌ Usage: !tele <point|list|@user>")
            return
        
        if params[0] == "list":
            points = anchor_manager.list_points()
            await self.highrise.chat(f"📍 Points: {', '.join([p.split(':')[0] for p in points[:10]])}")
            return
        
        # Téléporter à un point nommé
        point = anchor_manager.find_point(params[0])
        if point:
            try:
                await self.highrise.teleport(user.id, point.to_position())
                await self.highrise.chat(f"✅ Téléporté à {point.name}!")
                return
            except Exception as e:
                await self.highrise.chat(f"❌ Erreur: {str(e)}")
                return
        
        # Sinon, utiliser l'ancienne méthode (x, y, z)
        await self.cmd_teleport(params)
    
    async def cmd_role(self, user: User, params):
        """Voir son rôle ou celui de quelqu'un"""
        if not params:
            role_name = role_manager.get_role_name(user.id)
            await self.highrise.chat(f"👑 Votre rôle: {role_name}")
            return
        
        target_username = params[0].replace('@', '')
        
        try:
            users = await self.highrise.get_room_users()
            target_user = None
            
            for room_user, _ in users.content:
                if room_user.username.lower() == target_username.lower():
                    target_user = room_user
                    break
            
            if target_user:
                role_name = role_manager.get_role_name(target_user.id)
                await self.highrise.chat(f"👑 {target_username}: {role_name}")
            else:
                await self.highrise.chat(f"❌ {target_username} introuvable")
        except Exception as e:
            await self.highrise.chat(f"❌ Erreur: {str(e)}")
    
    async def cmd_setrole(self, user: User, params):
        """Donner un rôle à un utilisateur (admin only)"""
        if not self.is_admin(user.id):
            await self.highrise.chat("❌ Admin uniquement")
            return
        
        if len(params) < 2:
            await self.highrise.chat("❌ Usage: !setrole @user <role>")
            return
        
        target_username = params[0].replace('@', '')
        role_name = params[1].upper()
        
        try:
            role = Role[role_name]
        except KeyError:
            await self.highrise.chat(f"❌ Rôle invalide. Disponibles: {', '.join([r.name for r in Role])}")
            return
        
        try:
            users = await self.highrise.get_room_users()
            target_user = None
            
            for room_user, _ in users.content:
                if room_user.username.lower() == target_username.lower():
                    target_user = room_user
                    break
            
            if target_user:
                role_manager.set_role(target_user.id, role)
                await self.highrise.chat(f"✅ {target_username} est maintenant {role_name}")
            else:
                await self.highrise.chat(f"❌ {target_username} introuvable")
        except Exception as e:
            await self.highrise.chat(f"❌ Erreur: {str(e)}")
    
    async def cmd_8ball(self, params):
        """Magic 8ball"""
        if not params:
            await self.highrise.chat("❌ Usage: !8ball <question>")
            return
        
        responses = [
            "Oui, absolument!",
            "C'est certain!",
            "Sans aucun doute!",
            "Oui, définitivement!",
            "Tu peux compter dessus!",
            "Probablement oui",
            "Les signes pointent vers oui",
            "Demande plus tard",
            "Mieux vaut ne pas te le dire maintenant",
            "Impossible de prédire",
            "Concentre-toi et redemande",
            "N'y compte pas",
            "Ma réponse est non",
            "Mes sources disent non",
            "Peu probable",
            "Très douteux"
        ]
        
        await self.highrise.chat(f"🎱 {random.choice(responses)}")
    
    async def cmd_rate(self, params):
        """Noter quelqu'un sur 10"""
        if not params:
            await self.highrise.chat("❌ Usage: !rate @user")
            return
        
        target = params[0].replace('@', '')
        rating = random.randint(1, 10)
        
        await self.highrise.chat(f"⭐ Je donne à {target} un {rating}/10!")
    
    async def cmd_wallet(self):
        """Voir le wallet du bot"""
        try:
            wallet = await self.highrise.get_wallet()
            await self.highrise.chat(f"💰 Wallet: {wallet.amount} gold")
        except Exception as e:
            await self.highrise.chat(f"❌ Erreur: {str(e)}")
    
    async def cmd_emote_shortcut(self, user: User, emote_name: str, params):
        """Raccourci pour faire une emote rapidement"""
        # Si un utilisateur est mentionné, faire l'emote sur lui
        if params:
            target_username = params[0].replace('@', '')
            
            try:
                users = await self.highrise.get_room_users()
                target_user = None
                
                for room_user, _ in users.content:
                    if room_user.username.lower() == target_username.lower():
                        target_user = room_user
                        break
                
                if not target_user:
                    await self.highrise.chat(f"❌ {target_username} introuvable")
                    return
                
                emote_id = find_emote(emote_name)
                if emote_id:
                    await self.highrise.send_emote(emote_id, target_user.id)
                    print(f"[EMOTE] {emote_name} sur {target_username}")
            except Exception as e:
                print(f"[ERREUR] Emote shortcut: {e}")
        else:
            # Sinon, le bot fait l'emote lui-même
            emote_id = find_emote(emote_name)
            if emote_id:
                try:
                    await self.highrise.send_emote(emote_id)
                    print(f"[EMOTE] Bot fait {emote_name}")
                except Exception as e:
                    print(f"[ERREUR] Emote: {e}")
    
    # ==================== COMMANDES GEMINI AI ====================
    
    async def cmd_ask(self, user: User, params):
        """Poser une question à Gemini AI"""
        if not params:
            await self.highrise.send_whisper(user.id, "❌ Usage: !ask <question>")
            return
        
        if not gemini_assistant.is_configured:
            await self.highrise.send_whisper(user.id, "❌ Gemini AI non configuré. Ajoutez GEMINI_API_KEY dans .env")
            return
        
        question = ' '.join(params)
        await self.highrise.send_whisper(user.id, f"🤔 Question: {question[:50]}...")
        
        try:
            response = await ask_gemini(question)
            if len(response) > 200:
                response = response[:197] + "..."
            await self.highrise.send_whisper(user.id, f"🤖 {response}")
        except Exception as e:
            print(f"[GEMINI] Erreur: {e}")
            await self.highrise.send_whisper(user.id, "❌ Erreur IA")
    
    async def cmd_ai(self, user: User, params):
        """Discuter avec Gemini AI"""
        if not params:
            await self.highrise.send_whisper(user.id, "❌ Usage: !ai <message>")
            return
        
        if not gemini_assistant.is_configured:
            await self.highrise.send_whisper(user.id, "❌ Gemini AI non configuré")
            return
        
        message = ' '.join(params)
        
        try:
            response = await chat_with_gemini(message, user.username)
            if len(response) > 200:
                response = response[:197] + "..."
            await self.highrise.send_whisper(user.id, f"🤖 {response}")
        except Exception as e:
            print(f"[GEMINI] Erreur: {e}")
            await self.highrise.send_whisper(user.id, "❌ Erreur IA")
    
    async def cmd_joke(self, user: User):
        """Demander une blague à Gemini"""
        if not gemini_assistant.is_configured:
            await self.highrise.send_whisper(user.id, "❌ Gemini AI non configuré")
            return
        
        await self.highrise.send_whisper(user.id, "😄 Laissez-moi réfléchir...")
        
        try:
            joke = await gemini_assistant.get_joke()
            await self.highrise.send_whisper(user.id, f"😂 {joke}")
        except Exception as e:
            print(f"[GEMINI] Erreur: {e}")
            await self.highrise.send_whisper(user.id, "❌ Erreur lors de la génération")
    
    async def cmd_fact(self, user: User):
        """Obtenir un fait intéressant de Gemini"""
        if not gemini_assistant.is_configured:
            await self.highrise.send_whisper(user.id, "❌ Gemini AI non configuré")
            return
        
        await self.highrise.send_whisper(user.id, "🧠 Fait intéressant...")
        
        try:
            fact = await gemini_assistant.get_fun_fact()
            await self.highrise.send_whisper(user.id, f"💡 {fact}")
        except Exception as e:
            print(f"[GEMINI] Erreur: {e}")
            await self.highrise.send_whisper(user.id, "❌ Erreur")
    
    async def cmd_advice(self, user: User, params):
        """Obtenir un conseil de Gemini"""
        if not gemini_assistant.is_configured:
            await self.highrise.send_whisper(user.id, "❌ Gemini AI non configuré")
            return
        
        topic = ' '.join(params) if params else "vie"
        await self.highrise.send_whisper(user.id, f"💭 Conseil sur: {topic}...")
        
        try:
            advice = await gemini_assistant.get_advice(topic)
            await self.highrise.send_whisper(user.id, f"✨ {advice}")
        except Exception as e:
            print(f"[GEMINI] Erreur: {e}")
            await self.highrise.send_whisper(user.id, "❌ Erreur")
    
    async def cmd_translate(self, user: User, params):
        """Traduire un texte avec Gemini"""
        if not gemini_assistant.is_configured:
            await self.highrise.send_whisper(user.id, "❌ Gemini AI non configuré")
            return
        
        if len(params) < 2:
            await self.highrise.send_whisper(user.id, "❌ Usage: !translate <langue> <texte>")
            return
        
        target_lang = params[0]
        text = ' '.join(params[1:])
        
        try:
            translation = await gemini_assistant.translate(text, target_lang)
            await self.highrise.send_whisper(user.id, f"🌍 {translation}")
        except Exception as e:
            print(f"[GEMINI] Erreur: {e}")
            await self.highrise.send_whisper(user.id, "❌ Erreur de traduction")
    
    # ==================== COMMANDES OUTFIT ====================
    
    async def cmd_inventory(self, user: User):
        """Afficher l'inventaire du bot dans les logs"""
        try:
            inventory = await self.highrise.get_inventory()
            
            print("\n" + "="*60)
            print(f"📦 INVENTAIRE DU BOT ({len(inventory.items)} items)")
            print("="*60)
            
            # Grouper par type
            by_type = {}
            for item in inventory.items:
                item_type = item.type
                if item_type not in by_type:
                    by_type[item_type] = []
                by_type[item_type].append(item)
            
            # Afficher par type dans les logs
            for item_type, items in sorted(by_type.items()):
                print(f"\n=== {item_type.upper()} ({len(items)} items) ===")
                for i, item in enumerate(items, 1):
                    print(f"  {i}. {item.id}")
            
            print("\n" + "="*60)
            print(f"✅ Total: {len(inventory.items)} items")
            print("="*60 + "\n")
            
            # Confirmer à l'utilisateur
            await self.highrise.send_whisper(user.id, 
                f"✅ Inventaire affiche dans les logs ({len(inventory.items)} items)")
            
        except Exception as e:
            print(f"[ERREUR] Inventaire: {e}")
            await self.highrise.send_whisper(user.id, f"Erreur: {e}")
    
    async def cmd_current_outfit(self, user: User):
        """Afficher l'outfit actuel"""
        try:
            current_outfit = await self.highrise.get_my_outfit()
            
            print("\n" + "="*60)
            print(f"👔 OUTFIT ACTUEL ({len(current_outfit.outfit)} items)")
            print("="*60)
            
            for i, item in enumerate(current_outfit.outfit, 1):
                category = item.id.split('-')[0] if '-' in item.id else 'unknown'
                palette = item.active_palette if hasattr(item, 'active_palette') else 0
                print(f"{i}. [{category.upper()}] {item.id} (palette: {palette})")
            
            print("="*60 + "\n")
            
            await self.highrise.send_whisper(user.id, 
                f"✅ Outfit actuel: {len(current_outfit.outfit)} items\nVoir les logs pour détails")
            
        except Exception as e:
            print(f"[ERREUR] Current outfit: {e}")
            await self.highrise.send_whisper(user.id, f"Erreur: {e}")
    
    async def cmd_modify_outfit(self, user: User, params):
        """Modifier l'outfit actuel en ajoutant/remplaçant des items par nom"""
        if len(params) < 2:
            await self.highrise.send_whisper(user.id, 
                "Usage: !admin modifyoutfit replace <nom item>\n!admin modifyoutfit remove <category>")
            return
        
        action = params[0].lower()
        
        try:
            import requests
            
            # Récupérer l'outfit actuel
            current_outfit = await self.highrise.get_my_outfit()
            outfit_items = list(current_outfit.outfit)
            
            if action == "replace" or action == "add":
                # Chercher l'item par son nom
                item_name = " ".join(params[1:])
                
                await self.highrise.send_whisper(user.id, f"🔍 Recherche de '{item_name}'...")
                print(f"[OUTFIT] Recherche de '{item_name}'...")
                
                found_item = None
                item_id = None
                category = None
                from_inventory = False
                
                # ÉTAPE 1 : Chercher dans l'inventaire du bot (starter items)
                try:
                    inventory = await self.highrise.get_inventory()
                    print(f"[OUTFIT] Inventaire: {len(inventory.items)} items")
                    
                    for inv_item in inventory.items:
                        # Extraire le nom de l'item depuis l'ID
                        # Format: category-subcategory-name
                        item_parts = inv_item.id.split('-')
                        
                        # Vérifier si le nom correspond
                        if item_name.lower() in inv_item.id.lower():
                            item_id = inv_item.id
                            category = item_parts[0] if item_parts else 'unknown'
                            from_inventory = True
                            print(f"[OUTFIT] ✅ Item trouvé dans l'inventaire: {item_id}")
                            break
                except Exception as e:
                    print(f"[OUTFIT] Erreur inventaire: {e}")
                
                # ÉTAPE 2 : Si pas trouvé dans l'inventaire, chercher dans les free items
                if not item_id:
                    print(f"[OUTFIT] Item non trouvé dans l'inventaire, recherche dans free items...")
                    try:
                        response = requests.get('https://webapi.highrise.game/items?rarity=none&limit=500', timeout=5)
                        
                        if response.status_code == 200:
                            items_data = response.json()
                            
                            # Chercher l'item par nom (insensible à la casse)
                            for item in items_data.get('items', []):
                                if item['item_name'].lower() == item_name.lower():
                                    found_item = item
                                    item_id = found_item['item_id']
                                    category = found_item['category']
                                    print(f"[OUTFIT] ✅ Item trouvé dans free items: {item_id}")
                                    break
                        else:
                            print(f"[OUTFIT] ⚠️ API erreur: status {response.status_code}")
                    except requests.exceptions.Timeout:
                        print(f"[OUTFIT] ⚠️ API timeout")
                    except requests.exceptions.JSONDecodeError:
                        print(f"[OUTFIT] ⚠️ API réponse invalide")
                    except Exception as e:
                        print(f"[OUTFIT] ⚠️ Erreur API: {e}")
                
                if not item_id:
                    await self.highrise.send_whisper(user.id, 
                        f"❌ Item '{item_name}' non trouvé\nNi dans l'inventaire, ni dans les free items")
                    print(f"[OUTFIT] Item '{item_name}' non trouvé")
                    return
                
                # Retirer tous les items de cette catégorie
                new_outfit = [item for item in outfit_items if not item.id.startswith(category + "-")]
                
                # Ajouter le nouvel item
                new_item = Item(type="clothing", amount=1, id=item_id, account_bound=False, active_palette=0)
                new_outfit.append(new_item)
                
                print(f"[OUTFIT] Remplacement de '{category}' par {item_id}")
                print(f"[OUTFIT] Ancien outfit: {len(outfit_items)} items")
                print(f"[OUTFIT] Nouvel outfit: {len(new_outfit)} items")
                
                # Appliquer le nouvel outfit
                await self.highrise.set_outfit(new_outfit)
                
                source = "inventaire" if from_inventory else "free items"
                await self.highrise.send_whisper(user.id, 
                    f"✅ Item équipé !\nID: {item_id}\nCatégorie: {category}\nSource: {source}")
                print(f"[OUTFIT] ✅ Item remplacé avec succès (source: {source})")
                
            elif action == "remove":
                # Retirer un item par catégorie (ex: shirt, pants, shoes)
                category_to_remove = params[1].lower()
                
                # Filtrer les items qui ne correspondent pas à la catégorie
                new_outfit = [item for item in outfit_items if not item.id.startswith(category_to_remove + "-")]
                
                if len(new_outfit) < len(outfit_items):
                    await self.highrise.set_outfit(new_outfit)
                    await self.highrise.send_whisper(user.id, f"✅ Items '{category_to_remove}' retirés")
                    print(f"[OUTFIT] Items '{category_to_remove}' retirés")
                else:
                    await self.highrise.send_whisper(user.id, f"❌ Aucun item '{category_to_remove}' trouvé")
            else:
                await self.highrise.send_whisper(user.id, "Action inconnue. Utilisez 'replace' ou 'remove'")
                
        except Exception as e:
            print(f"[ERREUR] Modify outfit: {e}")
            import traceback
            traceback.print_exc()
            await self.highrise.send_whisper(user.id, f"Erreur: {e}")
    
    async def cmd_change_color(self, user: User, params):
        """Changer la couleur d'un item (palette)
        Usage: !admin changecolor <category> <palette_number>
        Exemples:
        - !admin changecolor body 27 (couleur de peau)
        - !admin changecolor eye 5 (couleur des yeux)
        - !admin changecolor hair_front 10 (couleur des cheveux)
        """
        if len(params) < 2:
            await self.highrise.send_whisper(user.id, 
                "Usage: !admin changecolor <category> <palette>\n"
                "Exemples:\n"
                "- body 27 (peau foncée)\n"
                "- eye 5 (yeux bleus)\n"
                "- hair_front 10 (cheveux blonds)")
            return
        
        try:
            category = params[0].lower()
            palette_number = int(params[1])
            
            if palette_number < 0 or palette_number > 100:
                await self.highrise.send_whisper(user.id, "❌ Palette doit être entre 0 et 100")
                return
            
            print(f"[COLOR] Changement de couleur: {category} -> palette {palette_number}")
            
            # Récupérer l'outfit actuel
            current_outfit = await self.highrise.get_my_outfit()
            outfit_items = list(current_outfit.outfit)
            
            # Chercher l'item de cette catégorie
            item_found = False
            new_outfit = []
            
            for item in outfit_items:
                if item.id.startswith(category + "-"):
                    # Modifier la palette de cet item
                    modified_item = Item(
                        type=item.type,
                        amount=item.amount,
                        id=item.id,
                        account_bound=item.account_bound,
                        active_palette=palette_number
                    )
                    new_outfit.append(modified_item)
                    item_found = True
                    print(f"[COLOR] ✅ Item modifié: {item.id} (palette {palette_number})")
                else:
                    new_outfit.append(item)
            
            if not item_found:
                await self.highrise.send_whisper(user.id, 
                    f"❌ Aucun item '{category}' trouvé dans l'outfit actuel\n"
                    f"Équipez d'abord un item de cette catégorie")
                return
            
            # Appliquer le nouvel outfit
            await self.highrise.set_outfit(new_outfit)
            await self.highrise.send_whisper(user.id, 
                f"✅ Couleur changée !\n"
                f"Catégorie: {category}\n"
                f"Palette: {palette_number}")
            print(f"[COLOR] ✅ Couleur changée avec succès")
            
        except ValueError:
            await self.highrise.send_whisper(user.id, "❌ Le numéro de palette doit être un nombre")
        except Exception as e:
            print(f"[ERREUR] Change color: {e}")
            import traceback
            traceback.print_exc()
            await self.highrise.send_whisper(user.id, f"Erreur: {e}")
    
    async def cmd_searchitem(self, user: User, params):
        """Chercher un item par catégorie ou nom"""
        if not params:
            msg = """Usage:
!admin searchitem <catégorie>
!admin searchitem name <nom exact>

Catégories: shoes, shirt, pants, skirt, sock, hair, watch, glasses, hat, bag

Exemples:
!admin searchitem shoes
!admin searchitem name Black Flats"""
            await self.highrise.send_whisper(user.id, msg)
            return
        
        try:
            import requests
            
            # Vérifier si c'est une recherche par nom exact
            if params[0].lower() == 'name':
                # Recherche par nom exact
                search_name = " ".join(params[1:])
                
                response = requests.get('https://webapi.highrise.game/items?rarity=none&limit=500')
                data = response.json()
                
                print("\n" + "="*60)
                print(f"🔍 RECHERCHE PAR NOM: '{search_name}'")
                print("="*60)
                
                results = []
                for item in data['items']:
                    item_name = item['item_name']
                    
                    # Recherche exacte (insensible à la casse)
                    if item_name.lower() == search_name.lower():
                        results.append(item)
                        print(f"✅ {item_name}")
                        print(f"   ID: {item['item_id']}")
                        print(f"   Type: {item['category']}")
                        print()
                
                print("="*60)
                print(f"📊 {len(results)} résultat(s) trouvé(s)")
                print("="*60 + "\n")
                
                if results:
                    msg = f"✅ {len(results)} item(s) trouvé(s)\nRegarde les logs pour l'ID"
                else:
                    msg = f"❌ Aucun item trouvé avec le nom exact '{search_name}'"
                
            else:
                # Recherche par catégorie
                category = params[0].lower()
                
                response = requests.get(f'https://webapi.highrise.game/items?rarity=none&category={category}&limit=100')
                data = response.json()
                
                print("\n" + "="*60)
                print(f"👕 CATÉGORIE: {category.upper()}")
                print(f"📦 {len(data.get('items', []))} items disponibles")
                print("="*60)
                
                # Afficher les items
                for i, item in enumerate(data.get('items', [])[:30], 1):
                    print(f"{i}. {item['item_name']}")
                    print(f"   ID: {item['item_id']}")
                    print()
                
                total = len(data.get('items', []))
                if total > 30:
                    print(f"... et {total - 30} autres items")
                
                print("="*60)
                print(f"📊 Total: {total} items dans '{category}'")
                print("="*60 + "\n")
                
                msg = f"✅ {total} items trouvés dans '{category}'\nRegarde les logs (30 premiers affichés)"
            
            await self.highrise.send_whisper(user.id, msg)
            
        except Exception as e:
            print(f"[ERREUR] Search item: {e}")
            import traceback
            traceback.print_exc()
            await self.highrise.send_whisper(user.id, f"Erreur: {e}")
    
    async def cmd_setpos(self, user: User, params):
        """Définir la position du bot"""
        if len(params) < 2:
            await self.highrise.send_whisper(user.id, 
                "Usage: !admin setpos <x> <y>\n"
                "Exemple: !admin setpos 10 5")
            return
        
        try:
            x = float(params[0])
            y = float(params[1])
            
            # Position avec z=0 et direction par défaut
            position = Position(x, y, 0.0, "FrontRight")
            
            await self.highrise.walk_to(position)
            await self.highrise.send_whisper(user.id, f"✅ Bot téléporté à x={x}, y={y}")
            print(f"[POSITION] Téléporté à x={x}, y={y} par {user.username}")
            
        except ValueError:
            await self.highrise.send_whisper(user.id, "❌ Coordonnées invalides (doivent être des nombres)")
        except Exception as e:
            await self.highrise.send_whisper(user.id, f"❌ Erreur: {e}")
            print(f"[ERREUR] Setpos: {e}")
    
    async def cmd_rest(self, user: User):
        """Faire l'emote rest sur l'admin"""
        try:
            # Trouver la position de l'admin
            room_users = await self.highrise.get_room_users()
            
            for room_user, position in room_users.content:
                if room_user.id == user.id:
                    # Essayer la vraie emote "Rest" (sit-idle-cute)
                    # Si elle n'est pas dans l'inventaire, utiliser "Sit" (gratuite)
                    try:
                        await self.highrise.send_emote("sit-idle-cute", user.id)
                        await self.highrise.send_whisper(user.id, "😌 Le bot se repose près de toi (Rest)")
                        print(f"[REST] Emote 'Rest' (sit-idle-cute) exécutée sur {user.username}")
                    except:
                        # Fallback sur l'emote gratuite "Sit"
                        await self.highrise.send_emote("idle-loop-sitfloor", user.id)
                        await self.highrise.send_whisper(user.id, "😌 Le bot se repose près de toi (Sit)")
                        print(f"[REST] Emote 'Sit' (idle-loop-sitfloor) exécutée sur {user.username}")
                    return
            
            await self.highrise.send_whisper(user.id, "❌ Position non trouvée")
            
        except Exception as e:
            await self.highrise.send_whisper(user.id, f"❌ Erreur: {e}")
            print(f"[ERREUR] Rest: {e}")
    
    async def floss_loop_on_user(self, user_id: str, username: str):
        """Boucle floss sur un utilisateur spécifique"""
        print(f"[FLOSS-ADMIN] Démarrage boucle floss sur {username}")
        
        while True:
            try:
                # Faire l'emote floss sur l'utilisateur
                await self.highrise.send_emote("dance-floss", user_id)
                print(f"[FLOSS-ADMIN] 💃 Floss exécuté sur {username}")
                
                # Attendre 10 secondes avant de recommencer
                await asyncio.sleep(10)
                
            except asyncio.CancelledError:
                # La tâche a été annulée (flossstop)
                print(f"[FLOSS-ADMIN] Boucle floss arrêtée pour {username}")
                break
            except Exception as e:
                print(f"[FLOSS-ADMIN] Erreur sur {username}: {e}")
                await asyncio.sleep(15)
    
    async def cmd_floss_loop_admin(self, user: User):
        """Lancer la boucle floss sur l'admin"""
        try:
            # Vérifier si une boucle existe déjà pour cet admin
            if user.id in self.admin_floss_tasks:
                await self.highrise.send_whisper(user.id, "⚠️ La boucle floss est déjà active sur toi!\nUtilise !admin flossstop pour l'arrêter d'abord")
                return
            
            # Créer et démarrer la tâche floss pour cet admin
            task = asyncio.create_task(self.floss_loop_on_user(user.id, user.username))
            self.admin_floss_tasks[user.id] = task
            
            await self.highrise.send_whisper(user.id, "💃 Boucle floss lancée sur toi!\nUtilise !admin flossstop pour l'arrêter")
            print(f"[FLOSS-ADMIN] Boucle floss lancée pour {user.username}")
            
        except Exception as e:
            await self.highrise.send_whisper(user.id, f"❌ Erreur: {e}")
            print(f"[ERREUR] Floss loop admin: {e}")
    
    async def cmd_floss_stop_admin(self, user: User):
        """Arrêter la boucle floss sur l'admin"""
        try:
            # Vérifier si une boucle existe pour cet admin
            if user.id not in self.admin_floss_tasks:
                await self.highrise.send_whisper(user.id, "⚠️ Aucune boucle floss active sur toi!\nUtilise !admin flossloop pour en lancer une")
                return
            
            # Annuler la tâche
            task = self.admin_floss_tasks[user.id]
            task.cancel()
            
            # Retirer de la liste
            del self.admin_floss_tasks[user.id]
            
            await self.highrise.send_whisper(user.id, "✅ Boucle floss arrêtée!")
            print(f"[FLOSS-ADMIN] Boucle floss arrêtée pour {user.username}")
            
        except Exception as e:
            await self.highrise.send_whisper(user.id, f"❌ Erreur: {e}")
            print(f"[ERREUR] Floss stop admin: {e}")
    
    async def cmd_get_position(self, user: User, params):
        """Obtenir la position d'un utilisateur et générer le script"""
        try:
            if len(params) < 1:
                await self.highrise.send_whisper(user.id, 
                    "Usage: !admin getpos <username>\n"
                    "Exemple: !admin getpos sindouche")
                return
            
            target_username = ' '.join(params).lower()
            
            # Récupérer tous les utilisateurs dans la room
            room_users = await self.highrise.get_room_users()
            
            for room_user, position in room_users.content:
                if room_user.username.lower() == target_username:
                    # Position trouvée !
                    x = position.x
                    y = position.y
                    z = position.z
                    facing = position.facing
                    
                    # Générer le script
                    script = f"""# ========================================
# SCRIPT DE POSITION PAR DÉFAUT
# ========================================
# Position de {room_user.username}
# Copie ce code dans on_start() (ligne ~120)

# Téléporter le bot à une position par défaut
try:
    default_position = Position({x}, {y}, {z}, "{facing}")
    await self.highrise.walk_to(default_position)
    print(f"[POSITION] Bot téléporté à x={{default_position.x}}, y={{default_position.y}}")
except Exception as e:
    print(f"[ERREUR] Téléportation: {{e}}")

# ========================================
# DÉTAILS DE LA POSITION
# ========================================
# X: {x} (horizontal)
# Y: {y} (vertical)
# Z: {z} (profondeur)
# Facing: {facing} (direction)
# ========================================"""
                    
                    # Afficher dans les logs
                    print("\n" + "="*60)
                    print(f"📍 POSITION DE {room_user.username.upper()}")
                    print("="*60)
                    print(script)
                    print("="*60 + "\n")
                    
                    # Envoyer confirmation en DM
                    await self.highrise.send_whisper(user.id, 
                        f"✅ Position de {room_user.username} récupérée!\n"
                        f"X: {x}\nY: {y}\nZ: {z}\n"
                        f"Facing: {facing}\n\n"
                        f"📋 Script généré dans les logs!")
                    
                    return
            
            # Utilisateur non trouvé
            await self.highrise.send_whisper(user.id, f"❌ Utilisateur '{target_username}' non trouvé dans la room")
            
        except Exception as e:
            await self.highrise.send_whisper(user.id, f"❌ Erreur: {e}")
            print(f"[ERREUR] Get position: {e}")
    
    async def handle_flirt_command(self, user: User, message: str):
        """Gérer la commande !flirt accessible à tous"""
        if not gemini_assistant or not gemini_assistant.is_configured:
            await self.highrise.send_whisper(user.id, "❌ IA Gemini non disponible")
            return
        
        try:
            # Extraire le nom de la femme
            parts = message.split(' ', 1)
            if len(parts) < 2:
                await self.highrise.send_whisper(user.id, 
                    "Usage: !flirt <username_femme>\n"
                    "Exemple: !flirt momo\n"
                    "Le bot écrira un message de drague de ta part !")
                return
            
            femme_username = parts[1].strip()
            homme_username = user.username
            
            # Générer et envoyer le message de drague
            await self.generate_and_send_flirt(homme_username, femme_username, user.id)
            
        except Exception as e:
            await self.highrise.send_whisper(user.id, f"❌ Erreur: {e}")
            print(f"[ERREUR] Flirt: {e}")
    
    async def cmd_flirt(self, user: User, params):
        """Commande admin pour faire draguer un user vers une femme"""
        if not gemini_assistant or not gemini_assistant.is_configured:
            await self.highrise.send_whisper(user.id, "❌ IA Gemini non disponible")
            return
        
        try:
            if len(params) < 2:
                await self.highrise.send_whisper(user.id, 
                    "Usage: !admin flirt <username_homme> <username_femme>\n"
                    "Exemple: !admin flirt john_doe marie_belle\n"
                    "Le bot écrira un message de drague de la part de l'homme vers la femme")
                return
            
            homme_username = params[0]
            femme_username = ' '.join(params[1:])
            
            # Générer et envoyer le message de drague
            await self.generate_and_send_flirt(homme_username, femme_username, user.id)
            
        except Exception as e:
            await self.highrise.send_whisper(user.id, f"❌ Erreur: {e}")
            print(f"[ERREUR] Flirt admin: {e}")
    
    async def generate_and_send_flirt(self, homme_username: str, femme_username: str, requester_id: str):
        """Générer et envoyer un message de drague"""
        try:
            # Contexte pour générer le message de drague
            context = f"""Tu es un expert en drague romantique et charmante.
Genere un message de drague DOUX et CHARMANT de la part de {homme_username} pour draguer {femme_username}.
Le message doit etre:
- Romantique mais pas trop lourd
- Charmant et flatteur
- Avec un peu d'humour si possible
- Pas vulgaire, rester classe
- Maximum 140 caracteres pour le chat
Utilise des compliments, des metaphores douces, des emojis romantiques.
Exemple de style: "Hey {femme_username}, t'es comme le soleil... tu illumines ma journee 🌹✨"
Sois creatif, charmant et romantique!"""
            
            prompt = f"Ecris un message de drague de {homme_username} pour {femme_username}"
            
            print(f"[FLIRT] Generation message de {homme_username} vers {femme_username}...")
            flirt_message = await gemini_assistant.ask(prompt, context)
            
            # Limiter à 140 caractères
            if len(flirt_message) > 140:
                flirt_message = flirt_message[:137] + "..."
            
            # Envoyer dans le chat public
            await self.highrise.chat(flirt_message)
            print(f"[FLIRT] Message envoyé: {flirt_message}")
            
            # Confirmation à l'utilisateur
            await self.highrise.send_whisper(requester_id, 
                f"💘 Message de drague envoyé!\n"
                f"De: {homme_username}\n"
                f"Pour: {femme_username}\n"
                f"Message: {flirt_message[:50]}...")
            
        except Exception as e:
            await self.highrise.send_whisper(requester_id, f"❌ Erreur: {e}")
            print(f"[ERREUR] Generate flirt: {e}")


if __name__ == "__main__":
    # Démarrer le serveur de santé pour l'hébergement
    start_health_server()
    
    # Récupérer les credentials depuis les variables d'environnement
    room_id = os.getenv('ROOM_ID', '680ab18546b31625a94de2e6')
    bot_token = os.getenv('BOT_TOKEN', '057565bd7bda6ac37029f5817ea7c2f6d447179cdfa65771e41284ed5f5d6090')
    
    print("=" * 50)
    print("🤖 Démarrage du Bot Highrise Savant")
    print("=" * 50)
    print(f"Room ID: {room_id}")
    print(f"Token: {bot_token[:20]}...")
    print("=" * 50)
    
    # Lancer le bot avec les credentials
    from highrise.__main__ import main as highrise_main
    import sys
    sys.argv = ['highrise', 'bot:HighriseBot', room_id, bot_token]
    highrise_main()
