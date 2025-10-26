# ✅ Checklist de Déploiement Replit

## 📦 Avant de Commencer

### Fichiers Requis
- [ ] `main.py` existe
- [ ] `bot.py` existe
- [ ] `emotes.py` existe
- [ ] `emotes_by_number.py` existe
- [ ] `roles.py` existe
- [ ] `anchors.py` existe
- [ ] `gemini_integration.py` existe
- [ ] `requirements.txt` existe
- [ ] `anchors.json` existe
- [ ] `.replit` existe

### Credentials Disponibles
- [ ] Token du bot: `057565bd7bda6ac37029f5817ea7c2f6d447179cdfa65771e41284ed5f5d6090`
- [ ] Room ID: `680ab18546b31625a94de2e6`
- [ ] Admin username: `sylver_ralx_lm`
- [ ] Clé Gemini API (optionnel)

---

## 🚀 Étapes de Déploiement

### Phase 1: Configuration Replit
- [ ] Compte Replit créé sur https://replit.com
- [ ] Nouveau Repl créé (Template: Python)
- [ ] Nom du Repl: `highrise-bot-savant` (ou autre)
- [ ] Visibilité: Private (recommandé)

### Phase 2: Upload des Fichiers
- [ ] Tous les fichiers `.py` uploadés
- [ ] `requirements.txt` uploadé
- [ ] `anchors.json` uploadé
- [ ] `.replit` uploadé
- [ ] **PAS** de `.env` uploadé (sécurité!)

### Phase 3: Configuration des Secrets
Dans l'onglet 🔒 Secrets:
- [ ] `BOT_TOKEN` ajouté
- [ ] `ROOM_ID` ajouté
- [ ] `ADMIN_USERNAMES` ajouté
- [ ] `GEMINI_API_KEY` ajouté (optionnel)

### Phase 4: Premier Lancement
- [ ] Bouton [Run] cliqué
- [ ] Installation des dépendances réussie
- [ ] Console affiche: "Health check server started"
- [ ] Console affiche: "Bot connecté!"
- [ ] Aucune erreur dans les logs

### Phase 5: Vérification dans Highrise
- [ ] Ouvrir l'app Highrise
- [ ] Aller dans la room `680ab18546b31625a94de2e6`
- [ ] Bot visible dans la liste des utilisateurs
- [ ] Tester: `!help` → Réponse reçue
- [ ] Tester: `@savant bonjour` → Réponse reçue
- [ ] Tester: `!emote dance` → Bot danse

### Phase 6: Configuration 24/7
Choisir UNE option:

#### Option A: Always On (Gratuit 3 mois)
- [ ] Aller dans Settings → Always On
- [ ] Activer Always On
- [ ] Vérifier le statut: "Always On enabled"

#### Option B: UptimeRobot (Gratuit à vie)
- [ ] Créer un compte sur https://uptimerobot.com
- [ ] Ajouter un nouveau moniteur
- [ ] Type: HTTP(s)
- [ ] URL: Copier depuis Replit (ex: `https://highrise-bot-savant.username.repl.co`)
- [ ] Intervalle: 5 minutes
- [ ] Moniteur activé

#### Option C: Cron-Job.org (Alternative)
- [ ] Créer un compte sur https://cron-job.org
- [ ] Créer un nouveau cron job
- [ ] URL: Copier depuis Replit
- [ ] Intervalle: 10 minutes
- [ ] Cron job activé

---

## 🔍 Vérifications Post-Déploiement

### Logs Replit
Vérifier que ces messages apparaissent:
- [ ] `✅ Health check server started on port 8080`
- [ ] `✅ Room ID: 680ab18546b31625a94de2e6`
- [ ] `✅ Token: 057565bd7bda6ac37029...`
- [ ] `🚀 Connexion au serveur Highrise...`
- [ ] `[INFO] Bot connecté!`

### Fonctionnalités du Bot
Tester chaque catégorie:

#### Commandes de Base
- [ ] `!help` → Liste des commandes
- [ ] `!info` → Infos du bot
- [ ] `!uptime` → Temps de fonctionnement

#### Emotes
- [ ] `!emote dance` → Bot danse
- [ ] `!emote wave` → Bot fait coucou
- [ ] `!emote sit` → Bot s'assoit
- [ ] `!allemote` → Liste des emotes

