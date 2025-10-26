# 👔 Changer les vêtements du bot Highrise

## 🎯 Méthode : set_outfit()

Pour changer les vêtements de ton bot, utilise la méthode `set_outfit()` du SDK Highrise.

## 📋 Comment obtenir l'ID d'une tenue

### Méthode 1 : Via l'application Highrise

1. **Crée une tenue dans le jeu**
   - Ouvre Highrise
   - Va dans ton dressing
   - Crée la tenue que tu veux pour ton bot
   - Sauvegarde-la

2. **Récupère l'ID de la tenue**
   - L'ID de la tenue est un identifiant unique
   - Tu peux le voir dans les paramètres de ta tenue

### Méthode 2 : Via le code (récupérer la tenue actuelle)

```python
async def get_current_outfit(self):
    """Récupérer la tenue actuelle du bot"""
    try:
        outfit = await self.highrise.get_outfit()
        print(f"[OUTFIT] Tenue actuelle: {outfit}")
        return outfit
    except Exception as e:
        print(f"[ERREUR] Impossible de récupérer la tenue: {e}")
```

## 💻 Code pour changer la tenue

### Option 1 : Changer au démarrage (on_start)

```python
async def on_start(self, session_metadata: SessionMetadata) -> None:
    print("[OK] Bot connecte!")
    
    # Changer la tenue du bot
    try:
        # Remplace 'OUTFIT_ID' par l'ID de ta tenue
        outfit_id = "OUTFIT_ID_ICI"
        await self.highrise.set_outfit(outfit_id)
        print(f"[OUTFIT] Tenue changee: {outfit_id}")
    except Exception as e:
        print(f"[ERREUR] Impossible de changer la tenue: {e}")
```

### Option 2 : Commande admin pour changer la tenue

Ajoute cette fonction dans `bot.py` :

```python
async def change_outfit(self, outfit_id: str):
    """Changer la tenue du bot"""
    try:
        await self.highrise.set_outfit(outfit_id)
        print(f"[OUTFIT] Tenue changee: {outfit_id}")
        return True
    except Exception as e:
        print(f"[ERREUR] Impossible de changer la tenue: {e}")
        return False
```

Puis dans `handle_admin_command`, ajoute :

```python
elif subcmd == 'outfit':
    if subparams:
        outfit_id = subparams[0]
        success = await self.change_outfit(outfit_id)
        if success:
            await self.highrise.send_whisper(user.id, f"Tenue changee: {outfit_id}")
        else:
            await self.highrise.send_whisper(user.id, "Erreur lors du changement de tenue")
    else:
        await self.highrise.send_whisper(user.id, "Usage: !admin outfit <outfit_id>")
```

**Usage :** `!admin outfit OUTFIT_ID_ICI`

### Option 3 : Changer la tenue aléatoirement

```python
async def random_outfit(self):
    """Changer la tenue aléatoirement parmi une liste"""
    import random
    
    # Liste de tes tenues préférées
    outfits = [
        "OUTFIT_ID_1",
        "OUTFIT_ID_2",
        "OUTFIT_ID_3",
        "OUTFIT_ID_4"
    ]
    
    outfit_id = random.choice(outfits)
    
    try:
        await self.highrise.set_outfit(outfit_id)
        print(f"[OUTFIT] Tenue aleatoire: {outfit_id}")
        return True
    except Exception as e:
        print(f"[ERREUR] {e}")
        return False
```

### Option 4 : Changer la tenue périodiquement

```python
async def outfit_rotation(self):
    """Changer la tenue toutes les heures"""
    outfits = [
        "OUTFIT_ID_1",
        "OUTFIT_ID_2",
        "OUTFIT_ID_3"
    ]
    
    current_index = 0
    
    while True:
        try:
            outfit_id = outfits[current_index]
            await self.highrise.set_outfit(outfit_id)
            print(f"[OUTFIT] Tenue changee: {outfit_id}")
            
            current_index = (current_index + 1) % len(outfits)
            
            # Attendre 1 heure
            await asyncio.sleep(3600)
        except Exception as e:
            print(f"[ERREUR] {e}")
            await asyncio.sleep(60)

# Dans on_start, démarre la rotation
async def on_start(self, session_metadata: SessionMetadata) -> None:
    # ... autres initialisations ...
    
    # Démarrer la rotation de tenues
    asyncio.create_task(self.outfit_rotation())
```

## 🔍 Trouver l'ID d'une tenue

### Méthode avec le code

Ajoute cette commande pour voir ta tenue actuelle :

```python
# Dans handle_admin_command
elif subcmd == 'getoutfit':
    try:
        outfit = await self.highrise.get_outfit()
        await self.highrise.send_whisper(user.id, f"Tenue actuelle: {outfit}")
        print(f"[OUTFIT] {outfit}")
    except Exception as e:
        await self.highrise.send_whisper(user.id, f"Erreur: {e}")
```

