
class Hero:
    """
    Generates a hero and saves hero information in json format within directory /characters
    """
    def __init__(self, hero_name: str, player_id: int, player_name: str):
        """
        Creates a character with a given name of a desired class, randomizes HP/Atk/Def based on class type and saves
        character to a text file.
        """
        self.name = hero_name
        self.class_ = ""
        self.max_hp = 50
        self.current_hp = 50
        self.bonus_hp = 0
        self.atk = 15
        self.defense = 0
        self.initiative = 1
        self.status = []
        self.crit_multiplier = 1.5
        self.crit_chance = 10
        self.bonus_crit = 0
        self.owner_id = player_id
        self.owner_name = player_name
        self.level = 1
        self.xp = 0
        self.inventory = []
        self.armory = []
        self.keys = []
        self.equipment = "None"
        self.armor = "None"
        self.gold = 0
