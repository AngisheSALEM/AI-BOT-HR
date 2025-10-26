# 🤖 Mode Assistant IA Conversationnel

## 🎯 Nouvelle fonctionnalité

Votre bot Highrise est maintenant un **assistant IA conversationnel** ! Il répond automatiquement à tous les messages avec l'intelligence artificielle Gemini.

## ✨ Comment ça marche

### Mode Chat Public
- **Avant** : Les utilisateurs devaient taper `!ask question` ou `!ai message`
- **Maintenant** : Les utilisateurs parlent directement au bot, il répond automatiquement !

**Exemple :**
```
User: Bonjour!
Bot: @User: Bonjour! Comment puis-je t'aider aujourd'hui? 😊

User: Raconte-moi une blague
Bot: @User: Pourquoi les plongeurs plongent-ils toujours en arrière? Parce que sinon ils tombent dans le bateau! 😄

User: Quelle est la capitale de la France?
Bot: @User: La capitale de la France est Paris! 🇫🇷
```

### Mode Whisper (Messages Privés)
Les utilisateurs peuvent aussi parler au bot en privé :
```
User (whisper): Comment vas-tu?
Bot (whisper): Je vais très bien, merci! Et toi? 😊
```

## 🎭 Personnalité du Bot

Le bot a maintenant une personnalité définie :
- **Nom** : Assistant Gemini
- **Rôle** : Assistant IA sympathique et utile
- **Style** : Poli, amical, utilise des emojis
- **Réponses** : Concises (max 200 caractères pour le chat)
- **Contexte** : Sait qu'il est dans le jeu Highrise

## 🛡️ Commandes Admin

Les commandes administratives sont maintenant protégées et préfixées par `!admin` :

### Utilisation
```
!admin help          - Liste des commandes admin
!admin emote <num>   - Faire une emote
!admin tp <lieu>     - Téléportation
!admin announce <msg> - Annonce publique
!admin kick <user>   - Expulser un utilisateur
!admin stats         - Statistiques du bot
!admin uptime        - Temps de fonctionnement
!admin wallet        - Voir le wallet
!admin users         - Liste des utilisateurs
```

### Sécurité
- ✅ Seuls les admins (définis dans `.env`) peuvent utiliser ces commandes
- ✅ Les commandes admin sont envoyées en whisper
- ✅ Message d'erreur si un non-admin essaie d'utiliser une commande

## 🔧 Configuration

### Fichier modifié : `bot.py`

**Changements principaux :**

1. **Fonction `on_chat`** : Répond avec Gemini au lieu de chercher des commandes
2. **Fonction `on_whisper`** : Répond avec Gemini en privé
3. **Fonction `respond_with_ai`** : Nouvelle fonction pour gérer les réponses IA
4. **Fonction `handle_admin_command`** : Gestion des commandes admin uniquement

### Contexte IA personnalisé

```python
context = """Tu es un assistant IA sympathique et utile dans le jeu Highrise.
Tu t'appelles Assistant Gemini et tu es là pour aider, discuter et divertir les joueurs.
Tu réponds de manière concise (maximum 200 caractères) car c'est un chat de jeu.
Tu es poli, amical et tu utilises parfois des emojis.
Tu discutes avec {username}."""
```

## 📊 Comportement

### Messages ignorés
Le bot ignore ses propres messages pour éviter les boucles :
```python
if user.username == "bot" or user.username.lower().startswith("bot"):
    return
```

### Gestion des erreurs
Si Gemini n'est pas disponible :
```
Bot: Desolé, mon IA n'est pas disponible pour le moment.
```

### Logs
```
[CHAT] username: message
[AI] Generation reponse pour username: message...
[AI] Reponse envoyee dans le chat
```

## 🎮 Cas d'usage

### 1. Assistant personnel
```
User: Quel temps fait-il à Paris?
Bot: @User: Je ne peux pas vérifier la météo en temps réel, mais je peux te donner des infos générales sur Paris! 🌍
```

