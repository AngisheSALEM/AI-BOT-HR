# 📊 Limites de l'API Gemini

## 🎯 Quotas gratuits (Free Tier)

### Gemini 1.5 Flash / 2.0 Flash

| Limite | Quota gratuit | Notes |
|--------|---------------|-------|
| **Requêtes par minute (RPM)** | 15 | 15 messages par minute |
| **Requêtes par jour (RPD)** | 1,500 | 1,500 messages par jour |
| **Tokens par minute (TPM)** | 1,000,000 | ~750,000 mots/minute |
| **Tokens par jour (TPD)** | Illimité | Pas de limite journalière |

### Gemini 1.5 Pro / 2.0 Pro

| Limite | Quota gratuit | Notes |
|--------|---------------|-------|
| **Requêtes par minute (RPM)** | 2 | Seulement 2 par minute |
| **Requêtes par jour (RPD)** | 50 | 50 messages par jour |
| **Tokens par minute (TPM)** | 32,000 | ~24,000 mots/minute |

## 🤖 Votre bot utilise : **Gemini 2.5 Flash**

Vérifiez dans `gemini_integration.py` :
```python
self.model = genai.GenerativeModel('models/gemini-2.5-flash')
```

### Limites applicables

✅ **15 requêtes par minute**
✅ **1,500 requêtes par jour**
✅ **1,000,000 tokens par minute**

## 📊 Calcul pour votre bot

### Scénario 1 : Utilisation modérée

**Hypothèse :**
- 5 utilisateurs actifs
- Chacun envoie 10 messages par heure
- Total : 50 messages/heure

**Calcul :**
- Par heure : 50 messages ✅ (bien en dessous de 15/min)
- Par jour : 1,200 messages ✅ (sous la limite de 1,500)

**Verdict :** ✅ Aucun problème

### Scénario 2 : Utilisation intensive

**Hypothèse :**
- 20 utilisateurs actifs
- Chacun envoie 20 messages par heure
- Total : 400 messages/heure

**Calcul :**
- Par heure : 400 messages ≈ 6.7 messages/min ✅
- Par jour : 9,600 messages ❌ (dépasse 1,500)

**Verdict :** ⚠️ Dépassement du quota journalier

### Scénario 3 : Pic d'activité

**Hypothèse :**
- 10 utilisateurs envoient des messages en même temps
- 1 message par seconde pendant 1 minute

**Calcul :**
- Par minute : 60 messages ❌ (dépasse 15/min)

**Verdict :** ❌ Rate limiting activé

## ⚠️ Que se passe-t-il si vous dépassez ?

### Dépassement RPM (15/minute)

**Erreur :**
```
google.api_core.exceptions.ResourceExhausted: 429 Quota exceeded
```

**Comportement actuel du bot :**
```python
except Exception as e:
    print(f"[AI] Erreur: {e}")
    error_msg = "Desolé, j'ai eu un probleme pour generer une reponse."
    await self.highrise.send_whisper(user.id, error_msg)
```

**Solution déjà implémentée :**
- Délai de 2 secondes entre requêtes par utilisateur ✅
- Maximum théorique : 30 requêtes/minute (si 30 utilisateurs différents)

### Dépassement RPD (1,500/jour)

**Erreur :**
```
google.api_core.exceptions.ResourceExhausted: 429 Daily quota exceeded
```

**Comportement :**
- Le bot ne pourra plus répondre jusqu'au lendemain
- Message d'erreur envoyé aux utilisateurs

**Solution :** Surveiller l'utilisation quotidienne

## 📈 Surveillance de votre quota

### Vérifier votre utilisation

