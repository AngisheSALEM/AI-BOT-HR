# 🏠 Changement de salle

## 📋 Informations extraites

### Lien de la salle
```
https://high.rs/room?id=68a3bb673afbda195c01af96&invite_id=68fd8b55c3b4ca00294e4ad7
```

### ID de la salle (Room ID)
```
68a3bb673afbda195c01af96
```

### ID d'invitation (Invite ID)
```
68fd8b55c3b4ca00294e4ad7
```

---

## 🚀 Commande pour lancer le bot

### Option 1 : Double-cliquer sur START.bat
```
START.bat
```
Le fichier a été mis à jour automatiquement avec le nouvel ID de salle.

### Option 2 : Commande manuelle
```bash
python -m highrise bot:HighriseBot 68a3bb673afbda195c01af96 057565bd7bda6ac37029f5817ea7c2f6d447179cdfa65771e41284ed5f5d6090
```

### Décomposition de la commande
```
python -m highrise bot:HighriseBot [ROOM_ID] [API_TOKEN]
```

- **bot:HighriseBot** - Chemin vers la classe du bot
- **68a3bb673afbda195c01af96** - ID de la nouvelle salle
- **057565bd7bda6ac37029f5817ea7c2f6d447179cdfa65771e41284ed5f5d6090** - Token API du bot

---

## 📊 Comparaison

| Élément | Ancienne salle | Nouvelle salle |
|---------|----------------|----------------|
| **Room ID** | 680ab18546b31625a94de2e6 | **68a3bb673afbda195c01af96** |
| **Token API** | 057565bd7b... (inchangé) | 057565bd7b... (inchangé) |

---

## ✅ Fichier mis à jour

### START.bat (ligne 10)
**Avant :**
```batch
python -m highrise bot:HighriseBot 680ab18546b31625a94de2e6 057565bd7bda6ac37029f5817ea7c2f6d447179cdfa65771e41284ed5f5d6090
```

**Maintenant :**
```batch
python -m highrise bot:HighriseBot 68a3bb673afbda195c01af96 057565bd7bda6ac37029f5817ea7c2f6d447179cdfa65771e41284ed5f5d6090
```

---

## 🎮 Lancer le bot

### Méthode 1 : Fichier batch (recommandé)
1. Double-cliquer sur **START.bat**
2. Le bot se connecte automatiquement à la nouvelle salle

### Méthode 2 : Terminal
1. Ouvrir le terminal dans le dossier du bot
2. Copier-coller la commande :
```bash
python -m highrise bot:HighriseBot 68a3bb673afbda195c01af96 057565bd7bda6ac37029f5817ea7c2f6d447179cdfa65771e41284ed5f5d6090
```
3. Appuyer sur Entrée

---

## 📋 Logs attendus au démarrage

```
========================================
   BOT HIGHRISE PYTHON AVANCE
========================================

Lancement du bot...

[POSITION] Bot téléporté à x=11.0, y=12.25, z=6.5
[OK] Message de bienvenue envoye
[INFO] Pour changer la bio, allez sur https://highrise.game/account/settings
[AMOUR] Envoi de la déclaration initiale...
[AMOUR] Tache de declarations d'amour demarree
[AMOUR] Declarations d'amour activees pour sindouche (toutes les 900s)
[FLOSS] Emote floss en boucle demarree
[NEWS] Tache de diffusion de nouvelles/faits demarree
[NEWS] Diffusion de nouvelles/faits activee (toutes les 420s = 7 min)
```

---

## ⚠️ Points importants

### Permissions requises
Pour que le bot fonctionne dans la nouvelle salle, il faut :
- ✅ Le bot doit être **invité** dans la salle
- ✅ Le bot doit avoir les **droits Designer** (ou la salle doit être à toi)
- ✅ Le token API doit être **valide**

### Si le bot ne se connecte pas
1. Vérifie que le bot est bien invité dans la salle
2. Vérifie que le bot a les droits nécessaires
3. Vérifie que l'ID de la salle est correct : `68a3bb673afbda195c01af96`

---

## 🔧 Autres fichiers à mettre à jour (optionnel)

Si tu veux mettre à jour d'autres fichiers qui mentionnent l'ancien Room ID :

### bot.py (si Room ID en dur)
Chercher `680ab18546b31625a94de2e6` et remplacer par `68a3bb673afbda195c01af96`

### Documentation
Mettre à jour les fichiers .md qui mentionnent l'ancien Room ID

---

## 📝 Résumé

| Information | Valeur |
|-------------|--------|
| **Nouvelle Room ID** | `68a3bb673afbda195c01af96` |
| **Invite ID** | `68fd8b55c3b4ca00294e4ad7` |
| **Token API** | `057565bd7b...` (inchangé) |
| **Fichier mis à jour** | START.bat |
| **Commande** | Double-cliquer sur START.bat |

---

## 🎯 Action immédiate

**Pour lancer le bot dans la nouvelle salle :**
1. ✅ Double-cliquer sur **START.bat**
2. ✅ Le bot se connecte automatiquement
3. ✅ Vérifier les logs de connexion

---

**Le bot est prêt à se connecter à la nouvelle salle ! 🚀✨**
