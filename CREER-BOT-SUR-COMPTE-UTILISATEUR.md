# 🤖 Créer un bot sur un compte utilisateur existant

## 🎯 Objectif

Créer un bot lié à ton compte utilisateur **S_______L_____** pour que le bot ait accès à tous les items de ce compte !

## 📋 Étapes détaillées

### Étape 1 : Se connecter avec le compte utilisateur

1. **Va sur** : https://create.highrise.game
2. **Clique sur "Log in"** (en haut à droite)
3. **Connecte-toi avec ton compte** `S_______L_____`
   - Utilise l'email et le mot de passe de ce compte

### Étape 2 : Accéder au Dashboard

1. Une fois connecté, **clique sur "Dashboard"** (dans le menu)
2. Ou va directement sur : https://create.highrise.game/dashboard

### Étape 3 : Créer un bot

1. Dans le Dashboard, **clique sur "Bots & API Keys"**
2. Ou va directement sur : https://create.highrise.game/dashboard/credentials/api-keys
3. **Clique sur "Create New Bot"** ou le bouton "+" pour créer un bot

### Étape 4 : Configurer le bot

1. **Donne un nom au bot**
   - Exemple : "S_______L_____ Bot" ou "My Assistant Bot"
   - Ce nom est juste pour toi, pour identifier le bot

2. **Clique sur "Create"**

### Étape 5 : Générer le token API

1. Une fois le bot créé, tu verras une liste de tes bots
2. **Trouve ton nouveau bot** dans la liste
3. **Clique sur "Generate API Token"** ou "Generate Token"
4. **⚠️ IMPORTANT : Copie le token immédiatement !**
   - Tu ne pourras le voir qu'une seule fois
   - Format : `057565bd7bda6ac37029f5817ea7c2f6d447179cdfa65771e41284ed5f5d6090`

### Étape 6 : Obtenir le Room ID

1. **Ouvre l'application Highrise** (mobile ou PC)
2. **Va dans une room** que tu possèdes (ou où tu as les droits designer)
3. **Clique sur l'icône info** de la room (en haut à droite)
4. **Clique sur "Share this Room"**
5. Tu vas obtenir un lien comme :
   ```
   https://highrise.game/room/680ab18546b31625a94de2e6
   ```
6. **Copie l'ID** (la partie après `/room/`) :
   ```
   680ab18546b31625a94de2e6
   ```

### Étape 7 : Configurer le .env

1. **Ouvre ton fichier `.env`**
2. **Remplace les valeurs** :

```env
# Token du bot (généré à l'étape 5)
TOKEN=057565bd7bda6ac37029f5817ea7c2f6d447179cdfa65771e41284ed5f5d6090

# Room ID (obtenu à l'étape 6)
ROOM_ID=680ab18546b31625a94de2e6

# Ton username pour être admin
ADMIN_USERNAMES=ton_username_principal

# Clé API Gemini (si tu l'as)
GEMINI_API_KEY=ta_cle_api_gemini
```

### Étape 8 : Lancer le bot

```bash
python -m highrise bot:HighriseBot ROOM_ID TOKEN
```

Ou avec les valeurs du .env :

```bash
python -m highrise bot:HighriseBot 680ab18546b31625a94de2e6 057565bd7bda6ac37029f5817ea7c2f6d447179cdfa65771e41284ed5f5d6090
```

## ✅ Résultat

Le bot sera maintenant lié au compte **S_______L_____** et aura accès à :

✅ **Tous les items** du compte S_______L_____
✅ **Le gold** du compte
✅ **L'inventaire complet** du compte

## 🎨 Vérifier l'inventaire du bot

Une fois le bot lancé, utilise :

```
!admin inventory
```

Tu verras **tous les items** du compte S_______L_____ dans les logs !

## 📝 Exemple complet

### 1. Connexion
- Va sur https://create.highrise.game
- Connecte-toi avec S_______L_____

### 2. Création du bot
- Dashboard → Bots & API Keys
- Create New Bot
- Nom : "S_______L_____ Assistant"
- Generate API Token → **Copie le token**

### 3. Room ID
- App Highrise → Ta room
- Info → Share this Room
- Copie l'ID : `680ab18546b31625a94de2e6`

### 4. Configuration .env
```env
TOKEN=le_token_copie
ROOM_ID=680ab18546b31625a94de2e6
ADMIN_USERNAMES=ton_username
GEMINI_API_KEY=ta_cle_gemini
```

### 5. Lancement
```bash
python -m highrise bot:HighriseBot 680ab18546b31625a94de2e6 le_token_copie
```

### 6. Vérification
```
!admin inventory
```

Tu verras tous les items de S_______L_____ ! 🎉

## ⚠️ Points importants

### Le bot apparaîtra comme un utilisateur séparé

- Le bot aura son propre nom (celui que tu as donné)
- Il apparaîtra comme un utilisateur différent dans la room
- **MAIS** il aura accès à l'inventaire du compte S_______L_____

### Droits nécessaires

Le bot doit avoir les **droits designer** dans la room :
- Si c'est **ta room** → Pas de problème
- Si c'est la room de quelqu'un d'autre → Demande les droits designer

### Un bot par compte

Tu peux créer **plusieurs bots** sur le même compte S_______L_____ :
- Chaque bot aura son propre token
- Tous auront accès au même inventaire
- Utile pour avoir plusieurs bots avec des fonctions différentes

## 🎯 Avantages

### Avec un bot lié à S_______L_____

✅ **Accès à tous les items** que tu as achetés sur ce compte
✅ **Accès au gold** du compte
✅ **Pas besoin d'acheter des items** spécifiquement pour le bot
✅ **Utilise les items** que tu as déjà

### Vs bot indépendant

❌ Bot indépendant = Seulement les starter items
❌ Doit acheter ses propres items
❌ Inventaire limité

## 📊 Résumé visuel

```
Compte S_______L_____
    ↓
    ├── Items (vêtements, accessoires)
    ├── Gold
    └── Bot créé sur ce compte
        ↓
        Accès à tout l'inventaire du compte !
```

## 🔗 Liens utiles

- **Créer un bot** : https://create.highrise.game/dashboard/credentials/api-keys
- **Dashboard** : https://create.highrise.game/dashboard
- **Documentation** : https://create.highrise.game/learn/guides/bots/creating-a-bot

## 🎉 C'est tout !

Une fois le bot créé sur ton compte S_______L_____, il aura accès à tous tes items !

**Prochaines étapes :**
1. Crée le bot sur https://create.highrise.game
2. Copie le token
3. Configure le .env
4. Lance le bot
5. Utilise `!admin inventory` pour voir tous tes items
6. Crée des outfits avec tes items !

---

**Le bot créé sur ton compte S_______L_____ aura accès à tous les items de ce compte ! 🎨**
