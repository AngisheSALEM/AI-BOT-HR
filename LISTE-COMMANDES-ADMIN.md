# 👑 Liste complète des commandes admin

## 🎮 Commandes de base

### 1. Aide
```
!admin help
```
Affiche l'aide des commandes admin

### 2. Emote
```
!admin emote <nom|numero>
```
Faire une emote avec le bot
- **Exemples** :
  - `!admin emote wave`
  - `!admin emote 1`
  - `!admin emote dance`

### 3. Téléportation
```
!admin tp <x> <y>
```
Téléporter le bot à une position
- **Exemple** : `!admin tp 10 5`

### 4. Annonce
```
!admin announce <message>
```
Envoyer une annonce dans le chat
- **Exemple** : `!admin announce Bienvenue à tous!`

### 5. Kick
```
!admin kick <username>
```
Expulser un utilisateur de la room
- **Exemple** : `!admin kick baduser`

### 6. Stats
```
!admin stats
```
Voir les statistiques du bot

### 7. Uptime
```
!admin uptime
```
Voir depuis combien de temps le bot est en ligne

### 8. Wallet
```
!admin wallet
```
Voir le wallet du bot (gold, gems)

### 9. Users
```
!admin users
```
Voir le nombre d'utilisateurs dans la room

---

## 👔 Commandes Outfit

### 10. Inventaire
```
!admin inventory
```
Afficher l'inventaire complet du bot dans les logs

### 11. Outfit actuel
```
!admin currentoutfit
```
Voir l'outfit actuellement équipé

### 12. Modifier l'outfit
```
!admin modifyoutfit replace <nom ou ID>
!admin modifyoutfit remove <category>
```
Équiper ou retirer des items

**Exemples - Starter items (inventaire) :**
```
!admin modifyoutfit replace flesh
!admin modifyoutfit replace eye
!admin modifyoutfit replace hair_front
!admin modifyoutfit replace hair_back
!admin modifyoutfit replace eyebrow
!admin modifyoutfit replace mouth
!admin modifyoutfit replace nose
```

**Exemples - Free items :**
```
!admin modifyoutfit replace Black Flats
!admin modifyoutfit replace Basic Pants
!admin modifyoutfit replace White Tee
!admin modifyoutfit replace Pleated Pink Skirt
```

**Exemples - Retirer :**
```
!admin modifyoutfit remove shoes
!admin modifyoutfit remove pants
!admin modifyoutfit remove hair_front
```

### 13. Changer les couleurs
```
!admin changecolor <category> <palette>
```
Changer la couleur d'un item (palette 0-100)

**Exemples - Couleur de peau :**
```
!admin changecolor body 0     # Peau très claire
!admin changecolor body 10    # Peau claire
!admin changecolor body 20    # Peau moyenne
!admin changecolor body 27    # Peau foncée
!admin changecolor body 40    # Peau très foncée
```

**Exemples - Couleur des yeux :**
```
!admin changecolor eye 0      # Yeux marron
!admin changecolor eye 5      # Yeux bleus
!admin changecolor eye 10     # Yeux verts
!admin changecolor eye 15     # Yeux gris
```

**Exemples - Couleur des cheveux :**
```
!admin changecolor hair_front 0    # Cheveux noirs
!admin changecolor hair_front 5    # Cheveux bruns
!admin changecolor hair_front 10   # Cheveux blonds
!admin changecolor hair_front 15   # Cheveux roux
!admin changecolor hair_front 20   # Cheveux blancs

!admin changecolor hair_back 10    # Même couleur pour l'arrière
```

**Exemples - Couleur des sourcils :**
```
!admin changecolor eyebrow 0    # Sourcils noirs
!admin changecolor eyebrow 10   # Sourcils blonds
```

**Exemples - Couleur de la bouche :**
```
!admin changecolor mouth 0    # Bouche naturelle
!admin changecolor mouth 5    # Bouche rouge
!admin changecolor mouth 10   # Bouche rose
```

### 14. Chercher des items
```
!admin searchitem <category>
!admin searchitem name <nom exact>
```
Chercher des items par catégorie ou nom

**Exemples :**
```
!admin searchitem shoes
!admin searchitem pants
!admin searchitem shirt
!admin searchitem name Black Flats
```

### 15. Analyser un outfit
```
!admin analyzeoutfit <username>
```
Analyser l'outfit d'un utilisateur et obtenir le code Python

**Exemple :**
```
!admin analyzeoutfit sindouche
```

