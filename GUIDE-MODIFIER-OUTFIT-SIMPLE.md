# 👕 Modifier l'outfit du bot - Guide Simple

## 🎯 Commande intuitive

Maintenant tu peux utiliser le **NOM** de l'item au lieu de l'ID !

## 💻 Utilisation

### Remplacer un item par son nom
```
!admin modifyoutfit replace <nom de l'item>
```

### Exemples

**Changer les chaussures :**
```
!admin modifyoutfit replace Black Flats
!admin modifyoutfit replace Pink Flats
!admin modifyoutfit replace White Converse
```

**Changer la jupe :**
```
!admin modifyoutfit replace Basic Skirt - Black
!admin modifyoutfit replace Pleated Pink Skirt
```

**Changer les chaussettes :**
```
!admin modifyoutfit replace White Socks
!admin modifyoutfit replace Black Thigh High Socks
```

**Changer la montre :**
```
!admin modifyoutfit replace Classic Black Watch
```

## 🔍 Comment ça marche

### 1. Tu envoies la commande
```
!admin modifyoutfit replace Pink Flats
```

### 2. Le bot cherche l'item
```
🔍 Recherche de 'Pink Flats'...
```

### 3. Si trouvé → Équipe automatiquement
```
✅ Pink Flats équipé !
Catégorie: shoes
```

### 4. Si non trouvé → Message d'erreur
```
❌ Item 'Pink Flatss' non trouvé dans les free items
```

## 📋 Noms d'items disponibles (exemples)

### Chaussures (shoes)
- `White Dans`
- `White Flats`
- `Pink Flats`
- `Black Flats`
- `White Converse`

### Jupes (skirt)
- `Basic Skirt - White`
- `Basic Skirt - Blue`
- `Basic Skirt - Black`
- `Pleated Pink Skirt`
- `Pleated Black Skirt`
- `Pleated Skirt Grey`

### Chaussettes (sock)
- `White Socks`
- `Black Socks`
- `White Thigh High Socks`
- `Black Thigh High Socks`
- `White Knee Length Socks`
- `Black Knee Length Socks`
- `Opaque White Tights`

### Montres (watch)
- `Classic Black Watch`

## 🎨 Workflow complet

### 1. Chercher des items disponibles
```
!admin searchitem shoes
```

**Résultat dans les logs :**
```
1. White Dans
2. White Flats
3. Pink Flats
4. Black Flats
5. White Converse
```

### 2. Copier le nom exact
```
Pink Flats
```

### 3. Équiper l'item
```
!admin modifyoutfit replace Pink Flats
```

### 4. Vérifier le résultat
```
!admin currentoutfit
```

## ⚠️ Important

### Nom exact requis
Le nom doit être **exact** (mais insensible à la casse) :

✅ **Correct :**
```
!admin modifyoutfit replace Pink Flats
!admin modifyoutfit replace pink flats
!admin modifyoutfit replace PINK FLATS
```

❌ **Incorrect :**
```
!admin modifyoutfit replace Pink Flat
!admin modifyoutfit replace Flats Pink
!admin modifyoutfit replace Pink
```

### Noms avec tirets
Certains items ont des tirets dans leur nom :
```
!admin modifyoutfit replace Basic Skirt - Black
!admin modifyoutfit replace Basic Skirt - White
```

### Plusieurs mots
Les noms avec plusieurs mots fonctionnent :
```
!admin modifyoutfit replace White Thigh High Socks
!admin modifyoutfit replace Black Knee Length Socks
```

## 🔧 Retirer un item

Pour retirer un item, utilise la catégorie :
```
!admin modifyoutfit remove shoes
!admin modifyoutfit remove skirt
!admin modifyoutfit remove sock
!admin modifyoutfit remove watch
```

## 💡 Astuces

### Trouver le nom exact
Si tu ne connais pas le nom exact :

**1. Cherche par catégorie**
```
!admin searchitem shoes
```

**2. Regarde les logs**
```
1. White Dans
   ID: shoes-n_whitedans

2. White Flats
   ID: shoes-n_starteritems2019flatswhite
```

**3. Copie le nom**
```
White Flats
```

**4. Utilise-le**
```
!admin modifyoutfit replace White Flats
```

### Tester plusieurs items rapidement
```
!admin modifyoutfit replace Pink Flats
!admin modifyoutfit replace Pleated Pink Skirt
!admin modifyoutfit replace White Thigh High Socks
```

## 📊 Comparaison

### Avant (compliqué)
```
!admin modifyoutfit replace shoes-n_starteritems2019flatspink
```
- ❌ ID long et difficile à retenir
- ❌ Besoin de chercher l'ID à chaque fois
- ❌ Risque d'erreur de frappe

### Maintenant (simple)
```
!admin modifyoutfit replace Pink Flats
```
- ✅ Nom simple et lisible
- ✅ Facile à retenir
- ✅ Recherche automatique de l'ID

## 🎉 Résumé

### Commande
```
!admin modifyoutfit replace <nom de l'item>
```

### Exemples pratiques
```
!admin modifyoutfit replace Black Flats
!admin modifyoutfit replace Basic Skirt - Black
!admin modifyoutfit replace White Socks
!admin modifyoutfit replace Classic Black Watch
```

### Workflow
1. **Cherche** : `!admin searchitem shoes`
2. **Copie le nom** : `Pink Flats`
3. **Équipe** : `!admin modifyoutfit replace Pink Flats`
4. **Vérifie** : `!admin currentoutfit`

---

**Plus besoin de retenir les IDs ! Utilise simplement le nom de l'item ! 👕✨**
