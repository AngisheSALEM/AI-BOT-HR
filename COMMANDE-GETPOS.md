# 📍 Commande : !admin getpos

## 🎯 Description

Cette commande permet de **récupérer la position exacte d'un utilisateur** et de **générer automatiquement le script** à copier dans `on_start()` pour que le bot se téléporte à cette position au démarrage.

---

## 🎮 Utilisation

### Syntaxe
```
!admin getpos <username>
```

### Exemples
```
!admin getpos sindouche
!admin getpos sylver_ralx_lm
!admin getpos autre_user
```

---

## 📋 Processus

### Étape 1 : Placer l'utilisateur
1. Place-toi (ou demande à un utilisateur) à l'endroit exact où tu veux que le bot se téléporte
2. Note bien le username de cet utilisateur

### Étape 2 : Récupérer la position
```
!admin getpos <username>
```

### Étape 3 : Copier le script
Le bot génère le script dans les **logs** (terminal)

### Étape 4 : Coller dans bot.py
Copie le script généré dans `on_start()` (ligne ~120)

---

## 📊 Résultat

### Dans les logs (terminal)
```
============================================================
📍 POSITION DE SINDOUCHE
============================================================
# ========================================
# SCRIPT DE POSITION PAR DÉFAUT
# ========================================
# Position de sindouche
# Copie ce code dans on_start() (ligne ~120)

# Téléporter le bot à une position par défaut
try:
    default_position = Position(10.5, 0.0, 5.5, "FrontRight")
    await self.highrise.walk_to(default_position)
    print(f"[POSITION] Bot téléporté à x={default_position.x}, y={default_position.y}")
except Exception as e:
    print(f"[ERREUR] Téléportation: {e}")

# ========================================
# DÉTAILS DE LA POSITION
# ========================================
# X: 10.5 (horizontal)
# Y: 0.0 (vertical)
# Z: 5.5 (profondeur)
# Facing: FrontRight (direction)
# ========================================
============================================================
```

### En DM (whisper)
```
✅ Position de sindouche récupérée!
X: 10.5
Y: 0.0
Z: 5.5
Facing: FrontRight

📋 Script généré dans les logs!
```

---

## 🔧 Comment utiliser le script généré

### 1. Copier le script
Copie le bloc de code généré dans les logs (entre les `try:` et `except:`)

### 2. Ouvrir bot.py
Ouvre le fichier `bot.py` et va à la ligne ~120 (dans la fonction `on_start()`)

### 3. Remplacer le code existant
Cherche ce bloc :
```python
# Téléporter le bot à une position par défaut (optionnel)
try:
    # Position par défaut : centre de la room
    default_position = Position(10.5, 0.0, 5.5, "FrontRight")
    await self.highrise.walk_to(default_position)
    print(f"[POSITION] Bot téléporté à x={default_position.x}, y={default_position.y}")
except Exception as e:
    print(f"[ERREUR] Téléportation: {e}")
```

### 4. Remplacer par le nouveau script
Remplace les valeurs de `Position()` par celles générées :
```python
# Téléporter le bot à une position par défaut
try:
    default_position = Position(12.3, 2.5, 8.7, "Front")  # Nouvelles valeurs
    await self.highrise.walk_to(default_position)
    print(f"[POSITION] Bot téléporté à x={default_position.x}, y={default_position.y}")
except Exception as e:
    print(f"[ERREUR] Téléportation: {e}")
```

### 5. Sauvegarder et relancer
- Sauvegarde `bot.py`
- Relance le bot
- Le bot se téléportera automatiquement à la nouvelle position !

---

## 🎯 Cas d'usage

### Cas 1 : Positionner le bot à l'entrée
1. Va te placer à l'entrée de la room
2. `!admin getpos sylver_ralx_lm`
3. Copie le script dans `bot.py`
4. Relance le bot → Il apparaît à l'entrée

### Cas 2 : Positionner le bot sur la scène
1. Va te placer sur la scène
2. `!admin getpos sylver_ralx_lm`
3. Copie le script dans `bot.py`
4. Relance le bot → Il apparaît sur la scène

### Cas 3 : Positionner le bot près d'un objet
1. Va te placer près de l'objet (DJ booth, canapé, etc.)
2. `!admin getpos sylver_ralx_lm`
3. Copie le script dans `bot.py`
4. Relance le bot → Il apparaît près de l'objet

### Cas 4 : Copier la position d'un autre utilisateur
1. Demande à un utilisateur de se placer où tu veux
2. `!admin getpos <son_username>`
3. Copie le script dans `bot.py`
4. Relance le bot → Il apparaît à sa position

---

## 📐 Comprendre les coordonnées

### X (horizontal)
- Position gauche/droite dans la room
- Exemple : `10.5`

### Y (vertical)
- Position bas/haut (hauteur)
- `0.0` = au sol
- `2.5` = en hauteur (scène, plateforme)
- Exemple : `0.0`

### Z (profondeur)
- Position avant/arrière
- Exemple : `5.5`

### Facing (direction)
Direction du regard :
- `Front` - Vers l'avant
- `Back` - Vers l'arrière
- `Left` - Vers la gauche
- `Right` - Vers la droite
- `FrontRight` - Diagonale avant-droite
- `FrontLeft` - Diagonale avant-gauche
- `BackRight` - Diagonale arrière-droite
- `BackLeft` - Diagonale arrière-gauche

