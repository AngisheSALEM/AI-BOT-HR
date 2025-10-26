# 📍 Documentation : Commandes Position et Rest

## 🎯 Commandes disponibles

### 1. !admin setpos - Définir la position du bot
### 2. !admin rest - Le bot se repose près de toi

---

## 📍 Commande : !admin setpos

### Description
Téléporte le bot à une position spécifique dans la room.

### Syntaxe
```
!admin setpos <x> <y>
```

### Paramètres
- **x** : Position horizontale (nombre décimal ou entier)
- **y** : Position verticale (nombre décimal ou entier)

### Exemples
```
!admin setpos 10 5
!admin setpos 15.5 8.0
!admin setpos 0 0
!admin setpos 20 12
!admin setpos 12.3 6.7
```

### Résultat
```
✅ Bot téléporté à x=10, y=5
```

### Logs
```
[POSITION] Téléporté à x=10, y=5 par sylver_ralx_lm
```

### Cas d'usage

#### Positionner le bot à l'entrée
```
!admin setpos 5 3
```

#### Positionner le bot au centre
```
!admin setpos 10 5
```

#### Positionner le bot sur une scène
```
!admin setpos 15 8
```

#### Positionner le bot dans un coin
```
!admin setpos 20 15
```

### Erreurs possibles

#### Coordonnées invalides
```
!admin setpos abc def
```
→ `❌ Coordonnées invalides (doivent être des nombres)`

#### Position hors limites
```
!admin setpos 999 999
```
→ Le bot essaie de se téléporter mais peut échouer si la position n'existe pas

### Notes techniques
- La position utilise `z=0.0` par défaut (niveau du sol)
- La direction est `FrontRight` par défaut
- Le bot utilise `walk_to()` pour se déplacer

---

## 😴 Commande : !admin rest

### Description
Le bot fait l'emote "sleep" (dormir) près de l'admin qui lance la commande.

### Syntaxe
```
!admin rest
```

### Paramètres
Aucun paramètre requis.

### Exemple
```
!admin rest
```

### Résultat
```
😴 Le bot se repose près de toi (sleep)
```

### Logs
```
[REST] Emote sleep exécutée sur sylver_ralx_lm
```

### Comportement
1. Le bot trouve ta position dans la room
2. Le bot exécute l'emote `idle-sleep` (dormir) vers toi
3. Tu reçois une confirmation en DM

### Emote utilisée
- **ID** : `idle-sleep`
- **Nom** : Sleep (Dormir)
- **Type** : Pose/Idle
- **Description** : Le bot dort/se repose

### Autres emotes similaires disponibles

Si tu veux changer l'emote de rest, voici les alternatives :

#### S'asseoir
```python
await self.highrise.send_emote("idle-loop-sitfloor", user.id)
```

#### Être fatigué
```python
await self.highrise.send_emote("emote-tired", user.id)
```

#### Réfléchir
```python
await self.highrise.send_emote("emote-think", user.id)
```

#### Poser (model)
```python
await self.highrise.send_emote("emote-model", user.id)
```

### Modifier l'emote de rest

Pour changer l'emote, édite le fichier `bot.py` à la ligne 2278 :

```python
# Emote actuelle (sleep)
await self.highrise.send_emote("idle-sleep", user.id)

# Alternatives :
await self.highrise.send_emote("idle-loop-sitfloor", user.id)  # S'asseoir
await self.highrise.send_emote("emote-tired", user.id)         # Fatigué
await self.highrise.send_emote("emote-think", user.id)         # Réfléchir
```

### Cas d'usage

#### Après avoir dansé
Le bot danse le floss en boucle, tu veux qu'il se repose :
```
!admin rest
```

#### Faire une pause
Le bot est actif, tu veux qu'il fasse une pause :
```
!admin rest
```

#### Photo de groupe
Tu veux que le bot dorme pour une photo :
```
!admin rest
```

