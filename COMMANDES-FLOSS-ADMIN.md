# 💃 Commandes Floss pour Admins

## 🎯 Nouvelles commandes

### 1. !admin flossloop - Lancer floss sur l'admin
### 2. !admin flossstop - Arrêter floss sur l'admin

---

## 💃 Commande : !admin flossloop

### Description
Lance une boucle floss **sur l'admin** qui exécute la commande. Le bot fait l'emote floss vers l'admin toutes les 10 secondes.

### Syntaxe
```
!admin flossloop
```

### Résultat
```
💃 Boucle floss lancée sur toi!
Utilise !admin flossstop pour l'arrêter
```

### Logs
```
[FLOSS-ADMIN] Boucle floss lancée pour sylver_ralx_lm
[FLOSS-ADMIN] 💃 Floss exécuté sur sylver_ralx_lm
[FLOSS-ADMIN] 💃 Floss exécuté sur sylver_ralx_lm
...
```

### Comportement
- Le bot fait l'emote floss **vers toi** toutes les 10 secondes
- La boucle continue jusqu'à ce que tu l'arrêtes avec `!admin flossstop`
- **Indépendant** de la boucle floss du bot (le bot continue sa propre boucle)

### Si déjà active
```
⚠️ La boucle floss est déjà active sur toi!
Utilise !admin flossstop pour l'arrêter d'abord
```

---

## 🛑 Commande : !admin flossstop

### Description
Arrête la boucle floss sur l'admin.

### Syntaxe
```
!admin flossstop
```

### Résultat
```
✅ Boucle floss arrêtée!
```

### Logs
```
[FLOSS-ADMIN] Boucle floss arrêtée pour sylver_ralx_lm
```

### Si aucune boucle active
```
⚠️ Aucune boucle floss active sur toi!
Utilise !admin flossloop pour en lancer une
```

---

## 🎮 Utilisation

### Scénario 1 : Lancer la boucle
```
!admin flossloop
```
→ Le bot commence à faire floss vers toi toutes les 10 secondes

### Scénario 2 : Arrêter la boucle
```
!admin flossstop
```
→ Le bot arrête de faire floss vers toi

### Scénario 3 : Plusieurs admins
Chaque admin peut avoir sa propre boucle floss :
- Admin 1 : `!admin flossloop` → Floss sur Admin 1
- Admin 2 : `!admin flossloop` → Floss sur Admin 2
- Les deux boucles fonctionnent en même temps !

---

## 🔄 Différence avec la boucle du bot

### Boucle du bot (automatique)
- **Démarre** : Automatiquement au lancement du bot
- **Cible** : Le bot lui-même (pas vers un utilisateur)
- **Arrêt** : Jamais (boucle infinie)
- **Fonction** : `floss_loop()` (ligne 372)

### Boucle admin (manuelle)
- **Démarre** : Avec `!admin flossloop`
- **Cible** : L'admin qui lance la commande
- **Arrêt** : Avec `!admin flossstop`
- **Fonction** : `floss_loop_on_user()` (ligne 2303)

### Indépendance
Les deux boucles sont **complètement indépendantes** :
- Le bot continue de danser floss pour lui-même
- En même temps, il peut faire floss vers un ou plusieurs admins
- Arrêter la boucle admin n'affecte pas la boucle du bot

---

## 📊 Gestion des tâches

### Structure
```python
# Dictionnaire des tâches floss par admin
self.admin_floss_tasks = {
    "user_id_1": task_1,
    "user_id_2": task_2,
    ...
}
```

### Création d'une tâche
```python
task = asyncio.create_task(self.floss_loop_on_user(user.id, user.username))
self.admin_floss_tasks[user.id] = task
```

### Annulation d'une tâche
```python
task = self.admin_floss_tasks[user.id]
task.cancel()
del self.admin_floss_tasks[user.id]
```

---

## 🎯 Cas d'usage

### Cas 1 : Admin veut danser avec le bot
```
!admin flossloop
```
→ Le bot et l'admin dansent ensemble le floss

### Cas 2 : Plusieurs admins dansent
```
Admin 1: !admin flossloop
Admin 2: !admin flossloop
Admin 3: !admin flossloop
```
→ Le bot fait floss vers les 3 admins en même temps

### Cas 3 : Arrêter sa propre boucle
```
!admin flossstop
```
→ Seule la boucle de cet admin s'arrête, les autres continuent

### Cas 4 : Session de danse temporaire
```
!admin flossloop
# Danse pendant 2 minutes
!admin flossstop
```

---

## 🔧 Code source

