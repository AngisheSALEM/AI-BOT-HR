# 📝 Comment changer la bio d'un bot Highrise

## 🎯 Méthode

Le SDK Highrise fournit la méthode `set_bot_profile()` pour modifier la bio du bot.

## 💻 Code

### Option 1 : Changer la bio au démarrage

Ajoute cette fonction dans `bot.py` dans la méthode `on_start()` :

```python
async def on_start(self, session_metadata: SessionMetadata):
    print(f"[OK] Bot connecte: {session_metadata.user_id}")
    print(f"[ROOM] Room ID: {session_metadata.room_info.room_id}")
    print(f"[AI] Mode: Assistant IA conversationnel")
    print(f"[AMOUR] Mode amoureux active pour {self.love_target}")
    
    # Changer la bio du bot
    try:
        await self.highrise.set_bot_profile(
            bio="🤖 Savant - Assistant IA intelligent\n💬 Mentionne-moi avec @s ou envoie-moi un DM!\n🎭 240+ emotes | 🎮 Jeux | 📊 Stats"
        )
        print("[BIO] Bio du bot mise à jour")
    except Exception as e:
        print(f"[ERREUR] Impossible de changer la bio: {e}")
    
    # ... reste du code
```

### Option 2 : Commande admin pour changer la bio

Ajoute cette commande dans les commandes admin :

```python
async def cmd_setbio(self, user: User, params):
    """Changer la bio du bot"""
    if not params:
        await self.highrise.send_whisper(user.id, "Usage: !admin setbio <nouvelle bio>")
        return
    
    new_bio = " ".join(params)
    
    try:
        await self.highrise.set_bot_profile(bio=new_bio)
        await self.highrise.send_whisper(user.id, f"✅ Bio changée:\n{new_bio}")
        print(f"[BIO] Bio changée par {user.username}: {new_bio}")
    except Exception as e:
        await self.highrise.send_whisper(user.id, f"❌ Erreur: {e}")
        print(f"[ERREUR] Changement bio: {e}")
```

Puis ajoute dans le handler :

```python
elif subcmd == 'setbio':
    await self.cmd_setbio(user, subparams)
```

## 📋 Exemples de bio

### Bio simple
```python
bio="🤖 Bot Highrise | !help pour les commandes"
```

### Bio avec emojis
```python
bio="🤖 Savant IA\n💬 Parle-moi!\n🎭 Emotes | 🎮 Jeux"
```

### Bio détaillée
```python
bio="""🤖 Savant - Assistant IA
💬 Mentionne @s ou DM
🎭 240+ emotes
🎮 Jeux: !roll, !flip, !rps
📊 Stats: !stats, !leaderboard
🤖 IA: !ask, !ai, !joke"""
```

### Bio avec ligne de séparation
```python
bio="━━━━━━━━━━━━━━━\n🤖 BOT SAVANT\n━━━━━━━━━━━━━━━\n💬 DM ou @s\n🎭 !commands"
```

## ⚠️ Limites

### Longueur maximale
- La bio Highrise a une **limite de caractères** (environ 150-200 caractères)
- Si la bio est trop longue, elle sera tronquée

### Caractères spéciaux
- ✅ Emojis supportés
- ✅ Retours à la ligne (`\n`) supportés
- ✅ Caractères spéciaux supportés

### Fréquence de changement
- ⚠️ Ne change pas la bio trop souvent (rate limiting possible)
- ✅ Une fois au démarrage est recommandé
- ✅ Ou via commande admin quand nécessaire

## 🎯 Implémentation complète

Voici le code complet à ajouter dans `bot.py` :

### 1. Dans `on_start()` (ligne ~70)

```python
async def on_start(self, session_metadata: SessionMetadata):
    print(f"[OK] Bot connecte: {session_metadata.user_id}")
    print(f"[ROOM] Room ID: {session_metadata.room_info.room_id}")
    print(f"[AI] Mode: Assistant IA conversationnel")
    print(f"[AMOUR] Mode amoureux active pour {self.love_target}")
    
    # Changer la bio du bot
    try:
        bot_bio = """🤖 Savant - Assistant IA
💬 Mentionne @s ou DM!
🎭 240+ emotes | 🎮 Jeux
📊 !commands pour la liste"""
        
        await self.highrise.set_bot_profile(bio=bot_bio)
        print(f"[BIO] Bio mise à jour: {bot_bio[:50]}...")
    except Exception as e:
        print(f"[ERREUR] Bio: {e}")
    
    # ... reste du code
```

