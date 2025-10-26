# 💘 Commande !flirt - Accessible à tous

## 🎯 Description

La commande `!flirt` est maintenant **accessible à TOUS les utilisateurs** de la room ! N'importe qui peut draguer quelqu'un avec l'aide de l'IA.

---

## 🎮 Utilisation

### Syntaxe (pour tous les users)
```
!flirt <username_femme>
```

### Exemples
```
!flirt momo
!flirt sandra_beauty
!flirt lisa_angel
!flirt marie_belle
```

---

## 💬 Résultat

### Dans le chat public
Le bot génère et envoie un message de drague romantique :
```
Hey momo, t'es comme le soleil... tu illumines ma journee 🌹✨
```

### En DM (confirmation)
L'utilisateur qui a lancé la commande reçoit une confirmation :
```
💘 Message de drague envoyé!
De: john_doe
Pour: momo
Message: Hey momo, t'es comme le soleil...
```

### Logs
```
[FLIRT] Generation message de john_doe vers momo...
[FLIRT] Message envoyé: Hey momo, t'es comme le soleil... tu illumines ma journee 🌹✨
```

---

## 🎭 Scénarios d'utilisation

### Scénario 1 : John veut draguer Momo
```
John: !flirt momo
Bot: Hey momo, ton sourire pourrait faire fondre la glace... et mon coeur 💕
John (DM): 💘 Message de drague envoyé!
```

### Scénario 2 : Alex veut draguer Sandra
```
Alex: !flirt sandra_beauty
Bot: sandra_beauty, t'es pas juste belle... t'es une oeuvre d'art qui marche 🌹✨
Alex (DM): 💘 Message de drague envoyé!
```

### Scénario 3 : Mike est timide
```
Mike: !flirt lisa_angel
Bot: lisa_angel, si t'étais une étoile, t'éclairerais tout le ciel 💫
Mike (DM): 💘 Message de drague envoyé!
```

---

## 🎨 Style des messages

### Caractéristiques
- ✅ Romantique mais pas trop lourd
- ✅ Charmant et flatteur
- ✅ Avec un peu d'humour
- ✅ Pas vulgaire, reste classe
- ✅ Maximum 140 caractères
- ✅ Emojis romantiques : 🌹💕✨💘❤️💫😍

### Exemples de messages générés

```
Hey momo, ton sourire pourrait faire fondre la glace... et mon coeur 💕

sandra_beauty, t'es pas juste belle... t'es une oeuvre d'art qui marche 🌹✨

lisa_angel, si t'étais une étoile, t'éclairerais tout le ciel 💫

marie_belle, ton regard me fait voyager sans bouger... magique 💘

momo, t'es le genre de fille qui rend les autres jalouses juste en existant 😍

sandra_beauty, t'es comme une chanson douce... impossible de t'oublier 🎵💕

lisa_angel, chaque fois que je te vois, le monde devient plus beau 🌹

momo, t'es la raison pour laquelle les poètes écrivent des vers 📝✨
```

---

## 🔒 Commande admin (optionnelle)

Les admins peuvent toujours utiliser la version avancée pour faire draguer quelqu'un d'autre :

### Syntaxe admin
```
!admin flirt <username_homme> <username_femme>
```

### Exemple
```
!admin flirt shy_guy beautiful_girl
```
→ Le bot envoie un message de la part de shy_guy vers beautiful_girl

---

## 📊 Différences entre les deux commandes

| Commande | Qui peut l'utiliser | Syntaxe | De la part de |
|----------|---------------------|---------|---------------|
| `!flirt <femme>` | **Tous les users** | `!flirt momo` | L'utilisateur lui-même |
| `!admin flirt <homme> <femme>` | **Admins seulement** | `!admin flirt john momo` | N'importe qui |

---

## 💡 Cas d'usage

### 1. Draguer quelqu'un
```
User: !flirt momo
```
→ Message romantique de la part de User vers momo

### 2. Briser la glace
```
User: !flirt new_girl
```
→ Message charmant pour commencer une conversation

### 3. Faire rire / animer
```
User: !flirt friend_girl
```
→ Message romantique pour rigoler entre amis

### 4. Être romantique
```
User: !flirt girlfriend
```
→ Message doux pour sa copine

---

## ⚠️ Erreurs possibles

### Pas de username spécifié
```
User: !flirt
Bot (DM): Usage: !flirt <username_femme>
          Exemple: !flirt momo
          Le bot écrira un message de drague de ta part !
```

### IA non disponible
```
Bot (DM): ❌ IA Gemini non disponible
```
→ Vérifie que GEMINI_API_KEY est configuré dans .env

---

## 🔧 Code source

### Détection de la commande (ligne 164-167)
```python
# Commande !flirt accessible à tous
if message.startswith('!flirt '):
    await self.handle_flirt_command(user, message)
    return
```

### Fonction handle_flirt_command (ligne 2454-2478)
```python
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
```

### Fonction generate_and_send_flirt (ligne 2504-2542)
```python
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
```

---

## 🎯 Avantages

### Pour les utilisateurs
- ✅ Accessible à tous (pas besoin d'être admin)
- ✅ Facile à utiliser : `!flirt <username>`
- ✅ Messages romantiques générés par IA
- ✅ Aide les timides à draguer
- ✅ Anime la room avec des messages charmants

### Pour les admins
- ✅ Gardent la version avancée `!admin flirt`
- ✅ Peuvent faire draguer n'importe qui
- ✅ Contrôle total

---

## 📋 Résumé

| Élément | Détail |
|---------|--------|
| **Commande** | `!flirt <username_femme>` |
| **Accès** | Tous les utilisateurs |
| **Résultat** | Message romantique dans le chat |
| **Confirmation** | DM privé |
| **Style** | Romantique, charmant, classe |
| **Limite** | 140 caractères |

---

## ✅ Test

### 1. N'importe quel user peut tester
```
!flirt momo
```

### 2. Vérifier le chat public
```
Hey momo, ton sourire pourrait faire fondre la glace... et mon coeur 💕
```

### 3. Vérifier le DM
```
💘 Message de drague envoyé!
De: john_doe
Pour: momo
Message: Hey momo, ton sourire pourrait faire fondre...
```

---

**Tout le monde peut maintenant draguer avec style grâce à l'IA ! 💘✨**
