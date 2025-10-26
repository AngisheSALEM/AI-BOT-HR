# Test de chargement de Gemini dans le contexte du bot
import os
from dotenv import load_dotenv

print("=" * 50)
print("TEST CHARGEMENT GEMINI DANS BOT")
print("=" * 50)

# Charger .env
load_dotenv()
print("\n[1] .env charge")

# Importer gemini_integration
try:
    from gemini_integration import initialize_gemini
    print("[2] Module gemini_integration importe")
except Exception as e:
    print(f"[ERREUR] Import gemini_integration: {e}")
    exit(1)

# Initialiser Gemini
try:
    gemini_assistant = initialize_gemini()
    print("[3] Gemini initialise")
except Exception as e:
    print(f"[ERREUR] Initialisation Gemini: {e}")
    exit(1)

# Vérifier la configuration
if gemini_assistant and gemini_assistant.is_configured:
    print("[4] Gemini est configure!")
else:
    print("[ERREUR] Gemini n'est pas configure")
    exit(1)

# Test de génération
import asyncio

async def test_generation():
    try:
        print("\n[5] Test de generation...")
        response = await gemini_assistant.ask("Dis bonjour en une phrase")
        print(f"[OK] Reponse: {response[:100]}")
        return True
    except Exception as e:
        print(f"[ERREUR] Generation: {e}")
        import traceback
        traceback.print_exc()
        return False

result = asyncio.run(test_generation())

if result:
    print("\n" + "=" * 50)
    print("TOUT FONCTIONNE!")
    print("=" * 50)
else:
    print("\n" + "=" * 50)
    print("PROBLEME DETECTE")
    print("=" * 50)
