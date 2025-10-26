# 💡 EXPLICATION : Comment les autres bots ont des cheveux/yeux

## 🎯 La vraie réponse

Les autres bots que tu as vus utilisent les **ITEMS DE BASE** qui sont **automatiquement dans l'inventaire** de chaque compte Highrise !

## 📦 Items de base (Starter Items)

Quand tu crées un compte Highrise, tu reçois automatiquement :

### 🧍 Corps (Body)
- `body-flesh` avec **50+ palettes de couleurs** (couleurs de peau)
- Chaque palette = une couleur différente
- Exemple : `active_palette=0` (peau claire), `active_palette=27` (peau foncée), etc.

### 👁️ Yeux (Eye)
- Plusieurs types d'yeux de base
- Avec palettes de couleurs (couleur des yeux)
- Exemples : `eye-basic`, `eye-round`, etc.

### 👁️ Sourcils (Eyebrow)
- Plusieurs formes de sourcils
- Avec palettes de couleurs
- Exemples : `eyebrow-basic`, `eyebrow-thick`, etc.

### 👄 Bouche (Mouth)
- Plusieurs formes de bouche
- Avec palettes de couleurs
- Exemples : `mouth-basic`, `mouth-smile`, etc.

### 💇 Cheveux (Hair)
- `hair_front` (cheveux devant)
- `hair_back` (cheveux derrière)
- Avec palettes de couleurs (couleur des cheveux)
- Exemples : `hair-front-basic`, `hair-back-long`, etc.

## 🔑 La différence clé

### Free Items (ce qu'on a trouvé)
- **48 items** équipables SANS être dans l'inventaire
- Seulement : nez, vêtements, chaussures, accessoires
- **PAS** de cheveux, yeux, corps

### Starter Items (ce que les autres bots utilisent)
- **100+ items** qui sont **dans l'inventaire** de chaque compte
- Inclut : corps, yeux, sourcils, bouche, cheveux, etc.
- **Nécessitent d'être dans l'inventaire** pour être équipés

## 💻 Comment les autres bots font

### 1. Le bot a un compte Highrise
Le compte du bot possède automatiquement les starter items dans son inventaire.

### 2. Le bot récupère son inventaire
```python
inventory = await self.highrise.get_inventory()
```

### 3. Le bot équipe les items de son inventaire
```python
# Exemple : changer la couleur de peau
body_item = Item(
    type="clothing",
    amount=1,
    id="body-flesh",
    account_bound=False,
    active_palette=27  # Couleur de peau différente
)

# Exemple : changer les yeux
eye_item = Item(
    type="clothing",
    amount=1,
    id="eye-basic2018newnose16",
    account_bound=False,
    active_palette=5  # Couleur des yeux différente
)

await self.highrise.set_outfit([body_item, eye_item, ...])
```

## 🎨 Les palettes de couleurs

Chaque item de base a des **palettes** :

### Body (couleur de peau)
- `active_palette=0` : Peau très claire
- `active_palette=10` : Peau claire
- `active_palette=20` : Peau moyenne
- `active_palette=27` : Peau foncée
- `active_palette=40` : Peau très foncée
- etc. (50+ palettes)

### Eye (couleur des yeux)
- `active_palette=0` : Yeux marron
- `active_palette=5` : Yeux bleus
- `active_palette=10` : Yeux verts
- etc.

### Hair (couleur des cheveux)
- `active_palette=0` : Cheveux noirs
- `active_palette=5` : Cheveux bruns
- `active_palette=10` : Cheveux blonds
- `active_palette=15` : Cheveux roux
- etc.

## ✅ Solution pour ton bot

### Étape 1 : Vérifier l'inventaire du bot
```
!admin inventory
```

Tu devrais voir des items comme :
- `body-flesh`
- `eye-...`
- `eyebrow-...`
- `mouth-...`
- `hair-front-...`
- `hair-back-...`

### Étape 2 : Utiliser ces items
Si ces items sont dans l'inventaire, le bot peut les équiper avec :
```
!admin modifyoutfit replace <nom de l'item>
```

### Étape 3 : Changer les couleurs
Pour changer les couleurs (peau, yeux, cheveux), il faut modifier le code pour supporter `active_palette`.

## 🔧 Modification nécessaire dans bot.py

Actuellement, le bot cherche seulement dans les "free items" (rarity=none).

Il faut aussi chercher dans **l'inventaire du bot** :

```python
# Chercher d'abord dans l'inventaire
inventory = await self.highrise.get_inventory()

for inv_item in inventory.items:
    if item_name.lower() in inv_item.id.lower():
        # Item trouvé dans l'inventaire !
        found_item = {
            'item_id': inv_item.id,
            'item_name': item_name,
            'category': inv_item.id.split('-')[0]  # body, eye, hair, etc.
        }
        break

# Si pas trouvé dans l'inventaire, chercher dans free items
if not found_item:
    response = requests.get('https://webapi.highrise.game/items?rarity=none&limit=500')
    # ...
```

## 🎯 Conclusion

**Les autres bots ont des cheveux/yeux/couleurs parce que :**

1. ✅ Leur compte a les **starter items** dans l'inventaire
2. ✅ Ils équipent ces items depuis leur inventaire
3. ✅ Ils utilisent les **palettes de couleurs** (active_palette)

**Ton bot peut faire pareil si :**

1. ✅ Le compte du bot a un inventaire (tous les comptes en ont un)
2. ✅ Tu modifies le code pour chercher dans l'inventaire
3. ✅ Tu ajoutes le support des palettes de couleurs

---

**Prochaine étape : Vérifier l'inventaire du bot avec `!admin inventory` pour voir quels items il possède !**
