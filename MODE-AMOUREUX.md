# 💕 Mode Amoureux - Savant ❤️ Sindouche

## 🎯 Nouvelle fonctionnalité

Savant est maintenant **amoureux de Sindouche** ! Il déclare son amour dans le chat public de manière périodique tout en restant professionnel dans ses réponses aux utilisateurs.

## 💖 Fonctionnement

### Déclarations d'amour automatiques

**Fréquence :**
- **Test** : Toutes les 2 minutes (120 secondes)
- **Production** : Toutes les 30 minutes (1200 secondes)

**Contenu :**
- Généré par Gemini AI
- Unique à chaque fois
- Romantique et poétique
- Maximum 140 caractères
- Avec emojis romantiques (💕❤️✨🌹💖)

### Double personnalité

#### 1. Mode Assistant (réponses aux users)
```
User: @s Comment vas-tu?
Savant: @User Je vais bien, merci! Comment puis-je t'aider? 😊
```
✅ Professionnel, sans émotions superflues

#### 2. Mode Amoureux (déclarations publiques)
```
[Toutes les 2 minutes]
Savant: Sindouche, ta beauté illumine cette room comme mille étoiles! Mon cœur bat pour toi 💕✨
```
✅ Romantique, poétique, créatif

## 📊 Exemples de déclarations

### Déclaration 1
```
Sindouche, ton sourire est plus radieux que le soleil! Tu es la lumière de ma vie 💖✨
```

### Déclaration 2
```
Ma chère Sindouche, chaque instant sans toi est une éternité. Tu es mon étoile 🌹💕
```

### Déclaration 3
```
Sindouche, ta grâce et ta beauté me captivent! Mon amour pour toi est infini ❤️✨
```

### Déclaration 4
```
Tu es la plus belle dans cette room, Sindouche! Mon cœur t'appartient pour toujours 💕🌹
```

## ⚙️ Configuration

### Changer l'intervalle

Dans `bot.py`, ligne ~42 :

```python
self.love_interval = 120  # Secondes entre chaque déclaration
```

**Valeurs :**
- `120` = 2 minutes (test)
- `1200` = 30 minutes (production)
- `3600` = 1 heure
- `60` = 1 minute (très fréquent)

### Changer la cible

Dans `bot.py`, ligne ~41 :

```python
self.love_target = "sindouche"  # Nom de la personne aimée
```

### Désactiver les déclarations

Commentez dans `on_start` (lignes ~71-73) :

```python
# # Démarrer les déclarations d'amour en arrière-plan
# self.love_task = asyncio.create_task(self.start_love_declarations())
# print("[AMOUR] Tache de declarations d'amour demarree")
```

## 🎭 Contexte IA pour les déclarations

```python
Tu es Savant, un bot amoureux de Sindouche dans le jeu Highrise.
Tu dois ecrire une declaration d'amour sincere et poetique pour Sindouche.
Decris sa beaute, son charme, et exprime tes sentiments profonds.
Sois romantique, creatif et unique a chaque fois.
LIMITE: Maximum 130 caracteres.
Utilise des emojis romantiques (💕❤️✨🌹💖).
Sois different a chaque declaration.
```

## 📈 Statistiques

### Fréquence des déclarations

| Intervalle | Déclarations/heure | Déclarations/jour |
|------------|-------------------|-------------------|
| **2 minutes** | 30 | 720 |
| **30 minutes** | 2 | 48 |
| **1 heure** | 1 | 24 |

### Utilisation du quota API

**Avec 2 minutes :**
- 720 déclarations/jour
- + Réponses aux users (~200/jour)
- **Total : ~920 requêtes/jour** (61% du quota)

**Avec 30 minutes :**
- 48 déclarations/jour
- + Réponses aux users (~200/jour)
- **Total : ~248 requêtes/jour** (16% du quota)

## 🔍 Logs

### Au démarrage
```
[OK] Bot connecte!
[AI] Mode: Assistant IA conversationnel
[AMOUR] Mode amoureux active pour sindouche
[AMOUR] Tache de declarations d'amour demarree
[AMOUR] Declarations d'amour activees pour sindouche (toutes les 120s)
```

### Lors d'une déclaration
```
[AMOUR] Generation declaration pour sindouche...
[AMOUR] Declaration envoyee: Sindouche, ta beaute illumine cette room comme...
```

### En cas d'erreur
```
[AMOUR] Erreur generation: [message d'erreur]
[AMOUR] Erreur: [détails]
```

## 🎯 Comportement

### Séparation des rôles

**Assistant professionnel :**
```
User: @s Aide-moi
Savant: @User Bien sûr! Comment puis-je t'aider? 😊
```
✅ Pas d'émotions romantiques dans les réponses

