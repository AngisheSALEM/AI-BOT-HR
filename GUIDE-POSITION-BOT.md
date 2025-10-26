# 📍 Guide : Modifier la position du bot

## 🎯 Méthodes disponibles

### 1. Téléportation (instantanée)
Le bot se déplace instantanément à la position

```python
await self.highrise.walk_to(Position(x, y, z, facing))
```

### 2. Marche (déplacement progressif)
Le bot marche vers la position (animation de marche)

```python
await self.highrise.walk_to(Position(x, y, z, facing))
```

## 🎮 Commandes admin

### Téléporter le bot
```
!admin tp <x> <y>
```

**Exemples :**
```
!admin tp 10 5
!admin tp 15.5 8.0
!admin tp 0 0
!admin tp 20 10
```

### Faire marcher le bot
```
!walk <x> <y>
```

**Exemple :**
```
!walk 12 6
```

## 📐 Comprendre les coordonnées

### Format Position
```python
from highrise import Position

Position(x, y, z, facing)
```

### Paramètres

- **x** : Position horizontale (gauche ← → droite)
  - Valeurs typiques : 0 à 30
  - Exemple : 10.5

- **y** : Position verticale (bas ↓ ↑ haut)
  - Valeurs typiques : 0 à 20
  - 0 = sol
  - Exemple : 5.0

- **z** : Profondeur (avant ↑ ↓ arrière)
  - Valeurs typiques : 0 à 20
  - Exemple : 5.5

- **facing** : Direction du regard
  - `"Front"` : Vers l'avant
  - `"Back"` : Vers l'arrière
  - `"Left"` : Vers la gauche
  - `"Right"` : Vers la droite
  - `"FrontRight"` : Diagonale avant-droite
  - `"FrontLeft"` : Diagonale avant-gauche
  - `"BackRight"` : Diagonale arrière-droite
  - `"BackLeft"` : Diagonale arrière-gauche

## 💻 Exemples de code

### Position au démarrage

Ajoute dans `on_start()` (déjà fait) :

```python
# Téléporter le bot à une position par défaut
try:
    default_position = Position(10.5, 0.0, 5.5, "FrontRight")
    await self.highrise.walk_to(default_position)
    print(f"[POSITION] Bot à x={default_position.x}, y={default_position.y}")
except Exception as e:
    print(f"[ERREUR] Téléportation: {e}")
```

### Positions prédéfinies

```python
# Centre de la room
center = Position(10.5, 0.0, 5.5, "FrontRight")

# Entrée de la room
entrance = Position(5.0, 0.0, 3.0, "Front")

# Coin supérieur droit
corner = Position(20.0, 0.0, 15.0, "BackLeft")

# Près du DJ booth (exemple)
dj_booth = Position(15.0, 2.0, 8.0, "Front")
```

### Téléporter vers un utilisateur

```python
async def teleport_to_user(self, target_username):
    """Téléporter le bot vers un utilisateur"""
    try:
        room_users = await self.highrise.get_room_users()
        
        for user, position in room_users.content:
            if user.username.lower() == target_username.lower():
                # Téléporter à la position de l'utilisateur
                await self.highrise.walk_to(position)
                print(f"[POSITION] Téléporté vers {user.username}")
                return
        
        print(f"[POSITION] Utilisateur {target_username} non trouvé")
    except Exception as e:
        print(f"[ERREUR] Téléportation: {e}")
```

### Patrouille automatique

```python
async def patrol(self):
    """Faire patrouiller le bot entre plusieurs positions"""
    patrol_points = [
        Position(5.0, 0.0, 5.0, "Front"),
        Position(15.0, 0.0, 5.0, "Right"),
        Position(15.0, 0.0, 15.0, "Back"),
        Position(5.0, 0.0, 15.0, "Left"),
    ]
    
    while True:
        for point in patrol_points:
            try:
                await self.highrise.walk_to(point)
                print(f"[PATROL] Position: x={point.x}, z={point.z}")
                await asyncio.sleep(10)  # Attendre 10 secondes
            except Exception as e:
                print(f"[ERREUR] Patrol: {e}")
        
        await asyncio.sleep(5)  # Pause avant de recommencer
```

### Suivre un utilisateur

