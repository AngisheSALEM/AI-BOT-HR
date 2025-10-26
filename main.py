#!/usr/bin/env python3
"""
Point d'entrée pour Replit
Lance le bot Highrise avec les credentials depuis les Secrets
"""

import os
import sys
from bot import start_health_server

def main():
    print("=" * 60)
    print("🤖 Bot Highrise Savant - Démarrage sur Replit")
    print("=" * 60)
    
    # Démarrer le serveur de santé (pour garder le bot actif)
    start_health_server()
    
    # Récupérer les credentials depuis les Secrets Replit
    room_id = os.getenv('ROOM_ID')
    bot_token = os.getenv('BOT_TOKEN')
    
    if not room_id or not bot_token:
        print("❌ ERREUR: ROOM_ID et BOT_TOKEN doivent être définis dans les Secrets!")
        print("👉 Allez dans l'onglet 'Secrets' (icône cadenas) et ajoutez:")
        print("   - ROOM_ID: votre room ID")
        print("   - BOT_TOKEN: votre token bot")
        sys.exit(1)
    
    print(f"✅ Room ID: {room_id}")
    print(f"✅ Token: {bot_token[:20]}...")
    print("=" * 60)
    print("🚀 Connexion au serveur Highrise...")
    print("=" * 60)
    
    # Lancer le bot
    from highrise.__main__ import main as highrise_main
    sys.argv = ['highrise', 'bot:HighriseBot', room_id, bot_token]
    highrise_main()

if __name__ == "__main__":
    main()
