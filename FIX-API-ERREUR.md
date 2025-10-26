# ✅ Fix : Erreur API Highrise

## 🐛 Problème résolu

### Erreur rencontrée
```
[ERREUR] Modify outfit: Expecting value: line 1 column 1 (char 0)
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```

### Cause
L'API Highrise (`https://webapi.highrise.game/items`) ne répond pas toujours correctement :
- Parfois elle retourne une réponse vide
- Parfois elle timeout
- Parfois elle retourne du HTML au lieu de JSON

## ✅ Solution implémentée

### Gestion d'erreur robuste
Le code gère maintenant tous les cas d'erreur :

1. **Timeout** : Si l'API ne répond pas en 5 secondes
2. **Status code** : Vérifie que la réponse est 200 OK
3. **JSON invalide** : Gère les réponses non-JSON
4. **Erreurs générales** : Catch-all pour autres erreurs

### Code ajouté
```python
try:
    response = requests.get('https://webapi.highrise.game/items?rarity=none&limit=500', timeout=5)
    
    if response.status_code == 200:
        items_data = response.json()
        
        # Chercher l'item par nom
        for item in items_data.get('items', []):
            if item['item_name'].lower() == item_name.lower():
                found_item = item
                item_id = found_item['item_id']
                category = found_item['category']
                print(f"[OUTFIT] ✅ Item trouvé dans free items: {item_id}")
                break
    else:
        print(f"[OUTFIT] ⚠️ API erreur: status {response.status_code}")
except requests.exceptions.Timeout:
    print(f"[OUTFIT] ⚠️ API timeout")
except requests.exceptions.JSONDecodeError:
    print(f"[OUTFIT] ⚠️ API réponse invalide")
except Exception as e:
    print(f"[OUTFIT] ⚠️ Erreur API: {e}")
```

## 🎯 Comportement maintenant

### Si l'API fonctionne
✅ L'item est trouvé dans les free items et équipé

### Si l'API ne fonctionne pas
⚠️ Le bot affiche un message d'erreur dans les logs mais **ne crash pas**

Le bot cherche d'abord dans l'inventaire (starter items) qui fonctionne toujours, donc :
- ✅ Les starter items fonctionnent toujours (body, eye, hair, etc.)
- ⚠️ Les free items peuvent échouer si l'API ne répond pas

## 💡 Solution alternative

Si l'API ne fonctionne pas, utilise l'**ID complet** de l'item :

### Au lieu de :
```
!admin modifyoutfit replace Black Flats
```

### Utilise :
```
!admin modifyoutfit replace shoes-n_starteritems2019blackflats
```

## 📋 Items qui fonctionnent toujours

Ces items sont dans l'inventaire du bot et ne dépendent pas de l'API :

### Starter items (toujours disponibles)
```
!admin modifyoutfit replace flesh          # Corps
!admin modifyoutfit replace eye            # Yeux
!admin modifyoutfit replace eyebrow        # Sourcils
!admin modifyoutfit replace nose           # Nez
!admin modifyoutfit replace mouth          # Bouche
!admin modifyoutfit replace hair_front     # Cheveux devant
!admin modifyoutfit replace hair_back      # Cheveux derrière
```

### Free items (dépendent de l'API)
```
!admin modifyoutfit replace Black Flats    # Peut échouer
!admin modifyoutfit replace Basic Pants    # Peut échouer
!admin modifyoutfit replace White Tee      # Peut échouer
```

## 🔧 Recommandations

### Pour les starter items
✅ Utilise les noms courts : `flesh`, `eye`, `hair_front`

### Pour les free items
Si l'API ne fonctionne pas :
1. Utilise `!admin searchitem <category>` quand l'API fonctionne
2. Note les IDs complets
3. Utilise les IDs complets au lieu des noms

### Exemple
```bash
# Quand l'API fonctionne
!admin searchitem shoes
# Note l'ID : shoes-n_starteritems2019blackflats

# Utilise l'ID complet
!admin modifyoutfit replace shoes-n_starteritems2019blackflats
```

## 📊 Résumé

| Situation | Avant | Après |
|-----------|-------|-------|
| API fonctionne | ✅ OK | ✅ OK |
| API timeout | ❌ Crash | ✅ Message d'erreur |
| API réponse invalide | ❌ Crash | ✅ Message d'erreur |
| Starter items | ✅ OK | ✅ OK |

---

**Le bot ne crashe plus si l'API Highrise ne répond pas ! ✅**
