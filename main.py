#!/usr/bin/env python3
"""
Point d'entrée pour Replit
Lance le bot Highrise avec les credentials depuis les Secrets
"""

import os
import sys
import socket
from bot import start_health_server

def get_replit_url():
    """Génère l'URL publique du Repl"""
    repl_slug = os.getenv('REPL_SLUG', 'ai-bot-hr')
    repl_owner = os.getenv('REPL_OWNER', 'salembalagizi9')
    
    # Replit génère automatiquement l'URL
    url = f"https://{repl_slug}.{repl_owner}.repl.co"
    return url

def main():
    print("=" * 60)
    print("🤖 Bot Highrise Savant - Démarrage sur Replit")
    print("=" * 60)
    
    # Démarrer le serveur de santé (pour garder le bot actif)
    start_health_server()
    
    # Afficher l'URL publique
    public_url = get_replit_url()
    print(f"🌐 URL publique: {public_url}")
    print(f"📋 Copiez cette URL dans UptimeRobot!")
    print("=" * 60)
    
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
    print(f"✅ Token: {bot_token[:20]}... (longueur: {len(bot_token)} caractères)")
    print("=" * 60)
    print("🚀 Connexion au serveur Highrise...")
    print("=" * 60)
    
    # Lancer le bot avec aiohttp
    from bot import HighriseBot
    from highrise import __main__ as hr_main
    import aiohttp
    
    # Lancer le bot
    try:
        # Utiliser la méthode officielle du SDK
        hr_main.main(HighriseBot, room_id, bot_token)
    except Exception as e:
        print(f"❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()