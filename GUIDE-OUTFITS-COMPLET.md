# 👕 Guide Complet des Outfits - Highrise Bot

## 📋 Règles officielles (selon le SDK)

### Items obligatoires minimum
Un outfit **DOIT** contenir :
1. `body-flesh` (avec `active_palette` pour la couleur de peau, défaut: 27)
2. `eye` (yeux)
3. `eyebrow` (sourcils)
4. `nose` (nez)
5. `mouth` (bouche)
6. **ET** l'un de ces combos :
   - `shirt` + `pants`
   - `shirt` + `skirt`
   - `dress`
   - `fullsuit`

**Sans ces items, le serveur rejettera l'outfit !**

### Types d'items

#### Free Items (gratuits)
- Items avec `rarity=none` dans l'API
- **Peuvent être équipés SANS être dans l'inventaire**
- Trouvables sur : https://webapi.highrise.game/items?rarity=none
- Exemples : chaussures basiques, jupes basiques, chaussettes, montres

#### Items payants
- **Doivent être dans l'inventaire** pour être équipés
- Peuvent être achetés avec `buy_item(item_id)` si `is_purchasable=true`
- Exemples : cheveux, vêtements premium, accessoires spéciaux

## 🎯 Approche recommandée

### Méthode 1 : Partir de l'outfit actuel (RECOMMANDÉ)

Le bot récupère automatiquement son outfit actuel au démarrage :

```python
# Au démarrage (dans on_start)
current_outfit = await self.highrise.get_my_outfit()
self.outfits["default"] = current_outfit.outfit
```

**Avantages :**
- ✅ Contient déjà tous les items obligatoires
- ✅ Pas de risque de rejet par le serveur
- ✅ Facile à modifier ensuite

### Méthode 2 : Créer un outfit complet from scratch

Si tu veux créer un outfit de zéro, tu DOIS inclure tous les items obligatoires :

```python
outfit = [
    # OBLIGATOIRES - Corps et visage
    Item(type="clothing", amount=1, id="body-flesh", account_bound=False, active_palette=27),
    Item(type="clothing", amount=1, id="eye-n_basic2018malesquaresleepy", account_bound=False, active_palette=7),
    Item(type="clothing", amount=1, id="eyebrow-n_basic2018newbrows07", account_bound=False, active_palette=0),
    Item(type="clothing", amount=1, id="nose-n_basic2018newnose05", account_bound=False, active_palette=0),
    Item(type="clothing", amount=1, id="mouth-basic2018chippermouth", account_bound=False, active_palette=-1),
    
    # OBLIGATOIRES - Vêtements (shirt + pants OU shirt + skirt)
    Item(type="clothing", amount=1, id="shirt-n_starteritems2019pulloverblack", account_bound=False, active_palette=0),
    Item(type="clothing", amount=1, id="pants-n_starteritems2019cuffedjeanswhite", account_bound=False, active_palette=0),
    
    # OPTIONNELS - Accessoires
    Item(type="clothing", amount=1, id="shoes-n_starteritems2019flatsblack", account_bound=False, active_palette=0),
    Item(type="clothing", amount=1, id="sock-n_starteritems2020whitesocks", account_bound=False, active_palette=0),
]
```

## 💻 Commandes disponibles

### 1. Voir l'outfit actuel
```
!admin currentoutfit
```

### 2. Analyser l'outfit d'un utilisateur
```
!admin analyzeoutfit username
```
Affiche tous les items avec noms et IDs + génère le code Python

### 3. Modifier l'outfit actuel

**Ajouter un item :**
```
!admin modifyoutfit add shoes-n_starteritems2019flatsblack
```

**Retirer un item par catégorie :**
```
!admin modifyoutfit remove shoes
!admin modifyoutfit remove shirt
```

### 4. Chercher des items

**Par catégorie :**
```
!admin searchitem shoes
!admin searchitem shirt
```

**Par nom exact :**
```
!admin searchitem name Black Flats
```

