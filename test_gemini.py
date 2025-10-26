# Test rapide de l'intégration Gemini
import asyncio
from dotenv import load_dotenv

# Charger .env AVANT d'initialiser Gemini
load_dotenv()

from gemini_integration import initialize_gemini

# Initialiser Gemini
gemini_assistant = initialize_gemini()

async def test_gemini():
    print("=" * 50)
    print("TEST DE L'INTEGRATION GEMINI")
    print("=" * 50)
    
    if gemini_assistant.is_configured:
        print("\n[OK] Gemini est configure!")
        print("\nTest 1: Poser une question simple...")
        try:
            response = await gemini_assistant.ask("Dis bonjour en une phrase")
            print(f"Reponse: {response[:100]}...")
            print("\n[OK] Test reussi!")
        except Exception as e:
            print(f"\n[ERREUR] {e}")
    else:
        print("\n[ATTENTION] Gemini n'est pas configure.")
        print("Ajoutez GEMINI_API_KEY dans le fichier .env")
    
    print("\n" + "=" * 50)

if __name__ == "__main__":
    asyncio.run(test_gemini())
