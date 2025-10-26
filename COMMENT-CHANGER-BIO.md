# 📝 Comment changer la bio du bot

## ⚠️ IMPORTANT : La bio ne peut PAS être modifiée via le SDK

Après recherche approfondie dans le SDK Highrise Python, **il n'existe AUCUNE méthode pour modifier la bio d'un bot via le code**.

### Méthodes disponibles dans le SDK
```python
# Méthodes Highrise disponibles:
chat()
send_whisper()
send_emote()
teleport()
walk_to()
get_my_outfit()
set_outfit()
get_inventory()
buy_item()
tip_user()
moderate_room()
# ... etc

# ❌ AUCUNE méthode pour la bio:
# set_my_bio() - N'EXISTE PAS
# update_bio() - N'EXISTE PAS
# change_bio() - N'EXISTE PAS
```

### API Web Highrise
L'API Web (https://webapi.highrise.game/) permet uniquement de **LIRE** les données, pas de les modifier :
- ✅ GET /users - Lire profil utilisateur
- ✅ GET /rooms - Lire infos room
- ✅ GET /items - Lire items
- ❌ POST/PUT/PATCH - Aucune méthode de modification

---

## ✅ SOLUTION : Changer la bio manuellement

### Étape 1 : Aller sur le site Highrise
```
https://highrise.game/account/settings
```

### Étape 2 : Se connecter avec le compte du bot
- Username du bot : (ton username bot)
- Mot de passe : (ton mot de passe bot)

### Étape 3 : Aller dans Settings (Paramètres)
- Cliquer sur l'icône de profil en haut à droite
- Sélectionner "Settings" ou "Paramètres"

### Étape 4 : Modifier la bio
- Trouver la section "Bio" ou "About Me"
- Copier-coller la bio recommandée ci-dessous

---

## 📝 Bio recommandée

### Version complète (si assez de place)
```
🤖 Savant - Chat Bot IA

Créé par @sylver_ralx_lm

💬 Commandes:
• Taguez-moi: @s + votre question
• Message privé: DM direct
• !flirt <crush> - Message de drague

❓ Posez-moi toutes vos questions!
Je peux répondre à tout 😊✨
```

### Version courte (si limite de caractères)
```
🤖 Savant - Chat Bot IA
Créé par @sylver_ralx_lm

💬 Commandes: @s + question | DM direct | !flirt <crush>

❓ Posez-moi toutes vos questions! 😊✨
```

### Version ultra-courte (si très limité)
```
🤖 Bot IA par @sylver_ralx_lm
Commandes: @s | DM | !flirt
Posez vos questions! 😊
```

---

## 🎯 Contenu de la bio

### Éléments essentiels
1. **Nom du bot** : Savant
2. **Type** : Chat Bot IA
3. **Créateur** : @sylver_ralx_lm
4. **Commandes** :
   - @s + question (tag dans le chat)
   - DM direct (message privé)
   - !flirt <crush> (drague)
5. **Invitation** : Posez-moi toutes vos questions!

---

## 📱 Capture d'écran (guide visuel)

### 1. Page de connexion
```
https://highrise.game/login
```
→ Entrer les identifiants du bot

### 2. Menu Settings
```
Profil → Settings → Bio
```

### 3. Champ Bio
```
[Champ texte]
Entrer la bio ici
[Sauvegarder]
```

---

## ⚙️ Code dans bot.py

### Ce qui a été retiré
```python
# ❌ ANCIEN CODE (ne fonctionne pas)
try:
    bio_text = "🤖 Savant - Chat Bot IA..."
    await self.highrise.set_my_bio(bio_text)  # Cette méthode n'existe pas!
    print(f"[BIO] Bio du profil définie")
except Exception as e:
    print(f"[ERREUR] Bio: {e}")
```

