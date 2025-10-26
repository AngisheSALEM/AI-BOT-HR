# 📝 Changelog - Gemini AI Integration

## Version 1.1 - Messages Privés (24 Oct 2025)

### ✨ Nouveauté
- **Toutes les réponses de Gemini sont maintenant envoyées en message privé (whisper)**
- Les conversations avec l'IA sont maintenant confidentielles et ne polluent plus le chat public

### 🔄 Modifications
- `cmd_ask()` : Réponses en whisper
- `cmd_ai()` : Réponses en whisper
- `cmd_joke()` : Réponses en whisper
- `cmd_fact()` : Réponses en whisper
- `cmd_advice()` : Réponses en whisper
- `cmd_translate()` : Réponses en whisper

### 📋 Comportement
**Avant :**
```
User: !ask Quelle est la capitale de la France?
Bot (chat public): 🤔 Question: Quelle est la capitale de la France?...
Bot (chat public): 🤖 La capitale de la France est Paris.
```

**Maintenant :**
```
User: !ask Quelle est la capitale de la France?
Bot (whisper privé à User): 🤔 Question: Quelle est la capitale de la France?...
Bot (whisper privé à User): 🤖 La capitale de la France est Paris.
```

### ✅ Avantages
1. **Confidentialité** : Les conversations avec l'IA restent privées
2. **Moins de spam** : Le chat public n'est pas pollué par les réponses IA
3. **Meilleure expérience** : Chaque utilisateur reçoit ses réponses personnellement
4. **Multi-utilisateurs** : Plusieurs personnes peuvent utiliser l'IA en même temps sans confusion

### 🎯 Utilisation
Utilisez les commandes normalement dans le chat public :
```
!ask Bonjour!
!ai Comment vas-tu?
!joke
!fact
```

Le bot vous répondra automatiquement en message privé ! 💬

---

## Version 1.0 - Intégration Initiale (24 Oct 2025)

### ✨ Fonctionnalités initiales
- Intégration de l'API Gemini de Google
- 6 commandes IA disponibles
- Module `gemini_integration.py`
- Documentation complète
- Support de la traduction multilingue

### 📦 Fichiers créés
- `gemini_integration.py`
- `GUIDE-GEMINI.md`
- `INSTALLATION-GEMINI.md`

### 🔧 Configuration
- Ajout de `GEMINI_API_KEY` dans `.env`
- Dépendance `google-generativeai==0.3.2`
