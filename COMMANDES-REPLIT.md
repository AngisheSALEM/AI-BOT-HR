# 🔧 Commandes Utiles pour Replit

## 📋 Accéder au Shell

Dans Replit, cliquer sur **"Shell"** dans la barre latérale (icône terminal)

---

## 🐍 Commandes Python

### Installer les Dépendances
```bash
pip install -r requirements.txt
```

### Installer un Package Spécifique
```bash
pip install highrise-bot-sdk==24.1.0
pip install google-generativeai==0.7.2
pip install python-dotenv==1.0.0
```

### Vérifier les Packages Installés
```bash
pip list
```

### Vérifier la Version de Python
```bash
python --version
```

### Lancer le Bot Manuellement
```bash
python main.py
```

### Tester un Module
```bash
python -c "from emotes import EMOTES; print(len(EMOTES))"
python -c "import highrise; print(highrise.__version__)"
```

---

## 📁 Commandes Fichiers

### Lister les Fichiers
```bash
ls -la
```

### Voir le Contenu d'un Fichier
```bash
cat main.py
cat requirements.txt
cat .replit
```

### Chercher un Fichier
```bash
find . -name "*.py"
find . -name "requirements.txt"
```

### Compter les Lignes de Code
```bash
wc -l *.py
```

---

## 🔍 Commandes de Débogage

### Vérifier les Variables d'Environnement
```bash
echo $BOT_TOKEN
echo $ROOM_ID
echo $ADMIN_USERNAMES
echo $GEMINI_API_KEY
```

**Note:** Les Secrets ne s'affichent pas dans le Shell pour des raisons de sécurité.

### Vérifier le Port
```bash
echo $PORT
```

### Tester la Connexion Internet
```bash
ping google.com -c 3
```

### Voir les Processus en Cours
```bash
ps aux
```

### Tuer un Processus (si le bot est bloqué)
```bash
pkill -f python
```

---

## 🧪 Commandes de Test

### Tester l'Import des Modules
```bash
python -c "import bot; print('✅ bot.py OK')"
python -c "import emotes; print('✅ emotes.py OK')"
python -c "import roles; print('✅ roles.py OK')"
python -c "import anchors; print('✅ anchors.py OK')"
python -c "import gemini_integration; print('✅ gemini_integration.py OK')"
```

### Tester Gemini
```bash
python -c "from gemini_integration import initialize_gemini; g = initialize_gemini(); print('✅ Gemini OK' if g else '❌ Gemini KO')"
```

### Compter les Emotes
```bash
python -c "from emotes import EMOTES; print(f'Emotes disponibles: {len(EMOTES)}')"
```

### Lister les Catégories d'Emotes
```bash
python -c "from emotes import EMOTE_CATEGORIES; print('Catégories:', list(EMOTE_CATEGORIES.keys()))"
```

---

## 🔄 Commandes Git (si connecté à GitHub)

### Voir le Statut
```bash
git status
```

### Voir les Changements
```bash
git diff
```

### Commit et Push
```bash
git add .
git commit -m "Update bot"
git push
```

### Pull les Derniers Changements
```bash
git pull
```

---

## 📊 Commandes de Monitoring

### Voir l'Utilisation Mémoire
```bash
free -h
```

### Voir l'Utilisation Disque
```bash
df -h
```

### Voir l'Uptime du Système
```bash
uptime
```

### Voir les Logs en Temps Réel
```bash
tail -f /tmp/bot.log
```
**Note:** Seulement si vous avez configuré un fichier de log.

---

## 🛠️ Commandes de Maintenance

### Nettoyer le Cache Python
```bash
find . -type d -name "__pycache__" -exec rm -rf {} +
find . -type f -name "*.pyc" -delete
```

### Réinstaller Tous les Packages
```bash
pip uninstall -y -r requirements.txt
pip install -r requirements.txt
```

### Mettre à Jour pip
```bash
pip install --upgrade pip
```

### Créer un Fichier requirements.txt à partir des Packages Installés
```bash
pip freeze > requirements_freeze.txt
```

---

## 🔐 Commandes de Sécurité

### Vérifier les Permissions des Fichiers
```bash
ls -l
```

### Changer les Permissions (si nécessaire)
```bash
chmod +x main.py
```

---

## 🎨 Commandes Utiles

### Afficher un Message Coloré
```bash
echo -e "\033[32m✅ Bot démarré avec succès!\033[0m"
echo -e "\033[31m❌ Erreur détectée!\033[0m"
```

### Créer un Fichier de Log
```bash
python main.py > bot.log 2>&1 &
```

### Voir les Dernières Lignes du Log
```bash
tail -n 50 bot.log
```

### Chercher dans les Logs
```bash
grep "ERROR" bot.log
grep "Bot connecté" bot.log
```

---

## 🚀 Scripts Rapides

### Script de Démarrage Complet
```bash
#!/bin/bash
echo "🔄 Installation des dépendances..."
pip install -r requirements.txt

echo "🧹 Nettoyage du cache..."
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null

echo "🚀 Démarrage du bot..."
python main.py
```

### Script de Test
```bash
#!/bin/bash
echo "🧪 Test des imports..."
python -c "import bot; import emotes; import roles; import anchors; import gemini_integration; print('✅ Tous les imports OK')"

echo "🧪 Test Gemini..."
python -c "from gemini_integration import initialize_gemini; g = initialize_gemini(); print('✅ Gemini OK' if g else '❌ Gemini KO')"

echo "🧪 Test des emotes..."
python -c "from emotes import EMOTES; print(f'✅ {len(EMOTES)} emotes disponibles')"

echo "✅ Tous les tests passés!"
```

---

## 📝 Commandes de Documentation

### Générer une Liste des Fichiers
```bash
tree -L 2
# ou
ls -R
```

### Compter les Lignes de Code Total
```bash
find . -name "*.py" -exec wc -l {} + | tail -1
```

### Lister les Fonctions dans bot.py
```bash
grep "def " bot.py
```

### Lister les Commandes du Bot
```bash
grep "!admin\|!emote\|!help" bot.py
```

---

## 🎯 Raccourcis Utiles

### Ctrl + C
Arrêter le processus en cours

### Ctrl + D
Quitter le Shell

### Ctrl + L
Effacer l'écran

### Ctrl + R
Chercher dans l'historique des commandes

### ↑ / ↓
Naviguer dans l'historique des commandes

---

## 🔥 Commandes d'Urgence

### Le Bot est Bloqué
```bash
pkill -9 python
python main.py
```

### Réinitialiser Complètement
```bash
rm -rf __pycache__
pip uninstall -y -r requirements.txt
pip install -r requirements.txt
python main.py
```

### Sauvegarder les Logs Avant Redémarrage
```bash
cp /var/log/replit.log backup_$(date +%Y%m%d_%H%M%S).log
```

---

## 💡 Astuces Pro

### Créer un Alias
```bash
alias start="python main.py"
alias test="python -m pytest"
alias clean="find . -type d -name '__pycache__' -exec rm -rf {} +"
```

### Surveiller les Changements de Fichiers
```bash
watch -n 5 'ls -lh *.py'
```

### Exécuter en Arrière-Plan
```bash
nohup python main.py > bot.log 2>&1 &
```

---

**Note:** Certaines commandes peuvent ne pas fonctionner dans Replit en raison des restrictions de sécurité. Utilisez principalement les commandes Python et pip.

---

**Créé le:** 26 octobre 2025  
**Plateforme:** Replit  
**Shell:** Bash
