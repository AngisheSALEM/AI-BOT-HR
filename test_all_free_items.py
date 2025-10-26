"""
Script pour tester tous les free items Highrise
Récupère les 584 items et teste lesquels sont équipables sans inventaire
"""

import requests
import json
from collections import defaultdict
import sys
import io

# Fix encoding pour Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("=" * 60)
print("TEST DE TOUS LES FREE ITEMS HIGHRISE")
print("=" * 60)

# Étape 1 : Récupérer tous les free items avec pagination
print("\n[1/4] Récupération de tous les free items...")

all_items = []
limit = 100
skip = 0
max_items = 1000  # Limiter à 1000 items pour éviter timeout

while len(all_items) < max_items:
    url = f'https://webapi.highrise.game/items?rarity=none&limit={limit}&skip={skip}'
    print(f"  Requête: skip={skip}, limit={limit}")
    
    try:
        response = requests.get(url)
        data = response.json()
        
        items = data.get('items', [])
        all_items.extend(items)
        
        print(f"  Récupérés: {len(items)} items (Total: {len(all_items)})")
        
        # Si on a récupéré moins que la limite, c'est la dernière page
        if len(items) < limit:
            break
        
        skip += limit
        
    except Exception as e:
        print(f"  Erreur: {e}")
        break

print(f"\n✅ Total récupéré: {len(all_items)} items")

# Étape 2 : Organiser par catégorie
print("\n[2/4] Organisation par catégorie...")

items_by_category = defaultdict(list)

for item in all_items:
    category = item.get('category', 'unknown')
    items_by_category[category].append(item)

print(f"\n📊 Catégories trouvées: {len(items_by_category)}")
for category, items in sorted(items_by_category.items()):
    print(f"  - {category.upper()}: {len(items)} items")

# Étape 3 : Identifier les items équipables (is_purchasable=false et is_tradable=false)
print("\n[3/4] Analyse des items équipables sans inventaire...")

truly_free_items = []
purchasable_items = []
tradable_items = []

for item in all_items:
    is_purchasable = item.get('is_purchasable', False)
    is_tradable = item.get('is_tradable', False)
    
    if not is_purchasable and not is_tradable:
        truly_free_items.append(item)
    elif is_purchasable:
        purchasable_items.append(item)
    elif is_tradable:
        tradable_items.append(item)

print(f"\n📋 Analyse:")
print(f"  - Items VRAIMENT gratuits (équipables sans inventaire): {len(truly_free_items)}")
print(f"  - Items achetables (nécessitent gold): {len(purchasable_items)}")
print(f"  - Items échangeables (nécessitent inventaire): {len(tradable_items)}")

# Étape 4 : Sauvegarder les résultats
print("\n[4/4] Sauvegarde des résultats...")

# Organiser les truly free items par catégorie
truly_free_by_category = defaultdict(list)
for item in truly_free_items:
    category = item.get('category', 'unknown')
    truly_free_by_category[category].append(item)

# Créer le rapport
report = {
    'total_free_items': len(all_items),
    'truly_free_items': len(truly_free_items),
    'purchasable_items': len(purchasable_items),
    'tradable_items': len(tradable_items),
    'categories': {}
}

for category, items in sorted(truly_free_by_category.items()):
    report['categories'][category] = {
        'count': len(items),
        'items': [
            {
                'id': item['item_id'],
                'name': item['item_name'],
                'is_purchasable': item.get('is_purchasable', False),
                'is_tradable': item.get('is_tradable', False),
                'pops_price': item.get('pops_sale_price', 0)
            }
            for item in sorted(items, key=lambda x: x['item_name'])
        ]
    }

# Sauvegarder en JSON
with open('free_items_report.json', 'w', encoding='utf-8') as f:
    json.dump(report, f, indent=2, ensure_ascii=False)

print(f"✅ Rapport sauvegardé: free_items_report.json")

# Créer un fichier Markdown lisible
print("\n[BONUS] Création du fichier Markdown...")

markdown = f"""# 📋 Rapport complet des Free Items Highrise

**Date de génération** : {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 📊 Statistiques globales

- **Total free items (rarity=none)** : {len(all_items)}
- **Items VRAIMENT gratuits** (équipables sans inventaire) : {len(truly_free_items)}
- **Items achetables** (nécessitent gold) : {len(purchasable_items)}
- **Items échangeables** (nécessitent inventaire) : {len(tradable_items)}

---

## 🎯 Items équipables SANS inventaire

Ces items peuvent être équipés par un bot sans être dans son inventaire.

"""

for category in sorted(truly_free_by_category.keys()):
    items = truly_free_by_category[category]
    
    emoji = {
        'shoes': '👟',
        'skirt': '👗',
        'sock': '🧦',
        'watch': '⌚',
        'shirt': '👕',
        'pants': '👖',
        'hair_front': '💇',
        'hair_back': '💇',
        'glasses': '👓',
        'hat': '🎩',
        'bag': '👜',
        'dress': '👗',
        'body': '🧍',
        'eye': '👁️',
        'eyebrow': '👁️',
        'nose': '👃',
        'mouth': '👄',
        'freckle': '✨',
        'tattoo': '🎨',
    }.get(category.lower(), '📦')
    
    markdown += f"\n### {emoji} {category.upper()} ({len(items)} items)\n\n"
    
    for item in sorted(items, key=lambda x: x['item_name']):
        markdown += f"#### {item['item_name']}\n"
        markdown += f"- **ID** : `{item['item_id']}`\n"
        markdown += f"- **Achetable** : {'Oui' if item.get('is_purchasable') else 'Non'}\n"
        markdown += f"- **Échangeable** : {'Oui' if item.get('is_tradable') else 'Non'}\n"
        
        if item.get('pops_sale_price', 0) > 0:
            markdown += f"- **Prix** : {item['pops_sale_price']} pops\n"
        
        markdown += f"\n**Commande :**\n```\n!admin modifyoutfit replace {item['item_name']}\n```\n\n"
        markdown += "---\n\n"

markdown += f"""
## 📊 Résumé par catégorie

| Catégorie | Nombre d'items |
|-----------|----------------|
"""

for category in sorted(truly_free_by_category.keys()):
    count = len(truly_free_by_category[category])
    markdown += f"| {category.upper()} | {count} |\n"

markdown += """

---

## 💡 Comment utiliser

### Équiper un item
```
!admin modifyoutfit replace <nom de l'item>
```

### Exemples
```
!admin modifyoutfit replace Black Flats
!admin modifyoutfit replace Basic Skirt - Black
!admin modifyoutfit replace White Socks
```

### Retirer un item
```
!admin modifyoutfit remove <category>
```

---

**Généré automatiquement par test_all_free_items.py**
"""

with open('FREE_ITEMS_COMPLET.md', 'w', encoding='utf-8') as f:
    f.write(markdown)

print(f"✅ Documentation créée: FREE_ITEMS_COMPLET.md")

# Afficher un résumé
print("\n" + "=" * 60)
print("RÉSUMÉ")
print("=" * 60)
print(f"\n📊 Items VRAIMENT gratuits par catégorie:\n")

for category in sorted(truly_free_by_category.keys()):
    count = len(truly_free_by_category[category])
    print(f"  {category.upper():20} : {count:3} items")

print(f"\n💾 Fichiers créés:")
print(f"  - free_items_report.json (données brutes)")
print(f"  - FREE_ITEMS_COMPLET.md (documentation)")

print("\n" + "=" * 60)
print("✅ TERMINÉ !")
print("=" * 60)
