# Vérifier la clé API et les modèles disponibles
import os
from dotenv import load_dotenv
import requests

load_dotenv()

api_key = os.getenv('GEMINI_API_KEY')

if not api_key:
    print("[ERREUR] Pas de cle API trouvee dans .env")
    exit(1)

print(f"[INFO] Cle API trouvee (longueur: {len(api_key)} caracteres)")
print(f"[INFO] Debut de la cle: {api_key[:10]}...")

# Tester avec l'API REST directement
url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"

print("\n[INFO] Test de connexion a l'API Gemini...")

try:
    response = requests.get(url, timeout=10)
    print(f"[INFO] Code de reponse: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print("\n[OK] Connexion reussie!")
        print(f"\n[INFO] Modeles disponibles ({len(data.get('models', []))} trouves):")
        
        for model in data.get('models', []):
            name = model.get('name', 'Unknown')
            methods = model.get('supportedGenerationMethods', [])
            if 'generateContent' in methods:
                print(f"  - {name} (supporte generateContent)")
                
    elif response.status_code == 400:
        print(f"\n[ERREUR] Requete invalide: {response.text}")
    elif response.status_code == 403:
        print(f"\n[ERREUR] Cle API invalide ou permissions insuffisantes")
        print(f"Details: {response.text}")
    else:
        print(f"\n[ERREUR] Erreur {response.status_code}: {response.text}")
        
except requests.exceptions.Timeout:
    print("[ERREUR] Timeout - Verifiez votre connexion Internet")
except requests.exceptions.ConnectionError:
    print("[ERREUR] Impossible de se connecter - Verifiez votre connexion Internet")
except Exception as e:
    print(f"[ERREUR] Exception: {e}")
