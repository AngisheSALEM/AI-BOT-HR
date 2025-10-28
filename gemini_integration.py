# Module d'intégration de l'API Gemini pour le bot Highrise
# Permet au bot de générer des réponses intelligentes via l'IA Gemini

import google.generativeai as genai
import os
from typing import Optional
import asyncio

class GeminiAssistant:
    """Assistant IA utilisant l'API Gemini de Google avec rotation automatique des clés"""
    
    def __init__(self, api_keys: Optional[list] = None):
        """
        Initialise l'assistant Gemini avec rotation de clés
        
        Args:
            api_keys: Liste de clés API Gemini (optionnel, utilise GEMINI_API_KEY* de .env par défaut)
        """
        # Charger les clés API depuis l'environnement ou utiliser celles fournies
        if api_keys:
            self.api_keys = api_keys
        else:
            # Chercher GEMINI_API_KEY, GEMINI_API_KEY_2, GEMINI_API_KEY_3, GEMINI_API_KEY_4
            self.api_keys = []
            for i in range(1, 5):
                key_name = f'GEMINI_API_KEY_{i}' if i > 1 else 'GEMINI_API_KEY'
                key = os.getenv(key_name)
                if key:
                    self.api_keys.append(key)
        
        self.current_key_index = 0
        self.request_count = 0
        self.max_requests_per_key = 100
        self.model = None
        self.is_configured = False
        
        if self.api_keys:
            self._configure_current_key()
        else:
            print("[GEMINI] ATTENTION Aucune cle API trouvee. Ajoutez GEMINI_API_KEY dans .env")
    
    def _configure_current_key(self):
        """Configure Gemini avec la clé API actuelle"""
        if not self.api_keys:
            return
        
        try:
            current_key = self.api_keys[self.current_key_index]
            genai.configure(api_key=current_key)
            # Essayer différents noms de modèles (avec models/ qui est requis)
            model_names = [
                'models/gemini-2.5-flash',
                'models/gemini-flash-latest',
                'models/gemini-2.0-flash',
                'models/gemini-pro-latest'
            ]
            
            model_loaded = False
            for model_name in model_names:
                try:
                    # Configurer le modèle avec timeout augmenté
                    generation_config = {
                        'temperature': 0.7,
                        'top_p': 0.95,
                        'top_k': 40,
                        'max_output_tokens': 512,  # Augmenté de 256 à 512
                    }
                    
                    # Safety settings plus permissifs pour le contenu romantique
                    safety_settings = [
                        {
                            "category": "HARM_CATEGORY_HARASSMENT",
                            "threshold": "BLOCK_ONLY_HIGH"
                        },
                        {
                            "category": "HARM_CATEGORY_HATE_SPEECH",
                            "threshold": "BLOCK_ONLY_HIGH"
                        },
                        {
                            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                            "threshold": "BLOCK_ONLY_HIGH"
                        },
                        {
                            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                            "threshold": "BLOCK_ONLY_HIGH"
                        }
                    ]
                    
                    self.model = genai.GenerativeModel(
                        model_name,
                        generation_config=generation_config,
                        safety_settings=safety_settings
                    )
                    self.is_configured = True
                    model_loaded = True
                    print(f"[GEMINI] OK API Gemini configuree avec succes (modele: {model_name})")
                    break
                except Exception:
                    continue
            
            if not model_loaded:
                print("[GEMINI] ERREUR Impossible de charger un modele Gemini")
                self.is_configured = False
            else:
                print(f"[GEMINI] Cle API {self.current_key_index + 1}/{len(self.api_keys)} active")
                    
        except Exception as e:
            print(f"[GEMINI] ERREUR de configuration: {e}")
            self.is_configured = False
    
    def _rotate_key(self):
        """Passe à la clé API suivante"""
        if len(self.api_keys) <= 1:
            # Une seule clé, on reset juste le compteur
            self.request_count = 0
            print(f"[GEMINI] Compteur reset: {self.request_count}/{self.max_requests_per_key}")
            return
        
        # Passer à la clé suivante
        self.current_key_index = (self.current_key_index + 1) % len(self.api_keys)
        self.request_count = 0
        
        print(f"[GEMINI] Rotation vers cle API {self.current_key_index + 1}/{len(self.api_keys)}")
        self._configure_current_key()
    
    async def ask(self, question: str, context: Optional[str] = None) -> str:
        """
        Pose une question à Gemini avec rotation automatique des clés
        
        Args:
            question: La question à poser
            context: Contexte additionnel (optionnel)
            
        Returns:
            La réponse de Gemini ou un message d'erreur
        """
        if not self.is_configured:
            return "[ERREUR] L'API Gemini n'est pas configuree. Verifiez votre cle API."
        
        # Incrémenter le compteur et vérifier si rotation nécessaire
        self.request_count += 1
        if self.request_count >= self.max_requests_per_key:
            self._rotate_key()
        
        # Retry jusqu'à 2 fois en cas d'erreur 504
        max_retries = 2
        for attempt in range(max_retries):
            try:
                # Construire le prompt avec contexte si fourni
                prompt = question
                if context:
                    prompt = f"Contexte: {context}\n\nQuestion: {question}"
                
                # Générer la réponse de manière asynchrone avec timeout
                loop = asyncio.get_event_loop()
                
                # Utiliser wait_for pour ajouter un timeout de 15 secondes
                response = await asyncio.wait_for(
                    loop.run_in_executor(
                        None, 
                        lambda: self.model.generate_content(prompt)
                    ),
                    timeout=15.0  # 15 secondes max
                )
                
                # Extraire le texte de la réponse avec gestion des erreurs
                if response:
                    try:
                        # Méthode 1: Accéder directement aux parts (recommandé par Gemini)
                        if hasattr(response, 'candidates') and response.candidates:
                            candidate = response.candidates[0]
                            
                            # Vérifier si bloqué par safety ou autre
                            if hasattr(candidate, 'finish_reason') and candidate.finish_reason != 1:  # 1 = STOP (normal)
                                finish_reason = candidate.finish_reason
                                print(f"[GEMINI] Reponse incomplete - finish_reason: {finish_reason}")
                                
                                # 2 = MAX_TOKENS : réponse tronquée mais utilisable
                                if finish_reason == 2:
                                    print(f"[GEMINI] ⚠️ Reponse tronquee (MAX_TOKENS) - extraction partielle")
                                    # Extraire quand même le texte disponible
                                    if hasattr(candidate, 'content') and hasattr(candidate.content, 'parts'):
                                        text_parts = []
                                        for part in candidate.content.parts:
                                            if hasattr(part, 'text'):
                                                text_parts.append(part.text)
                                        if text_parts:
                                            result = ''.join(text_parts)
                                            print(f"[GEMINI] ✅ Reponse partielle extraite ({len(result)} caracteres)")
                                            return result
                                
                                # 3 = SAFETY : bloqué par filtres
                                elif finish_reason == 3:
                                    if hasattr(candidate, 'safety_ratings'):
                                        print(f"[GEMINI] Safety ratings: {candidate.safety_ratings}")
                                    return "[ERREUR] Contenu bloque par les filtres de securite."
                                
                                # Autres raisons
                                else:
                                    return f"[ERREUR] Generation incomplete (reason: {finish_reason})."
                            
                            # Extraire le texte des parts
                            if hasattr(candidate, 'content') and hasattr(candidate.content, 'parts'):
                                text_parts = []
                                for part in candidate.content.parts:
                                    if hasattr(part, 'text'):
                                        text_parts.append(part.text)
                                
                                if text_parts:
                                    result = ''.join(text_parts)
                                    print(f"[GEMINI] ✅ Reponse extraite ({len(result)} caracteres)")
                                    return result
                        
                        # Méthode 2: Essayer response.text (pour compatibilité)
                        try:
                            if response.text:
                                return response.text
                        except (ValueError, AttributeError):
                            pass  # Ignorer l'erreur, on a déjà essayé les parts
                        
                        # Si aucune méthode ne fonctionne
                        print(f"[GEMINI] ❌ Impossible d'extraire le texte")
                        return "[ERREUR] Impossible d'extraire le texte de la reponse."
                        
                    except Exception as text_error:
                        print(f"[GEMINI] Erreur extraction texte: {text_error}")
                        import traceback
                        traceback.print_exc()
                        return "[ERREUR] Impossible d'extraire la reponse."
                else:
                    return "[ERREUR] Aucune reponse generee."
                    
            except asyncio.TimeoutError:
                print(f"[GEMINI] Timeout (tentative {attempt + 1}/{max_retries})")
                if attempt < max_retries - 1:
                    await asyncio.sleep(1)  # Attendre 1s avant de réessayer
                    continue
                return "[ERREUR] Timeout - Gemini prend trop de temps a repondre."
                
            except Exception as e:
                error_str = str(e)
                print(f"[GEMINI] Erreur lors de la generation: {e}")
                
                # Si erreur 504, réessayer
                if "504" in error_str or "Deadline" in error_str:
                    if attempt < max_retries - 1:
                        print(f"[GEMINI] Retry apres erreur 504 (tentative {attempt + 2}/{max_retries})")
                        await asyncio.sleep(2)  # Attendre 2s avant de réessayer
                        continue
                
                return f"[ERREUR] {error_str}"
        
        return "[ERREUR] Echec apres plusieurs tentatives."
    
    async def chat(self, message: str, username: str = "User") -> str:
        """
        Conversation naturelle avec Gemini
        
        Args:
            message: Le message de l'utilisateur
            username: Nom de l'utilisateur
            
        Returns:
            La réponse de Gemini
        """
        context = f"Tu es un assistant IA sympathique dans un jeu social appelé Highrise. Tu discutes avec {username}."
        return await self.ask(message, context)
    
    async def generate_response(self, prompt: str, max_length: int = 200) -> str:
        """
        Génère une réponse avec limite de longueur
        
        Args:
            prompt: Le prompt à envoyer
            max_length: Longueur maximale de la réponse en caractères
            
        Returns:
            La réponse tronquée si nécessaire
        """
        response = await self.ask(prompt)
        
        # Tronquer si trop long (pour le chat Highrise)
        if len(response) > max_length:
            response = response[:max_length-3] + "..."
        
        return response
    
    async def get_joke(self) -> str:
        """Génère une blague"""
        return await self.generate_response(
            "Raconte une blague courte et drôle (maximum 2 phrases).",
            max_length=150
        )
    
    async def get_fun_fact(self) -> str:
        """Génère un fait intéressant"""
        return await self.generate_response(
            "Donne-moi un fait intéressant et surprenant (1-2 phrases).",
            max_length=150
        )
    
    async def get_advice(self, topic: str = "vie") -> str:
        """Génère un conseil"""
        return await self.generate_response(
            f"Donne un conseil positif et motivant sur: {topic} (1-2 phrases).",
            max_length=150
        )
    
    async def translate(self, text: str, target_lang: str = "en") -> str:
        """Traduit un texte"""
        lang_names = {
            "en": "anglais",
            "fr": "français",
            "es": "espagnol",
            "de": "allemand",
            "it": "italien"
        }
        lang_name = lang_names.get(target_lang, target_lang)
        
        return await self.generate_response(
            f"Traduis ce texte en {lang_name}: {text}",
            max_length=200
        )
    
    async def summarize(self, text: str) -> str:
        """Résume un texte"""
        return await self.generate_response(
            f"Résume ce texte en une phrase courte: {text}",
            max_length=150
        )

# Instance globale de l'assistant (sera initialisée après le chargement de .env)
gemini_assistant = None

def initialize_gemini():
    """Initialise l'assistant Gemini après le chargement de .env"""
    global gemini_assistant
    if gemini_assistant is None:
        gemini_assistant = GeminiAssistant()
    return gemini_assistant

# Fonctions helper pour utilisation facile
async def ask_gemini(question: str, context: Optional[str] = None) -> str:
    """Fonction helper pour poser une question à Gemini"""
    return await gemini_assistant.ask(question, context)

async def chat_with_gemini(message: str, username: str = "User") -> str:
    """Fonction helper pour discuter avec Gemini"""
    return await gemini_assistant.chat(message, username)
