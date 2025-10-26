"""
Script pour vérifier les items de BASE (basic items)
Ces items sont différents des free items et incluent cheveux, yeux, etc.
"""

import requests
import sys
import io
from collections import defaultdict

# Fix encoding pour Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("=" * 60)
print("VÉRIFICATION DES BASIC ITEMS")
print("=" * 60)

# Tester différentes raretés
rarities = ['none', 'common', 'uncommon', 'rare']

all_categories = defaultdict(lambda: defaultdict(list))

for rarity in rarities:
    print(f"\n🔍 Recherche avec rarity={rarity}...")
    
    try:
        url = f'https://webapi.highrise.game/items?rarity={rarity}&limit=200'
        response = requests.get(url)
        data = response.json()
        
        items = data.get('items', [])
        print(f"  Trouvés: {len(items)} items")
        
        # Organiser par catégorie
        for item in items:
            category = item.get('category', 'unknown')
            
            # Ne garder que les items gratuits (is_purchasable=false, is_tradable=false)
            if not item.get('is_purchasable', False) and not item.get('is_tradable', False):
                all_categories[category][rarity].append(item)
        
    except Exception as e:
        print(f"  Erreur: {e}")

# Afficher les résultats
print("\n" + "=" * 60)
print("CATÉGORIES TROUVÉES (items gratuits)")
print("=" * 60)

important_categories = ['hair_front', 'hair_back', 'eye', 'eyebrow', 'nose', 'mouth', 'body', 'freckle']

for category in sorted(all_categories.keys()):
    items_by_rarity = all_categories[category]
    total = sum(len(items) for items in items_by_rarity.values())
    
    emoji = {
        'hair_front': '💇',
        'hair_back': '💇',
        'eye': '👁️',
        'eyebrow': '👁️',
        'nose': '👃',
        'mouth': '👄',
        'body': '🧍',
        'freckle': '✨',
        'shoes': '👟',
        'shirt': '👕',
        'pants': '👖',
    }.get(category, '📦')
    
    print(f"\n{emoji} {category.upper()}: {total} items gratuits")
    
    for rarity, items in items_by_rarity.items():
        print(f"  - {rarity}: {len(items)} items")
        
        # Afficher quelques exemples
        if category in important_categories and items:
            for item in items[:3]:
                print(f"    • {item['item_name']} ({item['id']})")

# Chercher spécifiquement les items de base
print("\n" + "=" * 60)
print("RECHERCHE D'ITEMS DE BASE SPÉCIFIQUES")
print("=" * 60)

# Chercher des patterns connus pour les items de base
base_patterns = [
    'basic',
    'starter',
    'default',
    'flesh',
    'skin'
]

print("\n🔍 Recherche d'items avec patterns de base...")

for pattern in base_patterns:
    try:
        url = f'https://webapi.highrise.game/items?limit=100'
        response = requests.get(url)
        data = response.json()
        
        items = data.get('items', [])
        
        matching_items = []
        for item in items:
            item_id = item.get('id', '').lower()
            item_name = item.get('item_name', '').lower()
            
            if pattern in item_id or pattern in item_name:
                category = item.get('category', 'unknown')
                if category in important_categories:
                    matching_items.append(item)
        
        if matching_items:
            print(f"\n📌 Pattern '{pattern}': {len(matching_items)} items")
            for item in matching_items[:5]:
                print(f"  • {item['item_name']} ({item['category']}) - {item['id']}")
                print(f"    Purchasable: {item.get('is_purchasable')}, Tradable: {item.get('is_tradable')}")
        
    except Exception as e:
        print(f"  Erreur pour pattern '{pattern}': {e}")

# Chercher les items body-flesh spécifiquement
print("\n" + "=" * 60)
print("ITEMS BODY (couleur de peau)")
print("=" * 60)

try:
    url = 'https://webapi.highrise.game/items?category=body&limit=50'
    response = requests.get(url)
    data = response.json()
    
    items = data.get('items', [])
    print(f"\n📊 Trouvés: {len(items)} items body")
    
    for item in items[:10]:
        print(f"\n• {item['item_name']}")
        print(f"  ID: {item['id']}")
        print(f"  Purchasable: {item.get('is_purchasable')}")
        print(f"  Tradable: {item.get('is_tradable')}")
        print(f"  Rarity: {item.get('rarity')}")
        
        # Vérifier les palettes
        palettes = item.get('color_palettes', [])
        if palettes:
            print(f"  Palettes: {len(palettes)} couleurs disponibles")
        
except Exception as e:
    print(f"Erreur: {e}")

print("\n" + "=" * 60)
print("✅ TERMINÉ !")
print("=" * 60)
