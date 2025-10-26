# 🎭 Guide des Emotes - Bot vs Utilisateurs

## 🤔 Différence Importante

### `!emote` - Le BOT fait l'emote
```
!emote wave
```
→ **Le bot lui-même** fait l'emote wave

### `!emoteto` - Faire une emote SUR un utilisateur
```
!emoteto @Alice kiss
```
→ **Le bot fait** l'emote kiss **sur Alice**

## 📋 Exemples d'Utilisation

### Le Bot Fait des Emotes (Lui-Même)
```
!emote wave          → Le bot fait coucou
!emote dance         → Le bot danse
!emote happy         → Le bot est content
!dance               → Le bot fait une danse aléatoire
!random              → Le bot fait une emote aléatoire
```

### Le Bot Fait des Emotes SUR les Users
```
!emoteto @Alice wave       → Le bot fait coucou à Alice
!emoteto @Bob kiss         → Le bot fait un bisou à Bob
!emoteto @Charlie hug      → Le bot fait un câlin à Charlie
!emoteto @Dana dance       → Le bot danse avec Dana
```

## 🎯 Cas d'Usage

### Accueillir Quelqu'un
```
!emoteto @NewUser wave
!emoteto @NewUser hello
```

### Célébrer
```
!emoteto @Winner clap
!emoteto @Winner happy
```

### Interactions Sociales
```
!emoteto @Friend hug
!emoteto @Friend kiss
!emoteto @Friend heart
```

### Fun
```
!emoteto @Someone dab
!emoteto @Someone flex
!emoteto @Someone silly
```

## 📝 Format des Commandes

### !emote
```
!emote <nom_emote>
```
- `<nom_emote>` : Nom de l'emote (wave, dance, happy, etc.)

### !emoteto
```
!emoteto <username> <nom_emote>
```
- `<username>` : Nom de l'utilisateur (avec ou sans @)
- `<nom_emote>` : Nom de l'emote

## 🎭 Liste des Emotes Disponibles

### Voir Toutes les Catégories
```
!emotes
```
→ Affiche : dances, social, emotions, poses, special, sports, fun, cute, winter

### Voir une Catégorie Spécifique
```
!emotes social
```
→ Affiche : wave, hello, bow, kiss, hug, yes, no, clap, thumbsup...

### Emotes Populaires

**Social**
- wave, hello, bow, kiss, hug, clap, thumbsup

**Emotions**
- happy, sad, laugh, cry, angry, shy, confused, tired

**Dances**
- savage, russian, macarena, floss, breakdance, penguin, zombie

**Fun**
- dab, facepalm, rofl, flex, robot, moonwalk, disco

**Cute**
- cute, uwu, heart, hearteyes

## 💡 Astuces

### 1. Pas Besoin du @
```
!emoteto Alice wave    ✅ Fonctionne
!emoteto @Alice wave   ✅ Fonctionne aussi
```

### 2. Noms Partiels
Le bot trouve l'emote même avec un nom partiel :
```
!emote sav    → Trouve "savage"
!emote hap    → Trouve "happy"
```

### 3. Combiner avec d'Autres Commandes
```
!emoteto @Alice wave
!whisper @Alice Salut!
```

## 🐛 Dépannage

### "Emote introuvable"
- Vérifiez l'orthographe
- Tapez `!emotes` pour voir les catégories
- Tapez `!emotes social` pour voir les emotes disponibles

### "User introuvable"
- Vérifiez que l'utilisateur est dans la room
- Vérifiez l'orthographe du nom
- Le nom est sensible à la casse

### L'emote ne s'affiche pas
- Vérifiez les logs dans le terminal
- Le bot doit avoir les droits "Designer"
- Certaines emotes peuvent nécessiter des permissions spéciales

## 📊 Différences Techniques

| Commande | Code | Effet |
|----------|------|-------|
| `!emote wave` | `send_emote("emote-wave")` | Bot fait l'emote |
| `!emoteto @User wave` | `send_emote("emote-wave", user_id)` | Bot fait l'emote sur User |

## 🎉 Exemples de Scénarios

### Accueil Automatique
Quand quelqu'un rejoint, le bot peut :
```python
# Automatique dans on_user_join()
await self.highrise.send_emote("emote-wave", user.id)
```

### Récompense
```
!emoteto @Winner clap
!emoteto @Winner hearteyes
```

### Animation de Room
```
!emoteto @User1 dance
!emoteto @User2 dance
!emoteto @User3 dance
```

### Interactions Fun
```
!emoteto @Friend kiss
!emoteto @Friend hug
!emoteto @Friend heart
```

## 🚀 Commandes Complètes

```
# Le bot fait des emotes
!emote wave
!emote dance
!emote happy
!dance
!random

# Le bot fait des emotes sur les users
!emoteto @Alice wave
!emoteto @Bob kiss
!emoteto @Charlie dance

# Voir les emotes disponibles
!emotes
!emotes social
!emotes dances
```

---

**Maintenant vous pouvez faire des emotes SUR les utilisateurs ! 🎭**
