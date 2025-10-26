# 👤 Analyser l'outfit d'un utilisateur

## 🎯 Nouvelle commande : !admin analyzeoutfit

Cette commande analyse l'outfit d'un utilisateur et affiche :
- ✅ **Nom complet** de chaque item
- ✅ **ID** de chaque item
- ✅ **Type** (shoes, shirt, pants, etc.)
- ✅ **Si c'est un free item**
- ✅ **Code Python** prêt à copier pour reproduire l'outfit !

## 💻 Utilisation

### Syntaxe
```
!admin analyzeoutfit <username>
```

### Exemple
```
!admin analyzeoutfit sylver_ralx_lm
```

## 📊 Résultat dans les logs

```
============================================================
👤 ANALYSE OUTFIT: sylver_ralx_lm
============================================================

📦 HAIR_FRONT
   Nom: Male Hair 05 Front
   ID: hair_front-n_malenew05
   Free: Oui

📦 HAIR_BACK
   Nom: Male Hair 05 Back
   ID: hair_back-n_malenew05
   Free: Oui

📦 SHIRT
   Nom: Denim Jacket Hoodie
   ID: shirt-n_room32019denimjackethoodie
   Free: Oui

📦 PANTS
   Nom: Cuffed Jeans White
   ID: pants-n_starteritems2019cuffedjeanswhite
   Free: Oui

📦 SHOES
   Nom: Grey Sock Sneakers
   ID: shoes-n_room32019socksneakersgrey
   Free: Oui

📦 BODY
   Nom: Flesh Body
   ID: body-flesh
   Free: Oui

📦 EYE
   Nom: Square Sleepy Eyes
   ID: eye-n_basic2018malesquaresleepy
   Free: Oui

============================================================
📊 Total: 7 items
============================================================

============================================================
💻 CODE PYTHON POUR COPIER CET OUTFIT:
============================================================

outfit = [
    Item(type="hair_front", id="hair_front-n_malenew05"),  # Male Hair 05 Front
    Item(type="hair_back", id="hair_back-n_malenew05"),  # Male Hair 05 Back
    Item(type="shirt", id="shirt-n_room32019denimjackethoodie"),  # Denim Jacket Hoodie
    Item(type="pants", id="pants-n_starteritems2019cuffedjeanswhite"),  # Cuffed Jeans White
    Item(type="shoes", id="shoes-n_room32019socksneakersgrey"),  # Grey Sock Sneakers
]

============================================================
```

## 🎨 Cas d'utilisation

### 1. Copier l'outfit d'un utilisateur

**Tu vois un utilisateur avec un bel outfit dans la room :**

```
!admin analyzeoutfit sylver_ralx_lm
```

**Le bot affiche tous les items avec leurs noms et IDs !**

### 2. Reproduire l'outfit sur ton bot

**Copie le code Python depuis les logs :**

```python
self.outfits = {
    "style_sylver": [
        Item(type="shirt", id="shirt-n_room32019denimjackethoodie"),  # Denim Jacket Hoodie
        Item(type="pants", id="pants-n_starteritems2019cuffedjeanswhite"),  # Cuffed Jeans White
        Item(type="shoes", id="shoes-n_room32019socksneakersgrey"),  # Grey Sock Sneakers
    ],
}
```

**Teste :**
```
!admin testoutfit style_sylver
```

### 3. Identifier des items inconnus

**Tu vois un item que tu aimes mais tu ne connais pas son nom :**

```
!admin analyzeoutfit username
```

**Le bot te donne le nom ET l'ID de chaque item !**

## 📋 Informations affichées

Pour chaque item de l'outfit :

### Dans les logs détaillés
- 📦 **Type** (SHIRT, PANTS, SHOES, etc.)
- 🏷️ **Nom complet** de l'item
- 🆔 **ID** complet
- 🎁 **Free** (Oui/Non)

### Code Python généré
```python
outfit = [
    Item(type="shirt", id="shirt-id"),  # Nom de l'item
    Item(type="pants", id="pants-id"),  # Nom de l'item
    ...
]
```

**Prêt à copier-coller dans `bot.py` !**

## 💡 Astuces

### Analyser ton propre outfit

```
!admin analyzeoutfit ton_username
```

Utile pour :
- Voir les IDs de tes items actuels
- Sauvegarder ton outfit actuel
- Créer une rotation avec tes outfits préférés

### Analyser plusieurs utilisateurs

```
!admin analyzeoutfit user1
!admin analyzeoutfit user2
!admin analyzeoutfit user3
```

Compare les styles et crée une collection d'outfits !

### Items non-free

Si un item n'est pas dans les free items :
```
📦 SHIRT
   Nom: Nom inconnu (item payant ou non-free)
   ID: shirt-premium-xyz
   Free: Non
```

L'ID est quand même affiché, mais le nom n'est pas trouvé dans l'API des free items.

## 🎯 Workflow complet

### 1. Trouve un utilisateur avec un bel outfit
```
!admin analyzeoutfit sylver_ralx_lm
```

### 2. Regarde les logs
```
============================================================
👤 ANALYSE OUTFIT: sylver_ralx_lm
============================================================

📦 SHIRT
   Nom: Denim Jacket Hoodie
   ID: shirt-n_room32019denimjackethoodie
   Free: Oui

📦 PANTS
   Nom: Cuffed Jeans White
   ID: pants-n_starteritems2019cuffedjeanswhite
   Free: Oui
```

### 3. Copie le code Python
```python
outfit = [
    Item(type="shirt", id="shirt-n_room32019denimjackethoodie"),
    Item(type="pants", id="pants-n_starteritems2019cuffedjeanswhite"),
]
```

### 4. Ajoute dans bot.py
```python
self.outfits = {
    "copie_sylver": [
        Item(type="shirt", id="shirt-n_room32019denimjackethoodie"),
        Item(type="pants", id="pants-n_starteritems2019cuffedjeanswhite"),
    ],
}
```

### 5. Teste
```
!admin testoutfit copie_sylver
```

## ⚠️ Important

### L'utilisateur doit être dans la room

La commande fonctionne seulement si l'utilisateur est **présent dans la room** au moment de l'analyse.

Si l'utilisateur n'est pas là :
```
❌ Utilisateur 'username' non trouvé dans la room
```

### Items du corps

Les items comme `body`, `eye`, `nose`, `mouth` sont des **caractéristiques du corps**.

Tu peux les ignorer dans ton outfit, ils sont automatiques :
```python
# Ne copie que les vêtements
outfit = [
    Item(type="shirt", id="..."),
    Item(type="pants", id="..."),
    Item(type="shoes", id="..."),
    # Ignore body, eye, nose, mouth, etc.
]
```

## 🔧 Commandes liées

```bash
# Analyser un outfit
!admin analyzeoutfit username

# Voir ton propre outfit
!admin currentoutfit

# Tester un outfit
!admin testoutfit casual

# Chercher un item
!admin searchitem shoes
```

## 🎉 Résumé

### Commande
```
!admin analyzeoutfit <username>
```

### Ce qu'elle fait
1. ✅ Récupère l'outfit de l'utilisateur
2. ✅ Trouve le nom de chaque item
3. ✅ Affiche les IDs
4. ✅ Indique si c'est un free item
5. ✅ Génère le code Python prêt à copier

### Résultat
- 📊 Tableau détaillé dans les logs
- 💻 Code Python prêt à utiliser
- 🎨 Outfit reproductible instantanément

---

**Analyse n'importe quel outfit et copie-le en 1 commande ! 👤✨**

**Essaie : `!admin analyzeoutfit username`**
