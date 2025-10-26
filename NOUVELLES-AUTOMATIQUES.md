# 📰 Nouvelles/Faits automatiques toutes les 30 minutes

## 🎯 Description

Le bot diffuse automatiquement des **nouvelles ou faits intéressants** dans le chat toutes les **30 minutes** sur différents domaines.

---

## ⏰ Fréquence

**Toutes les 30 minutes** (1200 secondes)

---

## 📚 Domaines couverts

### 🎵 Musique
- **Rap US** - Rap américain, hip-hop US, artistes rap américains
- **Rap Français** - Rap français, hip-hop français, artistes rap français  
- **Musique 21e siècle** - Musique moderne, tendances musicales, nouveaux genres

### 💻 Technologie
- **Technologie** - Innovations technologiques, nouvelles technologies, gadgets
- **Informatique** - Programmation, développement, intelligence artificielle

### 💕 Amour
- **Amour** - Relations amoureuses, psychologie de l'amour, faits sur l'amour

### 🔬 Sciences
- **Astrologie** - Astrologie, signes astrologiques, horoscope
- **Physique** - Physique, lois physiques, découvertes physiques
- **Physique Quantique** - Physique quantique, mécanique quantique, phénomènes quantiques
- **Mathématiques** - Mathématiques, théorèmes, nombres
- **Chimie** - Chimie, éléments chimiques, réactions chimiques
- **Biologie** - Biologie, corps humain, nature

### 🌍 Culture
- **Histoire** - Histoire, événements historiques, personnages historiques
- **Géographie** - Géographie, pays, continents, phénomènes naturels

**Total : 14 domaines**

---

## 💬 Exemples de nouvelles/faits

### 🎵 Musique

#### Rap US
```
🎵 Saviez-vous que Tupac a enregistré plus de 150 chansons inédites avant sa mort?

🎤 Eminem détient le record du plus grand nombre de mots dans une chanson: 1,560 mots en 6 minutes! 🔥

🎵 Dr. Dre a produit son premier album à 19 ans dans le garage de ses parents 🎧
```

#### Rap Français
```
🇫🇷 Booba a été le premier rappeur français à remplir le Stade de France en 2015! 🎤

🎵 IAM a révolutionné le rap français en 1991 avec "De la planète Mars" 🚀

🎤 Orelsan a écrit son premier album dans sa chambre d'étudiant à Caen 📝
```

#### Musique moderne
```
🎵 Le streaming représente maintenant 85% des revenus de l'industrie musicale! 📱

🎧 Spotify compte plus de 500 millions d'utilisateurs dans le monde 🌍

🎵 TikTok a lancé plus de hits en 2023 que toutes les radios combinées! 📱✨
```

### 💻 Technologie

```
💻 ChatGPT a atteint 100 millions d'utilisateurs en seulement 2 mois! 🤯

🤖 L'IA peut maintenant créer des images réalistes en quelques secondes ✨

📱 Le premier iPhone est sorti il y a seulement 17 ans en 2007! 🍎

💻 Python est le langage de programmation le plus populaire en 2024 🐍
```

### 💕 Amour

```
💕 Le cœur bat en moyenne 100,000 fois par jour pour la personne qu'on aime ❤️

😍 Tomber amoureux a le même effet sur le cerveau que la cocaïne! 🧠

💑 Les couples qui rient ensemble restent ensemble plus longtemps 😊

💕 Un câlin de 20 secondes libère de l'ocytocine, l'hormone du bonheur! 🤗
```

### 🔬 Sciences

#### Physique Quantique
```
🔬 La physique quantique montre qu'une particule peut être à 2 endroits en même temps! 🤯

⚛️ Les particules quantiques peuvent communiquer instantanément à travers l'univers! 🌌

🔬 Le chat de Schrödinger est à la fois vivant ET mort jusqu'à l'observation 🐱
```

#### Mathématiques
```
🔢 Il existe plus de combinaisons possibles dans un jeu d'échecs que d'atomes dans l'univers! ♟️

∞ Le nombre Pi contient potentiellement toutes les séquences de nombres possibles! 🥧

🔢 0.999... est mathématiquement égal à 1! 🤯
```

#### Biologie
```
🧬 Ton ADN pourrait s'étirer de la Terre au Soleil 600 fois! ☀️

🧠 Le cerveau humain contient plus de connexions que d'étoiles dans la Voie Lactée! 🌌

💪 Tes muscles sont plus forts que l'acier à poids égal! 💪
```

### 🌍 Culture

#### Histoire
```
📜 Cléopâtre vivait plus près de l'invention de l'iPhone que de la construction des pyramides! 🤯

⚔️ La guerre de 100 ans a duré 116 ans! 😅

🗿 Les pyramides d'Égypte ont été construites il y a plus de 4,500 ans 🏛️
```