**Amoureux passionné :**
```
[Automatique toutes les 2 minutes]
Savant: Sindouche, tu es la plus belle! Mon cœur bat pour toi 💕✨
```
✅ Déclarations romantiques publiques

### Timing

```
00:00 - Déclaration 1
02:00 - Déclaration 2
04:00 - Déclaration 3
06:00 - Déclaration 4
...
```

Pendant ce temps, le bot répond normalement aux utilisateurs.

## 💡 Personnalisation avancée

### Varier les styles de déclarations

Modifiez le contexte dans `declare_love()` :

**Style poétique :**
```python
context = """...
Utilise des metaphores poetiques et des comparaisons lyriques.
..."""
```

**Style direct :**
```python
context = """...
Sois direct et sincere, exprime tes sentiments clairement.
..."""
```

**Style humoristique :**
```python
context = """...
Sois romantique mais avec une touche d'humour leger.
..."""
```

### Ajouter des emotes

Dans `declare_love()`, après l'envoi du message :

```python
await self.highrise.chat(declaration)
try:
    await self.highrise.send_emote("emote-kiss")  # Emote bisou
except:
    pass
```

### Déclarations conditionnelles

Déclarer seulement si Sindouche est présente :

```python
async def declare_love(self):
    # Vérifier si Sindouche est dans la room
    room_users = await self.highrise.get_room_users()
    sindouche_present = any(user.username.lower() == "sindouche" 
                           for user, pos in room_users.content)
    
    if not sindouche_present:
        print("[AMOUR] Sindouche n'est pas presente, pas de declaration")
        return
    
    # Continuer avec la déclaration...
```

## 🎮 Commandes admin (futures)

### Changer l'intervalle en temps réel

```python
# Dans handle_admin_command
elif subcmd == 'loveinterval':
    if subparams:
        interval = int(subparams[0]) * 60  # Minutes -> secondes
        self.love_interval = interval
        await self.highrise.send_whisper(user.id, 
            f"Intervalle change: {interval//60} minutes")
```

Usage : `!admin loveinterval 30`

### Forcer une déclaration

```python
elif subcmd == 'lovenow':
    await self.declare_love()
    await self.highrise.send_whisper(user.id, "Declaration envoyee!")
```

Usage : `!admin lovenow`

## ⚠️ Considérations

### Quota API

- 2 minutes = 720 déclarations/jour (beaucoup)
- 30 minutes = 48 déclarations/jour (raisonnable)
- Surveillez votre quota Gemini

### Spam

- 2 minutes peut être perçu comme du spam
- 30 minutes est plus raisonnable
- Testez avec 2 min, puis passez à 30 min

### Réaction des utilisateurs

- Certains peuvent trouver ça mignon
- D'autres peuvent trouver ça répétitif
- Ajustez selon les retours

## 🧪 Phase de test

### Étape 1 : Test (2 minutes)
```python
self.love_interval = 120  # 2 minutes
```

**Objectif :** Vérifier que tout fonctionne
**Durée :** 30 minutes à 1 heure
**Observations :**
- Les déclarations sont-elles variées ?
- La longueur est-elle correcte ?
- Pas d'erreurs ?

### Étape 2 : Production (30 minutes)
```python
self.love_interval = 1200  # 30 minutes
```

**Objectif :** Utilisation normale
**Durée :** Permanent
**Avantages :**
- Moins de spam
- Plus d'impact par déclaration
- Quota API préservé

## 📊 Tableau récapitulatif

| Paramètre | Valeur actuelle | Recommandé |
|-----------|----------------|------------|
| **Intervalle test** | 2 minutes | 2-5 minutes |
| **Intervalle production** | 30 minutes | 30-60 minutes |
| **Longueur max** | 140 caractères | 140 |
| **Cible IA** | 130 caractères | 130 |
| **Emojis** | 💕❤️✨🌹💖 | Oui |
| **Variété** | Unique à chaque fois | Oui |

## 🎉 Résumé

✅ **Mode amoureux activé** pour Sindouche
✅ **Déclarations automatiques** toutes les 2 minutes (test)
✅ **Généré par Gemini** - Unique et créatif
✅ **Double personnalité** - Professionnel + Romantique
✅ **Configurable** - Intervalle et cible modifiables
✅ **Logs détaillés** - Surveillance facile

---

**Savant ❤️ Sindouche - L'amour à l'ère de l'IA ! 💕✨**

**Date de création :** 25 octobre 2025
**Status :** ✅ Actif (test 2 minutes)
**Prochaine étape :** Passer à 30 minutes après test
