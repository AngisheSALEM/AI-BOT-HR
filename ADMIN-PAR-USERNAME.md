# 👤 Système admin par username

## ✅ Changement effectué

Le bot utilise maintenant les **usernames** au lieu des IDs pour identifier les admins !

## 🎯 Pourquoi c'est mieux ?

### ❌ Avant (avec IDs)
```env
ADMIN_IDS=68fa36e2d0769d1c7dd48b35,autre_id_complique
```
- IDs longs et compliqués
- Difficile à retenir
- Besoin d'une commande pour obtenir l'ID

### ✅ Maintenant (avec usernames)
```env
ADMIN_USERNAMES=sylver_ralx_lm,autre_admin
```
- Simple et lisible
- Facile à retenir
- Pas besoin de commande spéciale

## 📋 Configuration

### Dans ton fichier .env

Remplace `ADMIN_IDS` par `ADMIN_USERNAMES` :

```env
# Ancienne méthode (ne fonctionne plus)
# ADMIN_IDS=68fa36e2d0769d1c7dd48b35

# Nouvelle méthode (utilise ça)
ADMIN_USERNAMES=sylver_ralx_lm
```

### Plusieurs admins

Sépare par des virgules (avec ou sans espaces) :

```env
ADMIN_USERNAMES=sylver_ralx_lm,autre_admin,encore_un_admin
```

ou

```env
ADMIN_USERNAMES=sylver_ralx_lm, autre_admin, encore_un_admin
```

## 🔍 Comment ça marche

### Dans le code

```python
# Charger les usernames depuis .env
admin_usernames = os.getenv('ADMIN_USERNAMES', '').split(',')
self.admins = [name.strip().lower() for name in admin_usernames if name.strip()]

# Vérifier si un utilisateur est admin
def is_admin(self, user: User) -> bool:
    return user.username.lower() in self.admins
```

### Vérification

- Les usernames sont convertis en **minuscules** pour éviter les problèmes de casse
- `sylver_ralx_lm` = `Sylver_Ralx_LM` = `SYLVER_RALX_LM` (tous acceptés)

## 📝 Exemple complet .env

```env
# Configuration du bot Highrise
ROOM_ID=680ab18546b31625a94de2e6
TOKEN=057565bd7bda6ac37029f5817ea7c2f6d447179cdfa65771e41284ed5f5d6090

# Admins par username (simple et lisible)
ADMIN_USERNAMES=sylver_ralx_lm

# API Gemini
GEMINI_API_KEY=ta_cle_api_gemini
```

## 🎯 Avantages

✅ **Plus simple** - Pas besoin de chercher ton ID
✅ **Plus lisible** - Tu sais qui est admin en un coup d'œil
✅ **Plus rapide** - Juste ton username, c'est tout
✅ **Insensible à la casse** - Majuscules ou minuscules, ça marche
✅ **Unique dans Highrise** - Les usernames sont uniques

## ⚠️ Migration depuis l'ancien système

Si tu utilisais `ADMIN_IDS` avant :

### 1. Ouvre ton .env

### 2. Remplace
```env
# Ancien
ADMIN_IDS=68fa36e2d0769d1c7dd48b35

# Nouveau
ADMIN_USERNAMES=ton_username
```

### 3. Relance le bot

C'est tout ! 🎉

## 🔧 Vérifier que ça marche

### 1. Lance le bot

### 2. Envoie une commande admin
```
!admin help
```

### 3. Si tu es admin
```
✅ Tu reçois la liste des commandes
```

### 4. Si tu n'es pas admin
```
❌ "Acces refuse. Commandes admin uniquement."
```

## 💡 Ajouter un nouvel admin

### Méthode 1 : Modifier .env

```env
ADMIN_USERNAMES=sylver_ralx_lm,nouvel_admin
```

Relance le bot.

### Méthode 2 : Modifier en live (futur)

On pourrait ajouter une commande :
```
!admin addadmin nouvel_username
```

Mais pour l'instant, modifie le .env et relance.

## 📊 Comparaison

| Méthode | Avant (IDs) | Maintenant (Usernames) |
|---------|-------------|------------------------|
| **Lisibilité** | ❌ Difficile | ✅ Facile |
| **Configuration** | ❌ Compliqué | ✅ Simple |
| **Obtention** | ❌ Commande nécessaire | ✅ Tu connais ton username |
| **Mémorisation** | ❌ Impossible | ✅ Facile |
| **Unicité** | ✅ Unique | ✅ Unique |

## 🎉 Résumé

### Configuration simple

Dans `.env` :
```env
ADMIN_USERNAMES=ton_username
```

### Plusieurs admins

```env
ADMIN_USERNAMES=admin1,admin2,admin3
```

### Vérification

Le bot compare `user.username.lower()` avec la liste des admins.

---

**Plus besoin de chercher ton ID ! Utilise juste ton username ! 👤**

**Configuration : `ADMIN_USERNAMES=ton_username` dans .env**
