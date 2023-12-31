# Package imports
import yaml
import random
import uuid


class Weapon:
    def __init__(self, name: str, rank: int, bonus_atk: int, bonus_def: int):
        self.name = name
        self.unique_id = None
        self.rank = rank
        self.bonus_atk = bonus_atk
        self.bonus_defense = bonus_def

    def __repr__(self):
        return self.name


class WeaponGenerator:
    def __init__(self):
        self.weapons = {}
        self._load_weapons()

    def _load_weapons(self):
        print("Loading Weapons...")
        with open("item_profiles/weapon_config.yaml", "r") as f:
            weapon_configs = yaml.safe_load(f)

        for weapon_name, weapon_data in weapon_configs.items():
            weapon = Weapon(
                name=weapon_name,
                rank=weapon_data.get("rank", 1),
                bonus_atk=weapon_data.get("bonus_atk", 0),
                bonus_def=weapon_data.get("bonus_def", 0)
            )
            rank = weapon.rank
            if rank not in self.weapons:
                self.weapons[rank] = []
            self.weapons[rank].append(weapon)

    def random_weapon(self, rank: int) -> Weapon | None:
        if rank in self.weapons:
            weapon = random.choice(self.weapons[rank])
            weapon.bonus_atk = random.randint(weapon.bonus_atk//2, weapon.bonus_atk)
            weapon.bonus_defense = random.randint(weapon.bonus_defense//2, weapon.bonus_defense)
            weapon.unique_id = str(uuid.uuid4())
            return weapon
        return None
