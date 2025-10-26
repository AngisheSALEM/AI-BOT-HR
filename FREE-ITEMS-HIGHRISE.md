# 🎁 FREE ITEMS - Habiller ton bot gratuitement !

## 🎉 DÉCOUVERTE IMPORTANTE !

Tu avais raison ! Il existe **584 items gratuits** (`rarity=none`) que les bots peuvent utiliser **SANS les acheter** !

## 🔗 API des Free Items

**URL :** https://webapi.highrise.game/items?rarity=none

Cette API liste **tous les items gratuits** disponibles pour les bots !

## 📋 Catégories d'items gratuits

D'après l'API, voici les catégories disponibles :

### 👕 Vêtements
- **Shirts** (hauts)
- **Pants** (pantalons)
- **Skirts** (jupes)
- **Shoes** (chaussures)
- **Socks** (chaussettes)

### 💍 Accessoires
- **Watch** (montres)
- **Glasses** (lunettes)
- **Hat** (chapeaux)
- **Bag** (sacs)

### 💇 Cheveux & Corps
- **Hair** (cheveux)
- **Body** (corps)
- **Eyes** (yeux)
- **Nose** (nez)
- **Mouth** (bouche)

## 🎨 Exemples d'items gratuits

### Chaussures (Shoes)
```python
"shoes-n_whitedans"  # White Dans
"shoes-n_starteritems2019flatswhite"  # White Flats
"shoes-n_starteritems2019flatspink"  # Pink Flats
"shoes-n_starteritems2019flatsblack"  # Black Flats
"shoes-n_starteritems2018conversewhite"  # White Converse
```

### Jupes (Skirts)
```python
"skirt-n_starteritems2018whiteskirt"  # Basic Skirt - White
"skirt-n_starteritems2018blueskirt"  # Basic Skirt - Blue
"skirt-n_starteritems2018blackskirt"  # Basic Skirt - Black
"skirt-n_room12019pleatedskirtpink"  # Pleated Pink Skirt
"skirt-n_room12019pleatedskirtblack"  # Pleated Black Skirt
```

### Chaussettes (Socks)
```python
"sock-n_starteritems2020whitesocks"  # White Socks
"sock-n_starteritems2020blacksocks"  # Black Socks
"sock-n_starteritems2020whitethighhighs"  # White Thigh High Socks
"sock-n_starteritems2020blackthighhighs"  # Black Thigh High Socks
"sock-n_starteritems2020whitekneelength"  # White Knee Length Socks
```

### Accessoires
```python
"watch-n_room32019blackwatch"  # Classic Black Watch
```

## 💻 Comment utiliser les free items

### Méthode 1 : Directement dans le code

Tu peux équiper **n'importe quel free item** sans l'avoir dans l'inventaire !

```python
self.outfits = {
    "casual": [
        Item(type="shoes", id="shoes-n_whitedans"),
        Item(type="skirt", id="skirt-n_starteritems2018blackskirt"),
        Item(type="sock", id="sock-n_starteritems2020blacksocks"),
    ],
    "elegant": [
        Item(type="shoes", id="shoes-n_starteritems2019flatsblack"),
        Item(type="skirt", id="skirt-n_starteritems2018whiteskirt"),
        Item(type="watch", id="watch-n_room32019blackwatch"),
    ],
}
```

### Méthode 2 : Récupérer la liste complète

Ajoute une commande pour télécharger tous les free items :

```python
elif subcmd == 'freeitems':
    try:
        import requests
        response = requests.get('https://webapi.highrise.game/items?rarity=none')
        data = response.json()
        
        print("\n" + "="*60)
        print(f"🎁 FREE ITEMS DISPONIBLES ({data['total']} items)")
        print("="*60)
        
        # Grouper par catégorie
        by_category = {}
        for item in data['items']:
            category = item['category']
            if category not in by_category:
                by_category[category] = []
            by_category[category].append(item)
        
        # Afficher par catégorie
        for category, items in sorted(by_category.items()):
            print(f"\n=== {category.upper()} ({len(items)} items) ===")
            for item in items[:20]:  # Limiter à 20 par catégorie
                print(f"  {item['item_id']} - {item['item_name']}")
        
        print("\n" + "="*60)
        
        await self.highrise.send_whisper(user.id, 
            f"✅ {data['total']} free items affiches dans les logs")
            
    except Exception as e:
        print(f"[ERREUR] Free items: {e}")
        await self.highrise.send_whisper(user.id, f"Erreur: {e}")
```

## 🎯 Créer des outfits avec free items

### Outfit Féminin
```python
"feminine": [
    Item(type="shoes", id="shoes-n_starteritems2019flatspink"),
    Item(type="skirt", id="skirt-n_room12019pleatedskirtpink"),
    Item(type="sock", id="sock-n_starteritems2020whitethighhighs"),
]
```

### Outfit Casual
```python
"casual": [
    Item(type="shoes", id="shoes-n_starteritems2018conversewhite"),
    Item(type="sock", id="sock-n_starteritems2020whitesocks"),
]
```

### Outfit Élégant
```python
"elegant": [
    Item(type="shoes", id="shoes-n_starteritems2019flatsblack"),
    Item(type="skirt", id="skirt-n_starteritems2018blackskirt"),
    Item(type="watch", id="watch-n_room32019blackwatch"),
]
```

## 📊 Statistiques

D'après l'API :
- **Total : 584 items gratuits**
- **Catégories multiples** : shoes, skirts, socks, watch, etc.
- **Tous utilisables** par les bots sans achat

## ⚠️ Important

### Free items vs Items achetés

**Free items (`rarity=none`) :**
- ✅ Utilisables **sans** les avoir dans l'inventaire
- ✅ **Gratuits** - pas besoin de gold
- ✅ **584 items** disponibles
- ✅ Identifiés par `"rarity": "none_"` dans l'API

**Items normaux :**
- ❌ Doivent être dans l'inventaire
- ❌ Doivent être achetés avec du gold
- ✅ Plus de variété

### Comment identifier un free item

Dans l'API, cherche :
```json
{
  "item_id": "shoes-n_whitedans",
  "rarity": "none_",
  "is_purchasable": true,
  "is_tradable": false
}
```

Si `"rarity": "none_"` → C'est un **free item** !

## 🔧 Commande à ajouter

Ajoute cette commande dans ton bot pour lister les free items :

```python
elif subcmd == 'freeitems':
    # Code ci-dessus
```

**Usage :** `!admin freeitems`

## 🎉 Conclusion

### Tu avais raison !

✅ **584 items gratuits** disponibles
✅ **Pas besoin de les acheter**
✅ **Pas besoin de les avoir dans l'inventaire**
✅ **Utilisables directement** dans les outfits

### Prochaines étapes

1. **Explore l'API** : https://webapi.highrise.game/items?rarity=none
2. **Choisis des items** que tu aimes
3. **Crée des outfits** avec ces items
4. **Teste** avec `!admin testoutfit`

---

**Il y a 584 items gratuits ! Tu peux créer plein d'outfits sans dépenser de gold ! 🎁✨**

**API : https://webapi.highrise.game/items?rarity=none**