---

## 🎮 Utilisation combinée

### Scénario 1 : Bot qui dort sur la scène
```
!admin setpos 15 8
!admin rest
```
→ Le bot va sur la scène et dort

### Scénario 2 : Bot qui se repose au centre
```
!admin setpos 10 5
!admin rest
```
→ Le bot va au centre et dort

### Scénario 3 : Bot qui dort à l'entrée
```
!admin setpos 5 3
!admin rest
```
→ Le bot va à l'entrée et dort

---

## 📊 Comparaison des emotes de repos

| Emote | ID | Description | Durée |
|-------|-----|-------------|-------|
| **Sleep** ⭐ | `idle-sleep` | Dormir (couché) | Continue |
| Sit | `idle-loop-sitfloor` | S'asseoir (au sol) | Continue |
| Tired | `emote-tired` | Fatigué (debout) | Courte |
| Think | `emote-think` | Réfléchir (main au menton) | Courte |

⭐ = Emote actuellement utilisée pour `!admin rest`

---

## 🔧 Code source

### Fonction cmd_setpos (ligne 2244-2267)
```python
async def cmd_setpos(self, user: User, params):
    """Définir la position du bot"""
    if len(params) < 2:
        await self.highrise.send_whisper(user.id, 
            "Usage: !admin setpos <x> <y>\n"
            "Exemple: !admin setpos 10 5")
        return
    
    try:
        x = float(params[0])
        y = float(params[1])
        
        # Position avec z=0 et direction par défaut
        position = Position(x, y, 0.0, "FrontRight")
        
        await self.highrise.walk_to(position)
        await self.highrise.send_whisper(user.id, f"✅ Bot téléporté à x={x}, y={y}")
        print(f"[POSITION] Téléporté à x={x}, y={y} par {user.username}")
        
    except ValueError:
        await self.highrise.send_whisper(user.id, "❌ Coordonnées invalides (doivent être des nombres)")
    except Exception as e:
        await self.highrise.send_whisper(user.id, f"❌ Erreur: {e}")
        print(f"[ERREUR] Setpos: {e}")
```

### Fonction cmd_rest (ligne 2269-2287)
```python
async def cmd_rest(self, user: User):
    """Faire l'emote rest (sleep) sur l'admin"""
    try:
        # Trouver la position de l'admin
        room_users = await self.highrise.get_room_users()
        
        for room_user, position in room_users.content:
            if room_user.id == user.id:
                # Faire l'emote sleep (rest) sur l'admin
                await self.highrise.send_emote("idle-sleep", user.id)
                await self.highrise.send_whisper(user.id, "😴 Le bot se repose près de toi (sleep)")
                print(f"[REST] Emote sleep exécutée sur {user.username}")
                return
        
        await self.highrise.send_whisper(user.id, "❌ Position non trouvée")
        
    except Exception as e:
        await self.highrise.send_whisper(user.id, f"❌ Erreur: {e}")
        print(f"[ERREUR] Rest: {e}")
```

---

## 📋 Résumé

| Commande | Syntaxe | Description | Exemple |
|----------|---------|-------------|---------|
| **setpos** | `!admin setpos <x> <y>` | Téléporter le bot | `!admin setpos 10 5` |
| **rest** | `!admin rest` | Bot dort près de toi | `!admin rest` |

### Emote rest
- **Emote actuelle** : `idle-sleep` (Dormir)
- **Alternatives** : `idle-loop-sitfloor` (S'asseoir), `emote-tired` (Fatigué)
- **Modification** : Ligne 2278 dans `bot.py`

---

## ✅ Vérification

### Test setpos
```
!admin setpos 10 5
```
→ `✅ Bot téléporté à x=10, y=5`

### Test rest
```
!admin rest
```
→ `😴 Le bot se repose près de toi (sleep)`

---

**Les commandes sont prêtes à l'emploi ! 📍😴**
