# 🎉 Nouvelles fonctionnalités ajoutées

## ✅ 3 nouvelles fonctionnalités

### 1. 💃 Emote Floss en boucle (automatique)
Le bot exécute l'emote **floss** en boucle indéfiniment !

**Comportement :**
- ✅ Démarre automatiquement au lancement du bot
- 💃 Exécute l'emote floss toutes les 10 secondes
- ♾️ Boucle infinie (ne s'arrête jamais)

**Logs :**
```
[FLOSS] Emote floss en boucle demarree
[FLOSS] 💃 Emote floss exécutée
[FLOSS] 💃 Emote floss exécutée
...
```

### 2. 📍 Commande setpos (définir la position)
Téléporter le bot à une position spécifique

**Commande :**
```
!admin setpos <x> <y>
```

**Exemples :**
```
!admin setpos 10 5
!admin setpos 15.5 8.0
!admin setpos 0 0
!admin setpos 20 12
```

**Résultat :**
```
✅ Bot téléporté à x=10, y=5
```

### 3. 😌 Commande rest (emote sit sur l'admin)
Le bot fait l'emote "rest" (sit) près de toi

**Commande :**
```
!admin rest
```

**Résultat :**
- Le bot s'assoit près de toi
- Message : `😌 Le bot se repose près de toi`

**Emote utilisée :** `idle-loop-sitfloor` (position assise)

## 🎮 Utilisation

### Floss en boucle
Aucune action requise ! Le bot commence automatiquement à danser le floss au démarrage.

### Téléporter le bot
```
!admin setpos 12 6
```

Le bot se déplace instantanément à la position x=12, y=6

### Faire reposer le bot
```
!admin rest
```

Le bot vient s'asseoir près de toi

## 📊 Résumé des modifications

### Fichier : bot.py

#### Ajouts dans `__init__()` (ligne 38-39)
```python
# Tâche pour l'emote floss en boucle
self.floss_task = None
```

#### Ajouts dans `on_start()` (ligne 142-144)
```python
# Démarrer l'emote floss en boucle
self.floss_task = asyncio.create_task(self.floss_loop())
print("[FLOSS] Emote floss en boucle demarree")
```

#### Nouvelle fonction `floss_loop()` (ligne 372-388)
```python
async def floss_loop(self):
    """Exécuter l'emote floss en boucle indéfiniment"""
    print("[FLOSS] Démarrage de la boucle floss...")
    
    while True:
        try:
            # Faire l'emote floss
            await self.highrise.send_emote("dance-floss")
            print("[FLOSS] 💃 Emote floss exécutée")
            
            # Attendre 10 secondes avant de recommencer
            await asyncio.sleep(10)
            
        except Exception as e:
            print(f"[FLOSS] Erreur: {e}")
            # Attendre un peu plus en cas d'erreur
            await asyncio.sleep(15)
```

#### Nouvelles commandes admin (ligne 575-578)
```python
elif subcmd == 'setpos':
    await self.cmd_setpos(user, subparams)
elif subcmd == 'rest':
    await self.cmd_rest(user)
```

#### Nouvelle fonction `cmd_setpos()` (ligne 2244-2267)
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

#### Nouvelle fonction `cmd_rest()` (ligne 2269-2287)
```python
async def cmd_rest(self, user: User):
    """Faire l'emote rest (sit) sur l'admin"""
    try:
        # Trouver la position de l'admin
        room_users = await self.highrise.get_room_users()
        
        for room_user, position in room_users.content:
            if room_user.id == user.id:
                # Faire l'emote sit (rest) sur l'admin
                await self.highrise.send_emote("idle-loop-sitfloor", user.id)
                await self.highrise.send_whisper(user.id, "😌 Le bot se repose près de toi")
                print(f"[REST] Emote rest exécutée sur {user.username}")
                return
        
        await self.highrise.send_whisper(user.id, "❌ Position non trouvée")
        
    except Exception as e:
        await self.highrise.send_whisper(user.id, f"❌ Erreur: {e}")
        print(f"[ERREUR] Rest: {e}")
```

## 🎯 Cas d'usage

### Scénario 1 : Bot DJ qui danse
Le bot est positionné sur la scène et danse le floss en continu
```
!admin setpos 15 8
```
→ Le bot se téléporte sur la scène et continue de danser

### Scénario 2 : Bot qui se repose
Après avoir dansé, tu veux que le bot se repose
```
!admin rest
```
→ Le bot vient s'asseoir près de toi

### Scénario 3 : Repositionner le bot
Le bot est mal placé, tu veux le déplacer
```
!admin setpos 10 5
```
→ Le bot se téléporte au centre

## ⚙️ Configuration

### Modifier la fréquence du floss
Dans `floss_loop()`, ligne 383 :
```python
await asyncio.sleep(10)  # Changer 10 pour modifier la fréquence
```

**Exemples :**
- `await asyncio.sleep(5)` → Floss toutes les 5 secondes
- `await asyncio.sleep(15)` → Floss toutes les 15 secondes
- `await asyncio.sleep(30)` → Floss toutes les 30 secondes

### Désactiver le floss automatique
Commente les lignes 142-144 dans `on_start()` :
```python
# # Démarrer l'emote floss en boucle
# self.floss_task = asyncio.create_task(self.floss_loop())
# print("[FLOSS] Emote floss en boucle demarree")
```

### Changer l'emote de rest
Dans `cmd_rest()`, ligne 2278, remplace `idle-loop-sitfloor` par une autre emote :
```python
await self.highrise.send_emote("idle-sleep", user.id)  # Dormir
await self.highrise.send_emote("emote-think", user.id)  # Réfléchir
await self.highrise.send_emote("idle-loop-sitfloor", user.id)  # S'asseoir
```

## 📋 Liste des commandes admin (mise à jour)

| # | Commande | Description |
|---|----------|-------------|
| 1 | `!admin help` | Aide |
| 2 | `!admin emote <nom\|numero>` | Faire une emote |
| 3 | `!admin tp <x> <y>` | Téléporter |
| 4 | `!admin setpos <x> <y>` | **NOUVEAU** - Définir la position |
| 5 | `!admin rest` | **NOUVEAU** - Emote rest sur l'admin |
| 6 | `!admin announce <message>` | Annonce |
| 7 | `!admin kick <username>` | Expulser |
| 8 | `!admin stats` | Statistiques |
| 9 | `!admin uptime` | Temps en ligne |
| 10 | `!admin wallet` | Voir le wallet |
| 11 | `!admin users` | Nombre d'utilisateurs |
| 12 | `!admin inventory` | Voir l'inventaire |
| 13 | `!admin currentoutfit` | Voir l'outfit actuel |
| 14 | `!admin modifyoutfit` | Modifier l'outfit |
| 15 | `!admin changecolor` | Changer les couleurs |
| 16 | `!admin searchitem` | Chercher des items |
| 17 | `!admin analyzeoutfit` | Analyser un outfit |
| 18 | `!admin checkoutfit` | Vérifier un outfit |
| 19 | `!admin testoutfit` | Tester un outfit |
| 20 | `!admin myid` | Voir son ID |
| 21 | `!admin buyitem` | Acheter un item |

**Total : 21 commandes admin**

## ✅ Résumé

| Fonctionnalité | Type | Statut |
|----------------|------|--------|
| Floss en boucle | Automatique | ✅ Actif au démarrage |
| `!admin setpos` | Commande | ✅ Disponible |
| `!admin rest` | Commande | ✅ Disponible |

---

**Le bot danse maintenant le floss en continu et peut être positionné où tu veux ! 💃🎉**
