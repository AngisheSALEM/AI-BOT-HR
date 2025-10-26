# 📋 Récapitulatif : Items et Commandes

## ⚠️ IMPORTANT

**Les commandes d'outfit ont été supprimées du bot.py**

Pour les réactiver, il faut :
1. Réimporter `Item` : `from highrise import BaseBot, User, Position, AnchorPosition, Item`
2. Rajouter les fonctions supprimées
3. Rajouter les commandes dans le handler

---

## 🎨 Items disponibles

### 📦 Starter Items (dans l'inventaire)

Ces items sont **automatiquement dans l'inventaire** de chaque compte Highrise.

#### 🧍 Corps (Body)
- **ID** : `body-flesh`
- **Palettes** : 0-50+ (couleurs de peau)
- **Commande** : `!admin modifyoutfit replace flesh`
- **Couleur** : `!admin changecolor body <0-50>`

#### 👁️ Yeux (Eye)
- **IDs** : `eye-basic2018...`, `eye-round...`, etc.
- **Palettes** : 0-20+ (couleurs des yeux)
- **Commande** : `!admin modifyoutfit replace eye`
- **Couleur** : `!admin changecolor eye <0-20>`

#### 👁️ Sourcils (Eyebrow)
- **IDs** : `eyebrow-basic...`, `eyebrow-thick...`, etc.
- **Palettes** : 0-20+ (couleurs)
- **Commande** : `!admin modifyoutfit replace eyebrow`
- **Couleur** : `!admin changecolor eyebrow <0-20>`

#### 👃 Nez (Nose)
- **IDs** : 7 types différents
  - `nose-n_basic2018newnose16` - Angular Nose
  - `nose-n_basic2018newnose15` - Button Nose
  - `nose-n_basic2018newnose19` - Freckle Nose
  - `nose-n_room22019nosestud` - Nose Stud
  - `nose-n_basic2018newnose17` - Septum Piercing
  - `nose-n_basic2018newnose18` - Silver Nose Ring
  - `nose-n_basic2018newnose14` - Soft Nose
- **Commande** : `!admin modifyoutfit replace <nom du nez>`

#### 👄 Bouche (Mouth)
- **IDs** : `mouth-basic...`, `mouth-smile...`, etc.
- **Palettes** : 0-20+ (couleurs)
- **Commande** : `!admin modifyoutfit replace mouth`
- **Couleur** : `!admin changecolor mouth <0-20>`

#### 💇 Cheveux Devant (Hair Front)
- **IDs** : `hair-front-basic...`, `hair-front-long...`, etc.
- **Palettes** : 0-30+ (couleurs des cheveux)
- **Commande** : `!admin modifyoutfit replace hair_front`
- **Couleur** : `!admin changecolor hair_front <0-30>`

#### 💇 Cheveux Derrière (Hair Back)
- **IDs** : `hair-back-basic...`, `hair-back-long...`, etc.
- **Palettes** : 0-30+ (couleurs des cheveux)
- **Commande** : `!admin modifyoutfit replace hair_back`
- **Couleur** : `!admin changecolor hair_back <0-30>`

---

### 🆓 Free Items (sans inventaire)

Ces items peuvent être équipés **sans être dans l'inventaire**.

#### 👟 Chaussures (11 items)
1. **Basic Black Boots** - `shoes-n_room12019bootsblack`
2. **Basic Black Sneakers** - `shoes-n_room12019sneakersblack`
3. **Basic Pink Sneakers** - `shoes-n_room12019sneakerspink`
4. **Basic Socks** - `shoes-n_starteritems2019unishoeswhite`
5. **Black High Tops** - `shoes-n_room12019hightopsblack`
6. **Pink Flats** - `shoes-n_room12019flatspink`
7. **Tan Boots** - `shoes-n_room12019bootstan`
8. **White Converse** - `shoes-n_room12019conversewhite`
9. **White Dans** - `shoes-n_room12019danswhite`
10. **White Flats** - `shoes-n_room12019flatswhite`
11. **White High Tops** - `shoes-n_room12019hightopswhite`

**Commande** : `!admin modifyoutfit replace <nom exact>`

#### 👖 Pantalons (13 items)
1. **Black Long Shorts** - `pants-n_room12019longshortblack`
2. **Black Undies** - `pants-n_starteritems2019maleundiesblack`
3. **Camo Tech Pants** - `pants-n_room12019techpantscamo`
4. **Camo Track Shorts** - `pants-n_room12019trackshortscamo`
5. **Denim Cut-Offs** - `pants-n_room12019denimcutoffs`
6. **Grey Sweatpants** - `pants-n_room12019sweatpantsgrey`
7. **Khaki Shorts** - `pants-n_room12019shortskhaki`
8. **Khaki Trousers** - `pants-n_room12019trouserskhaki`
9. **Olive Cargo Pants** - `pants-n_room12019cargopantsolive`
10. **Pink Sweatpants** - `pants-n_room12019sweatpantspink`
11. **Ripped Jeans** - `pants-n_room12019rippedjeans`
12. **Skinny Jeans** - `pants-n_room12019skinnyjeans`
13. **White Trousers** - `pants-n_room12019trouserswhite`

**Commande** : `!admin modifyoutfit replace <nom exact>`

