# Package imports
import yaml
import random
import uuid


class Armor:
    def __init__(self, name: str, rank: int, bonus_defense: int, bonus_hp: int):
        self.name = name
        self.unique_id = None
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

    def random_armor(self, rank: int) -> Armor | None:
        if rank in self.armors:
            armor = random.choice(self.armors[rank])
            armor.bonus_defense = random.randint(armor.bonus_defense // 2, armor.bonus_defense)
            armor.bonus_hp = random.randint(armor.bonus_hp // 2, armor.bonus_hp)
            armor.unique_id = str(uuid.uuid4())
            return armor
        return None