```python
async def follow_user(self, target_username):
    """Suivre un utilisateur en continu"""
    print(f"[FOLLOW] Début du suivi de {target_username}")
    
    while True:
        try:
            room_users = await self.highrise.get_room_users()
            
            for user, position in room_users.content:
                if user.username.lower() == target_username.lower():
                    # Se téléporter à la position de l'utilisateur
                    await self.highrise.walk_to(position)
                    break
            
            await asyncio.sleep(2)  # Vérifier toutes les 2 secondes
            
        except Exception as e:
            print(f"[ERREUR] Follow: {e}")
            await asyncio.sleep(5)
```

## 🗺️ Trouver les bonnes coordonnées

### Méthode 1 : Utiliser !admin users
La commande affiche les positions de tous les utilisateurs dans les logs

### Méthode 2 : Event on_user_move
Ajoute des logs dans `on_user_move()` :

```python
async def on_user_move(self, user: User, position: Position):
    print(f"[MOVE] {user.username}: x={position.x}, y={position.y}, z={position.z}")
```

### Méthode 3 : Commande de position
Ajoute une commande pour voir ta position :

```python
async def cmd_mypos(self, user: User):
    """Afficher la position de l'utilisateur"""
    try:
        room_users = await self.highrise.get_room_users()
        
        for room_user, position in room_users.content:
            if room_user.id == user.id:
                msg = f"📍 Ta position:\nX: {position.x}\nY: {position.y}\nZ: {position.z}\nDirection: {position.facing}"
                await self.highrise.send_whisper(user.id, msg)
                return
    except Exception as e:
        print(f"[ERREUR] MyPos: {e}")
```

## 🎯 Cas d'usage

### 1. Bot accueil à l'entrée
```python
# Dans on_start()
entrance_position = Position(5.0, 0.0, 3.0, "Front")
await self.highrise.walk_to(entrance_position)
```

### 2. Bot DJ sur scène
```python
# Position sur la scène
stage_position = Position(15.0, 2.5, 8.0, "Front")
await self.highrise.walk_to(stage_position)
```

### 3. Bot qui se déplace aléatoirement
```python
import random

async def random_walk(self):
    """Se déplacer aléatoirement dans la room"""
    while True:
        x = random.uniform(5.0, 20.0)
        z = random.uniform(5.0, 15.0)
        facing = random.choice(["Front", "Back", "Left", "Right"])
        
        position = Position(x, 0.0, z, facing)
        await self.highrise.walk_to(position)
        
        await asyncio.sleep(random.randint(10, 30))
```

### 4. Bot qui suit Sindouche
```python
# Dans on_start(), après les autres initialisations
self.follow_task = asyncio.create_task(self.follow_user("sindouche"))
```

## ⚠️ Limites et erreurs

### Erreur : Position invalide
```
[ERREUR] Téléportation: Invalid position
```
→ Les coordonnées sont hors des limites de la room
→ Vérifie que x, y, z sont dans les limites

### Erreur : Cannot walk to position
```
[ERREUR] Cannot walk to position
```
→ La position est bloquée (mur, objet)
→ Essaie une position différente

### Rate limiting
→ Ne téléporte pas le bot trop souvent (max 1 fois par seconde)
→ Ajoute des délais avec `await asyncio.sleep(1)`

## 📊 Résumé

| Action | Commande | Code |
|--------|----------|------|
| Téléporter | `!admin tp <x> <y>` | `await self.highrise.walk_to(Position(x, y, z, facing))` |
| Marcher | `!walk <x> <y>` | `await self.highrise.walk_to(Position(x, y, z, facing))` |
| Position au démarrage | - | Dans `on_start()` |
| Suivre un utilisateur | - | Boucle avec `walk_to()` |
| Patrouille | - | Boucle avec plusieurs positions |

## ✅ Configuration actuelle

Le bot se téléporte automatiquement au **centre de la room** au démarrage :
- Position : `x=10.5, y=0.0, z=5.5`
- Direction : `FrontRight`

Pour changer cette position, modifie la ligne 123 dans `bot.py` :
```python
default_position = Position(10.5, 0.0, 5.5, "FrontRight")
```

---

**Le bot peut maintenant se déplacer automatiquement dans la room ! 🎉**
