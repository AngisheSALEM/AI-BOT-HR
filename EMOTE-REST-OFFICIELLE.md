# 😌 Emote REST - Documentation officielle

## ✅ Vraie emote REST trouvée !

D'après la documentation officielle du SDK Highrise, la vraie emote "Rest" est :

### Emote officielle
```python
Emote(name="Rest", id="sit-idle-cute", duration=17.062613, is_free=False)
```

**Détails :**
- 📝 **Nom** : Rest
- 🆔 **ID** : `sit-idle-cute`
- ⏱️ **Durée** : 17.06 secondes
- 💰 **Gratuite** : ❌ Non (payante)

## ⚠️ Problème

Cette emote est **payante** (`is_free=False`), ce qui signifie :
- Le bot ne peut l'utiliser que si elle est dans son **inventaire**
- Si le bot n'a pas cette emote, il ne pourra pas l'exécuter

## ✅ Solution implémentée

La commande `!admin rest` utilise maintenant un **système de fallback** :

1. **Essaie d'abord** la vraie emote "Rest" (`sit-idle-cute`)
2. **Si elle échoue** (pas dans l'inventaire), utilise "Sit" (`idle-loop-sitfloor`) qui est gratuite

### Code
```python
try:
    # Essayer la vraie emote "Rest"
    await self.highrise.send_emote("sit-idle-cute", user.id)
    await self.highrise.send_whisper(user.id, "😌 Le bot se repose près de toi (Rest)")
except:
    # Fallback sur l'emote gratuite "Sit"
    await self.highrise.send_emote("idle-loop-sitfloor", user.id)
    await self.highrise.send_whisper(user.id, "😌 Le bot se repose près de toi (Sit)")
```

## 🎮 Utilisation

### Commande
```
!admin rest
```

### Résultats possibles

#### Si le bot a l'emote "Rest" dans son inventaire
```
😌 Le bot se repose près de toi (Rest)
```
**Logs :** `[REST] Emote 'Rest' (sit-idle-cute) exécutée sur sylver_ralx_lm`

#### Si le bot n'a pas l'emote "Rest"
```
😌 Le bot se repose près de toi (Sit)
```
**Logs :** `[REST] Emote 'Sit' (idle-loop-sitfloor) exécutée sur sylver_ralx_lm`

## 📋 Toutes les emotes "rest" disponibles

D'après la documentation officielle, voici toutes les emotes liées au repos :

| Nom | ID | Gratuite | Durée | Description |
|-----|-----|----------|-------|-------------|
| **Rest** | `sit-idle-cute` | ❌ Non | 17.06s | Position assise mignonne |
| Sit | `idle-loop-sitfloor` | ✅ Oui | 22.32s | S'asseoir au sol |
| Sleepy | `idle-sleep` | ❌ Non | 22.62s | Dormir |
| Tired | `emote-tired` | ✅ Oui | 4.61s | Fatigué |
| Relaxed | `idle_layingdown2` | ❌ Non | 21.55s | Allongé détendu |
| Attentive | `idle_layingdown` | ❌ Non | 24.59s | Allongé attentif |
| Relaxing | `idle-floorsleeping2` | ❌ Non | 17.25s | Dormir au sol 2 |
| Cozy Nap | `idle-floorsleeping` | ❌ Non | 13.94s | Sieste confortable |
| Relaxed | `sit-relaxed` | ❌ Non | 29.89s | Assis détendu |
| Laid Back | `sit-open` | ❌ Non | 26.03s | Assis ouvert |

## 💡 Recommandations

### Pour utiliser la vraie emote "Rest"
Le bot doit avoir l'emote `sit-idle-cute` dans son inventaire. Tu peux :
1. L'acheter dans le shop Highrise
2. Vérifier avec `!admin inventory` si elle est disponible

### Alternatives gratuites
Si tu veux une emote gratuite pour "rest" :
- **Sit** (`idle-loop-sitfloor`) - Gratuite, 22 secondes
- **Tired** (`emote-tired`) - Gratuite, 4 secondes

## 🔧 Modifier l'emote de fallback

Si tu veux changer l'emote de fallback, édite la ligne 2285 dans `bot.py` :

```python
# Fallback actuel (Sit)
await self.highrise.send_emote("idle-loop-sitfloor", user.id)

# Alternatives gratuites :
await self.highrise.send_emote("emote-tired", user.id)  # Fatigué
await self.highrise.send_emote("idle-enthusiastic", user.id)  # Enthousiasmé
```

## 📊 Comparaison

| Emote | Gratuite | Durée | Recommandé pour |
|-------|----------|-------|-----------------|
| Rest (sit-idle-cute) | ❌ | 17s | Si dans l'inventaire |
| Sit (idle-loop-sitfloor) | ✅ | 22s | Fallback par défaut |
| Tired (emote-tired) | ✅ | 4s | Animation courte |
| Sleepy (idle-sleep) | ❌ | 22s | Dormir |

## ✅ Résumé

### Emote officielle "Rest"
- **ID** : `sit-idle-cute`
- **Statut** : Payante
- **Utilisation** : Automatique si dans l'inventaire

### Système de fallback
- **Emote principale** : `sit-idle-cute` (Rest)
- **Emote de secours** : `idle-loop-sitfloor` (Sit)
- **Avantage** : Fonctionne toujours, même sans l'emote payante

### Commande
```
!admin rest
```

---

**Source** : Documentation officielle du SDK Highrise
**URL** : https://itsvini.addpotion.com/emotes

**Le bot utilise maintenant la vraie emote "Rest" avec fallback automatique ! 😌**
