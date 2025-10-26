# 🧪 Guide de test : Commandes Outfit

## ✅ Code restauré !

Toutes les fonctions d'outfit ont été restaurées dans `bot.py` :
- ✅ `cmd_inventory()` - Voir l'inventaire
- ✅ `cmd_current_outfit()` - Voir l'outfit actuel
- ✅ `cmd_modify_outfit()` - Modifier l'outfit
- ✅ `cmd_change_color()` - Changer les couleurs
- ✅ `cmd_searchitem()` - Chercher des items

## 🎮 Commandes disponibles

### 1. Voir l'inventaire
```
!admin inventory
```
**Résultat** : Affiche tous les items dans l'inventaire du bot (dans les logs)

### 2. Voir l'outfit actuel
```
!admin currentoutfit
```
**Résultat** : Affiche tous les items équipés actuellement

### 3. Équiper un item
```
!admin modifyoutfit replace <nom ou ID>
```

**Exemples :**
```
!admin modifyoutfit replace flesh
!admin modifyoutfit replace eye
!admin modifyoutfit replace hair_front
!admin modifyoutfit replace Black Flats
!admin modifyoutfit replace Basic Pants
```

### 4. Retirer un item
```
!admin modifyoutfit remove <category>
```

**Exemples :**
```
!admin modifyoutfit remove shoes
!admin modifyoutfit remove pants
```

### 5. Changer la couleur
```
!admin changecolor <category> <palette>
```

**Exemples :**
```
!admin changecolor body 27
!admin changecolor eye 5
!admin changecolor hair_front 10
```

### 6. Chercher des items
```
!admin searchitem <category>
!admin searchitem name <nom exact>
```

**Exemples :**
```
!admin searchitem shoes
!admin searchitem pants
!admin searchitem name Black Flats
```

## 🧪 Scénario de test complet

### Test 1 : Vérifier l'inventaire
```
!admin inventory
```
→ Vérifie que le bot a des items (body, eye, hair, etc.)

### Test 2 : Voir l'outfit actuel
```
!admin currentoutfit
```
→ Note les items actuellement équipés

### Test 3 : Équiper un corps
```
!admin modifyoutfit replace flesh
```
→ Le bot devrait équiper `body-flesh`

### Test 4 : Changer la couleur de peau
```
!admin changecolor body 27
```
→ La couleur de peau devrait changer

### Test 5 : Équiper des yeux
```
!admin modifyoutfit replace eye
```
→ Le bot devrait équiper des yeux de son inventaire

### Test 6 : Changer la couleur des yeux
```
!admin changecolor eye 5
```
→ La couleur des yeux devrait changer

### Test 7 : Équiper des cheveux
```
!admin modifyoutfit replace hair_front
!admin modifyoutfit replace hair_back
```
→ Le bot devrait équiper des cheveux

### Test 8 : Changer la couleur des cheveux
```
!admin changecolor hair_front 10
!admin changecolor hair_back 10
```
→ Les cheveux devraient devenir blonds

### Test 9 : Équiper des vêtements (free items)
```
!admin modifyoutfit replace Black Flats
!admin modifyoutfit replace Basic Pants
```
→ Le bot devrait équiper des chaussures et un pantalon

### Test 10 : Chercher des items
```
!admin searchitem shoes
```
→ Devrait afficher la liste des chaussures disponibles

## 🎨 Test complet d'apparence

Voici une séquence complète pour créer un look :

```bash
# 1. Vérifier l'inventaire
!admin inventory

# 2. Équiper le corps
!admin modifyoutfit replace flesh

# 3. Changer la couleur de peau (peau foncée)
!admin changecolor body 27

# 4. Équiper des yeux
!admin modifyoutfit replace eye

# 5. Changer la couleur des yeux (bleu)
!admin changecolor eye 5

# 6. Équiper des sourcils
!admin modifyoutfit replace eyebrow

# 7. Changer la couleur des sourcils
!admin changecolor eyebrow 10

# 8. Équiper un nez
!admin modifyoutfit replace nose

# 9. Équiper une bouche
!admin modifyoutfit replace mouth

# 10. Équiper des cheveux devant
!admin modifyoutfit replace hair_front

# 11. Équiper des cheveux derrière
!admin modifyoutfit replace hair_back

# 12. Changer la couleur des cheveux (blond)
!admin changecolor hair_front 10
!admin changecolor hair_back 10

# 13. Équiper des chaussures
!admin modifyoutfit replace Black Flats

# 14. Équiper un pantalon
!admin modifyoutfit replace Basic Pants

# 15. Équiper un shirt
!admin modifyoutfit replace White Tee

# 16. Vérifier le résultat
!admin currentoutfit
```

## ⚠️ Points importants

### Ordre d'équipement
1. **D'abord équiper l'item** avec `modifyoutfit replace`
2. **Puis changer la couleur** avec `changecolor`

### Catégories obligatoires
Un outfit DOIT contenir :
- ✅ `body` (corps)
- ✅ `eye` (yeux)
- ✅ `eyebrow` (sourcils)
- ✅ `nose` (nez)
- ✅ `mouth` (bouche)
- ✅ Vêtements : `shirt+pants` OU `shirt+skirt` OU `dress`

### Palettes de couleurs
- **Body** : 0-50 (couleurs de peau)
- **Eye** : 0-20 (couleurs des yeux)
- **Hair** : 0-30 (couleurs des cheveux)
- **Eyebrow** : 0-30 (couleurs des sourcils)
- **Mouth** : 0-20 (couleurs de la bouche)

## 🐛 Dépannage

### Erreur : "Item non trouvé"
→ Vérifie que l'item existe dans l'inventaire avec `!admin inventory`
→ Ou cherche l'item exact avec `!admin searchitem name <nom>`

### Erreur : "Aucun item trouvé dans l'outfit actuel"
→ Équipe d'abord l'item avec `modifyoutfit replace` avant de changer la couleur

### Le bot ne change pas d'apparence
→ Vérifie les logs pour voir les erreurs
→ Assure-toi que l'outfit contient tous les items obligatoires

## 📊 Résumé

| Commande | Description | Exemple |
|----------|-------------|---------|
| `!admin inventory` | Voir l'inventaire | - |
| `!admin currentoutfit` | Voir l'outfit actuel | - |
| `!admin modifyoutfit replace <item>` | Équiper un item | `replace flesh` |
| `!admin modifyoutfit remove <category>` | Retirer un item | `remove shoes` |
| `!admin changecolor <category> <palette>` | Changer la couleur | `changecolor body 27` |
| `!admin searchitem <category>` | Chercher des items | `searchitem shoes` |

---

**Le code est maintenant complet et fonctionnel ! 🎉**

**Teste les commandes dans Highrise pour vérifier que tout fonctionne !**
