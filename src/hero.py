# Package imports
import random

# Local imports
from armor import Armor


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
        self.bonus_atk = 0

        self.defense = 0
        self.bonus_def = 0

        self.initiative = 1
        self.bonus_initiative = 0

        self.crit_multiplier = 1.5  # Multiplier of dmg
        self.bonus_crit_multiplier = 0.0  # Additive to crit_multiplier

        self.crit_chance = 10
        self.bonus_crit_chance = 0  # Reductive to crit_chance, cannot exceed 10

        self.owner_id = player_id
        self.owner_name = player_name

        self.max_ep = 0
        self.current_ep = 0
        self.bonus_ep = 0

        self.level = 1
        self.xp = 0
        self.inventory = []
        self.status = []
        self.armory = []
        self.keys = []

        self.weapon = None
        self.armor = None

        self.gold = 0

    def roll_initiative(self):
        return random.randint(self.initiative // 2, self.initiative)

    def roll_damage(self) -> dict:
        atk = self.atk + self.bonus_atk
        damage = random.randint(atk // 2, atk)

        if random.randint(1, self.crit_chance - self.bonus_crit_chance) == 1:
            crit_multi = self.crit_multiplier + self.bonus_crit_multiplier
            damage = int(damage * crit_multi)
            return {"crit": True, "dmg": damage}

        return {"crit": False, "dmg": damage}

    def take_damage(self, damage: int) -> dict:
        total_defense = self.defense + self.bonus_def
        net_damage = max(damage - total_defense, 0)
        self.current_hp = max(self.current_hp - net_damage, 0)

        if net_damage == 0:
            return {"dmg_mitigated": True, "current_hp": self.current_hp}
        return {"dmg_mitigated": False, "current_hp": self.current_hp}

    def equip_armor(self, armor_id: str):
        for armor in self.armory:
            if armor.unique_id == armor_id:
                self.armory.remove(armor)
                self.armor = armor
                self.bonus_def += self.armor.bonus_defense
                self.bonus_hp += self.armor.bonus_hp

    def remove_armor(self):
        self.bonus_def -= self.armor.bonus_defense
        self.bonus_hp -= self.armor.bonus_hp
        self.armory.append(self.armor)
        self.armor = None

    def equip_weapon(self, weapon_id: str):
        for weapon in self.armory:
            if weapon.unique_id == weapon_id:
                self.armory.remove(weapon)
                self.weapon = weapon
                self.bonus_atk += self.weapon.bonus_atk
                self.bonus_def += self.weapon.bonus_defense

    def remove_weapon(self):
        self.bonus_atk -= self.weapon.bonus_atk
        self.bonus_def -= self.weapon.bonus_defense
        self.armory.append(self.weapon)
        self.weapon = None
