# 👕 Outfit par défaut configuré !

## ✅ Outfit ajouté

L'outfit analysé a été ajouté comme **outfit par défaut** du bot !

## 📋 Items inclus

### Vêtements principaux
- **Shirt** : `shirt-n_starteritems2019pulloverblack` (Pullover Black)
- **Pants** : `pants-n_room32019baggytrackpantsgreycamo` (Baggy Track Pants Grey Camo)
- **Shoes** : `shoes-maygifts2024flowersneaks` (Flower Sneaks)
- **Socks** : `sock-n_starteritems2020whitesocks` (White Socks) ✅ Free

### Accessoires
- **Watch** : `watch-n_room32019blackwatch` (Classic Black Watch) ✅ Free
- **Handbag** : `handbag-n_gonefishingf2p2024dionysuscoin` (Dionysus Coin)

### Cheveux
- **Hair Front** : `hair_front-n_malenew22` (Male Hair 22 Front)
- **Hair Back** : `hair_back-n_malenew22` (Male Hair 22 Back)

### Visage
- **Freckles** : `freckle-n_gettowork2022qifreynervoussweats` (Nervous Sweats)

## 🎯 Comportement du bot

### Au démarrage
Le bot équipe **automatiquement** cet outfit quand il se connecte :

```
[OK] Bot connecte!
[OUTFIT] Outfit par defaut equipe
```

### Tester l'outfit
Tu peux aussi tester l'outfit manuellement :

```
!admin testoutfit default
```

## 📝 Code dans bot.py

```python
self.outfits = {
    "default": [
        # Vêtements principaux
        Item(type="clothing", id="shirt-n_starteritems2019pulloverblack"),
        Item(type="clothing", id="pants-n_room32019baggytrackpantsgreycamo"),
        Item(type="clothing", id="shoes-maygifts2024flowersneaks"),
        Item(type="clothing", id="sock-n_starteritems2020whitesocks"),
        # Accessoires
        Item(type="clothing", id="watch-n_room32019blackwatch"),
        Item(type="clothing", id="handbag-n_gonefishingf2p2024dionysuscoin"),
        # Cheveux
        Item(type="clothing", id="hair_front-n_malenew22"),
        Item(type="clothing", id="hair_back-n_malenew22"),
        # Visage (optionnel, peut être enlevé)
        Item(type="clothing", id="freckle-n_gettowork2022qifreynervoussweats"),
    ],
}
```

## ⚠️ Note sur les items

### Items gratuits (Free) ✅
- `sock-n_starteritems2020whitesocks` - White Socks
- `watch-n_room32019blackwatch` - Classic Black Watch

Ces items sont **gratuits** et utilisables par tous les bots sans achat.

### Items payants/non-free
Les autres items (shirt, pants, shoes, etc.) ne sont **pas dans les free items**.

**Deux possibilités :**
1. Ces items sont dans l'inventaire du compte sur lequel le bot est créé
2. Le bot devra les acheter avec du gold

Si le bot n'a pas ces items, il y aura une erreur lors de l'équipement.

## 🔧 Vérifier si ça fonctionne

### 1. Lance le bot
```bash
python -m highrise bot:HighriseBot ROOM_ID TOKEN
```

### 2. Regarde les logs
```
[OK] Bot connecte!
[OUTFIT] Outfit par defaut equipe
```

### 3. Si erreur
```
[ERREUR] Outfit: Item not in inventory
```

Cela signifie que le bot n'a pas certains items dans son inventaire.

**Solutions :**
- Utilise seulement les **free items** (2 items dans cet outfit)
- Achète les items manquants avec `!admin buyitem`
- Crée le bot sur un compte qui possède déjà ces items

## 💡 Créer d'autres outfits

Tu peux ajouter d'autres outfits de la même manière :

```python
self.outfits = {
    "default": [
        # Outfit actuel
    ],
    "casual": [
        # Autre outfit
    ],
    "elegant": [
        # Encore un autre
    ],
}
```

Puis tester avec :
```
!admin testoutfit casual
!admin testoutfit elegant
```

## 🔄 Rotation automatique (optionnel)

Si tu veux que le bot change d'outfit automatiquement, ajoute dans `on_start()` :

```python
# Démarrer la rotation d'outfits toutes les 6 heures
asyncio.create_task(self.outfit_rotation_6h())
```

## 🎉 Résumé

✅ **Outfit par défaut configuré** avec 9 items
✅ **Équipement automatique** au démarrage
✅ **2 free items** (socks, watch)
✅ **7 items payants** (nécessitent d'être dans l'inventaire)

**Commandes utiles :**
- `!admin testoutfit default` - Tester l'outfit
- `!admin currentoutfit` - Voir l'outfit actuel
- `!admin inventory` - Voir l'inventaire du bot

---

**Le bot portera automatiquement cet outfit au démarrage ! 👕✨**
