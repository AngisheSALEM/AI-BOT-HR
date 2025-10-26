# ⏱️ Changer l'intervalle des déclarations d'amour

## 🎯 Guide rapide

### Passer de 2 minutes à 30 minutes

**Étape 1 : Ouvrir bot.py**

**Étape 2 : Trouver la ligne 42**
```python
self.love_interval = 120  # 2 minutes (120 secondes) pour test, puis 1200 pour 30 min
```

**Étape 3 : Changer la valeur**
```python
self.love_interval = 1200  # 30 minutes
```

**Étape 4 : Sauvegarder et relancer le bot**

## 📊 Valeurs courantes

| Intervalle | Secondes | Code |
|------------|----------|------|
| **1 minute** | 60 | `self.love_interval = 60` |
| **2 minutes** | 120 | `self.love_interval = 120` |
| **5 minutes** | 300 | `self.love_interval = 300` |
| **10 minutes** | 600 | `self.love_interval = 600` |
| **15 minutes** | 900 | `self.love_interval = 900` |
| **30 minutes** | 1200 | `self.love_interval = 1200` |
| **1 heure** | 3600 | `self.love_interval = 3600` |

## 🧪 Recommandations

### Phase de test (maintenant)
```python
self.love_interval = 120  # 2 minutes
```
✅ Tester pendant 30 minutes à 1 heure
✅ Vérifier que les déclarations sont variées
✅ Vérifier qu'il n'y a pas d'erreurs

### Phase de production (après test)
```python
self.love_interval = 1200  # 30 minutes
```
✅ Moins de spam
✅ Plus d'impact
✅ Quota API préservé

## 💡 Calcul personnalisé

**Formule :**
```
Secondes = Minutes × 60
```

**Exemples :**
- 20 minutes = 20 × 60 = 1200 secondes
- 45 minutes = 45 × 60 = 900 secondes
- 2 heures = 120 × 60 = 7200 secondes

## 🔄 Relancer le bot après modification

### Méthode 1 : Via terminal
```bash
# Arrêter le bot actuel
Ctrl+C

# Relancer
python -m highrise bot:HighriseBot 680ab18546b31625a94de2e6 057565bd7bda6ac37029f5817ea7c2f6d447179cdfa65771e41284ed5f5d6090
```

### Méthode 2 : Via START.bat
Double-cliquez sur `START.bat`

## ✅ Vérification

Après relancement, vous devriez voir :
```
[AMOUR] Mode amoureux active pour sindouche
[AMOUR] Tache de declarations d'amour demarree
[AMOUR] Declarations d'amour activees pour sindouche (toutes les 1200s)
```

Le nombre de secondes doit correspondre à votre nouvelle valeur !

---

**Conseil :** Commencez avec 2 minutes pour tester, puis passez à 30 minutes pour l'utilisation normale ! 💕
