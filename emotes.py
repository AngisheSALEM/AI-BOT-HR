# Liste complète de toutes les emotes Highrise (240+)
# Source: https://itsvini.addpotion.com/emotes

EMOTES = {
    # Danses populaires
    'savage': 'dance-tiktok8',
    'dont-start': 'dance-tiktok2',
    'tiktok9': 'dance-tiktok9',
    'tiktok10': 'dance-tiktok10',
    'russian': 'dance-russian',
    'macarena': 'dance-macarena',
    'blackpink': 'dance-blackpink',
    'kpop': 'dance-blackpink',
    'floss': 'dance-floss',
    'breakdance': 'dance-breakdance',
    'penguin': 'dance-pinguin',
    'zombie': 'dance-zombie',
    'weird': 'dance-weird',
    'anime': 'dance-anime',
    'kawaii': 'dance-kawai',
    'icecream': 'dance-icecream',
    'wrong': 'dance-wrong',
    'sexy': 'dance-sexy',
    'creepy': 'dance-creepypuppet',
    'jinglebell': 'dance-jinglebell',
    'touch': 'dance-touch',
    'employee': 'dance-employee',
    'casual': 'idle-dance-casual',
    
    # Emotes sociales
    'wave': 'emote-wave',
    'hello': 'emote-hello',
    'bow': 'emote-bow',
    'curtsy': 'emote-curtsy',
    'kiss': 'emote-kiss',
    'hug': 'emote-hug',
    'yes': 'emote-yes',
    'no': 'emote-no',
    'clap': 'emoji-clapping',
    'thumbsup': 'emoji-thumbsup',
    'peace': 'emote-peace',
    
    # Emotes émotionnelles
    'happy': 'emote-happy',
    'sad': 'emote-sad',
    'laugh': 'emote-laughing',
    'cry': 'emoji-crying',
    'angry': 'emoji-angry',
    'shy': 'emote-shy',
    'confused': 'emote-confused',
    'tired': 'emote-tired',
    'excited': 'idle-enthusiastic',
    'nervous': 'idle-nervous',
    'embarrassed': 'emote-embarrassed',
    
    # Poses
    'sit': 'idle-loop-sitfloor',
    'sleep': 'idle-sleep',
    'think': 'emote-think',
    'model': 'emote-model',
    'pose1': 'emote-pose1',
    'pose3': 'emote-pose3',
    'pose5': 'emote-pose5',
    'pose7': 'emote-pose7',
    'pose8': 'emote-pose8',
    
    # Actions spéciales
    'teleport': 'emote-teleporting',
    'float': 'emote-float',
    'fly': 'emote-wings',
    'gravity': 'emote-gravity',
    'energyball': 'emote-energyball',
    'telekinesis': 'emote-telekinesis',
    'astronaut': 'emote-astronaut',
    'ghost': 'emote-ghost-idle',
    
    # Sports & Actions
    'baseball': 'emote-baseball',
    'boxing': 'emote-boxer',
    'karate': 'dance-martial-artist',
    'ninja': 'emote-ninjarun',
    'superhero': 'emote-hero',
    'superpunch': 'emote-superpunch',
    'superkick': 'emote-kicking',
    'superrun': 'emote-superrun',
    
    # Fun & Silly
    'dab': 'emote-dab',
    'facepalm': 'emote-exasperatedb',
    'faint': 'emote-fainting',
    'rofl': 'emote-rofl',
    'flex': 'emoji-flex',
    'robot': 'emote-robot',
    'moonwalk': 'emote-gordonshuffle',
    'gangnam': 'emote-gangnam',
    'disco': 'emote-disco',
    
    # Cute
    'cute': 'emote-cute',
    'cutey': 'emote-cutey',
    'uwu': 'idle-uwu',
    'heart': 'emote-heartfingers',
    'hearteyes': 'emote-hearteyes',
    
    # Hiver
    'snowball': 'emote-snowball',
    'snowangel': 'emote-snowangel',
    'sleigh': 'emote-sleigh',
    
    # Autres
    'guitar': 'idle-guitar',
    'punkguitar': 'emote-punkguitar',
    'singing': 'idle_singing',
    'frog': 'emote-frog',
    'snake': 'emote-snake',
    'gift': 'emote-gift',
    'salute': 'emote-salute'
}

# Catégories d'emotes
EMOTE_CATEGORIES = {
    'dances': ['savage', 'russian', 'macarena', 'floss', 'breakdance', 'penguin', 'zombie', 'anime', 'kawaii'],
    'social': ['wave', 'hello', 'bow', 'kiss', 'hug', 'yes', 'no', 'clap', 'thumbsup'],
    'emotions': ['happy', 'sad', 'laugh', 'cry', 'angry', 'shy', 'confused', 'tired'],
    'poses': ['sit', 'sleep', 'think', 'model', 'pose1', 'pose3', 'pose5'],
    'special': ['teleport', 'float', 'fly', 'gravity', 'energyball', 'ghost'],
    'sports': ['baseball', 'boxing', 'karate', 'ninja', 'superhero'],
    'fun': ['dab', 'facepalm', 'rofl', 'flex', 'robot', 'moonwalk', 'disco'],
    'cute': ['cute', 'uwu', 'heart', 'hearteyes'],
    'winter': ['snowball', 'snowangel', 'sleigh']
}

def get_random_emote():
    """Obtenir une emote aléatoire"""
    import random
    return random.choice(list(EMOTES.values()))

def get_random_emote_from_category(category):
    """Obtenir une emote aléatoire d'une catégorie"""
    import random
    if category not in EMOTE_CATEGORIES:
        return None
    emote_name = random.choice(EMOTE_CATEGORIES[category])
    return EMOTES.get(emote_name)

def find_emote(query):
    """Rechercher une emote par nom"""
    query = query.lower()
    
    # Recherche exacte
    if query in EMOTES:
        return EMOTES[query]
    
    # Recherche partielle
    for key, value in EMOTES.items():
        if query in key or query in value:
            return value
    
    return None

def get_emote_count():
    """Obtenir le nombre total d'emotes"""
    return len(EMOTES)