#### 👕 Shirts (7 items)
1. **Green Puffer and Bra Top** - `shirt-n_room12019pufferbratopgreen`
2. **Green Puffer and T** - `shirt-n_room12019puffertgreen`
3. **Pink Bra Top** - `shirt-n_starteritems2019femaletoppink`
4. **Red Off-shoulder Track Jacket** - `shirt-n_room12019trackjacketoffshouldersred`
5. **Red Raglan Hoodie** - `shirt-n_room12019raglanhoodyred`
6. **Red Track Jacket** - `shirt-n_room12019trackjacketred`
7. **White Tee** - `shirt-n_starteritems2019maletshirtwhite`

**Commande** : `!admin modifyoutfit replace <nom exact>`

#### 👗 Jupes (3 items)
1. **Pleated Black Skirt** - `skirt-n_room12019pleatedskirtblack`
2. **Pleated Pink Skirt** - `skirt-n_room12019pleatedskirtpink`
3. **Pleated Skirt Grey** - `skirt-n_room12019pleatedskirtgrey`

**Commande** : `!admin modifyoutfit replace <nom exact>`

#### 🧦 Chaussettes (6 items)
1. **Black Knee Length Socks** - `sock-n_room12019kneelengthsocksblack`
2. **Black Thigh High Socks** - `sock-n_room12019thighhighsocksblack`
3. **Opaque White Tights** - `sock-n_room12019opaquetightswhite`
4. **Tall Socks** - `sock-n_starteritems2019unisockswhite`
5. **White Knee Length Socks** - `sock-n_room12019kneelengthsockswhite`
6. **White Thigh High Socks** - `sock-n_room12019thighhighsockswhite`

**Commande** : `!admin modifyoutfit replace <nom exact>`

#### ⌚ Montres (1 item)
1. **Classic Black Watch** - `watch-n_room32019blackwatch`

**Commande** : `!admin modifyoutfit replace Classic Black Watch`

---

## 🎮 Commandes (actuellement supprimées)

### Commandes d'équipement

#### Équiper un item
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

#### Retirer un item
```
!admin modifyoutfit remove <category>
```

**Exemples :**
```
!admin modifyoutfit remove shoes
!admin modifyoutfit remove pants
!admin modifyoutfit remove hair_front
```

### Commandes de couleur

#### Changer la couleur d'un item
```
!admin changecolor <category> <palette_number>
```

**Exemples :**
```
!admin changecolor body 27        # Peau foncée
!admin changecolor eye 5          # Yeux bleus
!admin changecolor hair_front 10  # Cheveux blonds
!admin changecolor hair_back 10   # Cheveux blonds (arrière)
!admin changecolor eyebrow 10     # Sourcils blonds
!admin changecolor mouth 5        # Bouche rouge
```

### Commandes d'information

#### Voir l'inventaire
```
!admin inventory
```

#### Voir l'outfit actuel
```
!admin currentoutfit
```

#### Analyser l'outfit d'un utilisateur
```
!admin analyzeoutfit <username>
```

#### Chercher des items
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

---

## 🎨 Guide des palettes de couleurs

### Couleur de peau (body)
- `0-5` : Peau très claire
- `6-15` : Peau claire
- `16-25` : Peau moyenne
- `26-35` : Peau foncée
- `36-50` : Peau très foncée

### Couleur des yeux (eye)
- `0` : Marron
- `5` : Bleu
- `10` : Vert
- `15` : Gris
- `20` : Noisette

### Couleur des cheveux (hair_front / hair_back)
- `0` : Noir
- `5` : Brun foncé
- `10` : Blond
- `15` : Roux
- `20` : Blanc/Gris
- `25` : Couleurs fantaisie

### Couleur des sourcils (eyebrow)
- Même palette que les cheveux (0-30)

### Couleur de la bouche (mouth)
- `0` : Naturel
- `5` : Rouge
- `10` : Rose
- `15` : Nude

---

## 📊 Récapitulatif

### Total des items disponibles

| Catégorie | Nombre | Source |
|-----------|--------|--------|
| 🧍 Body | 1+ | Inventaire (50+ couleurs) |
| 👁️ Eye | 5+ | Inventaire (20+ couleurs) |
| 👁️ Eyebrow | 5+ | Inventaire (20+ couleurs) |
| 👃 Nose | 7 | Free items |
| 👄 Mouth | 5+ | Inventaire (20+ couleurs) |
| 💇 Hair Front | 10+ | Inventaire (30+ couleurs) |
| 💇 Hair Back | 10+ | Inventaire (30+ couleurs) |
| 👟 Shoes | 11 | Free items |
| 👖 Pants | 13 | Free items |
| 👕 Shirt | 7 | Free items |
| 👗 Skirt | 3 | Free items |
| 🧦 Sock | 6 | Free items |
| ⌚ Watch | 1 | Free items |

**Total : 80+ items uniques + 150+ variations de couleurs**

---

## ⚠️ Pour réactiver les commandes

### 1. Réimporter Item
```python
from highrise import BaseBot, User, Position, AnchorPosition, Item
```

### 2. Rajouter les fonctions
- `cmd_modifyoutfit()`
- `cmd_changecolor()`
- `cmd_inventory()`
- `cmd_currentoutfit()`
- `cmd_searchitem()`
- `cmd_analyzeoutfit()`

### 3. Rajouter dans le handler
```python
elif subcmd == 'modifyoutfit':
    await self.cmd_modify_outfit(user, subparams)
elif subcmd == 'changecolor':
    await self.cmd_change_color(user, subparams)
elif subcmd == 'inventory':
    await self.cmd_inventory(user)
# etc.
```

---

**Créé le : 25 octobre 2025**
**Note : Les commandes ont été supprimées du bot.py actuel**