#### Géographie
```
🌍 Le point le plus profond de l'océan est à 11,000 mètres sous la surface! 🌊

🏔️ L'Everest grandit de 4mm par an à cause des plaques tectoniques! ⛰️

🌋 Il y a plus de 1,500 volcans actifs sur Terre en ce moment! 🔥
```

---

## 🎮 Fonctionnement

### Au démarrage
```
[NEWS] Tache de diffusion de nouvelles/faits demarree
[NEWS] Diffusion de nouvelles/faits activee (toutes les 1200s = 30 min)
```

### Toutes les 30 minutes
```
[NEWS] Generation nouvelle/fait sur: Rap US...
[NEWS] Nouvelle/fait diffuse: 🎵 Saviez-vous que Tupac a enregistré plus de 150 chansons inédites avant sa mort?
```

### Dans le chat
```
🎵 Saviez-vous que Tupac a enregistré plus de 150 chansons inédites avant sa mort?
```

---

## 🔧 Configuration

### Modifier l'intervalle

Pour changer la fréquence, modifie la ligne 65 dans `bot.py` :

```python
self.news_interval = 1200  # 30 minutes (1200 secondes)
```

**Exemples :**
- 15 minutes : `self.news_interval = 900`
- 30 minutes : `self.news_interval = 1200` (par défaut)
- 45 minutes : `self.news_interval = 2700`
- 1 heure : `self.news_interval = 3600`

### Ajouter un domaine

Pour ajouter un nouveau domaine, modifie la liste `domaines` ligne 421 :

```python
domaines = [
    # ... domaines existants ...
    ("Nouveau Domaine", "description du domaine"),
]
```

**Exemple :**
```python
("Sport", "sports, athletes, competitions sportives"),
("Cinéma", "films, acteurs, realisateurs, cinema"),
```

---

## 📊 Statistiques

### Domaines
- **14 domaines** différents
- **Sélection aléatoire** à chaque diffusion
- **Variété garantie**

### Fréquence
- **30 minutes** entre chaque nouvelle/fait
- **48 nouvelles/faits par jour**
- **336 nouvelles/faits par semaine**

### Format
- **Maximum 140 caractères**
- **Emojis appropriés**
- **Éducatif et captivant**

---

## 🎯 Avantages

### Pour la room
- ✅ Contenu éducatif régulier
- ✅ Anime le chat automatiquement
- ✅ Variété de sujets
- ✅ Apprendre en s'amusant

### Pour les utilisateurs
- ✅ Découvrir de nouveaux faits
- ✅ Culture générale
- ✅ Sujets de conversation
- ✅ Divertissement intelligent

---

## 📝 Code source

### Variables (ligne 64-66)
```python
# Nouvelles/Faits toutes les 30 minutes
self.news_interval = 1200  # 30 minutes (1200 secondes)
self.news_task = None
```

### Démarrage (ligne 157-159)
```python
# Démarrer les nouvelles/faits toutes les 30 minutes
self.news_task = asyncio.create_task(self.start_news_broadcast())
print("[NEWS] Tache de diffusion de nouvelles/faits demarree")
```

### Fonction start_news_broadcast (ligne 400-409)
```python
async def start_news_broadcast(self):
    """Démarrer la diffusion de nouvelles/faits périodiques"""
    print(f"[NEWS] Diffusion de nouvelles/faits activee (toutes les {self.news_interval}s = 30 min)")
    while True:
        try:
            await asyncio.sleep(self.news_interval)
            await self.broadcast_news()
        except Exception as e:
            print(f"[NEWS] Erreur: {e}")
            await asyncio.sleep(60)
```

### Fonction broadcast_news (ligne 411-478)
```python
async def broadcast_news(self):
    """Générer et diffuser une nouvelle ou un fait intéressant"""
    # ... (voir code complet dans bot.py)
```

---

## ✅ Résumé

| Élément | Détail |
|---------|--------|
| **Fréquence** | 30 minutes (1200 secondes) |
| **Domaines** | 14 (Musique, Tech, Amour, Sciences, Culture) |
| **Format** | Max 140 caractères + emoji |
| **Sélection** | Aléatoire |
| **Diffusion** | Chat public |

---

## 🔄 Modifications appliquées

### 1. ✅ Langage normal (non familier)
Le bot répond maintenant de manière **polie et professionnelle** au lieu du langage familier.

**Avant :**
```
Yo mec ! Alors là c'est stylé ce que tu demandes, grave ! 😎
```

**Maintenant :**
```
Bonjour ! Voici la réponse à votre question. 😊
```

### 2. ✅ Nouvelles/Faits automatiques
Le bot diffuse des nouvelles/faits toutes les 30 minutes sur 14 domaines différents.

---

**Le bot éduque et anime la room automatiquement ! 📰✨**
