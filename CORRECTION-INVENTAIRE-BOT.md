# ⚠️ CORRECTION : Inventaire des bots Highrise

## 🔍 Découverte importante

D'après la **documentation officielle** de Highrise :

> **"Every Highrise user, including bots, has a main inventory"**

## ❌ CE QUI NE FONCTIONNE PAS

### Les bots ont leur PROPRE inventaire

Même si tu crées un bot sur ton compte S_______L_____ qui a 500+ items :

❌ **Le bot n'a PAS accès aux items de ton compte**
❌ **Le bot a son propre inventaire séparé**
❌ **Le bot commence avec seulement les starter items (11 items)**

## 📋 Pourquoi seulement 11 items ?

Quand tu crées un bot, il obtient automatiquement :
- Items de corps (body, eyes, nose, mouth, etc.) : ~8 items
- 1 shirt (haut)
- 1 pants (pantalon)
- 1 shoes (chaussures)

**Total : ~11 items**

C'est l'inventaire de **départ** de tous les bots, peu importe le compte sur lequel ils sont créés.

## 💡 Solutions pour avoir plus d'items

### Solution 1 : Acheter des items avec le bot

Le bot peut acheter ses propres items avec du gold :

```python
await self.highrise.buy_item(item_id)
```

**Problème :** Le bot doit avoir du gold dans son wallet.

### Solution 2 : Utiliser les items gratuits (Free Items)

D'après la documentation, il existe des **"free items"** que les bots peuvent utiliser sans les acheter.

**À investiguer :** Liste des free items disponibles.

### Solution 3 : Acheter du gold pour le bot

1. Le bot reçoit des **tips** (pourboires)
2. Les tips sont convertis en **Earned Gold**
3. Utilise ce gold pour acheter des items

**Ou :**
- Ajoute du gold au wallet du bot (si possible via l'API)

### Solution 4 : Créer plusieurs bots

Si tu veux plusieurs styles :
- Crée plusieurs bots
- Achète différents items pour chaque bot
- Chaque bot a son propre style

## 🔍 Vérifier le wallet du bot

Pour voir combien de gold le bot a :

```
!admin wallet
```

Si le bot a du gold, tu peux acheter des items :

```
!admin buyitem shirt-n_room32019denimjackethoodie
```

## 📝 Ce que dit la documentation

### Inventaire des bots

> **"Bots can only access avatar items, which are essentially game items denoted by the type 'clothing'"**

Les bots peuvent seulement accéder aux items de type **"clothing"** (vêtements).

### Items account_bound

> **"Note that the account_bound parameter marks items limited to the bot account and untradeable"**

Les items du bot sont liés au compte du bot et ne peuvent pas être tradés.

### Pour équiper des items

> **"For an outfit to be valid and accepted by the API, certain requirements must be met. The bot must either use free items, which will be discussed later, or have at least one replica of the item in their inventory"**

Le bot doit :
- Soit utiliser des **free items**
- Soit **posséder l'item** dans son inventaire

## 🎯 Résumé de la situation

### Ce que tu pensais

```
Compte S_______L_____ (500+ items)
    ↓
    Bot créé sur ce compte
    ↓
    Bot a accès aux 500+ items ❌ FAUX
```

### La réalité

```
Compte S_______L_____ (500+ items)
    ↓
    Bot créé sur ce compte
    ↓
    Bot a son PROPRE inventaire (11 items de base)
    ↓
    Le bot doit acheter ses propres items
```

## 💰 Comment obtenir du gold pour le bot

### Méthode 1 : Tips (Pourboires)

Les utilisateurs peuvent envoyer des tips au bot :

```python
async def on_tip(self, sender: User, receiver: User, tip: CurrencyItem):
    # Le bot reçoit le tip automatiquement
    # Converti en Earned Gold
    pass
```

### Méthode 2 : Transférer du gold (si possible)

Vérifier si l'API permet de transférer du gold d'un compte à un autre.

### Méthode 3 : Acheter du gold

Si le bot est sur ton compte, tu peux peut-être acheter du gold pour ce compte.

## 🔧 Prochaines étapes

### 1. Vérifier le wallet du bot

```
!admin wallet
```

### 2. Si le bot a du gold, acheter des items

```
!admin buyitem shirt-n_room32019denimjackethoodie
!admin buyitem pants-n_room32019rippedjeans
!admin buyitem shoes-n_room12019sneakers
```

### 3. Vérifier l'inventaire après achat

```
!admin inventory
```

### 4. Créer des outfits avec les nouveaux items

```python
self.outfits = {
    "casual": [
        Item(type="shirt", id="shirt-n_room32019denimjackethoodie"),
        Item(type="pants", id="pants-n_room32019rippedjeans"),
        Item(type="shoes", id="shoes-n_room12019sneakers"),
    ],
}
```

## ⚠️ Conclusion importante

**Les bots ont leur propre inventaire séparé !**

- ❌ Créer un bot sur ton compte ≠ Le bot a tes items
- ✅ Le bot commence avec 11 items de base
- ✅ Le bot doit acheter ses propres items avec du gold
- ✅ Le bot peut recevoir des tips pour obtenir du gold

## 🔗 Sources

- [Understanding Bot Outfits in Highrise](https://create.highrise.game/learn/bots/guides/change-bot-appearance)
- Documentation officielle Highrise Bot SDK

---

**Désolé pour la confusion ! Les bots ont leur propre inventaire, même s'ils sont créés sur ton compte. Le bot doit acheter ses propres items avec du gold. 💰**