**Usage :** `!admin getoutfit`

## 📊 Structure d'une tenue

Une tenue Highrise contient :
- **outfit_id** : L'identifiant unique de la tenue
- **items** : Liste des items (vêtements, accessoires)
- Chaque item a un ID unique

## 💡 Exemple complet

```python
class HighriseBot(BaseBot):
    def __init__(self):
        super().__init__()
        # Liste de tenues
        self.outfits = {
            "casual": "OUTFIT_ID_CASUAL",
            "elegant": "OUTFIT_ID_ELEGANT",
            "sport": "OUTFIT_ID_SPORT"
        }
    
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("[OK] Bot connecte!")
        
        # Mettre la tenue "casual" au démarrage
        await self.change_outfit_by_name("casual")
    
    async def change_outfit_by_name(self, outfit_name: str):
        """Changer la tenue par son nom"""
        if outfit_name in self.outfits:
            outfit_id = self.outfits[outfit_name]
            try:
                await self.highrise.set_outfit(outfit_id)
                print(f"[OUTFIT] Tenue '{outfit_name}' activee")
                return True
            except Exception as e:
                print(f"[ERREUR] {e}")
                return False
        else:
            print(f"[ERREUR] Tenue '{outfit_name}' inconnue")
            return False
    
    # Dans handle_admin_command
    async def handle_admin_command(self, user: User, message: str):
        # ... autres commandes ...
        
        elif subcmd == 'outfit':
            if subparams:
                outfit_name = subparams[0]
                success = await self.change_outfit_by_name(outfit_name)
                if success:
                    await self.highrise.send_whisper(user.id, 
                        f"Tenue changee: {outfit_name}")
                else:
                    await self.highrise.send_whisper(user.id, 
                        f"Tenue '{outfit_name}' inconnue")
            else:
                available = ", ".join(self.outfits.keys())
                await self.highrise.send_whisper(user.id, 
                    f"Tenues disponibles: {available}")
```

**Usage :**
- `!admin outfit casual` - Tenue casual
- `!admin outfit elegant` - Tenue élégante
- `!admin outfit sport` - Tenue sport
- `!admin outfit` - Liste des tenues

## 🎨 Créer des tenues thématiques

### Tenues selon l'heure
```python
async def outfit_by_time(self):
    """Changer la tenue selon l'heure"""
    from datetime import datetime
    
    hour = datetime.now().hour
    
    if 6 <= hour < 12:
        outfit = "morning"  # Tenue du matin
    elif 12 <= hour < 18:
        outfit = "afternoon"  # Tenue d'après-midi
    elif 18 <= hour < 22:
        outfit = "evening"  # Tenue de soirée
    else:
        outfit = "night"  # Tenue de nuit
    
    await self.change_outfit_by_name(outfit)
```

### Tenues selon l'événement
```python
async def on_user_join(self, user: User, position: Position) -> None:
    # Changer de tenue quand Sindouche arrive
    if user.username.lower() == "sindouche":
        await self.change_outfit_by_name("elegant")
        await self.highrise.chat("✨ *change de tenue pour Sindouche* ✨")
```

## 📝 Notes importantes

### ⚠️ Limitations
- Tu dois avoir les items dans ton inventaire
- L'outfit_id doit être valide
- Le bot doit avoir les permissions nécessaires

### ✅ Bonnes pratiques
- Sauvegarde tes outfit_ids dans une variable
- Gère les erreurs avec try/except
- Teste d'abord avec une commande admin
- Utilise des noms descriptifs pour tes tenues

## 🔧 Debugging

Si ça ne fonctionne pas :

1. **Vérifie l'ID de la tenue**
   ```python
   print(f"[DEBUG] Tentative de changement: {outfit_id}")
   ```

2. **Vérifie les erreurs**
   ```python
   try:
       await self.highrise.set_outfit(outfit_id)
   except Exception as e:
       print(f"[ERREUR] Type: {type(e).__name__}")
       print(f"[ERREUR] Message: {e}")
   ```

3. **Vérifie que le bot a l'item**
   - Assure-toi que le bot possède tous les items de la tenue

## 🎯 Résumé

### Méthode simple
```python
await self.highrise.set_outfit("OUTFIT_ID")
```

### Avec gestion d'erreur
```python
try:
    await self.highrise.set_outfit("OUTFIT_ID")
    print("[OK] Tenue changee")
except Exception as e:
    print(f"[ERREUR] {e}")
```

### Commande admin
```python
!admin outfit OUTFIT_ID
```

---

**Pour changer la tenue de ton bot, tu as besoin de l'outfit_id de la tenue ! 👔✨**

**Utilise `!admin getoutfit` pour voir ta tenue actuelle et récupérer son ID.**
