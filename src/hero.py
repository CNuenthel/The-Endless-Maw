
class Hero:
    """
    Generates a hero and saves hero information in json format within directory /characters
    """
    def __init__(self, hero_name: str):
        """
        Creates a character with a given name of a desired class, randomizes HP/Atk/Def based on class type and saves
        character to a text file.
        """
        self.name = hero_name
        self.class_ = ""
        self.max_hp = 50
        self.current_hp = 50
        self.bonus_hp = 0
        self.atk = 0
        self.bonus_atk = 0
        self.defense = 0
        self.bonus_def = 0
        self.initiative = 0
        self.status = []
        self.crit_multiplier = 1.5
        self.bonus_crit = 0
        self.owner = ""
        self.name = ""
        self.level = 1
        self.xp = 0
        self.inventory = []
        self.armory = []
        self.keys = []
        self.equipment = "None"
        self.armor = "None"
        self.gold = 0
