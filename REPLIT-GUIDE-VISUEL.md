# 📸 Guide Visuel: Héberger sur Replit

## 🎯 Vue d'Ensemble

```
Votre PC → Upload sur Replit → Bot actif 24/7
```

---

## 📋 Étapes Visuelles

### 1️⃣ Page d'Accueil Replit

```
┌─────────────────────────────────────────┐
│  Replit                    [Sign up]    │
├─────────────────────────────────────────┤
│                                         │
│         [+ Create Repl]  ← CLIQUER ICI │
│                                         │
└─────────────────────────────────────────┘
```

### 2️⃣ Créer un Nouveau Repl

```
┌─────────────────────────────────────────┐
│  Create a Repl                          │
├─────────────────────────────────────────┤
│  Template: [Python ▼]                   │
│  Title: highrise-bot-savant             │
│  Visibility: ○ Public  ● Private        │
│                                         │
│              [Create Repl]              │
└─────────────────────────────────────────┘
```

### 3️⃣ Interface Replit

```
┌──────────┬────────────────────┬──────────┐
│  Files   │  Code Editor       │ Console  │
├──────────┼────────────────────┼──────────┤
│ 📁 Files │ main.py            │ [Run] ←  │
│ 🔒 Secrets│                   │ CLIQUER  │
│ 📦 Packages│ def main():      │          │
│ ⚙️ Settings│   print("...")   │ Logs:    │
│          │                    │ > Bot    │
│ [⋮] Menu │                    │ connecté │
│          │                    │          │
└──────────┴────────────────────┴──────────┘
```

### 4️⃣ Uploader les Fichiers

```
Cliquer sur [⋮] à côté de "Files"
↓
┌─────────────────────┐
│ Upload file         │ ← Pour 1 fichier
│ Upload folder       │ ← Pour tout le dossier
│ Create file         │
│ Create folder       │
└─────────────────────┘
```

### 5️⃣ Configurer les Secrets

```
Cliquer sur 🔒 Secrets
↓
┌─────────────────────────────────────┐
│  Secrets                            │
├─────────────────────────────────────┤
│  Key: BOT_TOKEN                     │
│  Value: 057565bd7bda6ac37029f58...  │
│                        [Add Secret] │
├─────────────────────────────────────┤
│  Key: ROOM_ID                       │
│  Value: 680ab18546b31625a94de2e6    │
│                        [Add Secret] │
└─────────────────────────────────────┘
```

### 6️⃣ Lancer le Bot

```
Cliquer sur [Run] (bouton vert en haut)
↓
Console affiche:
============================================================
🤖 Bot Highrise Savant - Démarrage sur Replit
============================================================
✅ Health check server started on port 8080
✅ Room ID: 680ab18546b31625a94de2e6
✅ Token: 057565bd7bda6ac37029...
============================================================
🚀 Connexion au serveur Highrise...
============================================================
[INFO] Bot connecté! ← BON SIGNE!
```

### 7️⃣ Activer Always On

```
Chercher dans les paramètres:
┌─────────────────────────────────────┐
│  ⚙️ Settings                        │
├─────────────────────────────────────┤
│  Always On                          │
│  Keep your Repl running 24/7        │
│                                     │
│  [●] Enable Always On               │
│                                     │
│  Free for 3 months!                 │
└─────────────────────────────────────┘
```

---

## 🎨 Structure des Fichiers dans Replit

```
highrise-bot-savant/
├── main.py              ← Point d'entrée (IMPORTANT!)
├── bot.py               ← Code principal du bot
├── emotes.py            ← Liste des emotes
├── emotes_by_number.py  ← Emotes par numéro
├── roles.py             ← Système de rôles
├── anchors.py           ← Points de téléportation
├── gemini_integration.py ← IA Gemini
├── requirements.txt     ← Dépendances Python
├── anchors.json         ← Positions sauvegardées
├── .replit              ← Config Replit (auto-créé)
└── 🔒 Secrets (pas un fichier, dans l'interface)
    ├── BOT_TOKEN
    ├── ROOM_ID
    ├── ADMIN_USERNAMES
    └── GEMINI_API_KEY
```

