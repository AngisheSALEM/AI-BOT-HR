# Système de rôles et permissions pour le bot Highrise

from enum import Enum
from typing import Dict, List, Set

class Role(Enum):
    """Rôles disponibles"""
    OWNER = "owner"
    ADMIN = "admin"
    MODERATOR = "moderator"
    VIP = "vip"
    USER = "user"

class Permission(Enum):
    """Permissions disponibles"""
    # Modération
    KICK = "kick"
    BAN = "ban"
    MUTE = "mute"
    UNBAN = "unban"
    
    # Téléportation
    TELEPORT_SELF = "teleport_self"
    TELEPORT_OTHERS = "teleport_others"
    
    # Emotes
    EMOTE_SELF = "emote_self"
    EMOTE_OTHERS = "emote_others"
    
    # Bot
    ANNOUNCE = "announce"
    PARADE = "parade"
    RAIN = "rain"
    
    # Stats
    VIEW_STATS = "view_stats"
    RESET_STATS = "reset_stats"
    
    # Wallet
    TIP = "tip"
    VIEW_WALLET = "view_wallet"

# Permissions par rôle
ROLE_PERMISSIONS: Dict[Role, Set[Permission]] = {
    Role.OWNER: {
        # Toutes les permissions
        Permission.KICK, Permission.BAN, Permission.MUTE, Permission.UNBAN,
        Permission.TELEPORT_SELF, Permission.TELEPORT_OTHERS,
        Permission.EMOTE_SELF, Permission.EMOTE_OTHERS,
        Permission.ANNOUNCE, Permission.PARADE, Permission.RAIN,
        Permission.VIEW_STATS, Permission.RESET_STATS,
        Permission.TIP, Permission.VIEW_WALLET,
    },
    Role.ADMIN: {
        Permission.KICK, Permission.BAN, Permission.MUTE, Permission.UNBAN,
        Permission.TELEPORT_SELF, Permission.TELEPORT_OTHERS,
        Permission.EMOTE_SELF, Permission.EMOTE_OTHERS,
        Permission.ANNOUNCE, Permission.PARADE, Permission.RAIN,
        Permission.VIEW_STATS,
        Permission.TIP, Permission.VIEW_WALLET,
    },
    Role.MODERATOR: {
        Permission.KICK, Permission.MUTE,
        Permission.TELEPORT_SELF, Permission.TELEPORT_OTHERS,
        Permission.EMOTE_SELF, Permission.EMOTE_OTHERS,
        Permission.VIEW_STATS,
    },
    Role.VIP: {
        Permission.TELEPORT_SELF,
        Permission.EMOTE_SELF, Permission.EMOTE_OTHERS,
        Permission.VIEW_STATS,
        Permission.TIP,
    },
    Role.USER: {
        Permission.TELEPORT_SELF,
        Permission.EMOTE_SELF,
        Permission.VIEW_STATS,
    },
}

class RoleManager:
    """Gestionnaire de rôles"""
    
    def __init__(self):
        # user_id -> Role
        self.user_roles: Dict[str, Role] = {}
        
    def set_role(self, user_id: str, role: Role):
        """Définir le rôle d'un utilisateur"""
        self.user_roles[user_id] = role
    
    def get_role(self, user_id: str) -> Role:
        """Obtenir le rôle d'un utilisateur"""
        return self.user_roles.get(user_id, Role.USER)
    
    def has_permission(self, user_id: str, permission: Permission) -> bool:
        """Vérifier si un utilisateur a une permission"""
        role = self.get_role(user_id)
        return permission in ROLE_PERMISSIONS.get(role, set())
    
    def get_permissions(self, user_id: str) -> Set[Permission]:
        """Obtenir toutes les permissions d'un utilisateur"""
        role = self.get_role(user_id)
        return ROLE_PERMISSIONS.get(role, set())
    
    def get_role_name(self, user_id: str) -> str:
        """Obtenir le nom du rôle"""
        role = self.get_role(user_id)
        return role.value.upper()
    
    def list_roles(self) -> List[str]:
        """Lister tous les rôles"""
        return [role.value.upper() for role in Role]
    
    def get_users_by_role(self, role: Role) -> List[str]:
        """Obtenir tous les utilisateurs avec un rôle spécifique"""
        return [user_id for user_id, user_role in self.user_roles.items() if user_role == role]

# Instance globale
role_manager = RoleManager()

def load_roles_from_env(admin_ids: str):
    """Charger les rôles depuis les variables d'environnement"""
    if admin_ids:
        for admin_id in admin_ids.split(','):
            admin_id = admin_id.strip()
            if admin_id:
                role_manager.set_role(admin_id, Role.ADMIN)
