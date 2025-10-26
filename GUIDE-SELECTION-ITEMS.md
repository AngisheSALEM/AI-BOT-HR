# 👕 Guide : Sélectionner des items pour créer un outfit

## 🎯 Comment ça marche

Pour créer un outfit, tu dois **sélectionner des items par catégorie** :
- **Haut (shirt)** : T-shirt, chemise, veste, etc.
- **Bas (pants)** : Pantalon, short, jupe, etc.
- **Chaussures (shoes)** : Baskets, bottes, etc.
- **Cheveux (hair)** : Coiffure
- **Accessoires** : Lunettes, chapeau, etc.

## 📋 Étape 1 : Voir ton inventaire

### Commande pour lister l'inventaire

Ajoute cette commande dans `handle_admin_command` (après les autres `elif subcmd`) :

```python
elif subcmd == 'inventory':
    try:
        inventory = await self.highrise.get_inventory()
        
        # Grouper par type
        by_type = {}
        for item in inventory.items:
            item_type = item.type
            if item_type not in by_type:
                by_type[item_type] = []
            by_type[item_type].append(item)
        
        # Envoyer par type
        for item_type, items in by_type.items():
            msg = f"\n=== {item_type.upper()} ===\n"
            for i, item in enumerate(items[:10], 1):  # Max 10 par type
                msg += f"{i}. {item.id}\n"
            await self.highrise.send_whisper(user.id, msg)
            await asyncio.sleep(0.5)
        
        await self.highrise.send_whisper(user.id, 
            f"\nTotal: {len(inventory.items)} items")
            
    except Exception as e:
        await self.highrise.send_whisper(user.id, f"Erreur: {e}")
```

**Usage :** `!admin inventory`

**Résultat :**
```
=== SHIRT ===
1. shirt-n_starteritems2019malet_shirt
2. shirt-n_room32019denimjackethoodie
3. shirt-n_room12019blackhoodie

=== PANTS ===
1. pants-n_starteritems2019malepants
2. pants-n_room32019rippedjeans

=== SHOES ===
1. shoes-n_starteritems2019maleshoes
2. shoes-n_room12019sneakers

=== HAIR ===
1. hair-front-n_malenew01
2. hair-back-n_malenew01

Total: 25 items
```

## 📋 Étape 2 : Créer un outfit avec les items

### Format d'un item

```python
from highrise import Item

item = Item(
    type="shirt",  # Type: shirt, pants, shoes, hair, etc.
    id="shirt-n_starteritems2019malet_shirt"  # ID exact de l'item
)
```

### Exemple d'outfit complet

```python
outfit_casual = [
    Item(type="shirt", id="shirt-n_starteritems2019malet_shirt"),
    Item(type="pants", id="pants-n_starteritems2019malepants"),
    Item(type="shoes", id="shoes-n_starteritems2019maleshoes"),
    Item(type="hair", id="hair-front-n_malenew01"),
    Item(type="hair", id="hair-back-n_malenew01")
]
```

## 📋 Étape 3 : Remplir les outfits dans bot.py

Dans `__init__`, remplace les listes vides par tes items :

```python
# Outfits pour rotation automatique
self.outfits = {
    "casual": [
        Item(type="shirt", id="shirt-n_starteritems2019malet_shirt"),
        Item(type="pants", id="pants-n_starteritems2019malepants"),
        Item(type="shoes", id="shoes-n_starteritems2019maleshoes"),
    ],
    "elegant": [
        Item(type="shirt", id="shirt-n_room32019suitjacket"),
        Item(type="pants", id="pants-n_room32019suitpants"),
        Item(type="shoes", id="shoes-n_room32019dressshoes"),
    ],
    "sport": [
        Item(type="shirt", id="shirt-n_room12019hoodie"),
        Item(type="pants", id="pants-n_room12019joggers"),
        Item(type="shoes", id="shoes-n_room12019sneakers"),
    ],
    "night": [
        Item(type="shirt", id="shirt-n_nightoutfit"),
        Item(type="pants", id="pants-n_nightoutfit"),
        Item(type="shoes", id="shoes-n_nightoutfit"),
    ]
}
```

## 📋 Étape 4 : Tester un outfit

### Commande pour tester

Ajoute dans `handle_admin_command` :

```python
elif subcmd == 'testoutfit':
    if subparams:
        outfit_name = subparams[0]
        success = await self.change_outfit_by_name(outfit_name)
        if success:
            await self.highrise.send_whisper(user.id, 
                f"Outfit '{outfit_name}' active!")
        else:
            await self.highrise.send_whisper(user.id, 
                f"Outfit '{outfit_name}' vide ou erreur")
    else:
        available = ", ".join(self.outfits.keys())
        await self.highrise.send_whisper(user.id, 
            f"Outfits: {available}")
```

**Usage :** 
- `!admin testoutfit casual` - Tester l'outfit casual
- `!admin testoutfit` - Voir les outfits disponibles

## 🎨 Types d'items disponibles

