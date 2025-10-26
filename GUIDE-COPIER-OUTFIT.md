# 👔 Guide : Copier ton outfit sur le bot

## 🎯 Objectif

Analyser ton outfit (avec starter items uniquement) et générer automatiquement toutes les commandes pour habiller le bot exactement comme toi, **y compris les couleurs** (skin tone, cheveux, yeux, etc.).

## 📋 Étapes

### 1. Rejoins la room avec le bot
- Assure-toi que ton bot est en ligne
- Rejoins la même room

### 2. Équipe ton outfit
Équipe-toi avec **uniquement des starter items** :
- 👤 Corps (body)
- 👁️ Yeux (eye)
- ✏️ Sourcils (eyebrow)
- 👃 Nez (nose)
- 👄 Bouche (mouth)
- 💇 Cheveux devant (hair_front)
- 💇 Cheveux derrière (hair_back)
- 👟 Chaussures (shoes)
- 👖 Pantalon (pants)
- 👕 Shirt (shirt)

**⚠️ Important** : N'équipe PAS de :
- ❌ Tatouages
- ❌ Blush
- ❌ Items payants
- ❌ Items non-starter

### 3. Lance la commande d'analyse
```
!admin analyzeoutfit <ton_username>
```

**Exemple :**
```
!admin analyzeoutfit sylver_ralx_lm
```

### 4. Récupère les commandes
Le bot va afficher dans les **logs** (console) :

#### 📋 Items par catégorie
```
👤 BODY
   ID: body-flesh
   Palette: 27

👁️ EYE
   ID: eye-n_basic2018malesquareeyes
   Palette: 5

💇 HAIR_FRONT
   ID: hair_front-n_malenew2019wavyhair
   Palette: 10
```

#### 🎨 Commandes prêtes à copier
```
1. !admin modifyoutfit replace body-flesh
2. !admin changecolor body 27
3. !admin modifyoutfit replace eye-n_basic2018malesquareeyes
4. !admin changecolor eye 5
5. !admin modifyoutfit replace hair_front-n_malenew2019wavyhair
6. !admin changecolor hair_front 10
...
```

### 5. Copie-colle les commandes
Copie chaque commande **une par une** dans le chat et envoie-les :

```
!admin modifyoutfit replace body-flesh
!admin changecolor body 27
!admin modifyoutfit replace eye-n_basic2018malesquareeyes
!admin changecolor eye 5
...
```

### 6. Vérifie le résultat
```
!admin currentoutfit
```

Le bot devrait maintenant avoir **exactement le même outfit que toi** ! 🎉

## 📊 Exemple complet

### Ton outfit
- 👤 Corps : Peau foncée (palette 27)
- 👁️ Yeux : Bleus (palette 5)
- 💇 Cheveux : Blonds (palette 10)
- 👟 Chaussures : Black Flats
- 👖 Pantalon : Basic Pants
- 👕 Shirt : White Tee

### Commandes générées
```
1. !admin modifyoutfit replace body-flesh
2. !admin changecolor body 27
3. !admin modifyoutfit replace eye-n_basic2018malesquareeyes
4. !admin changecolor eye 5
5. !admin modifyoutfit replace eyebrow-n_basic2018newbrows02
6. !admin changecolor eyebrow 10
7. !admin modifyoutfit replace nose-n_basic2018nose01
8. !admin modifyoutfit replace mouth-n_basic2018chippermouth
9. !admin modifyoutfit replace hair_front-n_malenew2019wavyhair
10. !admin changecolor hair_front 10
11. !admin modifyoutfit replace hair_back-n_malenew2019wavyhair
12. !admin changecolor hair_back 10
13. !admin modifyoutfit replace shoes-n_starteritems2019blackflats
14. !admin modifyoutfit replace pants-n_starteritems2019malepantsblack
15. !admin modifyoutfit replace shirt-n_starteritems2019maletshirtwhite
```

### Résultat
Le bot aura **exactement** :
- ✅ Même couleur de peau
- ✅ Même couleur d'yeux
- ✅ Même couleur de cheveux
- ✅ Même coiffure
- ✅ Mêmes vêtements
- ✅ Mêmes accessoires

## 💡 Astuces

### Sauvegarder les commandes
Tu peux copier toutes les commandes dans un fichier texte pour les réutiliser plus tard :

1. Copie toutes les commandes depuis les logs
2. Colle-les dans un fichier `outfit_bot.txt`
3. Quand tu veux changer l'outfit, copie-colle les commandes une par une

### Modifier une seule partie
Si tu veux juste changer la couleur des cheveux :
```
!admin changecolor hair_front 15
!admin changecolor hair_back 15
```

### Tester différentes couleurs
Tu peux tester différentes palettes :
```
!admin changecolor body 0    # Peau très claire
!admin changecolor body 10   # Peau claire
!admin changecolor body 20   # Peau moyenne
!admin changecolor body 27   # Peau foncée
!admin changecolor body 40   # Peau très foncée
```

## 🎨 Palettes de couleurs

### Body (Peau)
- `0-10` : Très clair
- `11-20` : Clair
- `21-30` : Moyen
- `31-40` : Foncé
- `41-50` : Très foncé

### Eye (Yeux)
- `0` : Marron
- `5` : Bleu
- `10` : Vert
- `15` : Gris
- `20` : Noisette

### Hair (Cheveux)
- `0` : Noir
- `5` : Brun foncé
- `10` : Blond
- `15` : Roux
- `20` : Blanc/Gris
- `25` : Couleurs vives

## 🐛 Dépannage

### "Utilisateur non trouvé"
→ Assure-toi d'être dans la même room que le bot

### "Item non trouvé"
→ L'item n'est pas un starter item ou n'est pas dans l'inventaire du bot
→ Vérifie avec `!admin inventory`

### Les couleurs ne changent pas
→ Assure-toi d'avoir équipé l'item AVANT de changer la couleur
→ Ordre : `modifyoutfit replace` puis `changecolor`

### Le bot ne ressemble pas exactement à moi
→ Vérifie que tu n'as pas de tatouages ou blush équipés
→ Vérifie que tous les items sont des starter items

## ✅ Résumé

1. **Équipe ton outfit** (starter items uniquement)
2. **Lance** `!admin analyzeoutfit <ton_username>`
3. **Copie les commandes** depuis les logs
4. **Colle-les une par une** dans le chat
5. **Vérifie** avec `!admin currentoutfit`

---

**Le bot aura maintenant exactement le même look que toi ! 🎉**
