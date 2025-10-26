# 💇 Réponse : Cheveux, Yeux et Couleurs

## ❌ Mauvaise nouvelle

Dans les **free items** (rarity=none), il n'y a **PAS** de :
- ❌ Cheveux (hair_front, hair_back)
- ❌ Yeux (eye) avec couleurs différentes
- ❌ Sourcils (eyebrow) avec couleurs
- ❌ Bouche (mouth) avec couleurs
- ❌ Corps (body) avec couleurs de peau

## 📊 Ce qui existe dans les free items

### Items trouvés (48 items uniques)
1. **👃 NOSE** - 7 items (nez différents)
2. **👖 PANTS** - 13 items
3. **👕 SHIRT** - 7 items
4. **👟 SHOES** - 11 items
5. **👗 SKIRT** - 3 items
6. **🧦 SOCK** - 6 items
7. **⌚ WATCH** - 1 item

### Items NON trouvés
- ❌ **hair_front** (cheveux devant)
- ❌ **hair_back** (cheveux derrière)
- ❌ **eye** (yeux)
- ❌ **eyebrow** (sourcils)
- ❌ **mouth** (bouche)
- ❌ **body** (corps/couleur de peau)
- ❌ **freckle** (taches de rousseur)

## 🎨 Comment changer les couleurs ?

### Pour les yeux, cheveux, corps, etc.

Ces éléments **NE SONT PAS** dans les free items. Ils sont :

1. **Items de base** (starter items dans l'inventaire)
   - Chaque compte a des yeux, cheveux, corps de base
   - Ils sont dans l'inventaire du compte
   - Le bot peut les utiliser s'ils sont dans son inventaire

2. **Items payants**
   - La plupart des cheveux/yeux sont payants
   - Nécessitent gold ou gems
   - Doivent être achetés puis ajoutés à l'inventaire

### Méthode pour le bot

#### Option 1 : Utiliser l'inventaire du bot
```python
# Le bot peut équiper ce qui est dans son inventaire
inventory = await self.highrise.get_inventory()

# Chercher des cheveux dans l'inventaire
for item in inventory.items:
    if 'hair' in item.id:
        print(f"Cheveux trouvés: {item.id}")
```

#### Option 2 : Acheter des items
```python
# Acheter un item avec gold (si disponible)
await self.highrise.buy_item("hair-front-...")
```

#### Option 3 : Utiliser les couleurs de palette

Certains items ont des **palettes de couleurs** :
```python
Item(
    type="clothing",
    amount=1,
    id="body-flesh",
    account_bound=False,
    active_palette=27  # Numéro de la palette (couleur de peau)
)
```

Les palettes disponibles varient selon l'item. Par exemple :
- `body-flesh` : active_palette de 0 à 50+ (différentes couleurs de peau)
- Certains cheveux : active_palette pour différentes couleurs

## 🔍 Vérification dans l'API

J'ai vérifié l'API Highrise :
- **Total items** : 48,875 items
- **Free items (rarity=none)** : ~584 items déclarés
- **Vraiment gratuits** : 48 items uniques équipables sans inventaire

Les cheveux, yeux, sourcils, bouche sont dans les autres catégories :
- `rarity=common` (payants avec gold)
- `rarity=rare` (payants avec gems)
- `rarity=epic`, `legendary`, etc.

## 💡 Solution pour ton bot

### Si le bot a un inventaire
1. Vérifie l'inventaire : `!admin inventory`
2. Cherche les items hair, eye, eyebrow, mouth
3. Équipe-les avec `!admin modifyoutfit replace <nom>`

### Si le bot n'a pas d'inventaire
Le bot ne peut équiper que les **48 free items** :
- 7 nez
- 13 pantalons
- 7 shirts
- 11 chaussures
- 3 jupes
- 6 chaussettes
- 1 montre

**Pas de cheveux, yeux, ou couleurs personnalisables.**

## 🎯 Recommandation

### Pour avoir plus d'options
1. **Crée le bot sur un compte** qui possède déjà des items
2. **Achète des items** avec le gold du compte
3. **Utilise les starter items** du compte

### Pour l'instant
Le bot peut modifier :
- Nez (7 options)
- Vêtements (pants, shirts, shoes, skirts, socks)
- Accessoires (watch)

Mais **pas** les cheveux, yeux, ou couleurs de peau sans inventaire.

---

**Conclusion : Les free items ne contiennent pas de cheveux, yeux, ou options de couleurs. Ces items sont payants ou nécessitent l'inventaire du compte.**