### 2. Divertissement
```
User: Raconte-moi une histoire
Bot: @User: Il était une fois, dans un monde virtuel appelé Highrise, un assistant IA qui aidait tous les joueurs... ✨
```

### 3. Questions & Réponses
```
User: Comment fonctionne Highrise?
Bot: @User: Highrise est un jeu social où tu peux créer ton avatar, décorer ta maison et rencontrer des amis! 🏠
```

### 4. Conversation naturelle
```
User: Je m'ennuie
Bot: @User: Que dirais-tu d'explorer la room, de faire des emotes ou de discuter avec d'autres joueurs? 😊
```

## ⚙️ Personnalisation

### Modifier la personnalité

Éditez le contexte dans `bot.py` (ligne ~156) :
```python
context = f"""Tu es [VOTRE DESCRIPTION ICI].
Tu t'appelles [NOM DU BOT].
[AUTRES INSTRUCTIONS]"""
```

### Modifier la longueur des réponses

Changez la limite (ligne ~167) :
```python
if len(response) > 200:  # Changez 200 par votre valeur
    response = response[:197] + "..."
```

### Ajouter des filtres

Ajoutez des conditions dans `on_chat` :
```python
# Ignorer certains mots
if "spam" in message.lower():
    return

# Répondre seulement si mentionné
if "@bot" not in message.lower():
    return
```

## 🚀 Avantages

### Pour les utilisateurs
- ✅ Plus besoin de mémoriser des commandes
- ✅ Conversation naturelle et fluide
- ✅ Réponses intelligentes et contextuelles
- ✅ Disponible 24/7

### Pour les admins
- ✅ Commandes protégées et organisées
- ✅ Logs détaillés des interactions
- ✅ Contrôle total via `!admin`
- ✅ Facile à personnaliser

## 📈 Statistiques

Le bot continue de tracker :
- Messages envoyés par utilisateur
- Emotes effectuées
- Tips reçus
- Temps de présence

Accessible via : `!admin stats`

## 🔄 Retour à l'ancien mode

Si vous voulez revenir au mode commandes :

1. Restaurez l'ancien `on_chat` :
```python
async def on_chat(self, user: User, message: str) -> None:
    if message.startswith('!'):
        await self.handle_command(user, message)
```

2. Supprimez la fonction `respond_with_ai`

## 💡 Conseils

### Performance
- Le bot répond à TOUS les messages, cela peut générer beaucoup de requêtes API
- Surveillez votre quota Gemini sur Google AI Studio
- Considérez ajouter un cooldown si nécessaire

### Modération
- Le bot répond à tout le monde sans filtre
- Ajoutez une liste noire si besoin
- Surveillez les conversations pour détecter les abus

### Optimisation
- Les réponses sont limitées à 200 caractères
- Le contexte est envoyé à chaque requête
- Considérez un système de cache pour les questions fréquentes

## 🆘 Dépannage

### Le bot ne répond pas
1. Vérifiez que Gemini est configuré : `python test_gemini.py`
2. Vérifiez les logs : `[AI] Generation reponse...`
3. Vérifiez votre clé API Gemini

### Le bot répond à ses propres messages
Vérifiez que le filtre est actif dans `on_chat` :
```python
if user.username == "bot" or user.username.lower().startswith("bot"):
    return
```

### Réponses trop longues
Ajustez la limite dans `respond_with_ai` :
```python
if len(response) > 200:
    response = response[:197] + "..."
```

## 📚 Fichiers modifiés

- ✅ `bot.py` - Logique conversationnelle
- ✅ `MODE-CONVERSATIONNEL.md` - Ce document

## 🎉 Conclusion

Votre bot est maintenant un véritable assistant IA conversationnel ! Les utilisateurs peuvent lui parler naturellement et recevoir des réponses intelligentes et contextuelles.

**Profitez de votre nouveau chatbot IA ! 🤖✨**
