"""
Script pour générer la liste complète des free items Highrise
Télécharge depuis l'API et crée un fichier Markdown organisé
"""

import requests
import json
from collections import defaultdict
import sys
import io

# Fix encoding pour Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("Téléchargement des items depuis l'API Highrise...")

# Télécharger les items
response = requests.get('https://webapi.highrise.game/items?rarity=none')
data = response.json()

items = data['items']
total = data['total']

print(f"{total} items téléchargés")

# Organiser par catégorie
items_by_category = defaultdict(list)

for item in items:
    category = item['category']
    items_by_category[category].append(item)

# Trier chaque catégorie par nom
for category in items_by_category:
    items_by_category[category].sort(key=lambda x: x['item_name'])

print(f"{len(items_by_category)} catégories trouvées")

# Créer le fichier Markdown
markdown = f"""# 📋 Liste complète des Free Items Highrise

**Total : {total} free items disponibles**

Source : https://webapi.highrise.game/items?rarity=none

Dernière mise à jour : Octobre 2025

---

## 📊 Table des matières

"""

# Ajouter la table des matières
categories_sorted = sorted(items_by_category.keys())
for category in categories_sorted:
    count = len(items_by_category[category])
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
        'handbag': '👜',
        'dress': '👗',
        'fullsuit': '🦺',
        'eye': '👁️',
        'eyebrow': '👁️',
        'nose': '👃',
        'mouth': '👄',
        'body': '🧍',
        'freckle': '✨',
        'mole': '✨',
        'earrings': '💍',
        'necklace': '📿',
        'tattoo': '🎨',
    }.get(category.lower(), '📦')
    
    markdown += f"- [{emoji} {category.upper()}](#{category.lower()}) ({count} items)\n"

markdown += "\n---\n\n"

# Ajouter chaque catégorie
for category in categories_sorted:
    items_list = items_by_category[category]
    
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
        'handbag': '👜',
        'dress': '👗',
        'fullsuit': '🦺',
        'eye': '👁️',
        'eyebrow': '👁️',
        'nose': '👃',
        'mouth': '👄',
        'body': '🧍',
        'freckle': '✨',
        'mole': '✨',
        'earrings': '💍',
        'necklace': '📿',
        'tattoo': '🎨',
    }.get(category.lower(), '📦')
    
    markdown += f"## {emoji} {category.upper()}\n\n"
    markdown += f"**{len(items_list)} items disponibles**\n\n"
    
    for item in items_list:
        markdown += f"### {item['item_name']}\n"
        markdown += f"- **ID** : `{item['item_id']}`\n"
        markdown += f"- **Catégorie** : {item['category']}\n"
        
        if item['is_purchasable']:
            markdown += f"- **Achetable** : ✅ Oui (avec gold)\n"
        else:
            markdown += f"- **Achetable** : ❌ Non\n"
        
        if item['is_tradable']:
            markdown += f"- **Échangeable** : ✅ Oui\n"
        else:
            markdown += f"- **Échangeable** : ❌ Non\n"
        
        if item['pops_sale_price'] > 0:
            markdown += f"- **Prix** : {item['pops_sale_price']} pops\n"
        
        markdown += f"\n**Commande :**\n"
        markdown += f"```\n!admin modifyoutfit replace {item['item_name']}\n```\n\n"
        markdown += "---\n\n"

# Ajouter le guide d'utilisation
markdown += """
## 💡 Guide d'utilisation

### Équiper un item
```
!admin modifyoutfit replace <nom de l'item>
```

**Exemples :**
```
!admin modifyoutfit replace Black Flats
!admin modifyoutfit replace Pleated Pink Skirt
!admin modifyoutfit replace White Thigh High Socks
```

### Retirer un item
```
!admin modifyoutfit remove <category>
```

**Exemples :**
```
!admin modifyoutfit remove shoes
!admin modifyoutfit remove skirt
```

### Chercher des items
```
!admin searchitem <category>
```

**Exemples :**
```
!admin searchitem shoes
!admin searchitem skirt
!admin searchitem sock
```

### Voir l'outfit actuel
```
!admin currentoutfit
```

### Analyser l'outfit d'un utilisateur
```
!admin analyzeoutfit <username>
```

---

## 📊 Statistiques

"""

# Ajouter les statistiques
markdown += f"### Total : {total} items\n\n"
markdown += "### Par catégorie :\n\n"

for category in categories_sorted:
    count = len(items_by_category[category])
    markdown += f"- **{category.upper()}** : {count} items\n"

# Compter les items achetables
purchasable_count = sum(1 for item in items if item['is_purchasable'])
tradable_count = sum(1 for item in items if item['is_tradable'])

markdown += f"\n### Items achetables avec gold : {purchasable_count}\n"
markdown += f"### Items échangeables : {tradable_count}\n"

markdown += """

---

**Généré automatiquement depuis l'API Highrise**
"""

# Sauvegarder le fichier
with open('LISTE-FREE-ITEMS-COMPLETE.md', 'w', encoding='utf-8') as f:
    f.write(markdown)

print(f"Fichier créé : LISTE-FREE-ITEMS-COMPLETE.md")
print(f"{total} items organisés en {len(items_by_category)} catégories")
print(f"Taille du fichier : {len(markdown)} caractères")

# Sauvegarder aussi le JSON brut
with open('free_items_raw.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"JSON brut sauvegardé : free_items_raw.json")