### 5. Vérifier l'inventaire
```
!admin inventory
```

### 6. Acheter un item
```
!admin buyitem shirt-n_starteritems2019pulloverblack
```

## 🎨 Workflow pratique

### Scénario 1 : Modifier l'outfit actuel

**1. Voir l'outfit actuel**
```
!admin currentoutfit
```

**2. Chercher un item à ajouter**
```
!admin searchitem shoes
```

**3. Ajouter l'item**
```
!admin modifyoutfit add shoes-n_starteritems2019flatspink
```

**4. Vérifier le résultat**
```
!admin currentoutfit
```

### Scénario 2 : Copier l'outfit d'un utilisateur

**1. Analyser l'outfit**
```
!admin analyzeoutfit sylver_ralx_lm
```

**2. Copier le code Python depuis les logs**
```python
outfit = [
    Item(type="clothing", amount=1, id="shirt-..."),
    Item(type="clothing", amount=1, id="pants-..."),
    ...
]
```

**3. Ajouter les items un par un**
```
!admin modifyoutfit add shirt-n_starteritems2019pulloverblack
!admin modifyoutfit add pants-n_room32019baggytrackpantsgreycamo
```

### Scénario 3 : Créer un outfit avec free items uniquement

**1. Chercher des free items**
```
!admin searchitem shoes
!admin searchitem skirt
```

**2. Vérifier que ce sont des free items**
Regarde dans les logs : `Free: Oui`

**3. Ajouter les items**
```
!admin modifyoutfit add shoes-n_starteritems2019flatsblack
!admin modifyoutfit add skirt-n_starteritems2018blackskirt
```

## ⚠️ Erreurs courantes

### Erreur : "Item not in inventory"
**Cause :** L'item n'est pas dans l'inventaire du bot

**Solutions :**
1. Utilise un **free item** à la place
2. Achète l'item : `!admin buyitem <item_id>`
3. Crée le bot sur un compte qui possède déjà l'item

### Erreur : "Invalid outfit"
**Cause :** L'outfit ne contient pas tous les items obligatoires

**Solution :** Pars de l'outfit actuel et modifie-le au lieu de créer un outfit from scratch

### Erreur : "Duplicate item category"
**Cause :** Tu essaies d'équiper 2 items de la même catégorie de base (ex: 2 bouches)

**Solution :** Retire l'ancien item avant d'ajouter le nouveau :
```
!admin modifyoutfit remove mouth
!admin modifyoutfit add mouth-basic2018chippermouth
```

## 📊 Structure d'un Item

```python
Item(
    type="clothing",           # Toujours "clothing" pour les vêtements
    amount=1,                  # Toujours 1 pour les outfits
    id="item-id",              # ID unique de l'item
    account_bound=False,       # False = échangeable (pas important pour les bots)
    active_palette=0           # Couleur/palette (0 par défaut, 27 pour body-flesh)
)
```

## 🎯 Résumé des bonnes pratiques

### ✅ À FAIRE
- Partir de l'outfit actuel du bot
- Utiliser `modifyoutfit` pour ajouter/retirer des items
- Utiliser des **free items** quand possible
- Vérifier l'inventaire avant d'équiper un item payant
- Analyser les outfits d'autres utilisateurs pour inspiration

### ❌ À ÉVITER
- Créer un outfit from scratch sans tous les items obligatoires
- Oublier `body-flesh`, `eye`, `eyebrow`, `nose`, `mouth`
- Essayer d'équiper des items non-free sans les avoir dans l'inventaire
- Équiper 2 items de la même catégorie de base

## 🔗 Ressources

- **API Free Items** : https://webapi.highrise.game/items?rarity=none
- **API Tous les Items** : https://webapi.highrise.game/items
- **Documentation SDK** : https://create.highrise.game/learn/bots/guides/change-bot-appearance

---

**Le bot récupère automatiquement son outfit actuel au démarrage. Utilise `!admin modifyoutfit` pour le personnaliser ! 👕✨**
