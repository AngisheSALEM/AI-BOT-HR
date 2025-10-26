# 🤖 Savant - Assistant IA Dual Mode

## 🎯 Fonctionnement

Votre bot **Savant** fonctionne maintenant en **deux modes** :

### 1️⃣ Mode Chat Public (avec mention @s)
Le bot répond dans le chat public **seulement** si vous le mentionnez avec `@s`

**Exemples :**
```
User: @s Bonjour!
Savant: @User Bonjour! Comment puis-je t'aider? 😊

User: @s Quelle est la capitale de la France?
Savant: @User La capitale de la France est Paris! 🇫🇷

User: @s
Savant: @User Oui? Comment puis-je t'aider? 😊
```

**Caractéristiques :**
- ✅ Réponses **courtes** (max 150 caractères)
- ✅ Visible par **tous** dans le chat
- ✅ Parfait pour des questions rapides
- ✅ Utilise `@username` pour répondre

### 2️⃣ Mode DM (Message Privé)
Le bot répond en **message privé** quand vous lui envoyez un whisper

**Exemples :**
```
User (DM): Bonjour Savant
Savant (DM): Bonjour! Comment puis-je t'aider aujourd'hui? 😊

User (DM): Raconte-moi une longue histoire
Savant (DM): Il était une fois, dans un monde virtuel appelé Highrise...
[Réponse détaillée jusqu'à 500 caractères]

User (DM): Explique-moi comment fonctionne Highrise
Savant (DM): Highrise est un jeu social où tu peux créer ton avatar...
[Réponse complète et détaillée]
```

**Caractéristiques :**
- ✅ Réponses **détaillées** (max 500 caractères)
- ✅ **Privé** - personne d'autre ne voit
- ✅ Parfait pour des conversations longues
- ✅ Historique visible dans votre boîte de réception
- ✅ Conversations personnalisées

---

## 📊 Comparaison des modes

| Fonctionnalité | Chat Public (@s) | DM (Whisper) |
|----------------|----------------------|--------------|
| **Déclencheur** | Mention `@s` | Message privé |
| **Visibilité** | Tout le monde | Privé |
| **Longueur** | Court (150 char) | Long (500 char) |
| **Usage** | Questions rapides | Conversations détaillées |
| **Historique** | Non sauvegardé | Sauvegardé dans boîte de réception |

---

## 🎭 Personnalité de Savant

### En Chat Public
```
Nom: Savant
Style: Concis et direct
Ton: Amical et poli
Emojis: Oui, modérément
Réponses: Courtes et précises
```

### En DM
```
Nom: Savant
Style: Détaillé et complet
Ton: Sympathique et serviable
Emojis: Oui, fréquemment
Réponses: Complètes et personnalisées
```

---

## 💬 Exemples d'utilisation

### Scénario 1 : Question rapide publique
```
User dans le chat: @s Quelle heure est-il?
Savant dans le chat: @User Il est environ [heure] 🕐
```

### Scénario 2 : Conversation privée
```
User en DM: Salut Savant, j'ai besoin de conseils
Savant en DM: Bonjour! Je suis là pour t'aider. De quoi as-tu besoin? 😊

User en DM: Comment faire des amis sur Highrise?
Savant en DM: Super question! Voici quelques conseils pour faire des amis sur Highrise:
1. Sois amical et poli
2. Participe aux conversations
3. Fais des emotes pour interagir
4. Rejoins des rooms populaires
N'hésite pas si tu as d'autres questions! 🌟
```

### Scénario 3 : Mention sans question
```
User dans le chat: @s
Savant dans le chat: @User Oui? Comment puis-je t'aider? 😊
```

---

## 🔧 Configuration technique

### Fichier modifié : `bot.py`

#### 1. Détection de mention dans `on_chat`
```python
if "@s" in message.lower():
    clean_message = message.replace("@s", "").strip()
    if clean_message:
        await self.respond_with_ai(user, clean_message, is_whisper=False)
    else:
        await self.highrise.chat(f"@{user.username} Oui? Comment puis-je t'aider? 😊")
```

#### 2. Réponses en DM dans `on_whisper`
```python
async def on_whisper(self, user: User, message: str) -> None:
    if message.startswith('!admin'):
        await self.handle_admin_command(user, message)
        return
    
    await self.respond_with_ai(user, message, is_whisper=True)
```

#### 3. Fonction `respond_with_ai` dual-mode
```python
async def respond_with_ai(self, user: User, message: str, is_whisper: bool = True):
    # Contexte différent selon le mode
    if is_whisper:
        # Contexte DM : détaillé
        context = "Tu es Savant... réponses détaillées..."
        max_length = 500
    else:
        # Contexte chat public : concis
        context = "Tu es Savant... réponses TRES concises..."
        max_length = 150
    
    # Envoi selon le mode
    if is_whisper:
        await self.highrise.send_whisper(user.id, response)
    else:
        await self.highrise.chat(f"@{user.username} {response}")
```

---

## 📝 Logs

### Chat Public
```
[CHAT] username: @s Bonjour
[AI-CHAT] Generation reponse pour username: Bonjour...
[AI-CHAT] Reponse envoyee dans le chat public
```

### DM
```
[WHISPER] username: Bonjour Savant
[AI-DM] Generation reponse pour username: Bonjour Savant...
[AI-DM] Reponse envoyee en whisper a username
```

---

## 🎯 Avantages