---

## 🔍 Où Trouver Quoi?

### Voir les Logs
```
Console (en bas à droite) → Tous les print() s'affichent ici
```

### Modifier le Code
```
Cliquer sur un fichier → Modifier → [Run] pour redémarrer
```

### Ajouter des Secrets
```
🔒 Secrets (barre latérale) → [Add Secret]
```

### Installer des Packages
```
📦 Packages (barre latérale) → Chercher → [Install]
OU
Shell → pip install nom-du-package
```

### Ouvrir un Terminal
```
Shell (barre latérale) → Terminal Python/Bash
```

---

## 🎯 Checklist Visuelle

Cochez au fur et à mesure:

```
☐ 1. Compte Replit créé
☐ 2. Repl créé (Python, Private)
☐ 3. Fichiers uploadés (voir structure ci-dessus)
☐ 4. main.py existe
☐ 5. Secrets configurés:
     ☐ BOT_TOKEN
     ☐ ROOM_ID
     ☐ ADMIN_USERNAMES
     ☐ GEMINI_API_KEY
☐ 6. [Run] cliqué
☐ 7. Console affiche "Bot connecté!"
☐ 8. Bot visible dans Highrise
☐ 9. !help fonctionne
☐ 10. Always On activé OU UptimeRobot configuré
```

---

## 🚨 Indicateurs de Problème

### ❌ Mauvais Signes dans la Console

```
❌ "Module not found"
→ Solution: Vérifier requirements.txt

❌ "ROOM_ID et BOT_TOKEN doivent être définis"
→ Solution: Ajouter dans Secrets

❌ "Connection refused"
→ Solution: Vérifier le token et room ID

❌ "Rate limit exceeded"
→ Solution: Attendre ou vérifier GEMINI_API_KEY
```

### ✅ Bons Signes dans la Console

```
✅ "Health check server started"
✅ "Bot connecté!"
✅ "Emote envoyée"
✅ "Message reçu de..."
```

---

## 📱 App Mobile Replit

Vous pouvez gérer votre bot depuis votre téléphone!

```
1. Télécharger "Replit Mobile" (App Store / Play Store)
2. Se connecter
3. Ouvrir votre Repl
4. Voir les logs en temps réel
5. Modifier le code
6. Redémarrer le bot
```

---

## 🔄 Workflow Quotidien

```
Matin:
1. Ouvrir Replit
2. Vérifier que le bot est actif (voyant vert)
3. Consulter les logs

Pendant la journée:
- Le bot tourne tout seul!
- Pas besoin de garder Replit ouvert

Si vous voulez modifier:
1. Ouvrir Replit
2. Modifier le fichier
3. [Run] pour redémarrer
4. Vérifier les logs
```

---

## 💡 Astuces Visuelles

### Raccourcis Clavier
```
Ctrl + S     → Sauvegarder
Ctrl + Enter → Run
Ctrl + /     → Commenter
Ctrl + F     → Chercher
```

### Thèmes
```
⚙️ Settings → Theme → Dark / Light
```

### Partager l'Écran
```
[Invite] (en haut) → Copier le lien → Partager
```

---

## 🎉 Résultat Final

```
┌─────────────────────────────────────────┐
│  Replit - highrise-bot-savant           │
│  ● Running                              │
├─────────────────────────────────────────┤
│  Console:                               │
│  ✅ Bot connecté!                       │
│  ✅ Always On activé                    │
│  ✅ 24/7 en ligne                       │
│                                         │
│  Dans Highrise:                         │
│  ✅ Bot visible dans la room            │
│  ✅ Répond aux commandes                │
│  ✅ @savant fonctionne                  │
└─────────────────────────────────────────┘
```

---

**Temps total:** 5-10 minutes  
**Difficulté:** ⭐⭐ (Facile)  
**Coût:** Gratuit (3 mois Always On)

**Besoin d'aide?** Consultez `HEBERGEMENT-REPLIT.md` pour plus de détails!
