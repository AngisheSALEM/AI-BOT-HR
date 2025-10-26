# 👔 Étapes simples pour créer des outfits

## 🎯 Ce que tu dois faire

### Étape 1 : Lance ton bot
```
python -m highrise bot:HighriseBot ROOM_ID TOKEN
```

### Étape 2 : Regarde ton inventaire
Envoie en DM au bot :
```
!admin inventory
```

Tu vas recevoir une liste comme ça :
```
=== SHIRT ===
1. shirt-n_starteritems2019malet_shirt
2. shirt-n_room32019denimjackethoodie
3. shirt-n_room12019blackhoodie

=== PANTS ===
1. pants-n_starteritems2019malepants
2. pants-n_room32019rippedjeans

=== SHOES ===
1. shoes-n_starteritems2019maleshoes
2. shoes-n_room12019sneakers

Total: 25 items
```

### Étape 3 : Note les IDs que tu veux utiliser

Par exemple pour un outfit casual :
- **Haut** : `shirt-n_starteritems2019malet_shirt`
- **Bas** : `pants-n_starteritems2019malepants`
- **Chaussures** : `shoes-n_starteritems2019maleshoes`

### Étape 4 : Modifie bot.py

Trouve cette section (ligne ~36) :
```python
# Outfits pour rotation automatique (remplace par tes vrais IDs)
self.outfits = {
    "casual": [],  # À remplir après avoir récupéré l'inventaire
    "elegant": [],
    "sport": [],
    "night": []
}
```

Remplace par (avec TES IDs) :
```python
# Outfits pour rotation automatique
self.outfits = {
    "casual": [
        Item(type="shirt", id="shirt-n_starteritems2019malet_shirt"),
        Item(type="pants", id="pants-n_starteritems2019malepants"),
        Item(type="shoes", id="shoes-n_starteritems2019maleshoes"),
    ],
    "elegant": [
        Item(type="shirt", id="TON_ID_SHIRT_ELEGANT"),
        Item(type="pants", id="TON_ID_PANTS_ELEGANT"),
        Item(type="shoes", id="TON_ID_SHOES_ELEGANT"),
    ],
    "sport": [
        Item(type="shirt", id="TON_ID_SHIRT_SPORT"),
        Item(type="pants", id="TON_ID_PANTS_SPORT"),
        Item(type="shoes", id="TON_ID_SHOES_SPORT"),
    ],
    "night": [
        Item(type="shirt", id="TON_ID_SHIRT_NIGHT"),
        Item(type="pants", id="TON_ID_PANTS_NIGHT"),
        Item(type="shoes", id="TON_ID_SHOES_NIGHT"),
    ]
}
```

### Étape 5 : Active la rotation 6h

Dans `on_start` (ligne ~58), ajoute après le message de bienvenue :

```python
async def on_start(self, session_metadata: SessionMetadata) -> None:
    print("[OK] Bot connecte!")
    print(f"[ID] Bot ID: {session_metadata.user_id}")
    print(f"[EMOTES] {get_emote_count()} emotes disponibles")
    print(f"[AI] Mode: Assistant IA conversationnel")
    
    try:
        await self.highrise.chat("🤖 Assistant IA Gemini en ligne! 💬")
        print("[OK] Message de bienvenue envoye")
    except Exception as e:
        print(f"[ERREUR] {e}")
    
    # AJOUTE CES 2 LIGNES :
    asyncio.create_task(self.outfit_rotation_6h())
    print("[OUTFIT] Rotation 6h demarree")
```

### Étape 6 : Teste !

Relance le bot et teste :
```
!admin testoutfit casual
```

Le bot va changer de tenue !

## 📝 Format d'un item

```python
Item(type="CATEGORIE", id="ID_EXACT")
```

### Catégories :
- `shirt` = Haut (t-shirt, chemise, veste)
- `pants` = Bas (pantalon, short)
- `shoes` = Chaussures
- `hair` = Cheveux
- `glasses` = Lunettes
- `hat` = Chapeau

## 🎯 Commandes disponibles

| Commande | Description |
|----------|-------------|
| `!admin inventory` | Voir tous les items du bot |
| `!admin testoutfit casual` | Tester l'outfit "casual" |
| `!admin testoutfit elegant` | Tester l'outfit "elegant" |
| `!admin testoutfit` | Voir les outfits disponibles |
| `!admin currentoutfit` | Voir l'outfit actuel |

## ⏱️ Rotation automatique

Une fois configuré, le bot va automatiquement changer d'outfit toutes les **6 heures** :
- 00h00 → casual
- 06h00 → elegant
- 12h00 → sport
- 18h00 → night
- 00h00 → casual (recommence)

## ⚠️ Important

- Les IDs doivent être **exacts** (copie-colle depuis `!admin inventory`)
- Le bot doit **posséder** les items dans son inventaire
- Les **déclarations d'amour** continuent normalement, pas de conflit ! 💕

## 🎉 Résumé rapide

1. `!admin inventory` → Note les IDs
2. Modifie `bot.py` ligne ~36 avec tes IDs
3. Ajoute la rotation dans `on_start` ligne ~58
4. Relance le bot
5. Teste avec `!admin testoutfit casual`
6. Profite de la rotation automatique ! 🎨

---

**Les déclarations d'amour ne sont PAS touchées ! 💕**
