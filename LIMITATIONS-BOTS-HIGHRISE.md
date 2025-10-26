# ⚠️ Limitations des bots Highrise

## 🔍 Recherches effectuées

D'après la documentation officielle de Highrise Bot SDK :

## ❌ Ce que les bots NE PEUVENT PAS faire

### 1. Trader/Échanger des items
> **"Take note that bots can only equip those items and not trade them"**

Les bots **ne peuvent pas** :
- ❌ Accepter des trades/échanges
- ❌ Envoyer des items à d'autres utilisateurs
- ❌ Recevoir des items via trade

**Source :** Documentation officielle Highrise Bot SDK

### 2. Recevoir des cadeaux
Les bots ne peuvent pas recevoir de cadeaux directement car :
- Ils ne peuvent pas accepter les trades
- Ils n'ont pas d'interface pour accepter

### 3. Acheter avec des bulles
Les bots peuvent seulement :
- ✅ Utiliser leur propre **wallet** (gold)
- ❌ **Pas de support pour les bulles** dans l'API actuelle

## ✅ Ce que les bots PEUVENT faire

### 1. Acheter des items avec du gold

```python
await self.highrise.buy_item(item_id)
```

**Limitations :**
- Le bot doit avoir du **gold** dans son wallet
- Certains items ne sont **pas disponibles** à l'achat via l'API
- Les bots ne peuvent acheter qu'**une seule fois** chaque item (pas d'utilité d'en avoir plusieurs)

### 2. Équiper des items

```python
await self.highrise.set_outfit([
    Item(type="shirt", id="shirt_id"),
    Item(type="pants", id="pants_id"),
])
```

### 3. Recevoir des tips (pourboires)

```python
async def on_tip(self, sender: User, receiver: User, tip: CurrencyItem) -> None:
    # Les tips sont automatiquement convertis en "Earned Gold"
    pass
```

**Important :** Les tips reçus par les bots sont convertis en **Earned Gold** qui peut être échangé contre de l'argent réel !

### 4. Envoyer des tips

```python
await self.highrise.tip_user(user_id, "gold_bar_1")
```

Valeurs possibles :
- `gold_bar_1`
- `gold_bar_5`
- `gold_bar_10`
- `gold_bar_50`
- `gold_bar_100`
- `gold_bar_500`
- `gold_bar_1k`
- `gold_bar_5000`
- `gold_bar_10k`

## 💰 Wallet du bot

### Vérifier le wallet

```python
wallet = await self.highrise.get_wallet()
gold = wallet.gold
```

### Types de gold

1. **Gold normal** : Peut être utilisé pour acheter des items
2. **Earned Gold** : Reçu via tips, peut être converti en argent réel

## 🛍️ Acheter des items

### Méthode officielle

```python
await self.highrise.buy_item(item_id)
```

**Limitations documentées :**
- ✅ Le bot utilise son propre wallet
- ❌ Certains items ne sont pas disponibles à l'achat
- ❌ Pas besoin d'acheter plusieurs fois le même item
- ❌ Les items achetés ne peuvent pas être tradés

### Pas de support pour les bulles

L'API actuelle ne supporte **que le gold**, pas les bulles.

## 📋 Solutions pour avoir des items

### ❌ Ce qui NE FONCTIONNE PAS

1. **Envoyer des cadeaux au bot** → Les bots ne peuvent pas accepter les trades
2. **Acheter avec des bulles** → Pas de support dans l'API
3. **Trader avec le bot** → Les bots ne peuvent pas trader

### ✅ Ce qui FONCTIONNE

1. **Acheter avec du gold via l'API**
   ```
   !admin buyitem <item_id>
   ```
   - Nécessite que le bot ait du gold
   - Seulement les items disponibles à l'achat

2. **Utiliser les items de départ**
   - Tous les bots ont des items de base (starter items)
   - Utilise-les pour créer un outfit simple

3. **Créer le bot sur un compte utilisateur avec des items**
   - Crée un compte utilisateur normal
   - Achète des items sur ce compte
   - Crée un bot lié à ce compte
   - Le bot aura accès à l'inventaire du compte

## 🎯 Recommandations

### Pour avoir plus d'items

**Option 1 : Acheter avec le gold du bot**
```
!admin wallet           # Vérifier le gold
!admin buyitem <id>     # Acheter un item
```

**Option 2 : Utiliser un compte utilisateur**
1. Crée un compte Highrise normal
2. Achète des items sur ce compte (avec gold ou bulles)
3. Crée un bot lié à ce compte
4. Le bot aura accès aux items du compte

**Option 3 : Utiliser les items de base**
- Tous les bots ont des starter items
- Crée un outfit simple avec ces items

## 📝 Résumé

### Bots PEUVENT
✅ Acheter des items avec **gold** (via API)
✅ Équiper des items
✅ Recevoir des tips (convertis en Earned Gold)
✅ Envoyer des tips

### Bots NE PEUVENT PAS
❌ Accepter des trades/cadeaux
❌ Trader des items
❌ Acheter avec des **bulles**
❌ Recevoir des items d'autres utilisateurs

## 🔗 Sources

- [Highrise Python Bot SDK - GitHub](https://github.com/pocketzworld/python-bot-sdk)
- [Highrise Create Portal - Documentation officielle](https://create.highrise.game/learn/guides/bots/)

---

**Les bots ont des limitations importantes ! Ils ne peuvent pas trader ni recevoir de cadeaux. Utilise `buy_item()` avec du gold pour acheter des items. ⚠️**