### Pour les utilisateurs
- ✅ **Flexibilité** : Choisir entre public ou privé
- ✅ **Discrétion** : Conversations privées en DM
- ✅ **Rapidité** : Réponses courtes en public
- ✅ **Détail** : Réponses complètes en privé
- ✅ **Historique** : Messages DM sauvegardés

### Pour la communauté
- ✅ **Pas de spam** : Bot ne répond que si mentionné
- ✅ **Chat propre** : Réponses courtes en public
- ✅ **Engagement** : Encourage l'utilisation de @mentions
- ✅ **Interaction** : Tout le monde peut voir les réponses publiques

### Technique
- ✅ **Économie API** : Moins de requêtes (seulement si mentionné)
- ✅ **Optimisation** : Réponses adaptées au contexte
- ✅ **Flexibilité** : Deux modes distincts
- ✅ **Contrôle** : Gestion précise des interactions

---

## 🚀 Comment utiliser

### En tant qu'utilisateur

#### Pour une question publique rapide :
1. Dans le chat, tapez : `@s [votre question]`
2. Le bot répond dans le chat public
3. Tout le monde peut voir la réponse

#### Pour une conversation privée :
1. Ouvrez la boîte de messages
2. Envoyez un message privé au bot
3. Le bot vous répond en privé
4. Continuez la conversation
5. L'historique est sauvegardé

### En tant qu'admin

Les commandes admin fonctionnent toujours :
```
!admin help
!admin stats
!admin emote 5
!admin announce Message
```

---

## 📱 Boîte de réception

### Accès à l'historique
Tous les messages DM avec Savant sont sauvegardés dans votre boîte de réception Highrise :

1. Ouvrez votre boîte de messages
2. Cherchez la conversation avec le bot
3. Vous pouvez relire tout l'historique
4. Continuez la conversation à tout moment

### Avantages
- ✅ Historique complet des conversations
- ✅ Accessible à tout moment
- ✅ Privé et personnel
- ✅ Pas de limite de temps

---

## ⚙️ Personnalisation

### Changer le nom de mention

Dans `bot.py`, ligne ~76 :
```python
if "@s" in message.lower():
```

Remplacez `@s` par votre nom préféré :
```python
if "@assistant" in message.lower():
if "@helper" in message.lower():
if "@bot" in message.lower():
```

### Modifier les longueurs de réponse

Dans `bot.py`, lignes ~185-190 :
```python
if is_whisper:
    if len(response) > 500:  # Changez 500
        response = response[:497] + "..."
else:
    if len(response) > 150:  # Changez 150
        response = response[:147] + "..."
```

### Personnaliser les contextes

Modifiez les contextes dans `respond_with_ai` (lignes ~165-175) :
```python
# Pour DM
context = f"""Tu es [NOM], [DESCRIPTION]...
[VOS INSTRUCTIONS POUR DM]"""

# Pour chat public
context = f"""Tu es [NOM], [DESCRIPTION]...
[VOS INSTRUCTIONS POUR CHAT PUBLIC]"""
```

---

## 🎮 Cas d'usage

### 1. Support rapide (Public)
```
User: @s Comment téléporter?
Savant: @User Utilise les points de téléportation ou demande à un admin! 🚀
```

### 2. Aide détaillée (DM)
```
User (DM): Comment décorer ma maison?
Savant (DM): Excellente question! Voici un guide complet:
1. Entre en mode édition
2. Sélectionne des meubles dans le catalogue
3. Place-les où tu veux
4. Ajuste la rotation et la hauteur
5. Sauvegarde tes modifications
Tu peux aussi acheter des items premium pour plus d'options! 🏠✨
```

### 3. Conversation sociale (DM)
```
User (DM): Je m'ennuie, que faire?
Savant (DM): Je comprends! Voici quelques idées:
- Explore différentes rooms
- Participe aux événements
- Fais des emotes avec d'autres joueurs
- Décore ta maison
- Rejoins des groupes sociaux
Qu'est-ce qui t'intéresse le plus? 😊
```

### 4. Information publique (Public)
```
User: @s C'est quoi Highrise?
Savant: @User Highrise est un jeu social où tu crées ton avatar et rencontres des amis! 🎮
```

---

## ⚠️ Points importants

### Quota API
- Moins de requêtes qu'avant (seulement si mentionné en public)
- Les DM génèrent toujours des requêtes
- Surveillez votre quota Gemini

### Modération
- Réponses publiques visibles par tous
- Réponses DM privées
- Surveillez les deux types d'interactions

### Performance
- Chat public : ~1-2 secondes
- DM : ~2-3 secondes (réponses plus longues)

---

## 🆘 Dépannage

### Le bot ne répond pas en public
- Vérifiez que vous utilisez `@s` (en minuscules)
- Le bot ignore ses propres messages
- Vérifiez que Gemini est configuré

### Le bot ne répond pas en DM
- Vérifiez que vous envoyez un message privé (whisper)
- Pas besoin de `@s` en DM
- Vérifiez les logs : `[AI-DM]`

### Réponses trop longues/courtes
Ajustez les limites dans `respond_with_ai` :
- Chat public : ligne ~189 (actuellement 150)
- DM : ligne ~185 (actuellement 500)

---

## 📚 Résumé

✅ **Deux modes** : Chat public (@s) et DM
✅ **Réponses adaptées** : Courtes en public, détaillées en privé
✅ **Historique DM** : Sauvegardé dans la boîte de réception
✅ **Pas de spam** : Répond seulement si mentionné en public
✅ **Flexible** : Choisissez votre mode de communication

---

**Profitez de Savant, votre assistant IA dual-mode ! 🤖✨**
