# 🚀 Guide de Démarrage Rapide - Bot Python

## ✅ Étapes Rapides

### 1. Vérifier Python

```bash
python --version
```

Si Python n'est pas installé : https://www.python.org/downloads/

### 2. Installer les Dépendances

```bash
cd "d:\Desktop\hr bot python"
pip install -r requirements.txt
```

### 3. Configurer le Bot

Ouvrez le fichier `.env` et remplissez avec vos identifiants :

```env
BOT_TOKEN=057565bd7b... (votre token COMPLET)
ROOM_ID=680ab18546b31625a94de2e6
ADMIN_IDS=votre_id_utilisateur
```

⚠️ **IMPORTANT** : Le token doit être COMPLET (~50-60 caractères), pas juste les 10 premiers !

### 4. Lancer le Bot

```bash
python bot.py
```

## ✅ Logs Attendus

```
🚀 Démarrage du bot Python...
🔑 Token: 057565bd7b...
🏠 Room: 680ab18546b31625a94de2e6
✅ Bot connecté: [nom de votre room]
🆔 Bot ID: [id]
🎭 100 emotes disponibles
📨 Message de bienvenue envoyé
```

## 🎮 Tester le Bot

1. Allez dans Highrise
2. Entrez dans votre room
3. Le bot devrait être là !
4. Tapez `!help` dans le chat
5. Le bot répond ! 🎉

## 📋 Commandes à Tester

```
!help          - Voir l'aide
!dance         - Le bot danse
!emote wave    - Le bot fait coucou
!roll          - Lancer un dé
!users         - Nombre d'utilisateurs
!stats         - Vos statistiques
!ping          - Test de connexion
```

## 🐛 Problèmes Courants

### "python n'est pas reconnu"

**Solution :** Python n'est pas installé ou pas dans le PATH
```bash
# Téléchargez Python depuis python.org
# Réinstallez en cochant "Add Python to PATH"
```

### "No module named 'highrise'"

**Solution :**
```bash
pip install -r requirements.txt
```

### Le bot ne se connecte pas

**Solution :**
- Vérifiez que le token est COMPLET dans `.env`
- Vérifiez le Room ID
- Assurez-vous que le bot a les droits "Designer"

## 🎯 Prochaines Étapes

Une fois que le bot fonctionne :

1. ✅ Testez toutes les commandes
2. ✅ Ajoutez votre Admin ID dans `.env`
3. ✅ Testez les commandes admin (!announce, !parade)
4. ✅ Personnalisez les messages
5. ✅ Déployez sur un serveur pour le 24/7

## 🚀 Déploiement 24/7

Pour faire tourner le bot en permanence :
- **Replit** : Facile, gratuit (avec keep-alive)
- **Railway** : Performant, 5$/mois
- **Oracle Cloud** : Gratuit à vie

---

**Le bot Python fonctionne parfaitement ! 🐍**

Contrairement au SDK JavaScript qui est buggé, le SDK Python est stable et officiel.
