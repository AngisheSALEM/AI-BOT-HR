# 🚀 Installation rapide de Gemini AI

## ⚡ Installation en 3 étapes

### Étape 1 : Installer les dépendances
Ouvrez PowerShell dans le dossier du bot et exécutez :
```powershell
pip install -r requirements.txt
```

### Étape 2 : Obtenir votre clé API
1. Allez sur https://makersuite.google.com/app/apikey
2. Connectez-vous avec votre compte Google
3. Cliquez sur "Create API Key"
4. Copiez la clé (commence par `AIzaSy...`)

### Étape 3 : Configurer le bot
1. Ouvrez le fichier `.env`
2. Ajoutez cette ligne :
   ```
   GEMINI_API_KEY=votre_cle_api_ici
   ```
3. Remplacez `votre_cle_api_ici` par votre vraie clé

## ✅ Test rapide

Lancez le bot avec `START.bat` puis testez dans Highrise :
```
!joke
!fact
!ask Bonjour!
```

Si ça fonctionne, vous verrez des réponses de l'IA ! 🎉

## 📚 Documentation complète

Consultez **GUIDE-GEMINI.md** pour :
- Toutes les commandes disponibles
- Exemples d'utilisation
- Dépannage
- Cas d'usage avancés

## 🆘 Problème ?

**Erreur "Gemini AI non configuré" ?**
→ Vérifiez que `GEMINI_API_KEY` est bien dans `.env`

**Erreur "Erreur IA" ?**
→ Vérifiez votre connexion Internet et votre clé API

**Besoin d'aide ?**
→ Consultez la section "Dépannage" dans GUIDE-GEMINI.md