---

## ⚠️ Erreurs possibles

### Utilisateur non trouvé
```
❌ Utilisateur 'username' non trouvé dans la room
```
→ Vérifie que l'utilisateur est bien dans la room
→ Vérifie l'orthographe du username

### Pas de paramètre
```
Usage: !admin getpos <username>
Exemple: !admin getpos sindouche
```
→ Tu as oublié de spécifier le username

---

## 💡 Astuces

### 1. Tester avant de modifier bot.py
Utilise `!admin setpos <x> <y>` pour tester la position avant de la mettre par défaut :
```
!admin getpos sindouche
# Récupère X: 10.5, Y: 0.0
!admin setpos 10.5 0.0
# Teste si la position est bonne
```

### 2. Sauvegarder plusieurs positions
Tu peux générer plusieurs scripts et les sauvegarder dans un fichier texte pour les réutiliser plus tard.

### 3. Précision maximale
Pour une précision maximale, place-toi exactement où tu veux que le bot soit, puis utilise `!admin getpos` immédiatement.

### 4. Direction importante
La direction (`facing`) est importante pour que le bot regarde dans la bonne direction (vers la scène, vers l'entrée, etc.)

---

## 🔧 Code source

### Fonction cmd_get_position (ligne 2367-2434)
```python
async def cmd_get_position(self, user: User, params):
    """Obtenir la position d'un utilisateur et générer le script"""
    try:
        if len(params) < 1:
            await self.highrise.send_whisper(user.id, 
                "Usage: !admin getpos <username>\n"
                "Exemple: !admin getpos sindouche")
            return
        
        target_username = ' '.join(params).lower()
        
        # Récupérer tous les utilisateurs dans la room
        room_users = await self.highrise.get_room_users()
        
        for room_user, position in room_users.content:
            if room_user.username.lower() == target_username:
                # Position trouvée !
                x = position.x
                y = position.y
                z = position.z
                facing = position.facing
                
                # Générer le script
                script = f"""# ========================================
# SCRIPT DE POSITION PAR DÉFAUT
# ========================================
# Position de {room_user.username}
# Copie ce code dans on_start() (ligne ~120)

# Téléporter le bot à une position par défaut
try:
    default_position = Position({x}, {y}, {z}, "{facing}")
    await self.highrise.walk_to(default_position)
    print(f"[POSITION] Bot téléporté à x={{default_position.x}}, y={{default_position.y}}")
except Exception as e:
    print(f"[ERREUR] Téléportation: {{e}}")

# ========================================
# DÉTAILS DE LA POSITION
# ========================================
# X: {x} (horizontal)
# Y: {y} (vertical)
# Z: {z} (profondeur)
# Facing: {facing} (direction)
# ========================================"""
                
                # Afficher dans les logs
                print("\n" + "="*60)
                print(f"📍 POSITION DE {room_user.username.upper()}")
                print("="*60)
                print(script)
                print("="*60 + "\n")
                
                # Envoyer confirmation en DM
                await self.highrise.send_whisper(user.id, 
                    f"✅ Position de {room_user.username} récupérée!\n"
                    f"X: {x}\nY: {y}\nZ: {z}\n"
                    f"Facing: {facing}\n\n"
                    f"📋 Script généré dans les logs!")
                
                return
        
        # Utilisateur non trouvé
        await self.highrise.send_whisper(user.id, f"❌ Utilisateur '{target_username}' non trouvé dans la room")
        
    except Exception as e:
        await self.highrise.send_whisper(user.id, f"❌ Erreur: {e}")
        print(f"[ERREUR] Get position: {e}")
```

---

## 📋 Workflow complet

### 1️⃣ Placer l'utilisateur
Place-toi où tu veux que le bot apparaisse

### 2️⃣ Récupérer la position
```
!admin getpos sylver_ralx_lm
```

### 3️⃣ Copier le script
Copie le script dans les logs (terminal)

### 4️⃣ Modifier bot.py
Ouvre `bot.py` et va à la ligne ~120

### 5️⃣ Remplacer les valeurs
Remplace les valeurs dans `Position(x, y, z, "facing")`

### 6️⃣ Sauvegarder
Sauvegarde `bot.py`

### 7️⃣ Relancer le bot
Relance le bot pour appliquer la nouvelle position

### 8️⃣ Vérifier
Le bot apparaît à la position exacte !

---

## ✅ Résumé

| Étape | Action | Commande |
|-------|--------|----------|
| 1 | Se placer | - |
| 2 | Récupérer position | `!admin getpos <username>` |
| 3 | Copier script | Depuis les logs |
| 4 | Modifier bot.py | Ligne ~120 |
| 5 | Relancer | `START.bat` |

### Avantages
- ✅ Précision maximale
- ✅ Script généré automatiquement
- ✅ Facile à copier/coller
- ✅ Détails complets (X, Y, Z, Facing)
- ✅ Fonctionne avec n'importe quel utilisateur

---

**Tu peux maintenant positionner le bot exactement où tu veux avec une précision parfaite ! 📍✨**