### 16. Vérifier un outfit
```
!admin checkoutfit <nom_outfit>
```
Vérifier quels items d'un outfit sont manquants dans l'inventaire

### 17. Tester un outfit
```
!admin testoutfit <nom>
```
Tester un outfit prédéfini

### 18. Mon ID
```
!admin myid
```
Afficher ton ID utilisateur

### 19. Acheter un item
```
!admin buyitem <item_id>
```
Acheter un item du shop avec le gold du bot

**Exemple :**
```
!admin buyitem shirt-n_room12019puffertgreen
```

---

## 📊 Résumé

| # | Commande | Description |
|---|----------|-------------|
| 1 | `!admin help` | Aide |
| 2 | `!admin emote <nom\|numero>` | Faire une emote |
| 3 | `!admin tp <x> <y>` | Téléporter |
| 4 | `!admin announce <message>` | Annonce |
| 5 | `!admin kick <username>` | Expulser |
| 6 | `!admin stats` | Statistiques |
| 7 | `!admin uptime` | Temps en ligne |
| 8 | `!admin wallet` | Voir le wallet |
| 9 | `!admin users` | Nombre d'utilisateurs |
| 10 | `!admin inventory` | Voir l'inventaire |
| 11 | `!admin currentoutfit` | Voir l'outfit actuel |
| 12 | `!admin modifyoutfit` | Modifier l'outfit |
| 13 | `!admin changecolor` | Changer les couleurs |
| 14 | `!admin searchitem` | Chercher des items |
| 15 | `!admin analyzeoutfit` | Analyser un outfit |
| 16 | `!admin checkoutfit` | Vérifier un outfit |
| 17 | `!admin testoutfit` | Tester un outfit |
| 18 | `!admin myid` | Voir son ID |
| 19 | `!admin buyitem` | Acheter un item |

**Total : 19 commandes admin**

---

## 🎯 Exemples d'utilisation

### Changer l'apparence complète du bot
```bash
# 1. Voir l'inventaire
!admin inventory

# 2. Équiper le corps
!admin modifyoutfit replace flesh

# 3. Changer la couleur de peau
!admin changecolor body 27

# 4. Équiper des yeux
!admin modifyoutfit replace eye

# 5. Changer la couleur des yeux
!admin changecolor eye 5

# 6. Équiper des cheveux
!admin modifyoutfit replace hair_front
!admin modifyoutfit replace hair_back

# 7. Changer la couleur des cheveux
!admin changecolor hair_front 10
!admin changecolor hair_back 10

# 8. Équiper des sourcils
!admin modifyoutfit replace eyebrow

# 9. Changer la couleur des sourcils
!admin changecolor eyebrow 10

# 10. Équiper des vêtements
!admin modifyoutfit replace Black Flats
!admin modifyoutfit replace Basic Pants
!admin modifyoutfit replace White Tee

# 11. Vérifier le résultat
!admin currentoutfit
```

### Copier l'outfit d'un utilisateur
```bash
# 1. Analyser l'outfit
!admin analyzeoutfit sindouche

# 2. Le code Python s'affiche dans les logs
# 3. Copie les IDs des items
# 4. Équipe-les un par un
!admin modifyoutfit replace <item_id>
```

### Chercher et équiper un item
```bash
# 1. Chercher des chaussures
!admin searchitem shoes

# 2. Équiper celles que tu veux
!admin modifyoutfit replace Black Flats
```

---

## ⚠️ Notes importantes

### Qui peut utiliser ces commandes ?
- Seulement les utilisateurs listés dans `ADMIN_USERNAMES` dans le fichier `.env`

### Ordre d'équipement
1. **D'abord équiper l'item** avec `modifyoutfit replace`
2. **Puis changer la couleur** avec `changecolor`

### Items obligatoires
Un outfit DOIT contenir :
- ✅ `body` (corps)
- ✅ `eye` (yeux)
- ✅ `eyebrow` (sourcils)
- ✅ `nose` (nez)
- ✅ `mouth` (bouche)
- ✅ Vêtements : `shirt+pants` OU `shirt+skirt` OU `dress`

### Catégories disponibles
- `body` - Corps
- `eye` - Yeux
- `eyebrow` - Sourcils
- `nose` - Nez
- `mouth` - Bouche
- `hair_front` - Cheveux devant
- `hair_back` - Cheveux derrière
- `shoes` - Chaussures
- `pants` - Pantalons
- `shirt` - Shirts
- `skirt` - Jupes
- `sock` - Chaussettes
- `watch` - Montres

---

**Total : 19 commandes admin disponibles ! 👑**
