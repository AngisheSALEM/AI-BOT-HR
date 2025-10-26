# 🚀 Guide Complet: Héberger Bot Highrise sur Replit (GRATUIT)

## ✨ Avantages de Replit

- ✅ **100% Gratuit** (pas de carte bancaire)
- ✅ **Toujours actif** avec Always On (gratuit pendant 3 mois)
- ✅ **Interface simple** (éditeur de code intégré)
- ✅ **Déploiement instantané** (pas de configuration complexe)
- ✅ **Console en temps réel** (voir les logs du bot)
- ✅ **Secrets sécurisés** (variables d'environnement protégées)

## 📋 Étape 1: Créer un Compte Replit

1. Aller sur **https://replit.com**
2. Cliquer sur **"Sign up"**
3. Créer un compte avec:
   - Email
   - GitHub (recommandé)
   - Google

## 📋 Étape 2: Créer un Nouveau Repl

1. Une fois connecté, cliquer sur **"+ Create Repl"**
2. Sélectionner:
   - **Template:** Python
   - **Title:** highrise-bot-savant (ou votre nom)
   - **Visibility:** Private (recommandé)
3. Cliquer sur **"Create Repl"**

## 📋 Étape 3: Uploader les Fichiers

### Option A: Upload Manuel (Recommandé pour débutants)

1. Dans l'éditeur Replit, cliquer sur les **3 points** à côté de "Files"
2. Cliquer sur **"Upload file"** ou **"Upload folder"**
3. Uploader TOUS ces fichiers:
   ```
   ✅ bot.py
   ✅ emotes.py
   ✅ emotes_by_number.py
   ✅ roles.py
   ✅ anchors.py
   ✅ gemini_integration.py
   ✅ requirements.txt
   ✅ anchors.json
   ✅ main.py (à créer - voir ci-dessous)
   ```

4. **NE PAS uploader:**
   ```
   ❌ .env (on va le créer dans Replit)
   ❌ __pycache__/
   ❌ *.pyc
   ```

### Option B: Import depuis GitHub (Pour utilisateurs avancés)

1. Pousser votre code sur GitHub
2. Dans Replit, cliquer sur **"Import from GitHub"**
3. Coller l'URL de votre repository
4. Replit clone automatiquement tout

## 📋 Étape 4: Créer le Fichier `main.py`

Replit cherche toujours un fichier `main.py` comme point d'entrée.

**Créer `main.py` avec ce contenu:**

```python
#!/usr/bin/env python3
"""
Point d'entrée pour Replit
Lance le bot Highrise avec les credentials depuis les Secrets
"""

import os
import sys
from bot import start_health_server

def main():
    print("=" * 60)
    print("🤖 Bot Highrise Savant - Démarrage sur Replit")
    print("=" * 60)
    
    # Démarrer le serveur de santé (pour garder le bot actif)
    start_health_server()
    
    # Récupérer les credentials depuis les Secrets Replit
    room_id = os.getenv('ROOM_ID')
    bot_token = os.getenv('BOT_TOKEN')
    
    if not room_id or not bot_token:
        print("❌ ERREUR: ROOM_ID et BOT_TOKEN doivent être définis dans les Secrets!")
        print("👉 Allez dans l'onglet 'Secrets' (icône cadenas) et ajoutez:")
        print("   - ROOM_ID: votre room ID")
        print("   - BOT_TOKEN: votre token bot")
        sys.exit(1)
    
    print(f"✅ Room ID: {room_id}")
    print(f"✅ Token: {bot_token[:20]}...")
    print("=" * 60)
    print("🚀 Connexion au serveur Highrise...")
    print("=" * 60)
    
    # Lancer le bot
    from highrise.__main__ import main as highrise_main
    sys.argv = ['highrise', 'bot:HighriseBot', room_id, bot_token]
    highrise_main()

if __name__ == "__main__":
    main()
```

## 📋 Étape 5: Configurer les Secrets (Variables d'Environnement)

1. Dans l'éditeur Replit, chercher l'icône **🔒 "Secrets"** dans la barre latérale gauche
2. Cliquer dessus
3. Ajouter ces secrets (un par un):

### Secret 1: BOT_TOKEN
- **Key:** `BOT_TOKEN`
- **Value:** `057565bd7bda6ac37029f5817ea7c2f6d447179cdfa65771e41284ed5f5d6090`

### Secret 2: ROOM_ID
- **Key:** `ROOM_ID`
- **Value:** `680ab18546b31625a94de2e6`

### Secret 3: ADMIN_USERNAMES
- **Key:** `ADMIN_USERNAMES`
- **Value:** `sylver_ralx_lm`

### Secret 4: GEMINI_API_KEY
- **Key:** `GEMINI_API_KEY`
- **Value:** `votre_cle_gemini_ici`

**Important:** Les Secrets sont sécurisés et ne sont jamais visibles dans le code!

## 📋 Étape 6: Configurer `requirements.txt`

Vérifier que `requirements.txt` contient:

```txt
highrise-bot-sdk==24.1.0
python-dotenv==1.0.0
google-generativeai==0.7.2
```

## 📋 Étape 7: Configurer `.replit`

Replit crée automatiquement un fichier `.replit`. Modifier son contenu:

```toml
run = "python main.py"
entrypoint = "main.py"
modules = ["python-3.11"]

[nix]
channel = "stable-23_11"

[deployment]
run = ["python", "main.py"]
deploymentTarget = "cloudrun"
```

## 📋 Étape 8: Lancer le Bot

1. Cliquer sur le gros bouton vert **"Run"** en haut
2. Replit va:
   - Installer les dépendances (`pip install -r requirements.txt`)
   - Lancer `main.py`
   - Afficher les logs dans la console

3. Vous devriez voir:
   ```
   ============================================================
   🤖 Bot Highrise Savant - Démarrage sur Replit
   ============================================================
   ✅ Health check server started on port 8080
   ✅ Room ID: 680ab18546b31625a94de2e6
   ✅ Token: 057565bd7bda6ac37029...
   ============================================================
   🚀 Connexion au serveur Highrise...
   ============================================================
   [INFO] Bot connecté!
   ```

## 📋 Étape 9: Garder le Bot Actif 24/7 (Always On)

### Option 1: Always On (Gratuit pendant 3 mois)

1. Dans votre Repl, chercher l'onglet **"Deployments"** ou **"Always On"**
2. Activer **"Always On"**
3. Le bot restera actif même si vous fermez l'onglet!

**Note:** Always On est gratuit pendant 3 mois pour les nouveaux comptes.

### Option 2: UptimeRobot (Gratuit à vie)

Si Always On expire, utilisez UptimeRobot pour "pinger" votre bot:

1. Aller sur **https://uptimerobot.com**
2. Créer un compte gratuit
3. Ajouter un nouveau moniteur:
   - **Monitor Type:** HTTP(s)
   - **Friendly Name:** Highrise Bot
   - **URL:** `https://VOTRE-REPL.replit.app` (copier depuis Replit)
   - **Monitoring Interval:** 5 minutes
4. Cliquer sur **"Create Monitor"**

UptimeRobot va "pinger" votre bot toutes les 5 minutes, le gardant actif!

### Option 3: Cron-Job.org (Alternative gratuite)

1. Aller sur **https://cron-job.org**
2. Créer un compte gratuit
3. Créer un cron job:
   - **URL:** `https://VOTRE-REPL.replit.app`
   - **Interval:** Toutes les 10 minutes
4. Activer le cron job

## 📋 Étape 10: Vérifier que Tout Fonctionne

### Dans Replit:
1. Vérifier les logs dans la console
2. Chercher: `[INFO] Bot connecté!`
3. Chercher: `✅ Health check server started`

### Dans Highrise:
1. Ouvrir l'app Highrise
2. Aller dans votre room
3. Le bot devrait être connecté!
4. Tester une commande: `!help`
5. Tester Savant: `@savant bonjour`

## 🔧 Dépannage

### Problème 1: "Module not found"
**Solution:**
1. Vérifier que `requirements.txt` existe
2. Cliquer sur "Shell" dans Replit
3. Taper: `pip install -r requirements.txt`
4. Relancer le bot

### Problème 2: "ROOM_ID et BOT_TOKEN doivent être définis"
**Solution:**
1. Aller dans l'onglet **Secrets** (🔒)
2. Vérifier que `ROOM_ID` et `BOT_TOKEN` sont bien ajoutés
3. Vérifier qu'il n'y a pas d'espaces avant/après les valeurs
4. Relancer le bot

### Problème 3: Le bot se déconnecte après quelques minutes
**Solution:**
1. Activer **Always On** dans Replit
2. OU configurer UptimeRobot (voir Étape 9)

### Problème 4: "Rate limit exceeded" (Gemini)
**Solution:**
1. Vérifier que `GEMINI_API_KEY` est correct dans les Secrets
2. Attendre quelques minutes (quota API)
3. Le bot continue de fonctionner (seules les commandes IA sont affectées)

### Problème 5: Le bot ne répond pas aux commandes
**Solution:**
1. Vérifier dans les logs: `[INFO] Bot connecté!`
2. Vérifier que vous êtes dans la bonne room
3. Tester avec `!help` (commande de base)
4. Vérifier que le bot n'est pas banni de la room

## 📊 Avantages vs Inconvénients

### ✅ Avantages
- Interface ultra-simple (pas besoin de terminal)
- Éditeur de code intégré
- Console en temps réel
- Gratuit avec Always On (3 mois)
- Pas de carte bancaire
- Déploiement instantané

### ⚠️ Inconvénients
- Always On limité à 3 mois (puis payant $7/mois)
- Moins de RAM que Railway/Render (512MB)
- Peut être lent pendant les heures de pointe

## 🎯 Astuces Pro

### 1. Voir les Logs en Temps Réel
- Cliquer sur **"Console"** en bas
- Tous les `print()` du bot s'affichent ici

### 2. Modifier le Code en Direct
- Modifier n'importe quel fichier dans l'éditeur
- Cliquer sur **"Run"** pour redémarrer avec les changements

### 3. Utiliser le Shell
- Cliquer sur **"Shell"** (icône terminal)
- Taper des commandes Python:
  ```bash
  python -c "from emotes import EMOTES; print(len(EMOTES))"
  ```

### 4. Partager votre Bot
- Cliquer sur **"Invite"** en haut à droite
- Inviter des collaborateurs à modifier le code

### 5. Forker pour Tester
- Cliquer sur les 3 points → **"Fork"**
- Créer une copie pour tester sans risque

## 📱 Gérer depuis Mobile

Replit a une app mobile!

1. Télécharger **"Replit Mobile"** (iOS/Android)
2. Se connecter avec votre compte
3. Voir les logs, modifier le code, redémarrer le bot

## 🔄 Mettre à Jour le Bot

### Méthode 1: Éditeur Replit
1. Modifier les fichiers directement dans Replit
2. Cliquer sur **"Run"** pour redémarrer

### Méthode 2: Upload de Nouveaux Fichiers
1. Télécharger les nouveaux fichiers depuis votre PC
2. Uploader dans Replit (remplace les anciens)
3. Redémarrer

### Méthode 3: GitHub (Avancé)
1. Pousser les changements sur GitHub
2. Dans Replit: **"Pull from GitHub"**
3. Redémarrer

## 💰 Coûts (Après 3 Mois)

Si vous voulez garder Always On après 3 mois:

- **Always On:** $7/mois
- **Hacker Plan:** $7/mois (inclut Always On + bonus)

**Alternative gratuite:** Utiliser UptimeRobot (voir Étape 9)

## 🆚 Comparaison avec Autres Plateformes

| Critère | Replit | Render | Railway |
|---------|--------|--------|---------|
| **Prix** | Gratuit 3 mois | Gratuit | Gratuit |
| **Facilité** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Uptime** | 99.5% | 99.5% | 99.8% |
| **RAM** | 512MB | 512MB | 512MB |
| **Éditeur** | ✅ Intégré | ❌ Non | ❌ Non |
| **Console** | ✅ Temps réel | ✅ Logs | ✅ Logs |
| **Mobile** | ✅ App | ❌ Non | ❌ Non |

## 📞 Support

- **Documentation Replit:** https://docs.replit.com
- **Community:** https://ask.replit.com
- **Discord:** https://replit.com/discord

## ✅ Checklist Finale

Avant de déclarer victoire, vérifier:

- [ ] Compte Replit créé
- [ ] Repl créé avec template Python
- [ ] Tous les fichiers uploadés
- [ ] `main.py` créé
- [ ] Secrets configurés (BOT_TOKEN, ROOM_ID, etc.)
- [ ] `requirements.txt` correct
- [ ] Bot lancé avec succès
- [ ] Bot visible dans Highrise
- [ ] Commande `!help` fonctionne
- [ ] `@savant` répond
- [ ] Always On activé OU UptimeRobot configuré

## 🎉 Félicitations!

Votre bot Highrise est maintenant hébergé 24/7 sur Replit!

**Prochaines étapes:**
1. Personnaliser les commandes
2. Ajouter de nouveaux outfits
3. Configurer plus d'emotes
4. Inviter des amis dans votre room!

---

**Créé le:** 26 octobre 2025  
**Plateforme:** Replit (Free Tier)  
**Bot:** Highrise Savant  
**Statut:** ✅ Production Ready