### Ce qui a été ajouté
```python
# ✅ NOUVEAU CODE (ligne 146-153)
# NOTE: La bio ne peut PAS être modifiée via le SDK Highrise
# Il faut la changer manuellement sur le site web: https://highrise.game/account/settings
# Bio recommandée:
# 🤖 Savant - Chat Bot IA
# Créé par @sylver_ralx_lm
# 💬 Commandes: @s + question | DM direct | !flirt <crush>
# ❓ Posez-moi toutes vos questions! 😊✨
print("[INFO] Pour changer la bio, allez sur https://highrise.game/account/settings")
```

---

## 📋 Logs au démarrage

### Avant (avec erreur)
```
[ERREUR] Bio: 'Highrise' object has no attribute 'set_my_bio'
```

### Maintenant (avec info)
```
[INFO] Pour changer la bio, allez sur https://highrise.game/account/settings
```

---

## 🔍 Recherche effectuée

### 1. Méthodes du SDK
```python
# Toutes les méthodes de BaseBot:
before_start
on_channel
on_chat
on_emote
on_message
on_moderate
on_reaction
on_start
on_tip
on_user_join
on_user_leave
on_user_move
on_voice_change
on_whisper

# Toutes les méthodes de Highrise:
add_user_to_voice
buy_item
buy_room_boost
buy_voice_time
call_in
change_backpack
change_room_privilege
chat
get_backpack
get_conversations
get_inventory
get_messages
get_my_outfit
get_room_privilege
get_room_users
get_user_outfit
get_voice_status
get_wallet
leave_conversation
moderate_room
move_user_to_room
react
remove_user_from_voice
send_channel
send_emote
send_message
send_message_bulk
send_whisper
set_indicator
set_outfit
teleport
tip_user
walk_to

# ❌ Aucune méthode pour la bio!
```

### 2. Documentation officielle
- GitHub : https://github.com/pocketzworld/python-bot-sdk
- Web API : https://webapi.highrise.game/
- Forum : https://createforum.highrise.game/

**Résultat :** Aucune mention de modification de bio via code

### 3. API Web
- Endpoints disponibles : Users, Rooms, Posts, Items, Grabs
- Méthodes : GET uniquement (lecture seule)
- ❌ Pas de POST/PUT/PATCH pour modifier

---

## 💡 Pourquoi la bio ne peut pas être modifiée via code ?

### Raisons probables
1. **Sécurité** : Empêcher les bots de changer leur bio automatiquement
2. **Spam** : Éviter que des bots changent leur bio en boucle
3. **Modération** : Permettre aux admins de contrôler le contenu
4. **Design** : La bio est considérée comme une info statique

### Ce qui peut être modifié via code
- ✅ Outfit (tenue)
- ✅ Position (téléportation)
- ✅ Messages (chat, whisper)
- ✅ Emotes
- ✅ Réactions
- ✅ Inventaire (acheter items)

### Ce qui ne peut PAS être modifié via code
- ❌ Bio
- ❌ Username
- ❌ Avatar de profil
- ❌ Paramètres de compte

---

## ✅ Résumé

| Élément | Modifiable via code ? | Comment le modifier ? |
|---------|----------------------|----------------------|
| **Bio** | ❌ NON | Manuellement sur le site web |
| **Outfit** | ✅ OUI | `set_outfit()` |
| **Position** | ✅ OUI | `teleport()` / `walk_to()` |
| **Messages** | ✅ OUI | `chat()` / `send_whisper()` |

---

## 🎯 Action requise

### Pour changer la bio du bot :
1. ✅ Va sur https://highrise.game/account/settings
2. ✅ Connecte-toi avec le compte du bot
3. ✅ Trouve la section "Bio"
4. ✅ Copie-colle la bio recommandée
5. ✅ Sauvegarde

### Bio à copier-coller :
```
🤖 Savant - Chat Bot IA
Créé par @sylver_ralx_lm

💬 Commandes: @s + question | DM direct | !flirt <crush>

❓ Posez-moi toutes vos questions! 😊✨
```

---

**La bio doit être changée MANUELLEMENT sur le site web Highrise ! 📝✨**