### Fonction floss_loop_on_user (ligne 2303-2322)
```python
async def floss_loop_on_user(self, user_id: str, username: str):
    """Boucle floss sur un utilisateur spécifique"""
    print(f"[FLOSS-ADMIN] Démarrage boucle floss sur {username}")
    
    while True:
        try:
            # Faire l'emote floss sur l'utilisateur
            await self.highrise.send_emote("dance-floss", user_id)
            print(f"[FLOSS-ADMIN] 💃 Floss exécuté sur {username}")
            
            # Attendre 10 secondes avant de recommencer
            await asyncio.sleep(10)
            
        except asyncio.CancelledError:
            # La tâche a été annulée (flossstop)
            print(f"[FLOSS-ADMIN] Boucle floss arrêtée pour {username}")
            break
        except Exception as e:
            print(f"[FLOSS-ADMIN] Erreur sur {username}: {e}")
            await asyncio.sleep(15)
```

### Fonction cmd_floss_loop_admin (ligne 2324-2341)
```python
async def cmd_floss_loop_admin(self, user: User):
    """Lancer la boucle floss sur l'admin"""
    try:
        # Vérifier si une boucle existe déjà pour cet admin
        if user.id in self.admin_floss_tasks:
            await self.highrise.send_whisper(user.id, "⚠️ La boucle floss est déjà active sur toi!")
            return
        
        # Créer et démarrer la tâche floss pour cet admin
        task = asyncio.create_task(self.floss_loop_on_user(user.id, user.username))
        self.admin_floss_tasks[user.id] = task
        
        await self.highrise.send_whisper(user.id, "💃 Boucle floss lancée sur toi!")
        print(f"[FLOSS-ADMIN] Boucle floss lancée pour {user.username}")
        
    except Exception as e:
        await self.highrise.send_whisper(user.id, f"❌ Erreur: {e}")
```

### Fonction cmd_floss_stop_admin (ligne 2343-2363)
```python
async def cmd_floss_stop_admin(self, user: User):
    """Arrêter la boucle floss sur l'admin"""
    try:
        # Vérifier si une boucle existe pour cet admin
        if user.id not in self.admin_floss_tasks:
            await self.highrise.send_whisper(user.id, "⚠️ Aucune boucle floss active sur toi!")
            return
        
        # Annuler la tâche
        task = self.admin_floss_tasks[user.id]
        task.cancel()
        
        # Retirer de la liste
        del self.admin_floss_tasks[user.id]
        
        await self.highrise.send_whisper(user.id, "✅ Boucle floss arrêtée!")
        print(f"[FLOSS-ADMIN] Boucle floss arrêtée pour {user.username}")
```

---

## ⚙️ Configuration

### Modifier la fréquence
Pour changer la fréquence du floss sur les admins, édite la ligne 2314 :

```python
await asyncio.sleep(10)  # Change 10 pour modifier
```

**Exemples :**
- `await asyncio.sleep(5)` → Floss toutes les 5 secondes
- `await asyncio.sleep(15)` → Floss toutes les 15 secondes
- `await asyncio.sleep(30)` → Floss toutes les 30 secondes

---

## 📋 Résumé

| Commande | Description | Résultat |
|----------|-------------|----------|
| `!admin flossloop` | Lance floss sur l'admin | `💃 Boucle floss lancée sur toi!` |
| `!admin flossstop` | Arrête floss sur l'admin | `✅ Boucle floss arrêtée!` |

### Caractéristiques
- ✅ Boucles indépendantes par admin
- ✅ N'affecte pas la boucle du bot
- ✅ Plusieurs admins peuvent avoir leur boucle en même temps
- ✅ Fréquence : 10 secondes par défaut
- ✅ Gestion automatique des tâches (création/annulation)

### Logs
- `[FLOSS]` → Boucle du bot
- `[FLOSS-ADMIN]` → Boucles des admins

---

## ✅ Test

### 1. Lancer la boucle
```
!admin flossloop
```
→ `💃 Boucle floss lancée sur toi!`

### 2. Vérifier les logs
```
[FLOSS-ADMIN] Boucle floss lancée pour sylver_ralx_lm
[FLOSS-ADMIN] 💃 Floss exécuté sur sylver_ralx_lm
```

### 3. Arrêter la boucle
```
!admin flossstop
```
→ `✅ Boucle floss arrêtée!`

### 4. Vérifier que le bot continue
Le bot continue sa propre boucle floss indépendamment :
```
[FLOSS] 💃 Emote floss exécutée
[FLOSS] 💃 Emote floss exécutée
```

---

**Le bot peut maintenant faire floss sur les admins individuellement ! 💃🎉**
