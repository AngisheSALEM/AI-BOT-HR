# 📋 Liste Complète des Commandes

## 🎭 EMOTES (240+)

### Commandes de Base
- `!emotes` - Afficher toutes les catégories d'emotes
- `!emotes <catégorie>` - Afficher les emotes d'une catégorie
- `!emote <nom>` - Faire une emote spécifique
- `!dance` - Faire une danse aléatoire
- `!random` - Faire une emote complètement aléatoire

### Catégories Disponibles
1. **dances** - Danses populaires (savage, russian, macarena, floss, breakdance, penguin, zombie, anime, kawaii)
2. **social** - Interactions sociales (wave, hello, bow, kiss, hug, yes, no, clap, thumbsup)
3. **emotions** - Émotions (happy, sad, laugh, cry, angry, shy, confused, tired)
4. **poses** - Poses statiques (sit, sleep, think, model, pose1, pose3, pose5)
5. **special** - Effets spéciaux (teleport, float, fly, gravity, energyball, ghost)
6. **sports** - Sports et actions (baseball, boxing, karate, ninja, superhero)
7. **fun** - Fun et silly (dab, facepalm, rofl, flex, robot, moonwalk, disco)
8. **cute** - Mignon (cute, uwu, heart, hearteyes)
9. **winter** - Hiver (snowball, snowangel, sleigh)

### Exemples d'Emotes Populaires
```
!emote savage       - Danse Savage TikTok
!emote wave         - Faire coucou
!emote happy        - Être content
!emote sit          - S'asseoir
!emote fly          - Voler avec des ailes
!emote dab          - Faire un dab
!emote heart        - Faire un cœur avec les mains
!emote snowball     - Lancer une boule de neige
```

## 👥 SOCIAL

### Informations
- `!users` - Afficher le nombre d'utilisateurs connectés
- `!stats` - Voir vos statistiques personnelles (messages, emotes, tips, temps)
- `!leaderboard` - Voir le top 5 des utilisateurs les plus actifs

### Interactions
- `!greet <username>` - Saluer un utilisateur spécifique
  - Exemple : `!greet @Alice`

## 🎮 JEUX

### Dés
- `!roll` - Lancer un dé de 1 à 100
- `!roll <max>` - Lancer un dé de 1 à max
  - Exemple : `!roll 50` - Dé de 1 à 50
  - Exemple : `!roll 6` - Dé de 1 à 6

### Pile ou Face
- `!flip` - Lancer une pièce (Pile ou Face)

### Pierre-Papier-Ciseaux
- `!rps pierre` - Jouer pierre
- `!rps papier` - Jouer papier
- `!rps ciseaux` - Jouer ciseaux

## ℹ️ INFORMATIONS

- `!time` - Afficher l'heure et la date actuelles
- `!ping` - Tester la connexion du bot (répond "Pong!")
- `!uptime` - Voir depuis combien de temps le bot est en ligne
- `!help` - Afficher l'aide rapide
- `!commands` - Afficher cette liste complète

## 🚶 DÉPLACEMENT

### Téléportation
- `!tp <x> <y>` - Téléporter le bot à une position
- `!tp <x> <y> <z>` - Téléporter avec coordonnée Z
  - Exemple : `!tp 5 10` - Téléporter à (5, 10, 0)
  - Exemple : `!tp 0 0 2` - Téléporter à (0, 0, 2)

### Marche
- `!walk <x> <y>` - Faire marcher le bot vers une position
- `!walk <x> <y> <z>` - Marcher avec coordonnée Z
  - Exemple : `!walk 10 5` - Marcher vers (10, 5, 0)

## 👑 COMMANDES ADMIN

⚠️ **Réservées aux administrateurs uniquement**

### Annonces
- `!announce <message>` - Faire une annonce officielle
  - Exemple : `!announce Bienvenue à tous dans la room!`
  - Exemple : `!announce Event dans 10 minutes!`

### Modération
- `!kick <username>` - Expulser un utilisateur (en développement)
  - Exemple : `!kick @Spammer`

