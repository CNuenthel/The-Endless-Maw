from typing import Union, Literal
import random


class Items:
    def __init__(self):
        self.tier1_items = [
            "Monster Scanner",
            "Fireball Scroll",
            "Healing Potion",
            "Whetstone",
            "Smelling Salts"
        ]

        self.tier2_items = [
            "Blood Of Berserker",
            "Witchbolt Wand",
            "Blood Dagger",
            "Tome Of Wisdom",
            "Decay Bomb"
        ]

        self.tier3_items = [
            "Scroll Of Summoning",
            "Gravity Bomb",
            "Mesmer Stone",
            "Gift Of Arawn",
            "Sundering Axe"
        ]

        self.tier4_items = [
            "Eldritch Keybox",
            "Bardic Tale"
        ]

        self.keys = [
            "Blood-Soaked Key",
            "Mountain Key",
            "Dimensional Key",
            "Tortoise Key"
        ]

        self.master = [
            "Monster Scanner",
            "Fireball Scroll",
            "Healing Potion",
            "Whetstone",
            "Smelling Salts",
            "Blood Of Berserker",
            "Witchbolt Wand",
            "Blood Dagger",
            "Tome Of Wisdom",
            "Decay Bomb",
            "Scroll Of Summoning",
            "Gravity Bomb",
            "Mesmer Stone",
            "Gift Of Arawn",
            "Sundering Axe",
            "Eldritch Keybox",
            "Bardic Tale",
        ]

    def random_item(self, mon_rank: Union[int, Literal[1], Literal[9]], drop_chance: int):
        """
        Returns a random item based on given rank and drop chance
        """
        if mon_rank == 9:
            if random.randint(1, drop_chance) == 1:
                return random.choice(self.keys)
            return random.choice(self.master)

        elif mon_rank < 4:
            if random.randint(1, drop_chance) == 1:
                return random.choice(self.tier1_items)
            return None

        elif 4 <= mon_rank <= 7:
            if random.randint(1, drop_chance) == 1:
                return random.choice(self.tier2_items)
            return None

        elif 7 < mon_rank >= 8:
            if random.randint(1, drop_chance) == 1:
                return random.choice(self.tier3_items)
            return None
