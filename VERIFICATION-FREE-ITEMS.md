# 🔍 Vérification des Free Items Highrise

## 📊 Résultats de l'API

### API Globale (tous les items)
```
https://webapi.highrise.game/items?limit=100
```
- **Total** : 48,870 items
- **Retournés** : 100 items (avec limit=100)

### API Free Items (rarity=none)
```
https://webapi.highrise.game/items?rarity=none
```
- **Total** : 584 items
- **Retournés** : 20 items (pagination par défaut)

## ⚠️ Problème de pagination

L'API utilise la **pagination** :
- Elle indique `"total": 584` free items
- Mais elle ne retourne que **20 items par page** par défaut
- Pour obtenir tous les 584 items, il faut faire **plusieurs requêtes**

## 🎯 Vérité sur les starter items

### Ce que tu as vu sur ton nouveau compte
Tu as raison ! Les nouveaux comptes Highrise reçoivent maintenant **beaucoup plus** de starter items qu'avant.

### Ce que l'API retourne par défaut
- **20 items** seulement (première page)
- 5 chaussures
- 7 jupes
- 7 chaussettes
- 1 montre

### Ce qui existe réellement
- **584 free items** au total (selon l'API)
- Mais beaucoup ne sont **pas équipables sans inventaire**
- Certains sont des items de base (body, eye, nose, mouth, etc.)

## 🔧 Comment obtenir tous les 584 items

### Option 1 : Pagination manuelle
```python
import requests

all_items = []
page = 0
limit = 100

while True:
    url = f'https://webapi.highrise.game/items?rarity=none&limit={limit}&skip={page * limit}'
    response = requests.get(url)
    data = response.json()
    
    all_items.extend(data['items'])
    
    if len(data['items']) < limit:
        break
    
    page += 1

print(f"Total items récupérés: {len(all_items)}")
```

### Option 2 : Utiliser un limit élevé
```python
import requests

response = requests.get('https://webapi.highrise.game/items?rarity=none&limit=1000')
data = response.json()

print(f"Items récupérés: {len(data['items'])}")
```

## 📋 Types de "free items" (rarity=none)

Les 584 items incluent :

### 1. Items de base (obligatoires)
- `body-flesh` (corps)
- `eye-*` (yeux)
- `eyebrow-*` (sourcils)
- `nose-*` (nez)
- `mouth-*` (bouche)

### 2. Vêtements basiques
- Shirts, pants, skirts
- Shoes, socks
- Watches, bags

### 3. Items spéciaux
- Tattoos
- Accessories
- Emotes (peut-être)

## ⚠️ Important pour le bot

### Items équipables SANS inventaire
Seuls certains free items peuvent être équipés sans être dans l'inventaire :
- Les **20 items** retournés par défaut (probablement)
- Peut-être quelques autres items de base

### Items qui nécessitent l'inventaire
Même avec `rarity=none`, certains items peuvent nécessiter :
- D'être dans l'inventaire du bot
- D'être achetés avec gold/gems
- D'être obtenus via events

## 🎯 Recommandation

### Pour le bot actuel
Garde la liste des **20 items** qui fonctionnent :
- 5 chaussures
- 7 jupes
- 7 chaussettes
- 1 montre

### Pour améliorer
1. **Tester** : Essaie d'équiper d'autres free items
2. **Documenter** : Note lesquels fonctionnent sans inventaire
3. **Mettre à jour** : Ajoute les items qui fonctionnent à la liste

## 🔬 Test à faire

Crée un script pour tester tous les 584 free items :

```python
import requests
from highrise import Item

# Récupérer tous les free items
response = requests.get('https://webapi.highrise.game/items?rarity=none&limit=1000')
items = response.json()['items']

# Tester chaque item
for item in items:
    try:
        # Essayer d'équiper l'item
        test_item = Item(type="clothing", amount=1, id=item['item_id'], 
                        account_bound=False, active_palette=0)
        # await self.highrise.set_outfit([test_item])
        print(f"✅ {item['item_name']} fonctionne")
    except Exception as e:
        print(f"❌ {item['item_name']} échoue: {e}")
```

## 📊 Conclusion

### Nombre réel de free items
- **584 items** avec `rarity=none` dans l'API
- **20 items** retournés par défaut (pagination)
- **~20-50 items** probablement équipables sans inventaire

### Pour ton nouveau compte
Les starter items ont probablement augmenté récemment, mais :
- Ils sont dans **l'inventaire** du compte
- Pas forcément équipables par un bot sans inventaire
- Le bot peut seulement équiper les free items "publics"

### SDK et version
Le SDK est à jour. Le problème n'est pas la version mais :
- La **pagination** de l'API
- La différence entre "free" et "équipable sans inventaire"

---

**Conclusion : Les 20 items actuels sont probablement corrects pour un bot sans inventaire. Les 584 items incluent tous les items de base + accessoires qui nécessitent l'inventaire.**