### 2. Ajouter la commande admin (ligne ~518)

Dans le handler des commandes admin, ajoute :

```python
elif subcmd == 'setbio':
    await self.cmd_setbio(user, subparams)
```

### 3. Ajouter la fonction (après les autres cmd_)

```python
async def cmd_setbio(self, user: User, params):
    """Changer la bio du bot"""
    if not params:
        await self.highrise.send_whisper(user.id, 
            "Usage: !admin setbio <nouvelle bio>\n"
            "Exemple: !admin setbio 🤖 Bot IA | !help")
        return
    
    new_bio = " ".join(params)
    
    # Vérifier la longueur
    if len(new_bio) > 200:
        await self.highrise.send_whisper(user.id, 
            f"❌ Bio trop longue ({len(new_bio)} caractères)\n"
            f"Maximum: 200 caractères")
        return
    
    try:
        await self.highrise.set_bot_profile(bio=new_bio)
        await self.highrise.send_whisper(user.id, 
            f"✅ Bio changée ({len(new_bio)} caractères):\n{new_bio}")
        print(f"[BIO] Changée par {user.username}: {new_bio}")
    except Exception as e:
        await self.highrise.send_whisper(user.id, f"❌ Erreur: {e}")
        print(f"[ERREUR] Changement bio: {e}")
```

## 🧪 Test

### Tester au démarrage
1. Lance le bot
2. Vérifie les logs : `[BIO] Bio mise à jour`
3. Va sur le profil du bot dans Highrise
4. La bio devrait être mise à jour

### Tester avec la commande
```
!admin setbio 🤖 Nouvelle bio de test!
```

## 📊 Exemples de bio pour différents bots

### Bot de modération
```python
bio="🛡️ Bot Modération\n⚠️ Respect des règles\n👮 !help pour aide"
```

### Bot de jeux
```python
bio="🎮 Bot Jeux\n🎲 !roll | 🪙 !flip\n✊ !rps | 🎱 !8ball"
```

### Bot IA
```python
bio="🤖 Savant IA\n💬 @s ou DM\n🧠 !ask | 😂 !joke\n💡 !fact | ✨ !advice"
```

### Bot événements
```python
bio="🎉 Bot Événements\n📅 Prochains events\n🎊 !events pour info"
```

## ⚙️ Configuration avancée

### Bio dynamique selon l'heure
```python
from datetime import datetime

async def update_bio_with_time(self):
    hour = datetime.now().hour
    
    if 6 <= hour < 12:
        greeting = "☀️ Bonjour!"
    elif 12 <= hour < 18:
        greeting = "🌤️ Bon après-midi!"
    else:
        greeting = "🌙 Bonsoir!"
    
    bio = f"{greeting}\n🤖 Savant IA\n💬 @s ou DM"
    
    try:
        await self.highrise.set_bot_profile(bio=bio)
        print(f"[BIO] Mise à jour: {greeting}")
    except Exception as e:
        print(f"[ERREUR] Bio: {e}")
```

### Bio avec compteur d'utilisateurs
```python
async def update_bio_with_users(self):
    try:
        users = await self.highrise.get_room_users()
        user_count = len(users.content)
        
        bio = f"🤖 Savant IA\n👥 {user_count} utilisateurs\n💬 @s ou DM"
        
        await self.highrise.set_bot_profile(bio=bio)
        print(f"[BIO] Mise à jour: {user_count} users")
    except Exception as e:
        print(f"[ERREUR] Bio: {e}")
```

---

## ✅ Résumé

**Pour changer la bio du bot :**

1. **Au démarrage** : Ajoute `await self.highrise.set_bot_profile(bio="...")` dans `on_start()`
2. **Avec commande** : Crée `cmd_setbio()` et ajoute `!admin setbio`
3. **Limite** : ~200 caractères max
4. **Format** : Emojis et `\n` supportés

**Commande finale :**
```
!admin setbio 🤖 Savant IA | 💬 @s ou DM | 🎭 !commands
```