| Type | Description | Exemple d'ID |
|------|-------------|--------------|
| **shirt** | Haut (t-shirt, chemise, veste) | `shirt-n_starteritems2019malet_shirt` |
| **pants** | Bas (pantalon, short, jupe) | `pants-n_starteritems2019malepants` |
| **shoes** | Chaussures | `shoes-n_starteritems2019maleshoes` |
| **hair** | Cheveux (front/back) | `hair-front-n_malenew01` |
| **glasses** | Lunettes | `glasses-n_2019glasses` |
| **hat** | Chapeau | `hat-n_2019cap` |
| **bag** | Sac | `bag-n_2019backpack` |
| **watch** | Montre | `watch-n_2019watch` |

## 💡 Exemple complet étape par étape

### 1. Lance le bot et utilise la commande
```
!admin inventory
```

### 2. Note les IDs qui t'intéressent
```
SHIRT:
- shirt-n_starteritems2019malet_shirt (casual)
- shirt-n_room32019suitjacket (elegant)

PANTS:
- pants-n_starteritems2019malepants (casual)
- pants-n_room32019suitpants (elegant)

SHOES:
- shoes-n_starteritems2019maleshoes (casual)
- shoes-n_room32019dressshoes (elegant)
```

### 3. Crée tes outfits dans bot.py

Trouve cette section dans `__init__` (ligne ~36) :

```python
# Outfits pour rotation automatique (remplace par tes vrais IDs)
self.outfits = {
    "casual": [],  # À remplir
    "elegant": [],
    "sport": [],
    "night": []
}
```

Remplace par :

```python
# Outfits pour rotation automatique
self.outfits = {
    "casual": [
        Item(type="shirt", id="shirt-n_starteritems2019malet_shirt"),
        Item(type="pants", id="pants-n_starteritems2019malepants"),
        Item(type="shoes", id="shoes-n_starteritems2019maleshoes"),
    ],
    "elegant": [
        Item(type="shirt", id="shirt-n_room32019suitjacket"),
        Item(type="pants", id="pants-n_room32019suitpants"),
        Item(type="shoes", id="shoes-n_room32019dressshoes"),
    ],
    "sport": [
        Item(type="shirt", id="shirt-n_room12019hoodie"),
        Item(type="pants", id="pants-n_room12019joggers"),
        Item(type="shoes", id="shoes-n_room12019sneakers"),
    ],
    "night": [
        Item(type="shirt", id="shirt-n_nightoutfit"),
        Item(type="pants", id="pants-n_nightoutfit"),
        Item(type="shoes", id="shoes-n_nightoutfit"),
    ]
}
```

### 4. Teste l'outfit
```
!admin testoutfit casual
```

### 5. Active la rotation 6h

Dans `on_start`, ajoute (si pas déjà fait) :

```python
# Démarrer la rotation d'outfits
asyncio.create_task(self.outfit_rotation_6h())
print("[OUTFIT] Rotation 6h demarree")
```

## 🔧 Commandes utiles à ajouter

### Voir l'outfit actuel
```python
elif subcmd == 'currentoutfit':
    try:
        outfit = await self.highrise.get_outfit()
        msg = "Outfit actuel:\n"
        for item in outfit:
            msg += f"- {item.type}: {item.id}\n"
        await self.highrise.send_whisper(user.id, msg)
    except Exception as e:
        await self.highrise.send_whisper(user.id, f"Erreur: {e}")
```

### Sauvegarder l'inventaire dans un fichier
```python
elif subcmd == 'saveinventory':
    try:
        inventory = await self.highrise.get_inventory()
        
        with open('inventory.txt', 'w', encoding='utf-8') as f:
            for item in inventory.items:
                f.write(f"Type: {item.type}\n")
                f.write(f"ID: {item.id}\n")
                f.write("---\n")
        
        await self.highrise.send_whisper(user.id, 
            f"Inventaire sauve: {len(inventory.items)} items dans inventory.txt")
    except Exception as e:
        await self.highrise.send_whisper(user.id, f"Erreur: {e}")
```

## 📝 Résumé

### Pour créer un outfit :

1. **Récupère l'inventaire** : `!admin inventory`
2. **Note les IDs** des items que tu veux
3. **Crée l'outfit** dans `bot.py` :
   ```python
   "casual": [
       Item(type="shirt", id="TON_ID_SHIRT"),
       Item(type="pants", id="TON_ID_PANTS"),
       Item(type="shoes", id="TON_ID_SHOES"),
   ]
   ```
4. **Teste** : `!admin testoutfit casual`
5. **Active la rotation** : La rotation 6h se lance automatiquement

### Structure d'un item :
```python
Item(type="CATEGORIE", id="ID_EXACT_DE_L_ITEM")
```

### Catégories principales :
- `shirt` - Haut
- `pants` - Bas
- `shoes` - Chaussures
- `hair` - Cheveux
- `glasses` - Lunettes
- `hat` - Chapeau

---

**Tu peux combiner autant d'items que tu veux dans un outfit !**

**Les déclarations d'amour ne sont PAS touchées, elles continuent normalement ! 💕**
