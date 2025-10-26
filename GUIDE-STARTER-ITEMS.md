# 🎨 Guide : Utiliser les Starter Items

## ✅ Modifications apportées

Le bot peut maintenant :
1. ✅ Équiper des items de son **inventaire** (starter items)
2. ✅ Équiper des **free items** (sans inventaire)
3. ✅ Changer les **couleurs** (palettes)

## 📋 Nouvelles fonctionnalités

### 1. Équiper un item (inventaire OU free items)

```
!admin modifyoutfit replace <nom ou partie de l'ID>
```

Le bot cherche **d'abord dans son inventaire**, puis dans les free items.

#### Exemples pour starter items

```
!admin modifyoutfit replace flesh
→ Équipe body-flesh (corps de base)

!admin modifyoutfit replace hair
→ Équipe le premier cheveu trouvé dans l'inventaire

!admin modifyoutfit replace eye
→ Équipe les premiers yeux trouvés

!admin modifyoutfit replace eyebrow
→ Équipe les premiers sourcils trouvés

!admin modifyoutfit replace mouth
→ Équipe la première bouche trouvée
```

### 2. Changer les couleurs (palettes)

```
!admin changecolor <category> <palette_number>
```

#### Exemples de couleurs

**Couleur de peau (body)**
```
!admin changecolor body 0    → Peau très claire
!admin changecolor body 10   → Peau claire
!admin changecolor body 20   → Peau moyenne
!admin changecolor body 27   → Peau foncée
!admin changecolor body 40   → Peau très foncée
```

**Couleur des yeux (eye)**
```
!admin changecolor eye 0     → Yeux marron
!admin changecolor eye 5     → Yeux bleus
!admin changecolor eye 10    → Yeux verts
!admin changecolor eye 15    → Yeux gris
```

**Couleur des cheveux (hair_front / hair_back)**
```
!admin changecolor hair_front 0    → Cheveux noirs
!admin changecolor hair_front 5    → Cheveux bruns
!admin changecolor hair_front 10   → Cheveux blonds
!admin changecolor hair_front 15   → Cheveux roux
!admin changecolor hair_front 20   → Cheveux blancs

!admin changecolor hair_back 10    → Même couleur pour l'arrière
```

**Couleur des sourcils (eyebrow)**
```
!admin changecolor eyebrow 0    → Sourcils noirs
!admin changecolor eyebrow 10   → Sourcils blonds
```

**Couleur de la bouche (mouth)**
```
!admin changecolor mouth 0    → Bouche naturelle
!admin changecolor mouth 5    → Bouche rouge
!admin changecolor mouth 10   → Bouche rose
```

## 🎯 Workflow complet

### Exemple : Changer l'apparence complète du bot

```bash
# 1. Vérifier l'inventaire
!admin inventory

# 2. Équiper le corps
!admin modifyoutfit replace flesh

# 3. Changer la couleur de peau
!admin changecolor body 27

# 4. Équiper des yeux
!admin modifyoutfit replace eye

# 5. Changer la couleur des yeux
!admin changecolor eye 5

# 6. Équiper des cheveux devant
!admin modifyoutfit replace hair_front

# 7. Équiper des cheveux derrière
!admin modifyoutfit replace hair_back

# 8. Changer la couleur des cheveux
!admin changecolor hair_front 10
!admin changecolor hair_back 10

# 9. Équiper des sourcils
!admin modifyoutfit replace eyebrow

# 10. Changer la couleur des sourcils
!admin changecolor eyebrow 10

# 11. Équiper une bouche
!admin modifyoutfit replace mouth

# 12. Vérifier l'outfit actuel
!admin currentoutfit
```

## 📊 Catégories disponibles

### Starter Items (dans l'inventaire)
- **body** - Corps avec couleur de peau
- **eye** - Yeux avec couleur
- **eyebrow** - Sourcils avec couleur
- **nose** - Nez
- **mouth** - Bouche avec couleur
- **hair_front** - Cheveux devant avec couleur
- **hair_back** - Cheveux derrière avec couleur
- **freckle** - Taches de rousseur (optionnel)

### Free Items (sans inventaire)
- **shoes** - Chaussures (11 options)
- **pants** - Pantalons (13 options)
- **shirt** - Shirts (7 options)
- **skirt** - Jupes (3 options)
- **sock** - Chaussettes (6 options)
- **watch** - Montres (1 option)
- **nose** - Nez (7 options)

## 🔍 Comment trouver les IDs exacts

### Méthode 1 : Vérifier l'inventaire
```
!admin inventory
```

Cela affiche tous les items dans l'inventaire avec leurs IDs complets.

### Méthode 2 : Analyser l'outfit actuel
```
!admin currentoutfit
```

Cela affiche tous les items équipés actuellement.

### Méthode 3 : Chercher par catégorie
```
!admin searchitem body
!admin searchitem eye
!admin searchitem hair
```

## ⚠️ Notes importantes

### Palettes de couleurs
- Chaque item a un nombre différent de palettes disponibles
- Les numéros vont généralement de **0 à 50+**
- Si tu utilises un numéro trop élevé, l'item peut ne pas changer
- Teste différents numéros pour trouver la couleur désirée

### Ordre d'équipement
1. **Équipe d'abord l'item** avec `modifyoutfit replace`
2. **Puis change la couleur** avec `changecolor`

Si tu changes la couleur avant d'équiper l'item, ça ne fonctionnera pas.

### Items obligatoires
Un outfit DOIT contenir :
- ✅ `body-flesh` (corps)
- ✅ `eye` (yeux)
- ✅ `eyebrow` (sourcils)
- ✅ `nose` (nez)
- ✅ `mouth` (bouche)
- ✅ Vêtements : `shirt+pants` OU `shirt+skirt` OU `dress` OU `fullsuit`

## 🎨 Exemples de combinaisons

### Look 1 : Peau claire, yeux bleus, cheveux blonds
```
!admin modifyoutfit replace flesh
!admin changecolor body 10
!admin modifyoutfit replace eye
!admin changecolor eye 5
!admin modifyoutfit replace hair_front
!admin modifyoutfit replace hair_back
!admin changecolor hair_front 10
!admin changecolor hair_back 10
```

### Look 2 : Peau foncée, yeux marron, cheveux noirs
```
!admin modifyoutfit replace flesh
!admin changecolor body 27
!admin modifyoutfit replace eye
!admin changecolor eye 0
!admin modifyoutfit replace hair_front
!admin modifyoutfit replace hair_back
!admin changecolor hair_front 0
!admin changecolor hair_back 0
```

### Look 3 : Peau moyenne, yeux verts, cheveux roux
```
!admin modifyoutfit replace flesh
!admin changecolor body 20
!admin modifyoutfit replace eye
!admin changecolor eye 10
!admin modifyoutfit replace hair_front
!admin modifyoutfit replace hair_back
!admin changecolor hair_front 15
!admin changecolor hair_back 15
```

## 🎯 Résumé

**Avant :**
- ❌ Seulement 48 free items (vêtements)
- ❌ Pas de cheveux, yeux, couleurs

**Maintenant :**
- ✅ Accès à l'inventaire complet (100+ items)
- ✅ Cheveux, yeux, sourcils, bouche
- ✅ Couleurs personnalisables (50+ palettes)
- ✅ Free items (48 vêtements)

**Le bot peut maintenant avoir une apparence complète et personnalisée ! 🎉**
