# 🔍 Chercher des items par catégorie ou nom

## 🎯 Commande : !admin searchitem

Deux modes de recherche :
1. **Par catégorie** - Liste tous les items d'une catégorie
2. **Par nom exact** - Trouve l'ID d'un item spécifique

## 💻 Utilisation

### Mode 1 : Recherche par catégorie
```
!admin searchitem <catégorie>
```

**Catégories disponibles :**
- `shoes` - Chaussures
- `shirt` - Hauts
- `pants` - Pantalons
- `skirt` - Jupes
- `sock` - Chaussettes
- `hair` - Cheveux
- `watch` - Montres
- `glasses` - Lunettes
- `hat` - Chapeaux
- `bag` - Sacs

**Exemple - Voir toutes les chaussures :**
```
!admin searchitem shoes
```

**Résultat dans les logs :**
```
============================================================
👕 CATÉGORIE: SHOES
📦 18 items disponibles
============================================================
1. White Dans
   ID: shoes-n_whitedans

2. White Flats
   ID: shoes-n_starteritems2019flatswhite

3. Pink Flats
   ID: shoes-n_starteritems2019flatspink

4. Black Flats
   ID: shoes-n_starteritems2019flatsblack

5. White Converse
   ID: shoes-n_starteritems2018conversewhite

... (30 premiers affichés)
============================================================
📊 Total: 18 items dans 'shoes'
============================================================
```

### Mode 2 : Recherche par nom exact
```
!admin searchitem name <nom exact>
```

**Exemple - Trouver l'ID de "Black Flats" :**
```
!admin searchitem name Black Flats
```

**Résultat dans les logs :**
```
============================================================
🔍 RECHERCHE PAR NOM: 'Black Flats'
============================================================
✅ Black Flats
   ID: shoes-n_starteritems2019flatsblack
   Type: shoes
   Free: Oui

============================================================
📊 1 résultat(s) trouvé(s)
============================================================
```

## 📋 Exemples de recherches

### Par catégorie
```bash
# Toutes les chaussures
!admin searchitem shoes

# Toutes les jupes
!admin searchitem skirt

# Toutes les chaussettes
!admin searchitem sock

# Tous les hauts
!admin searchitem shirt

# Tous les pantalons
!admin searchitem pants

# Toutes les montres
!admin searchitem watch
```

### Par nom exact
```bash
# Chercher "Black Flats"
!admin searchitem name Black Flats

# Chercher "White Converse"
!admin searchitem name White Converse

# Chercher "Pleated Pink Skirt"
!admin searchitem name Pleated Pink Skirt

# Chercher "Classic Black Watch"
!admin searchitem name Classic Black Watch

# Chercher "White Thigh High Socks"
!admin searchitem name White Thigh High Socks
```

## 🎨 Workflow complet

### Méthode 1 : Chercher par catégorie

**1. Lister toutes les chaussures**
```
!admin searchitem shoes
```

**2. Regarder les logs et choisir**
```
3. Pink Flats
   ID: shoes-n_starteritems2019flatspink
```

**3. Copier l'ID**
```
shoes-n_starteritems2019flatspink
```

**4. Utiliser dans bot.py**
```python
Item(type="shoes", id="shoes-n_starteritems2019flatspink")
```

### Méthode 2 : Chercher par nom exact

**1. Tu vois "Black Flats" dans Highrise**

**2. Chercher l'ID exact**
```
!admin searchitem name Black Flats
```

**3. Copier l'ID depuis les logs**
```
shoes-n_starteritems2019flatsblack
```

**4. Utiliser dans bot.py**
```python
Item(type="shoes", id="shoes-n_starteritems2019flatsblack")
```

## 💡 Astuces

### Recherche partielle
La recherche fonctionne avec des mots partiels :
- `!admin searchitem black` → Trouve tous les items avec "black" dans le nom
- `!admin searchitem sock` → Trouve tous les types de chaussettes

### Plusieurs mots
Tu peux chercher plusieurs mots :
```
!admin searchitem white flats
```

### Sensibilité à la casse
La recherche n'est **pas sensible** à la casse :
- `black` = `Black` = `BLACK`

## 📊 Informations affichées

Pour chaque item trouvé :
- ✅ **Nom complet** de l'item
- ✅ **ID** (à copier pour l'utiliser)
- ✅ **Type** (shoes, skirt, sock, etc.)
- ✅ **Free** (Oui = gratuit, utilisable sans achat)

## 🎯 Exemples pratiques

### Créer un outfit noir
```
!admin searchitem black
```

Copie les IDs et crée :
```python
"black_outfit": [
    Item(type="shoes", id="shoes-n_starteritems2019flatsblack"),
    Item(type="skirt", id="skirt-n_starteritems2018blackskirt"),
    Item(type="sock", id="sock-n_starteritems2020blacksocks"),
    Item(type="watch", id="watch-n_room32019blackwatch"),
]
```

### Créer un outfit rose
```
!admin searchitem pink
```

Résultat :
```python
"pink_outfit": [
    Item(type="shoes", id="shoes-n_starteritems2019flatspink"),
    Item(type="skirt", id="skirt-n_room12019pleatedskirtpink"),
]
```

### Chercher des chaussures spécifiques
```
!admin searchitem converse
```

Résultat :
```python
"casual": [
    Item(type="shoes", id="shoes-n_starteritems2018conversewhite"),
]
```

## ⚠️ Important

### La commande cherche dans les free items
- Actuellement, la commande cherche dans les **584 free items**
- Ces items sont **gratuits** et **utilisables sans achat**
- Si tu veux chercher dans TOUS les items (payants inclus), on peut modifier la commande

### Résultats dans les logs
- Les résultats s'affichent dans les **logs du bot**
- Tu reçois une **confirmation en DM**
- Copie les IDs depuis les logs

## 🔧 Commandes liées

```bash
# Chercher un item
!admin searchitem black

# Voir l'inventaire actuel
!admin inventory

# Tester un outfit
!admin testoutfit casual

# Voir l'outfit actuel
!admin currentoutfit
```

## 🎉 Résumé

### Commande
```
!admin searchitem <nom>
```

### Exemples
```
!admin searchitem black
!admin searchitem white shoes
!admin searchitem skirt
!admin searchitem converse
```

### Résultat
- Liste des items correspondants
- Avec leurs IDs
- Dans les logs du bot
- Prêts à copier et utiliser !

---

**Cherche n'importe quel item par son nom et récupère son ID ! 🔍✨**
