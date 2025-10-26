# 👔 Outfit par défaut du bot

## ✅ Configuration

Le bot s'équipe automatiquement avec cet outfit au démarrage.

## 📋 Items équipés

### 👤 Corps & Visage
- **Body** : `body-flesh` (Palette: 4)
- **Eyes** : `eye-m_12b` (Palette: 2)
- **Eyebrows** : `eyebrow-n_04` (Palette: 1)
- **Nose** : `nose-n_01` (Palette: 0)
- **Mouth** : `mouth-basic2018chubbymouth` (Palette: -1)

### 💇 Cheveux
- **Hair Front** : `hair_front-n_malenew22` (Palette: 1)
- **Hair Back** : `hair_back-n_malenew22` (Palette: 1)

### 👕 Vêtements
- **Shirt** : `shirt-n_registrationavatars2023pastelboyhoodie`
- **Pants** : `pants-n_room32019longshortswithsocksblack`
- **Shoes** : `shoes-n_registrationavatars2023furrysneakers`

### 👓 Accessoires
- **Glasses** : `glasses-n_10`
- **Handbag** : `handbag-n_room12019iphoneblack` (iPhone)
- **Necklace** : `necklace-n_SCSpring2018camera` (Caméra)

## 🎨 Couleurs

- **Peau** : Palette 4 (claire)
- **Yeux** : Palette 2 (bleus)
- **Sourcils** : Palette 1 (bruns)
- **Cheveux** : Palette 1 (bruns)

## 🔄 Comportement

### Au démarrage
✅ Le bot équipe automatiquement cet outfit quand il se connecte

### Logs
```
[OUTFIT] Chargement de l'outfit par défaut...
[OUTFIT] ✅ Outfit par défaut équipé (13 items)
```

## 🛠️ Modifier l'outfit par défaut

Pour changer l'outfit par défaut du bot :

### Option 1 : Analyser un autre utilisateur
1. Équipe l'utilisateur avec le nouvel outfit
2. Lance `!admin analyzeoutfit <username>`
3. Copie le code Python généré
4. Remplace le code dans `bot.py` (lignes 93-107)

### Option 2 : Modifier manuellement
Édite le fichier `bot.py` à la ligne 93 et modifie la liste `default_outfit`.

## 📊 Total

- **13 items** équipés
- **4 couleurs** personnalisées (body, eye, eyebrow, hair)
- **3 accessoires** (lunettes, iPhone, caméra)

---

**Le bot s'habillera automatiquement comme StationDroop à chaque démarrage ! 🎉**
