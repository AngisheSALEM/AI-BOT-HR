# 🤖 Guide d'intégration Gemini AI

## 📋 Vue d'ensemble

Votre bot Highrise est maintenant équipé de l'intelligence artificielle **Gemini** de Google ! Le bot peut maintenant répondre à des questions, discuter naturellement, raconter des blagues, donner des conseils et bien plus encore.

---

## 🔧 Configuration

### 1. Obtenir une clé API Gemini

1. Visitez [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Connectez-vous avec votre compte Google
3. Cliquez sur **"Create API Key"**
4. Copiez la clé générée (elle ressemble à : `AIzaSy...`)

### 2. Configurer le bot

1. Ouvrez le fichier `.env` dans le dossier du bot
2. Ajoutez cette ligne à la fin :
   ```
   GEMINI_API_KEY=votre_cle_api_ici
   ```
3. Remplacez `votre_cle_api_ici` par votre vraie clé API

**Exemple complet du fichier .env :**
```env
BOT_TOKEN=057565bd7bda6ac37029f5817ea7c2f6d447179cdfa65771e41284ed5f5d6090
ROOM_ID=680ab18546b31625a94de2e6
ADMIN_IDS=votre_id_admin
GEMINI_API_KEY=AIzaSyABC123XYZ789_votre_vraie_cle
```

### 3. Installer les dépendances

Ouvrez PowerShell dans le dossier du bot et exécutez :
```powershell
pip install -r requirements.txt
```

---

## 🎮 Commandes disponibles

**🔒 Toutes les réponses de Gemini sont envoyées en message privé (whisper) pour plus de confidentialité !**

### 🤔 **!ask** - Poser une question
Posez n'importe quelle question à Gemini AI. La réponse sera envoyée en privé.

**Exemples :**
```
!ask Quelle est la capitale de la France?
!ask Comment fonctionne l'intelligence artificielle?
!ask Qu'est-ce que Highrise?
```

---

### 💬 **!ai** - Discussion naturelle
Discutez naturellement avec l'IA comme avec un ami. Réponse en privé.

**Exemples :**
```
!ai Salut, comment vas-tu?
!ai Raconte-moi quelque chose d'intéressant
!ai Que penses-tu de ce jeu?
```

---

### 😂 **!joke** - Blague aléatoire
Demandez à Gemini de raconter une blague.

**Exemple :**
```
!joke
```

**Réponse possible :**
> 😂 Pourquoi les plongeurs plongent-ils toujours en arrière ? Parce que sinon ils tombent dans le bateau !

---

### 💡 **!fact** - Fait intéressant
Obtenez un fait intéressant et surprenant.

**Exemple :**
```
!fact
```

**Réponse possible :**
> 💡 Les pieuvres ont trois cœurs et leur sang est bleu !

---

### ✨ **!advice** - Conseil motivant
Recevez un conseil positif sur un sujet.

**Exemples :**
```
!advice
!advice amitié
!advice motivation
!advice gaming
```

**Réponse possible :**
> ✨ N'oublie jamais : chaque petit pas compte. La persévérance est la clé du succès !

---

### 🌍 **!translate** - Traduction
Traduisez un texte dans une autre langue.

**Format :** `!translate <langue> <texte>`

**Exemples :**
```
!translate en Bonjour tout le monde
!translate es Comment allez-vous?
!translate de Je suis heureux
```

**Langues supportées :**
- `en` = Anglais
- `fr` = Français
- `es` = Espagnol
- `de` = Allemand
- `it` = Italien

---

## 📊 Caractéristiques techniques

### Limitations
- **Longueur des réponses :** Les réponses sont limitées à 200 caractères pour s'adapter au chat Highrise
- **Temps de réponse :** 1-3 secondes selon la complexité de la question
- **Quota API :** Vérifiez les limites de votre clé API sur Google AI Studio

### Gestion des erreurs
Si Gemini n'est pas configuré, le bot affichera :
```
❌ Gemini AI non configuré. Ajoutez GEMINI_API_KEY dans .env
```

### Logs
Les interactions avec Gemini sont loguées dans la console :
```
[GEMINI] ✓ API Gemini configurée avec succès
[GEMINI] Erreur: <détails de l'erreur>
```

---

## 🎯 Cas d'usage

### 1. Bot éducatif
```
!ask Explique-moi la photosynthèse
!ask Qui a inventé l'ordinateur?
```

### 2. Divertissement
```
!joke
!fact
!ai Raconte-moi une histoire courte
```

### 3. Assistant personnel
```
!advice stress
!translate en Je t'aime
!ask Quel temps fait-il à Paris?
```

### 4. Modération intelligente
```
!ask Comment gérer un conflit dans une communauté?
!advice leadership
```

---

## 🔒 Sécurité

### Protection de la clé API
- ✅ La clé est stockée dans `.env` (ignoré par Git)
- ✅ Ne partagez JAMAIS votre clé API publiquement
- ✅ Régénérez votre clé si elle est compromise

### Bonnes pratiques
1. Utilisez une clé API dédiée pour chaque bot
2. Surveillez votre usage sur Google AI Studio
3. Définissez des quotas pour éviter les abus

---

## 🐛 Dépannage

### Problème : "Gemini AI non configuré"
**Solution :** Vérifiez que `GEMINI_API_KEY` est bien dans `.env`

### Problème : "Erreur IA"
**Solutions possibles :**
1. Vérifiez votre connexion Internet
2. Vérifiez que votre clé API est valide
3. Vérifiez les quotas de votre API sur Google AI Studio

### Problème : Réponses tronquées
**Explication :** Les réponses sont limitées à 200 caractères pour le chat Highrise. C'est normal !

### Problème : Temps de réponse lent
**Solutions :**
1. Vérifiez votre connexion Internet
2. Simplifiez vos questions
3. Les questions complexes prennent plus de temps

---

## 📝 Architecture technique

### Fichiers créés
- `gemini_integration.py` - Module d'intégration Gemini
- `GUIDE-GEMINI.md` - Ce guide

### Fichiers modifiés
- `bot.py` - Ajout des commandes Gemini
- `requirements.txt` - Ajout de `google-generativeai`
- `.env.example` - Ajout de `GEMINI_API_KEY`

### Dépendances ajoutées
```
google-generativeai==0.3.2
```

---

## 🚀 Prochaines étapes

### Idées d'amélioration
1. **Historique de conversation** - Mémoriser le contexte des discussions
2. **Personnalisation** - Ajuster le ton et le style des réponses
3. **Modération automatique** - Détecter les messages inappropriés
4. **Génération d'images** - Intégrer Gemini Vision
5. **Commandes personnalisées** - Créer vos propres commandes IA

### Ressources utiles
- [Documentation Gemini](https://ai.google.dev/docs)
- [Google AI Studio](https://makersuite.google.com/)
- [Highrise Bot SDK](https://create.highrise.game/learn/guides/bots)

---

## 💬 Support

Si vous rencontrez des problèmes :
1. Vérifiez ce guide
2. Consultez les logs dans la console
3. Vérifiez votre configuration `.env`
4. Testez votre clé API sur Google AI Studio

---

## ✅ Checklist de démarrage

- [ ] Obtenir une clé API Gemini
- [ ] Ajouter `GEMINI_API_KEY` dans `.env`
- [ ] Installer les dépendances (`pip install -r requirements.txt`)
- [ ] Lancer le bot (`START.bat`)
- [ ] Tester avec `!joke` ou `!fact`
- [ ] Tester avec `!ask Bonjour!`

---

**🎉 Félicitations ! Votre bot est maintenant équipé de l'IA Gemini !**
