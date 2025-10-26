# 🐍 Bot Highrise Python - Version Complète

Bot Highrise avec **TOUTES** les fonctionnalités en Python !

## ✨ Fonctionnalités

- ✅ **240+ emotes** organisées par catégories
- ✅ **Système de téléportation** et déplacement
- ✅ **Commandes administrateur** (kick, announce, parade, rain)
- ✅ **Jeux intégrés** (dés, pile/face, PFC)
- ✅ **Statistiques utilisateurs** en temps réel
- ✅ **Leaderboard** des plus actifs
- ✅ **Animations spéciales** (parade, pluie d'emotes)
- ✅ **Messages de bienvenue** personnalisés
- ✅ **Réactions automatiques** aux tips et emotes

## 📦 Installation

### 1. Installer Python

Si vous n'avez pas Python :
- Téléchargez depuis : https://www.python.org/downloads/
- Version recommandée : Python 3.10 ou supérieur
- ⚠️ Cochez "Add Python to PATH" lors de l'installation

### 2. Vérifier l'installation

```bash
python --version
# Devrait afficher: Python 3.10.x ou supérieur
```

### 3. Installer les dépendances

```bash
cd "d:\Desktop\hr bot python"
pip install -r requirements.txt
```

## ⚙️ Configuration

### 1. Créer le fichier .env

Le fichier `.env` existe déjà. Ouvrez-le et remplissez :

```env
BOT_TOKEN=votre_token_complet_ici
ROOM_ID=votre_room_id_ici
ADMIN_IDS=votre_id_utilisateur
```

### 2. Obtenir vos identifiants

**BOT_TOKEN :**
1. https://create.highrise.game
2. Dashboard → Bots & API Keys
3. Create Bot → Generate API Token
4. Copiez le token COMPLET (~50-60 caractères)

**ROOM_ID :**
1. App Highrise → Entrez dans votre room
2. Info (ℹ️) → Share this Room
3. Copiez l'ID depuis le lien

**ADMIN_IDS :**
1. App Highrise → Votre profil
2. Share Profile
3. Copiez votre ID depuis le lien

## 🚀 Démarrage

```bash
python bot.py
```

Vous devriez voir :
```
✅ Bot connecté: [nom de votre room]
🆔 Bot ID: [id]
🎭 100 emotes disponibles
📨 Message de bienvenue envoyé
```

## 📋 Commandes Disponibles

### 🎭 Emotes (240+)

| Commande | Description |
|----------|-------------|
| `!emotes` | Liste des catégories |
| `!emotes <catégorie>` | Emotes d'une catégorie |
| `!emote <nom>` | Faire une emote |
| `!dance` | Danse aléatoire |
| `!random` | Emote aléatoire |

**Catégories** : dances, social, emotions, poses, special, sports, fun, cute, winter

**Exemples** :
- `!emote savage` - Danse Savage
- `!emote wave` - Faire coucou
- `!emote happy` - Être content
- `!dance` - Danse aléatoire

### 👥 Social

| Commande | Description |
|----------|-------------|
| `!users` | Nombre d'utilisateurs |
| `!stats` | Vos statistiques |
| `!leaderboard` | Top 5 des plus actifs |
| `!greet <user>` | Saluer quelqu'un |

### 🎮 Jeux

| Commande | Description |
|----------|-------------|
| `!roll [max]` | Lancer un dé (1-100 par défaut) |
| `!flip` | Pile ou face |
| `!rps <choix>` | Pierre/papier/ciseaux |

**Exemples** :
- `!roll` - Dé de 1 à 100
- `!roll 50` - Dé de 1 à 50
- `!rps pierre` - Jouer pierre

### ℹ️ Informations

| Commande | Description |
|----------|-------------|
| `!time` | Heure et date |
| `!ping` | Test de connexion |
| `!uptime` | Temps en ligne |
| `!help` | Aide rapide |
| `!commands` | Liste complète |

### 🚶 Déplacement

| Commande | Description |
|----------|-------------|
| `!tp <x> <y> [z]` | Téléporter le bot |
| `!walk <x> <y> [z]` | Marcher vers position |

**Exemples** :
- `!tp 5 10` - Téléporter à (5, 10, 0)
- `!walk 0 0` - Marcher vers (0, 0, 0)

### 👑 Commandes Admin

| Commande | Description |
|----------|-------------|
| `!announce <msg>` | Faire une annonce |
| `!kick <user>` | Expulser (en dev) |
| `!parade` | Parade d'emotes automatique |
| `!rain <emote>` | Pluie d'emotes |

**Exemples** :
- `!announce Bienvenue à tous!`
- `!parade` - Lance une parade automatique
- `!rain happy` - Pluie d'emotes happy

## 🎯 Fonctionnalités Automatiques

### Messages de Bienvenue
Le bot accueille automatiquement chaque nouvel arrivant avec :
- Message personnalisé aléatoire
- Emote de bienvenue (wave)

### Réactions aux Tips
Le bot réagit automatiquement aux tips avec :
- Message de remerciement
- Emote hearteyes

### Statistiques en Temps Réel
Le bot track automatiquement :
- Nombre de messages
- Nombre d'emotes
- Tips envoyés
- Temps passé

## 📁 Structure du Projet

```
hr bot python/
├── bot.py              # Bot principal
├── emotes.py           # 240+ emotes
├── requirements.txt    # Dépendances Python
├── .env               # Configuration (à remplir)
├── .env.example       # Exemple de configuration
└── README.md          # Ce fichier
```

## 🐛 Dépannage

### "ModuleNotFoundError: No module named 'highrise'"

**Solution :**
```bash
pip install -r requirements.txt
```

### "BOT_TOKEN is required"

**Solution :**
- Vérifiez que le fichier `.env` existe
- Vérifiez que `BOT_TOKEN` est rempli
- Le token doit être complet (~50-60 caractères)

### Le bot ne se connecte pas

**Solution :**
- Vérifiez le token (doit être complet)
- Vérifiez le Room ID
- Assurez-vous que le bot a les droits "Designer"

### Le bot ne répond pas aux commandes

**Solution :**
- Vérifiez que le bot est bien connecté (logs)
- Les commandes doivent commencer par `!`
- Exemple : `!help` pas `help`

### Erreur de téléportation

**Solution :**
- Les coordonnées doivent être des nombres
- Exemple : `!tp 5 10` pas `!tp cinq dix`
- Certaines zones peuvent être inaccessibles

## 🎮 Exemples d'Utilisation

### Scénario 1 : Accueil Automatique
```
[User rejoint]
Bot: "Bienvenue User! 🎉"
Bot: [fait emote-wave]
```

### Scénario 2 : Jeu de Dés
```
User: !roll 100
Bot: "🎲 User: 42/100"
```

### Scénario 3 : Pierre-Papier-Ciseaux
```
User: !rps pierre
Bot: "✊✋✌️ Toi: pierre | Moi: ciseaux
Tu gagnes! 🎉"
```

### Scénario 4 : Parade Admin
```
Admin: !parade
Bot: "🎭 PARADE D'EMOTES!"
Bot: [fait wave, happy, bow, clap avec pauses]
Bot: "🎉 Parade terminée!"
```

## 🚀 Déploiement 24/7

Pour faire tourner le bot en permanence, consultez les guides d'hébergement :
- **Replit** : Facile, gratuit
- **Railway** : Performant, 5$/mois
- **Oracle Cloud** : Gratuit à vie, plus technique

## 📊 Comparaison Python vs JavaScript

| | **Python** | **JavaScript** |
|---|---|---|
| **Fonctionne** | ✅ Oui | ❌ SDK buggé |
| **Facilité** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Documentation** | ✅ Complète | ⚠️ Limitée |
| **Support** | ✅ Officiel | ⚠️ Communautaire |
| **Stabilité** | ✅ Stable | ❌ Bugs |

## 💡 Personnalisation

### Ajouter une Commande

Dans `bot.py`, ajoutez dans `handle_command` :
```python
elif cmd == 'macommande':
    await self.cmd_ma_commande(params)
```

Puis créez la fonction :
```python
async def cmd_ma_commande(self, params):
    await self.highrise.chat("Ma commande!")
```

### Modifier les Messages de Bienvenue

Dans `on_user_join`, modifiez la liste `greetings`.

### Ajouter des Emotes

Dans `emotes.py`, ajoutez dans le dictionnaire `EMOTES`.

## 📞 Support

Si vous avez des problèmes :
1. Vérifiez les logs dans le terminal
2. Vérifiez que Python est bien installé
3. Vérifiez que les dépendances sont installées
4. Vérifiez le fichier `.env`

## 🎉 C'est Prêt !

Votre bot Python est maintenant opérationnel avec toutes les fonctionnalités ! 🐍

**Commande pour lancer :**
```bash
python bot.py
```

Amusez-vous bien ! 🎮