### Animations Spéciales
- `!parade` - Lancer une parade d'emotes automatique
  - Le bot fait plusieurs emotes à la suite avec des pauses
  - Emotes : wave, happy, bow, clap

- `!rain <emote>` - Créer une pluie d'emotes
  - Exemple : `!rain happy` - Pluie d'emotes happy
  - Exemple : `!rain heart` - Pluie de cœurs
  - Le bot répète l'emote 5 fois rapidement

## 🤖 FONCTIONNALITÉS AUTOMATIQUES

### Messages de Bienvenue
Le bot accueille automatiquement chaque nouvel arrivant :
- Message personnalisé aléatoire
- Emote de bienvenue (wave)

### Réactions aux Tips
Quand quelqu'un envoie un tip :
- Message de remerciement personnalisé
- Emote hearteyes

### Tracking des Stats
Le bot enregistre automatiquement :
- Nombre de messages envoyés
- Nombre d'emotes effectuées
- Tips envoyés
- Temps passé dans la room

## 📊 EXEMPLES D'UTILISATION

### Scénario 1 : Découvrir les Emotes
```
User: !emotes
Bot: "🎭 Catégories: dances, social, emotions, poses, special, sports, fun, cute, winter"

User: !emotes dances
Bot: "🎭 dances: savage, russian, macarena, floss, breakdance, penguin, zombie, anime, kawaii..."

User: !emote savage
Bot: [fait la danse savage]
Bot: "🎭 savage!"
```

### Scénario 2 : Jouer aux Jeux
```
User: !roll 100
Bot: "🎲 User: 42/100"

User: !flip
Bot: "🪙 Pile ⚪!"

User: !rps pierre
Bot: "✊✋✌️ Toi: pierre | Moi: ciseaux
Tu gagnes! 🎉"
```

### Scénario 3 : Voir les Stats
```
User: !stats
Bot: "📊 User:
💬 25 msg
🎭 10 emotes
💰 2 tips
⏱️ 15 min"

User: !leaderboard
Bot: "🏆 TOP 5:
1. 50 msg
2. 35 msg
3. 25 msg
4. 20 msg
5. 15 msg"
```

### Scénario 4 : Admin - Parade
```
Admin: !parade
Bot: "🎭 PARADE D'EMOTES!"
Bot: [fait wave]
[pause 3 secondes]
Bot: [fait happy]
[pause 3 secondes]
Bot: [fait bow]
[pause 3 secondes]
Bot: [fait clap]
Bot: "🎉 Parade terminée!"
```

### Scénario 5 : Admin - Pluie d'Emotes
```
Admin: !rain heart
Bot: "🌧️ PLUIE D'EMOTES!"
Bot: [fait heart 5 fois rapidement avec 1 sec de pause]
```

## 💡 ASTUCES

### Pour les Utilisateurs
- Utilisez `!emotes` pour découvrir toutes les catégories
- `!dance` pour une surprise aléatoire
- `!stats` pour voir votre activité
- `!roll` pour des décisions aléatoires

### Pour les Admins
- `!announce` pour les événements importants
- `!parade` pour animer la room
- `!rain` pour créer une ambiance festive
- Combinez plusieurs commandes pour des effets sympas

## 🎯 COMMANDES LES PLUS POPULAIRES

1. **!dance** - Toujours amusant
2. **!roll** - Pour les jeux et décisions
3. **!emote wave** - Classique
4. **!stats** - Voir sa progression
5. **!flip** - Rapide et simple
6. **!rps** - Compétitif
7. **!parade** - Spectaculaire (admin)
8. **!rain** - Festif (admin)

## 📝 NOTES

- Toutes les commandes commencent par `!`
- Les commandes ne sont pas sensibles à la casse
- Les noms d'emotes peuvent être partiels (ex: `!emote sav` trouve "savage")
- Les commandes admin nécessitent d'être dans ADMIN_IDS
- Le bot répond toujours, même en cas d'erreur

---

**Total : 30+ commandes + 240+ emotes = Possibilités infinies ! 🎮**
