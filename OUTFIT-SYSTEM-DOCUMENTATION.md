# 👕 Système de gestion d'outfit - Documentation complète

## 🎯 Vue d'ensemble

Le bot peut changer son outfit en utilisant `self.highrise.set_outfit(outfit)`.

### Capacités du bot
- ✅ Équiper des **free items** (sans être dans l'inventaire)
- ✅ Équiper des **items de son inventaire**
- ✅ Modifier son outfit par **nom d'item** (recherche automatique)
- ✅ Récupérer son outfit actuel au démarrage
- ✅ Analyser l'outfit d'autres utilisateurs

---

## 📋 Free items disponibles (20 items)

### 👟 Chaussures (5)
- Black Flats
- Pink Flats
- White Flats
- White Dans
- White Converse

### 👗 Jupes (7)
- Basic Skirt - Black
- Basic Skirt - Blue
- Basic Skirt - White
- Plaid Skirt With Socks
- Pleated Black Skirt
- Pleated Pink Skirt
- Pleated Skirt Grey

### 🧦 Chaussettes (7)
- Black Knee Length Socks
- Black Socks
- Black Thigh High Socks
- Opaque White Tights
- White Knee Length Socks
- White Socks
- White Thigh High Socks

### ⌚ Montres (1)
- Classic Black Watch

---

## 💻 Commandes disponibles

### 1. Modifier l'outfit (par nom)
```
!admin modifyoutfit replace <nom de l'item>
```

**Exemples :**
```
!admin modifyoutfit replace Black Flats
!admin modifyoutfit replace Pleated Pink Skirt
!admin modifyoutfit replace White Thigh High Socks
```

### 2. Retirer un item
```
!admin modifyoutfit remove <category>
```

### 3. Voir l'outfit actuel
```
!admin currentoutfit
```

### 4. Analyser l'outfit d'un utilisateur
```
!admin analyzeoutfit <username>
```

### 5. Chercher des items
```
!admin searchitem <category>
```

### 6. Voir l'inventaire
```
!admin inventory
```

### 7. Acheter un item
```
!admin buyitem <item_id>
```

---

## 🔧 Utilisation dans le code

### Récupérer l'outfit actuel
```python
current_outfit = await self.highrise.get_my_outfit()
outfit_items = current_outfit.outfit
```

### Créer un outfit
```python
from highrise import Item

outfit = [
    Item(type="clothing", amount=1, id="shoes-n_starteritems2019flatsblack", 
         account_bound=False, active_palette=0),
    Item(type="clothing", amount=1, id="skirt-n_starteritems2018blackskirt", 
         account_bound=False, active_palette=0),
]
```

### Appliquer un outfit
```python
await self.highrise.set_outfit(outfit)
```

### Modifier un item
```python
# Récupérer l'outfit actuel
current_outfit = await self.highrise.get_my_outfit()
outfit_items = list(current_outfit.outfit)

# Retirer les chaussures
outfit_items = [item for item in outfit_items if not item.id.startswith("shoes-")]

# Ajouter nouvelles chaussures
new_shoes = Item(type="clothing", amount=1, id="shoes-n_starteritems2019flatspink",
                 account_bound=False, active_palette=0)
outfit_items.append(new_shoes)

# Appliquer
await self.highrise.set_outfit(outfit_items)
```

---

## ⚠️ Règles importantes

### Items obligatoires minimum
Un outfit DOIT contenir :
- `body-flesh` (avec active_palette pour couleur de peau)
- `eye`, `eyebrow`, `nose`, `mouth`
- ET : `shirt+pants` OU `shirt+skirt` OU `dress` OU `fullsuit`

### Types d'items
- **Free items** : Équipables sans inventaire (~20 items)
- **Items payants** : Doivent être dans l'inventaire

---

## 📊 Structure d'un Item

```python
Item(
    type="clothing",
    amount=1,
    id="item-id",
    account_bound=False,
    active_palette=0
)
```

---

## 🎯 Résumé

**Le bot peut équiper :**
- 20 free items (shoes, skirt, sock, watch)
- Items de son inventaire

**Commande principale :**
```
!admin modifyoutfit replace <nom item>
```

**Fichiers de documentation :**
- OUTFIT-SYSTEM-DOCUMENTATION.md (ce fichier)
- GUIDE-MODIFIER-OUTFIT-SIMPLE.md
- GUIDE-OUTFITS-COMPLET.md
- LISTE-FREE-ITEMS-COMPLETE.md
