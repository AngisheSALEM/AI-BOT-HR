# Emotes Highrise par NUMÉRO (sans espaces)
# Utilisable avec !emote 1, !emote 2, etc.

EMOTES_BY_NUMBER = {
    # Format: numéro -> (nom, emote_id)
    1: ("wave", "emote-wave"),
    2: ("hello", "emote-hello"),
    3: ("bow", "emote-bow"),
    4: ("clap", "emote-clap"),
    5: ("thumbsup", "emote-thumbsup"),
    6: ("yes", "emote-yes"),
    7: ("no", "emote-no"),
    8: ("kiss", "emote-kiss"),
    9: ("hug", "emote-hug"),
    10: ("shy", "emote-shy"),
    11: ("happy", "emote-happy"),
    12: ("sad", "emote-sad"),
    13: ("laugh", "emote-laugh"),
    14: ("cry", "emote-crying"),
    15: ("angry", "emote-angry"),
    16: ("confused", "emote-confused"),
    17: ("tired", "emote-tired"),
    18: ("sleepy", "emote-sleepy"),
    19: ("dance", "idle-dance-casual"),
    20: ("savage", "dance-tiktok2"),
    21: ("russian", "dance-russian"),
    22: ("macarena", "dance-macarena"),
    23: ("breakdance", "dance-breakdance"),
    24: ("penguin", "dance-pinguin"),
    25: ("sit", "emote-sit"),
    26: ("sleep", "emote-sleep"),
    27: ("think", "emote-think"),
    28: ("dab", "emote-dab"),
    29: ("facepalm", "emote-facepalm"),
    30: ("rofl", "emote-rofl"),
    31: ("flex", "emoji-flex"),
    32: ("celebrate", "emoji-celebrate"),
    33: ("cute", "emote-cute"),
    34: ("uwu", "idle-uwu"),
    35: ("heart", "emote-heart"),
    36: ("hearteyes", "emote-hearteyes"),
    37: ("wink", "emote-wink"),
    38: ("float", "emote-float"),
    39: ("gravity", "emote-gravity"),
    40: ("teleport", "emote-teleporting"),
    41: ("astronaut", "emote-astronaut"),
    42: ("ninja", "emote-ninja"),
    43: ("karate", "emote-karate"),
    44: ("robot", "emote-robot"),
    45: ("disco", "emote-disco"),
    46: ("moonwalk", "emote-moonwalk"),
    47: ("model", "emote-model"),
    48: ("pose", "emote-pose1"),
    49: ("guitar", "emote-guitar"),
    50: ("sing", "emote-sing"),
    51: ("baseball", "emote-baseball"),
    52: ("boxer", "emote-boxer"),
    53: ("snowball", "emote-snowball"),
    54: ("snowangel", "emote-snowangel"),
    55: ("sleigh", "emote-sleigh"),
    56: ("ghostfloat", "emote-ghost-float"),
    57: ("zombierun", "emote-zombierun"),
    58: ("creepypuppet", "emote-creepy-puppet"),
    59: ("possessed", "emote-possessed"),
    60: ("levitate", "emote-levitate"),
    61: ("energyball", "emote-energyball"),
    62: ("swordfight", "emote-swordfight"),
    63: ("punkguitar", "emote-punkguitar"),
    64: ("icecream", "emote-icecream"),
    65: ("jetpack", "emote-jetpack"),
    66: ("dizzy", "emote-dizzy"),
    67: ("hyped", "emote-hyped"),
    68: ("charging", "emote-charging"),
    69: ("shovel", "emote-shovel"),
    70: ("launch", "emote-launch"),
    71: ("maniac", "emote-maniac"),
    72: ("snake", "emote-snake"),
    73: ("frog", "emote-frog"),
    74: ("superpose", "emote-superpose"),
    75: ("fashionista", "emote-fashionista"),
    76: ("theatrical", "emote-theatrical"),
    77: ("greedy", "emote-greedy"),
    78: ("lust", "emote-lust"),
    79: ("hot", "emote-hot"),
    80: ("kpop", "emote-kpop"),
    81: ("curtsy", "emote-curtsy"),
    82: ("telekinesis", "emote-telekinesis"),
    83: ("ropepull", "emote-ropepull"),
    84: ("headball", "emote-headball"),
    85: ("lounge", "emote-lounge"),
    86: ("relaxed", "emote-relaxed"),
    87: ("blush", "emote-blush"),
    88: ("weird", "dance-weird"),
    89: ("tiktok8", "dance-tiktok8"),
    90: ("tiktok9", "dance-tiktok9"),
    91: ("tiktok10", "dance-tiktok10"),
    92: ("tiktok4", "idle-dance-tiktok4"),
    93: ("wild", "idle-wild"),
    94: ("nervous", "idle-nervous"),
    95: ("sitfloor", "idle-loop-sitfloor"),
    96: ("aerobics", "idle-loop-aerobics"),
    97: ("enthusiastic", "idle-enthusiastic"),
    98: ("floorsleeping", "idle-floorsleeping"),
    99: ("swag", "idle-dance-swag"),
    100: ("toilet", "idle-toilet"),
}

# Nom -> Numéro (pour recherche inverse)
EMOTE_NAME_TO_NUMBER = {name: num for num, (name, _) in EMOTES_BY_NUMBER.items()}

def get_emote_by_number(number: int) -> tuple:
    """Obtenir un emote par numéro"""
    return EMOTES_BY_NUMBER.get(number)

def get_emote_number(name: str) -> int:
    """Obtenir le numéro d'un emote par nom"""
    return EMOTE_NAME_TO_NUMBER.get(name.lower())

def list_emotes_by_number(start: int = 1, end: int = 20) -> str:
    """Lister les emotes par numéro"""
    result = []
    for num in range(start, min(end + 1, 101)):
        if num in EMOTES_BY_NUMBER:
            name, _ = EMOTES_BY_NUMBER[num]
            result.append(f"{num}={name}")
    return ", ".join(result)
