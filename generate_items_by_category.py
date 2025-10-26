"""
Script pour générer la liste des free items organisée par catégorie
"""

import json
import sys
import io

# Fix encoding pour Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("📋 Génération de la liste des items par catégorie...\n")

# Charger les données du rapport
try:
    with open('free_items_report.json', 'r', encoding='utf-8') as f:
        report = json.load(f)
except FileNotFoundError:
    print("❌ Erreur: free_items_report.json non trouvé")
    print("Exécutez d'abord: python test_all_free_items.py")
    exit(1)

categories = report['categories']

# Créer le fichier Markdown
markdown = f"""# 📋 Liste des Free Items par Catégorie

**Total d'items gratuits** : {report['truly_free_items']} items

---

## 📊 Table des matières

"""

# Ajouter la table des matières
for category in sorted(categories.keys()):
    count = categories[category]['count']
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
    
    markdown += f"- [{emoji} {category.upper()}](#{category.lower()}) - {count} items\n"

markdown += "\n---\n\n"

# Ajouter chaque catégorie
for category in sorted(categories.keys()):
    items = categories[category]['items']
    count = len(items)
    
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
    
    markdown += f"## {emoji} {category.upper()}\n\n"
    markdown += f"**{count} items disponibles**\n\n"
    
    # Créer un tableau
    markdown += "| # | Nom de l'item | ID | Commande |\n"
    markdown += "|---|---------------|----|---------|\n"
    
    for idx, item in enumerate(items, 1):
        name = item['name']
        item_id = item['id']
        # Échapper les pipes dans le nom
        name_escaped = name.replace('|', '\\|')
        markdown += f"| {idx} | {name_escaped} | `{item_id}` | `!admin modifyoutfit replace {name}` |\n"
    
    markdown += "\n---\n\n"

# Ajouter le résumé final
markdown += """## 📊 Résumé

| Catégorie | Nombre d'items |
|-----------|----------------|
"""

for category in sorted(categories.keys()):
    count = categories[category]['count']
    markdown += f"| {category.upper()} | {count} |\n"

markdown += f"""
**Total** : {report['truly_free_items']} items gratuits

---

## 💡 Comment utiliser

### Équiper un item
```
!admin modifyoutfit replace <nom de l'item>
```

### Exemples
```
!admin modifyoutfit replace Black Flats
!admin modifyoutfit replace Basic Pants
!admin modifyoutfit replace Angular Nose
```

### Chercher des items par catégorie
```
!admin searchitem <category>
```

### Exemples
```
!admin searchitem shoes
!admin searchitem pants
!admin searchitem shirt
```

### Retirer un item
```
!admin modifyoutfit remove <category>
```

---

**Généré automatiquement le {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}**
"""

# Sauvegarder le fichier
with open('ITEMS_PAR_CATEGORIE.md', 'w', encoding='utf-8') as f:
    f.write(markdown)

print("✅ Fichier créé: ITEMS_PAR_CATEGORIE.md")

# Créer aussi des fichiers séparés par catégorie
print("\n📁 Création des fichiers par catégorie...")

for category in sorted(categories.keys()):
    items = categories[category]['items']
    count = len(items)
    
    cat_markdown = f"""# {category.upper()} - {count} items

## Liste complète

"""
    
    for idx, item in enumerate(items, 1):
        cat_markdown += f"### {idx}. {item['name']}\n"
        cat_markdown += f"- **ID** : `{item['id']}`\n"
        cat_markdown += f"- **Commande** : `!admin modifyoutfit replace {item['name']}`\n\n"
    
    filename = f"items_{category.lower()}.md"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(cat_markdown)
    
    print(f"  ✅ {filename} ({count} items)")

# Afficher un aperçu
print("\n" + "=" * 60)
print("APERÇU DES CATÉGORIES")
print("=" * 60)

for category in sorted(categories.keys()):
    count = categories[category]['count']
    items = categories[category]['items']
    
    print(f"\n{category.upper()} ({count} items):")
    
    # Afficher les 5 premiers items
    for item in items[:5]:
        print(f"  - {item['name']}")
    
    if count > 5:
        print(f"  ... et {count - 5} autres")

print("\n" + "=" * 60)
print("✅ TERMINÉ !")
print("=" * 60)
print("\nFichiers créés:")
print("  - ITEMS_PAR_CATEGORIE.md (liste complète)")
print("  - items_<category>.md (un fichier par catégorie)")
