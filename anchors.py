# Système de points de téléportation (Anchors) pour Highrise

from typing import Dict, List, Tuple
from highrise.models import Position, AnchorPosition

class TeleportPoint:
    """Point de téléportation"""
    def __init__(self, name: str, x: float, y: float, z: float, description: str = ""):
        self.name = name
        self.x = x
        self.y = y
        self.z = z
        self.description = description
    
    def to_position(self) -> Position:
        """Convertir en Position"""
        return Position(self.x, self.y, self.z)
    
    def __str__(self):
        return f"{self.name} ({self.x}, {self.y}, {self.z})"

class AnchorManager:
    """Gestionnaire de points d'ancrage"""
    
    def __init__(self):
        # Points de téléportation prédéfinis
        self.points: Dict[str, TeleportPoint] = {}
        self._init_default_points()
    
    def _init_default_points(self):
        """Initialiser les points par défaut"""
        # Points communs (à adapter selon votre room)
        self.add_point("spawn", 0, 0, 0, "Point d'apparition")
        self.add_point("center", 10, 0, 0, "Centre de la room")
        self.add_point("stage", 15, 0, 0, "Scène")
        self.add_point("vip", 20, 0, 0, "Zone VIP")
        self.add_point("lounge", 5, 0, 0, "Salon")
        
        # Étages (si votre room en a)
        self.add_point("floor1", 0, 0, 0, "Étage 1")
        self.add_point("floor2", 0, 5, 0, "Étage 2")
        self.add_point("floor3", 0, 10, 0, "Étage 3")
        
        # Zones spéciales
        self.add_point("dance", 12, 0, 0, "Piste de danse")
        self.add_point("chill", 8, 0, 0, "Zone chill")
        self.add_point("games", 18, 0, 0, "Zone jeux")
    
    def add_point(self, name: str, x: float, y: float, z: float, description: str = ""):
        """Ajouter un point de téléportation"""
        self.points[name.lower()] = TeleportPoint(name, x, y, z, description)
    
    def remove_point(self, name: str) -> bool:
        """Supprimer un point"""
        name = name.lower()
        if name in self.points:
            del self.points[name]
            return True
        return False
    
    def get_point(self, name: str) -> TeleportPoint:
        """Obtenir un point par nom"""
        return self.points.get(name.lower())
    
    def list_points(self) -> List[str]:
        """Lister tous les points"""
        return [f"{point.name}: {point.description}" for point in self.points.values()]
    
    def find_point(self, query: str) -> TeleportPoint:
        """Trouver un point par recherche partielle"""
        query = query.lower()
        
        # Recherche exacte
        if query in self.points:
            return self.points[query]
        
        # Recherche partielle
        for name, point in self.points.items():
            if query in name or name in query:
                return point
        
        return None
    
    def get_closest_point(self, x: float, y: float, z: float) -> Tuple[str, TeleportPoint]:
        """Trouver le point le plus proche"""
        if not self.points:
            return None, None
        
        min_dist = float('inf')
        closest = None
        closest_name = None
        
        for name, point in self.points.items():
            dist = ((point.x - x)**2 + (point.y - y)**2 + (point.z - z)**2)**0.5
            if dist < min_dist:
                min_dist = dist
                closest = point
                closest_name = name
        
        return closest_name, closest

# Instance globale
anchor_manager = AnchorManager()

def load_anchors_from_file(filename: str = "anchors.json"):
    """Charger les points depuis un fichier JSON"""
    import json
    import os
    
    if not os.path.exists(filename):
        return
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for name, info in data.items():
                anchor_manager.add_point(
                    name,
                    info['x'],
                    info['y'],
                    info['z'],
                    info.get('description', '')
                )
    except Exception as e:
        print(f"[ERREUR] Chargement anchors: {e}")

def save_anchors_to_file(filename: str = "anchors.json"):
    """Sauvegarder les points dans un fichier JSON"""
    import json
    
    data = {}
    for name, point in anchor_manager.points.items():
        data[name] = {
            'x': point.x,
            'y': point.y,
            'z': point.z,
            'description': point.description
        }
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"[ERREUR] Sauvegarde anchors: {e}")
