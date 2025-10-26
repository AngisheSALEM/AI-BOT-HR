# 🛍️ Acheter des items via l'API Highrise

## 🎯 Méthodes pour obtenir des items

### Méthode 1 : Cadeaux (AUTOMATIQUE)

Les cadeaux dans Highrise sont **automatiquement acceptés** !

**Comment faire :**
1. Lance le bot dans une room
2. Rejoins avec ton compte
3. Envoie un cadeau au bot
4. ✅ Le bot reçoit automatiquement l'item (pas besoin d'accepter)

### Méthode 2 : Acheter via l'API

Le SDK Highrise permet d'acheter des items directement !

## 📋 Acheter des items avec l'API

### Fonction : buy_item()

```python
await self.highrise.buy_item(item_id: str)
```

### Exemple de commande admin

Ajoute cette commande dans `handle_admin_command` :

```python
elif subcmd == 'buyitem':
    if subparams:
        item_id = subparams[0]
        try:
            await self.highrise.buy_item(item_id)
            await self.highrise.send_whisper(user.id, f"✅ Item acheté: {item_id}")
            print(f"[SHOP] Item acheté: {item_id}")
        except Exception as e:
            await self.highrise.send_whisper(user.id, f"❌ Erreur: {e}")
            print(f"[SHOP] Erreur achat: {e}")
    else:
        await self.highrise.send_whisper(user.id, "Usage: !admin buyitem <item_id>")
```

**Usage :**
```
!admin buyitem shirt-n_room32019denimjackethoodie
```

## 🔍 Trouver les IDs des items du shop

### Méthode 1 : API get_item_catalog()

Il existe une méthode pour récupérer le catalogue :

```python
async def cmd_catalog(self, user: User):
    """Afficher le catalogue d'items disponibles"""
    try:
        # Note: Cette méthode peut ne pas être disponible dans toutes les versions
        catalog = await self.highrise.get_item_catalog()
        
        print("\n" + "="*60)
        print("🛍️ CATALOGUE D'ITEMS DISPONIBLES")
        print("="*60)
        
        for item in catalog[:50]:  # Limiter à 50 items
            print(f"ID: {item.id}")
            print(f"Type: {item.type}")
            print(f"Prix: {item.price} gold")
            print("---")
        
        await self.highrise.send_whisper(user.id, 
            "✅ Catalogue affiché dans les logs")
            
    except Exception as e:
        print(f"[ERREUR] Catalogue: {e}")
        await self.highrise.send_whisper(user.id, f"Erreur: {e}")
```

### Méthode 2 : IDs connus

Voici quelques IDs d'items populaires :

#### Shirts (Hauts)
```
shirt-n_room32019denimjackethoodie
shirt-n_room12019blackhoodie
shirt-n_room22019whitehoodie
shirt-n_starteritems2019malet_shirt
```

#### Pants (Pantalons)
```
pants-n_starteritems2019malepants
pants-n_room32019rippedjeans
pants-n_room12019joggers
pants-n_starteritems2019cuffedjeanswhite
```

#### Shoes (Chaussures)
```
shoes-n_starteritems2019maleshoes
shoes-n_room12019sneakers
shoes-n_room32019socksneakersgrey
```

### Méthode 3 : Site web Highrise

Tu peux aussi regarder les items sur :
- https://highrise.game (site officiel)
- Le shop dans l'application

Les IDs suivent généralement ce format :
```
type-n_collection_name
```

## 💰 Vérifier le wallet du bot

Avant d'acheter, vérifie combien de gold le bot a :

```python
async def cmd_wallet(self):
    """Afficher le wallet du bot"""
    try:
        wallet = await self.highrise.get_wallet()
        gold = wallet.gold
        await self.highrise.chat(f"💰 Gold: {gold}")
        print(f"[WALLET] Gold disponible: {gold}")
    except Exception as e:
        print(f"[ERREUR] Wallet: {e}")
```

**Usage :**
```
!admin wallet
```

## 🛒 Acheter plusieurs items

Crée une commande pour acheter plusieurs items d'un coup :

```python
elif subcmd == 'buyoutfit':
    # Acheter un outfit complet
    outfit_items = [
        "shirt-n_room32019denimjackethoodie",
        "pants-n_room32019rippedjeans",
        "shoes-n_room12019sneakers"
    ]
    
    success_count = 0
    for item_id in outfit_items:
        try:
            await self.highrise.buy_item(item_id)
            success_count += 1
            print(f"[SHOP] ✅ Acheté: {item_id}")
            await asyncio.sleep(1)  # Pause entre achats
        except Exception as e:
            print(f"[SHOP] ❌ Erreur {item_id}: {e}")
    
    await self.highrise.send_whisper(user.id, 
        f"✅ {success_count}/{len(outfit_items)} items achetés")
```

## ⚠️ Limitations

### Le bot doit avoir du gold

Si le bot n'a pas assez de gold :
1. Tu ne peux pas acheter d'items
2. Il faut ajouter du gold au compte du bot

### Comment ajouter du gold au bot ?

**Problème :** Les bots ne peuvent pas acheter du gold directement.

**Solutions :**
1. **Envoyer du gold depuis ton compte** (si possible)
2. **Créer le bot sur un compte utilisateur** qui a du gold
3. **Utiliser les items gratuits** du starter pack

## 💡 Solution recommandée

### Pour commencer : Utiliser les cadeaux

1. **Lance le bot**
2. **Envoie-lui des vêtements** depuis ton compte
3. Les items sont **automatiquement acceptés**
4. Utilise `!admin inventory` pour voir les nouveaux items

### Pour plus tard : Acheter via API

Quand le bot aura du gold, utilise :
```
!admin buyitem <item_id>
```

## 📝 Code complet à ajouter

Ajoute dans `handle_admin_command` :

```python
elif subcmd == 'buyitem':
    if subparams:
        item_id = subparams[0]
        try:
            # Vérifier le wallet d'abord
            wallet = await self.highrise.get_wallet()
            print(f"[SHOP] Gold disponible: {wallet.gold}")
            
            # Acheter l'item
            await self.highrise.buy_item(item_id)
            await self.highrise.send_whisper(user.id, f"✅ Item acheté: {item_id}")
            print(f"[SHOP] ✅ Item acheté: {item_id}")
            
            # Vérifier le nouveau wallet
            new_wallet = await self.highrise.get_wallet()
            print(f"[SHOP] Gold restant: {new_wallet.gold}")
            
        except Exception as e:
            await self.highrise.send_whisper(user.id, f"❌ Erreur: {e}")
            print(f"[SHOP] ❌ Erreur: {e}")
    else:
        await self.highrise.send_whisper(user.id, "Usage: !admin buyitem <item_id>")
```

## 🎯 Résumé

### Cadeaux (SIMPLE)
- ✅ Automatiquement acceptés
- ✅ Gratuit
- ✅ Fonctionne immédiatement

### Acheter via API (AVANCÉ)
- ✅ Automatique
- ❌ Nécessite du gold
- ✅ Commande: `!admin buyitem <item_id>`

### Vérifier le wallet
```
!admin wallet
```

### Acheter un item
```
!admin buyitem shirt-n_room32019denimjackethoodie
```

---

**Les cadeaux sont automatiquement acceptés ! Mais tu peux aussi acheter via l'API si le bot a du gold ! 🛍️**
