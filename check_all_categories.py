"""
Script pour vérifier TOUTES les catégories disponibles dans les free items
"""

import requests
import sys
import io
from collections import defaultdict

# Fix encoding pour Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("=" * 60)
print("VÉRIFICATION DE TOUTES LES CATÉGORIES")
print("=" * 60)

print("\n🔍 Récupération de tous les free items...\n")

all_items = []
limit = 100
skip = 0
max_items = 2000  # Augmenter la limite

while len(all_items) < max_items:
    url = f'https://webapi.highrise.game/items?rarity=none&limit={limit}&skip={skip}'
    
    try:
        response = requests.get(url)
        data = response.json()
        
        items = data.get('items', [])
        if not items:
            break
            
        all_items.extend(items)
        print(f"  Récupérés: {len(all_items)} items...")
        
        if len(items) < limit:
            break
        
        skip += limit
        
    except Exception as e:
        print(f"  Erreur: {e}")
        break

print(f"\n✅ Total récupéré: {len(all_items)} items\n")

# Organiser par catégorie
items_by_category = defaultdict(list)

for item in all_items:
    category = item.get('category', 'unknown')
    items_by_category[category].append(item)

# Dédupliquer par ID
print("🔧 Déduplication par ID...\n")

deduplicated = {}
for category, items in items_by_category.items():
    unique_items = {}
    for item in items:
        item_id = item['id']
        if item_id not in unique_items:
            unique_items[item_id] = item
    
    deduplicated[category] = list(unique_items.values())

# Afficher toutes les catégories
print("=" * 60)
print("TOUTES LES CATÉGORIES TROUVÉES")
print("=" * 60)

emoji_map = {
    'shoes': '👟',
    'skirt': '👗',
    'sock': '🧦',
    'watch': '⌚',
    'shirt': '👕',
    'pants': '👖',
    'hair_front': '💇',
    'hair_back': '💇',
    'hair': '💇',
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
    'earrings': '💎',
    'necklace': '📿',
    'handbag': '👜',
    'fishing_rod': '🎣',
}

for category in sorted(deduplicated.keys()):
    items = deduplicated[category]
    emoji = emoji_map.get(category.lower(), '📦')
    
    # Compter les items vraiment gratuits
    truly_free = [item for item in items if not item.get('is_purchasable', False) and not item.get('is_tradable', False)]
    
    print(f"\n{emoji} {category.upper()}")
    print(f"  Total: {len(items)} items")
    print(f"  Gratuits (équipables sans inventaire): {len(truly_free)} items")
    
    if truly_free:
        print(f"  Exemples:")
        for item in truly_free[:5]:
            print(f"    - {item['item_name']}")
        if len(truly_free) > 5:
            print(f"    ... et {len(truly_free) - 5} autres")

print("\n" + "=" * 60)
print("RÉSUMÉ")
print("=" * 60)

total_items = sum(len(items) for items in deduplicated.values())
total_free = sum(len([item for item in items if not item.get('is_purchasable', False) and not item.get('is_tradable', False)]) for items in deduplicated.values())

print(f"\n📊 Statistiques:")
print(f"  Catégories trouvées: {len(deduplicated)}")
print(f"  Total items: {total_items}")
print(f"  Items gratuits: {total_free}")

# Catégories importantes pour le visage
print("\n" + "=" * 60)
print("CATÉGORIES IMPORTANTES POUR LE VISAGE")
print("=" * 60)

face_categories = ['eye', 'eyebrow', 'nose', 'mouth', 'freckle', 'hair_front', 'hair_back', 'hair', 'body']

for cat in face_categories:
    if cat in deduplicated:
        items = deduplicated[cat]
        truly_free = [item for item in items if not item.get('is_purchasable', False) and not item.get('is_tradable', False)]
        
        emoji = emoji_map.get(cat.lower(), '📦')
        print(f"\n{emoji} {cat.upper()}: {len(truly_free)} items gratuits")
        
        if truly_free:
            for item in truly_free[:10]:
                print(f"  - {item['item_name']} ({item['id']})")
            if len(truly_free) > 10:
                print(f"  ... et {len(truly_free) - 10} autres")
    else:
        print(f"\n❌ {cat.upper()}: Non trouvé")

print("\n" + "=" * 60)
print("✅ TERMINÉ !")
print("=" * 60)