1. Allez sur [Google AI Studio](https://makersuite.google.com/)
2. Cliquez sur votre projet
3. Allez dans "Quota & System limits"
4. Vous verrez :
   - Requêtes utilisées aujourd'hui
   - Requêtes restantes
   - Graphiques d'utilisation

### Créer un compteur dans le bot

Je peux ajouter un système de comptage si vous voulez :

```python
# Dans __init__
self.daily_requests = 0
self.last_reset = datetime.now().date()

# Dans respond_with_ai
if datetime.now().date() > self.last_reset:
    self.daily_requests = 0
    self.last_reset = datetime.now().date()

self.daily_requests += 1
print(f"[QUOTA] Requetes aujourd'hui: {self.daily_requests}/1500")

if self.daily_requests > 1400:
    print(f"[QUOTA] ⚠️ Attention: {1500 - self.daily_requests} requetes restantes!")
```

## 💡 Solutions pour augmenter les limites

### Option 1 : Passer au plan payant

**Gemini API Paid Tier :**
- **RPM :** 1,000 (au lieu de 15)
- **RPD :** 10,000+ (au lieu de 1,500)
- **Prix :** ~$0.00025 par 1K tokens (très peu cher)

**Coût estimé :**
- 1,000 messages/jour ≈ $0.25/jour
- 10,000 messages/jour ≈ $2.50/jour

### Option 2 : Optimiser l'utilisation

**Déjà fait :**
- ✅ Délai de 2 secondes entre requêtes
- ✅ Réponses courtes (moins de tokens)
- ✅ Pas de répétition inutile

**À ajouter :**
- Cache des réponses fréquentes
- Limite par utilisateur (ex: 10 messages/heure)
- File d'attente si trop de requêtes

### Option 3 : Utiliser plusieurs clés API

Créer plusieurs projets Google AI avec différentes clés :
- Clé 1 : 1,500 requêtes/jour
- Clé 2 : 1,500 requêtes/jour
- Total : 3,000 requêtes/jour

**Rotation automatique des clés**

## 🛡️ Protection contre le dépassement

### Solution 1 : Limite par utilisateur

```python
# Dans __init__
self.user_daily_limit = {}  # user_id: count

# Dans respond_with_ai
user_count = self.user_daily_limit.get(user.id, 0)
if user_count >= 20:  # Max 20 messages/jour par user
    await self.highrise.send_whisper(user.id, 
        "Tu as atteint ta limite quotidienne. Reviens demain! 😊")
    return

self.user_daily_limit[user.id] = user_count + 1
```

### Solution 2 : File d'attente

```python
# Si trop de requêtes en attente
if len(self.request_queue) > 10:
    await self.highrise.send_whisper(user.id,
        "Je suis occupé, réessaie dans quelques secondes! ⏳")
    return
```

### Solution 3 : Mode dégradé

```python
# Si quota presque atteint
if self.daily_requests > 1400:
    # Répondre seulement aux DM, pas au chat public
    if not is_whisper:
        return
```

## 📊 Estimation pour votre cas

### Utilisation actuelle estimée

**Hypothèse réaliste :**
- 10 utilisateurs actifs par jour
- Chacun envoie 15 messages
- Total : 150 messages/jour

**Résultat :**
- 150/1,500 = **10% du quota** ✅
- Largement suffisant !

### Seuil d'alerte

⚠️ **Surveillez si :**
- Plus de 50 utilisateurs actifs/jour
- Plus de 1,000 messages/jour
- Pics de plus de 10 messages/minute

## 🔍 Vérifier votre quota actuel

### Méthode 1 : Google AI Studio

1. [https://makersuite.google.com/](https://makersuite.google.com/)
2. Connectez-vous
3. Cliquez sur "API Keys"
4. Sélectionnez votre clé
5. Voyez l'utilisation

### Méthode 2 : Via l'API

```python
# Ajouter dans gemini_integration.py
def get_quota_info(self):
    """Afficher les informations de quota"""
    # Note: L'API Gemini ne fournit pas directement les quotas
    # Il faut surveiller via Google Cloud Console
    print("[QUOTA] Consultez https://makersuite.google.com/ pour voir votre quota")
```

## 📝 Recommandations

### Pour votre bot actuel

✅ **Pas de changement nécessaire** si :
- Moins de 30 utilisateurs actifs/jour
- Moins de 500 messages/jour
- Utilisation normale

⚠️ **Ajouter un compteur** si :
- Plus de 50 utilisateurs actifs/jour
- Plus de 1,000 messages/jour
- Vous voulez surveiller l'utilisation

❌ **Passer au plan payant** si :
- Plus de 100 utilisateurs actifs/jour
- Plus de 1,500 messages/jour
- Utilisation intensive

### Implémentation recommandée

**Niveau 1 : Compteur simple**
```python
# Afficher le nombre de requêtes
print(f"[QUOTA] Requete #{self.daily_requests}")
```

**Niveau 2 : Alerte**
```python
# Alerter si proche de la limite
if self.daily_requests > 1400:
    print(f"[QUOTA] ⚠️ ALERTE: {1500 - self.daily_requests} requetes restantes!")
```

**Niveau 3 : Protection**
```python
# Bloquer si limite atteinte
if self.daily_requests >= 1500:
    await self.highrise.chat("⚠️ Quota journalier atteint. Réessayez demain!")
    return
```

## 🎯 Résumé

| Aspect | Votre situation |
|--------|-----------------|
| **Quota gratuit** | 1,500 requêtes/jour |
| **Utilisation estimée** | 150-500 requêtes/jour |
| **Marge** | ✅ Large (70-90%) |
| **Risque de dépassement** | ❌ Faible |
| **Action requise** | ✅ Aucune pour l'instant |
| **Surveillance** | ⚠️ Recommandée |

## 🔗 Liens utiles

- [Google AI Studio](https://makersuite.google.com/) - Voir votre quota
- [Gemini API Pricing](https://ai.google.dev/pricing) - Tarifs officiels
- [Quota Limits](https://ai.google.dev/gemini-api/docs/quota) - Documentation

---

**Conclusion :** Avec votre utilisation actuelle, vous êtes **largement en dessous des limites** ! 🎉

Voulez-vous que j'ajoute un **système de comptage** pour surveiller votre utilisation ?
