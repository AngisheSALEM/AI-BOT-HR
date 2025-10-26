# 🚀 LANCER LE BOT - Guide Ultra Simple

## ✅ Étape 1 : Configurer le .env

Ouvrez le fichier `.env` et remplissez :

```env
BOT_TOKEN=votre_token_complet_ici
ROOM_ID=680ab18546b31625a94de2e6
ADMIN_IDS=votre_id_utilisateur
```

### Comment Obtenir le Token COMPLET ?

1. Allez sur https://create.highrise.game
2. Dashboard → Bots & API Keys
3. Votre bot → Generate API Token
4. **COPIEZ TOUT** (le token fait ~50-60 caractères)

Exemple de token complet :
```
057565bd7b4c8e9a2f1d3b6e8a9c2d4f5e7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2
```

## ✅ Étape 2 : Installer les Dépendances

Ouvrez PowerShell et tapez :

```powershell
cd "d:\Desktop\hr bot python"
pip install highrise-bot-sdk python-dotenv
```

Attendez que ça finisse (peut prendre 1-2 minutes).

## ✅ Étape 3 : Lancer le Bot

```powershell
python bot.py
```

## ✅ Étape 4 : Vérifier

Vous devriez voir :

```
🚀 Démarrage du bot Python...
🔑 Token: 057565bd7b...
🏠 Room: 680ab18546b31625a94de2e6
✅ Bot connecté: [nom de votre room]
🆔 Bot ID: [id]
🎭 100 emotes disponibles
📨 Message de bienvenue envoyé
```

## ✅ Étape 5 : Tester dans Highrise

1. Ouvrez Highrise
2. Allez dans votre room
3. Le bot est là !
4. Tapez : `!help`
5. Le bot répond ! 🎉

## 🎮 Commandes à Tester

```
!help          - Aide
!dance         - Danse aléatoire
!emote wave    - Faire coucou
!roll          - Lancer un dé
!flip          - Pile ou face
!users         - Nombre d'utilisateurs
!stats         - Vos statistiques
!ping          - Test
!emotes        - Liste des emotes
!tp 5 10       - Téléporter le bot
!follow @User  - Suivre quelqu'un
```

## 🐛 Problèmes Courants

### "ModuleNotFoundError: No module named 'highrise'"

**Solution :**
```powershell
pip install highrise-bot-sdk python-dotenv
```

### "BOT_TOKEN is required"

**Solution :**
- Le fichier `.env` n'existe pas OU
- Le `BOT_TOKEN` est vide OU
- Le token est incomplet

Vérifiez que le token fait ~50-60 caractères.

### Le bot ne se connecte pas

**Solution :**
1. Vérifiez que le token est COMPLET
2. Vérifiez le Room ID
3. Vérifiez que le bot a les droits "Designer"

### "Connection closed"

**Solution :**
- Token invalide → Régénérez-le
- Pas de droits → Donnez les droits "Designer" au bot

## 🛑 Arrêter le Bot

Dans le terminal où le bot tourne :
```
Ctrl + C
```

## 🔄 Relancer le Bot

```powershell
python bot.py
```

## 📝 Commandes Complètes

### Tout en Une Fois

```powershell
# 1. Aller dans le dossier
cd "d:\Desktop\hr bot python"

# 2. Installer (première fois seulement)
pip install highrise-bot-sdk python-dotenv

# 3. Lancer
python bot.py
```

## ✅ C'est Tout !

Votre bot est maintenant en ligne ! 🎉

---

**Besoin d'aide ?** Consultez `README.md` ou `GUIDE-DEMARRAGE.md`
