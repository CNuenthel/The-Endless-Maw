import yaml
import random


class Armor:
    def __init__(self, name: str, rank: int, bonus_defense: int, bonus_hp: int):
        self.name = name
        self.rank = rank
        self.bonus_defense = bonus_defense
        self.bonus_hp = bonus_hp

    def __repr__(self):
        return self.name


class ArmorGenerator:
    def __init__(self):
        self.armors = {}
        self._load_armors()

    def _load_armors(self):
        print("Loading Armors...")
        with open("item_profiles/armor_config.yaml", "r") as f:
            armor_configs = yaml.safe_load(f)

        for armor_name, armor_data in armor_configs.items():
            armor = Armor(
                name=armor_name,
                rank=armor_data.get("rank", 1),
                bonus_defense=armor_data.get("bonus_defense", 0),
                bonus_hp=armor_data.get("bonus_hp", 0)
            )
            rank = armor.rank
            if rank not in self.armors:
                self.armors[rank] = []
            self.armors[rank].append(armor)

    def random_armor(self, rank: int) -> Armor:
        if rank in self.armors:
            return random.choice(self.armors[rank])
        else:
            return None


# class Legendary:
#     def __init__(self):
#         self.legends = ["Rod Of Lordly Might", "Natures Mantle", "Vestige Blade", "Chidori",
#                         "Yamatos Training Katana", "Forbidden Fruit"]
