# 🚀 Guide du Bot Highrise Avancé

## ✅ Fichiers Créés

1. **`emotes_complete.py`** - 150+ emotes avec noms espacés
2. **`roles.py`** - Système de rôles et permissions
3. **`anchors.py`** - Points de téléportation nommés
4. **`bot_advanced.py`** - Bot complet (à créer)

## 🎯 Nouvelles Fonctionnalités

### 1️⃣ MODÉRATION COMPLÈTE

```python
# Kick
!kick @user [raison]
Exemple: !kick @Spammer Spam

# Ban
!ban @user [durée_minutes] [raison]
Exemple: !ban @Toxic 60 Comportement toxique

# Mute
!mute @user [durée_minutes] [raison]
Exemple: !mute @Loud 30 Trop bruyant

# Unban
!unban @user
Exemple: !unban @Reformed
```

### 2️⃣ TÉLÉPORTATION AVANCÉE

```python
# Liste des points
!tele list
!tele points

# Téléporter à un point nommé
!tele spawn
!tele vip
!tele floor2
!tele dance

# Téléporter un utilisateur
!tele @user spawn
!tele @user 10 5 0

# Ajouter un point
!tele add <nom> <x> <y> <z> [description]
Exemple: !tele add party 15 0 0 Zone fête

# Supprimer un point
!tele remove <nom>
```

### 3️⃣ EMOTES AVANCÉES

```python
# Noms avec espaces
!emote ghost float
!emote zombie run
!emote snow angel
!emote punk guitar

# Raccourcis rapides
!wave @user
!kiss @user
!hug @user
!heart @user
!clap @user
!thumbsup @user

# Liste complète
!emote list
!emote fast
```

### 4️⃣ SYSTÈME DE RÔLES

```python
# Voir son rôle
!role
!myrole

# Voir le rôle de quelqu'un
!role @user

# Liste des rôles
!role list

# Donner un rôle (admin only)
!setrole @user <role>
Exemple: !setrole @Helper moderator

# Rôles disponibles:
- OWNER - Propriétaire (toutes permissions)
- ADMIN - Administrateur (presque tout)
- MODERATOR - Modérateur (kick, mute, teleport)
- VIP - VIP (teleport, emotes)
- USER - Utilisateur (basique)
```

### 5️⃣ LEADERBOARDS AVANCÉS

```python
# Leaderboard général
!lb
!leaderboard

# Par catégorie
!lb time      - Temps passé
!lb tips      - Tips envoyés
!lb chat      - Messages envoyés
!lb emotes    - Emotes effectuées

# Reset (admin only)
!lb reset
```

### 6️⃣ COMMANDES FUN

```python
# 8ball
!8ball <question>
Exemple: !8ball Est-ce que je vais gagner?

# Rate
!rate @user
Exemple: !rate @Alice

# Roast
!roast @user
Exemple: !roast @Bob

# Love
!love @user1 @user2
Exemple: !love @Alice @Bob

# Match
!match @user
Exemple: !match @Charlie

# Duel
!duel @user
Exemple: !duel @Enemy
```

### 7️⃣ WALLET & TIPS

```python
# Voir son wallet
!wallet
!balance

# Envoyer un tip
!tip @user <montant>
Exemple: !tip @Helper 10

# Montants disponibles:
1, 5, 10, 50, 100, 500, 1000, 5000, 10000
```

### 8️⃣ INVENTAIRE & OUTFIT

```python
# Voir son inventaire
!inventory
!inv

# Voir son outfit
!outfit

# Changer d'outfit (admin)
!changeoutfit
```

## 📊 Permissions par Rôle

| Permission | USER | VIP | MOD | ADMIN | OWNER |
|------------|------|-----|-----|-------|-------|
| Emotes | ✅ | ✅ | ✅ | ✅ | ✅ |
| Teleport self | ✅ | ✅ | ✅ | ✅ | ✅ |
| Teleport others | ❌ | ❌ | ✅ | ✅ | ✅ |
| Kick | ❌ | ❌ | ✅ | ✅ | ✅ |
| Ban | ❌ | ❌ | ❌ | ✅ | ✅ |
| Mute | ❌ | ❌ | ✅ | ✅ | ✅ |
| Announce | ❌ | ❌ | ❌ | ✅ | ✅ |
| Reset stats | ❌ | ❌ | ❌ | ❌ | ✅ |

## 🎮 Exemples d'Utilisation

### Scénario 1 : Modération
```
Moderator: !kick @Spammer Spam
Bot: "Spammer a été expulsé. Raison: Spam"

Admin: !ban @Toxic 60 Comportement toxique
Bot: "Toxic a été banni pour 60 minutes. Raison: Comportement toxique"

Moderator: !mute @Loud 30
Bot: "Loud a été mute pour 30 minutes"
```

### Scénario 2 : Téléportation
```
User: !tele list
Bot: "Points disponibles: spawn, center, vip, floor2, dance, chill"

User: !tele vip
Bot: "Téléporté à vip!"

Admin: !tele @NewUser spawn
Bot: "NewUser téléporté à spawn!"
```

### Scénario 3 : Emotes Avancées
```
User: !emote ghost float
Bot: [fait l'emote ghost float]

User: !kiss @Alice
Bot: [fait un bisou à Alice]

User: !wave @Everyone
Bot: [fait coucou à Everyone]
```

### Scénario 4 : Rôles
```
User: !role
Bot: "Votre rôle: USER"

Admin: !setrole @Helper moderator
Bot: "Helper est maintenant MODERATOR"

User: !role @Helper
Bot: "Helper: MODERATOR"
```

### Scénario 5 : Fun
```
User: !8ball Vais-je gagner?
Bot: "🎱 Oui, absolument!"

User: !rate @Alice
Bot: "Je donne à Alice un 9/10! ⭐"

User: !love @Bob @Charlie
Bot: "💕 Bob et Charlie: 87% compatibles!"
```

## 🔧 Configuration

### 1. Fichier .env
```env
BOT_TOKEN=votre_token
ROOM_ID=votre_room_id
ADMIN_IDS=id1,id2,id3
OWNER_ID=votre_id
```

### 2. Fichier anchors.json (optionnel)
```json
{
  "spawn": {"x": 0, "y": 0, "z": 0, "description": "Point d'apparition"},
  "vip": {"x": 20, "y": 0, "z": 0, "description": "Zone VIP"},
  "floor2": {"x": 0, "y": 5, "z": 0, "description": "Étage 2"}
}
```

## 🚀 Lancer le Bot Avancé

```powershell
# Méthode 1 : Commande directe
python -m highrise bot_advanced:AdvancedBot 680ab18546b31625a94de2e6 057565bd7bda6ac37029f5817ea7c2f6d447179cdfa65771e41284ed5f5d6090

# Méthode 2 : Script de lancement (à créer)
python start_advanced.py
```

## 📝 Prochaines Étapes

1. ✅ Créer `bot_advanced.py` avec toutes les commandes
2. ✅ Tester les fonctionnalités
3. ✅ Ajuster les points de téléportation selon votre room
4. ✅ Configurer les rôles des utilisateurs

## 💡 Astuces

- Utilisez `!help` pour voir toutes les commandes
- Les noms d'emotes supportent les espaces maintenant
- Les points de téléportation sont personnalisables
- Le système de rôles est flexible

---

**Votre bot est maintenant 10x plus puissant ! 🚀**
