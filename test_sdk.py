# Test des méthodes disponibles dans le SDK
from highrise import BaseBot
import inspect

class TestBot(BaseBot):
    async def on_start(self, session_metadata):
        print("=== METHODES DISPONIBLES DANS self.highrise ===")
        methods = [m for m in dir(self.highrise) if not m.startswith('_')]
        for method in sorted(methods):
            attr = getattr(self.highrise, method)
            if callable(attr):
                sig = str(inspect.signature(attr)) if hasattr(inspect, 'signature') else ''
                print(f"  {method}{sig}")
        
        print("\n=== ATTRIBUTS ===")
        attrs = [m for m in dir(self.highrise) if not m.startswith('_') and not callable(getattr(self.highrise, m))]
        for attr in sorted(attrs):
            print(f"  {attr}")

if __name__ == "__main__":
    import sys
    from highrise.__main__ import main as cli_main
    
    TOKEN = "057565bd7bda6ac37029f5817ea7c2f6d447179cdfa65771e41284ed5f5d6090"
    ROOM = "680ab18546b31625a94de2e6"
    
    sys.argv = ['test_sdk.py', 'test_sdk:TestBot', ROOM, TOKEN]
    cli_main()