#### IA Savant (Mode Public)
- [ ] `@savant bonjour` → Réponse courte (max 140 char)
- [ ] `@savant comment vas-tu?` → Réponse
- [ ] Pas de réponse si pas mentionné (normal)

#### IA Savant (Mode Privé)
- [ ] Envoyer DM au bot: "Bonjour" → Réponse détaillée (max 245 char)
- [ ] Envoyer DM: "Raconte-moi une histoire" → Réponse
- [ ] Historique sauvegardé dans la boîte de réception

#### Commandes Admin (si vous êtes `sylver_ralx_lm`)
- [ ] `!admin tp` → Téléportation
- [ ] `!admin inventory` → Inventaire dans les logs
- [ ] `!admin currentoutfit` → Outfit actuel

---

## 🚨 Dépannage

### Problème 1: Bot ne démarre pas
**Symptômes:**
- Erreur dans la console
- Pas de "Bot connecté!"

**Solutions:**
- [ ] Vérifier que tous les Secrets sont définis
- [ ] Vérifier qu'il n'y a pas d'espaces dans les Secrets
- [ ] Vérifier que `requirements.txt` est correct
- [ ] Cliquer sur "Stop" puis "Run" pour redémarrer

### Problème 2: "Module not found"
**Symptômes:**
- `ModuleNotFoundError: No module named 'highrise'`

**Solutions:**
- [ ] Ouvrir le Shell dans Replit
- [ ] Taper: `pip install -r requirements.txt`
- [ ] Attendre la fin de l'installation
- [ ] Cliquer sur "Run"

### Problème 3: Bot se déconnecte
**Symptômes:**
- Bot connecté puis déconnecté après quelques minutes
- "Connection lost" dans les logs

**Solutions:**
- [ ] Activer Always On (si pas déjà fait)
- [ ] OU configurer UptimeRobot
- [ ] Vérifier que le token est correct
- [ ] Vérifier que le bot n'est pas banni de la room

### Problème 4: Savant ne répond pas
**Symptômes:**
- `@savant bonjour` ne donne aucune réponse

**Solutions:**
- [ ] Vérifier que `GEMINI_API_KEY` est défini dans les Secrets
- [ ] Vérifier que la clé Gemini est valide
- [ ] Vérifier les quotas Gemini (15 req/min, 1500 req/jour)
- [ ] Attendre quelques minutes si rate limit

### Problème 5: Commandes admin ne marchent pas
**Symptômes:**
- `!admin tp` ne fait rien

**Solutions:**
- [ ] Vérifier que votre username est dans `ADMIN_USERNAMES`
- [ ] Vérifier l'orthographe: `sylver_ralx_lm` (sensible à la casse)
- [ ] Redémarrer le bot après modification des Secrets

---

## 📊 Monitoring

### Quotidien
- [ ] Ouvrir Replit
- [ ] Vérifier le voyant vert (bot actif)
- [ ] Consulter les logs (erreurs?)
- [ ] Tester une commande dans Highrise

### Hebdomadaire
- [ ] Vérifier l'uptime (Always On ou UptimeRobot)
- [ ] Vérifier les quotas Gemini
- [ ] Mettre à jour le code si nécessaire

### Mensuel
- [ ] Vérifier la date d'expiration Always On (3 mois)
- [ ] Préparer UptimeRobot si Always On expire
- [ ] Sauvegarder les logs importants

---

## 🎯 Objectifs Atteints

Une fois cette checklist complétée:
- ✅ Bot hébergé 24/7 sur Replit
- ✅ Toutes les fonctionnalités opérationnelles
- ✅ IA Savant active (public + privé)
- ✅ Commandes admin fonctionnelles
- ✅ Monitoring en place
- ✅ Gratuit pendant 3 mois minimum

---

## 📞 Support

Si un problème persiste:
1. Consulter `HEBERGEMENT-REPLIT.md` (guide complet)
2. Consulter `REPLIT-GUIDE-VISUEL.md` (guide visuel)
3. Vérifier les logs dans la console Replit
4. Chercher l'erreur sur Google
5. Demander sur le Discord Highrise

---

**Date de déploiement:** _________________  
**Statut:** ☐ En cours  ☐ Terminé  ☐ Problème  
**Notes:** _________________________________

---

**Créé le:** 26 octobre 2025  
**Version:** 1.0  
**Plateforme:** Replit
