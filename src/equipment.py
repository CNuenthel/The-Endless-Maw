import yaml
import random

# Load armor configurations
with open("item_profiles/armor_config.yaml", "r") as f:
    armor_configs = yaml.safe_load(f)

RANK1 = armor_configs["RANK1"]
RANK2 = armor_configs["RANK2"]
RANK3 = armor_configs["RANK3"]
RANK4 = armor_configs["RANK4"]

# Load weapon configurations
with open("item_profiles/weapon_config.yaml", "r") as f:
    weapon_configs = yaml.safe_load(f)

print(type(armor_configs["Padded Armor"]["bonus_defense"]))


class Armor:
    def __init__(self, name: str, bonus_defense: int, bonus_hp: int):
        self.name = name
        self.bonus_defense = bonus_defense
        self.bonus_hp = bonus_hp


class ArmorGenerator:
    def __init__(self):
        self.rank1_armors = list(RANK1.keys())
        self.rank2_armors = list(RANK2.keys())
        self.rank3_armors = list(RANK3.keys())
        self.rank4_armors = list(RANK4.keys())

    def random_armor(self, rank: int):
        pass


class Legendary:
    def __init__(self):
        self.legends = ["Rod Of Lordly Might", "Natures Mantle", "Vestige Blade", "Chidori",
                        "Yamatos Training Katana", "Forbidden Fruit"]
