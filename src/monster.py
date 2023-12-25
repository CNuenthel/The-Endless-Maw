# Package imports
import random
import json
import yaml
from typing import Union, Literal

# Internal file imports
import item
import equipment

# Load monster configurations and parse data
with open("monster_profiles/monster_config.yaml", "r") as f:
    monster_configs = yaml.safe_load(f)

mon_dmg = monster_configs["Monster_Damage"]
mon_def = monster_configs["Monster_Defense"]
mon_hp = monster_configs["Monster_HP"]
mon_drop_chance = monster_configs["Monster_Item_Drop_Chance"]
mon_xp = monster_configs["Monster_XP"]
mon_inish = monster_configs["Monster_Initiative"]

# Load monster profiles
with open("monster_profiles/rank1.json", "r") as f:
    rank1 = json.load(f)
with open("monster_profiles/rank2.json", "r") as f:
    rank2 = json.load(f)
with open("monster_profiles/rank3.json", "r") as f:
    rank3 = json.load(f)
with open("monster_profiles/rank4.json", "r") as f:
    rank4 = json.load(f)
with open("monster_profiles/rank5.json", "r") as f:
    rank5 = json.load(f)
with open("monster_profiles/rank6.json", "r") as f:
    rank6 = json.load(f)
with open("monster_profiles/rank7.json", "r") as f:
    rank7 = json.load(f)
with open("monster_profiles/rank8.json", "r") as f:
    rank8 = json.load(f)
with open("monster_profiles/rank9.json", "r") as f:
    rank9 = json.load(f)
with open("monster_profiles/rank10.json", "r") as f:
    rank10 = json.load(f)


class Monster:
    def __init__(self, name: str, url: str, sp_atk: str, max_hp: int, atk: int, defense: int, inish: int,
                 itm: str, xp: int):
        self.name = name
        self.url = url
        self.sp_atk = sp_atk
        self.max_hp = max_hp
        self.atk = atk
        self.defense = defense
        self.initiative = inish
        self.item = itm
        self.xp = xp


class MonsterBuilder:
    """
    Generates a monster and saves monster information in json format within directory /monsters
    """

    def __init__(self):
        """
        Creates a randomly selected monster based on rank, randomly rolls HP/Atk/Def
        based on rank windows and saves monster to a text file.
        """
        self.item_generator = item.Items()
        self.legendary_generator = equipment.Legendary()

    def generate_monster(self, rank: int) -> Monster:

        if rank < 1 or rank > 10:
            raise ValueError("Monster rank must be between 1 and 10")

        if rank == 1:
            monster = random.choice(list(rank1.keys()))
            mon_data = rank1[monster]
            max_dmg = mon_dmg["RANK1_MAX_DMG"]
            max_def = mon_def["RANK1_DEFENSE"]
            max_hp = mon_hp["RANK1_MAX_HP"]
            max_inish = mon_inish["RANK1_INITIATIVE"]
            item_drop = mon_drop_chance["RANK1_DROP_CHANCE"]
            max_xp = mon_xp["RANK1_XP"]

            print(f"Building {monster}")
            return Monster(
                name=monster,
                url=mon_data["url"],
                sp_atk=mon_data["text"],
                max_hp=random.randint(max_hp//2, max_hp),
                atk=random.randint(max_dmg//2, max_dmg),
                defense=random.randint(max_def//2, max_def),
                inish=random.randint(max_inish//2, max_inish),
                itm=self.item_generator.random_item(1, item_drop),
                xp=random.randint(max_xp - max_xp//3, max_xp)
            )

        elif rank == 2:
            monster = random.choice(list(rank2.keys()))
            mon_data = rank2[monster]
            max_dmg = mon_dmg["RANK2_MAX_DMG"]
            max_def = mon_def["RANK2_DEFENSE"]
            max_hp = mon_hp["RANK2_MAX_HP"]
            max_inish = mon_inish["RANK2_INITIATIVE"]
            item_drop = mon_drop_chance["RANK2_DROP_CHANCE"]
            max_xp = mon_xp["RANK2_XP"]

            print(f"Building {monster}")
            return Monster(
                name=monster,
                url=mon_data["url"],
                sp_atk=mon_data["text"],
                max_hp=random.randint(max_hp // 2, max_hp),
                atk=random.randint(max_dmg // 2, max_dmg),
                defense=random.randint(max_def // 2, max_def),
                inish=random.randint(max_inish // 2, max_inish),
                itm=self.item_generator.random_item(2, item_drop),
                xp=random.randint(max_xp - max_xp // 3, max_xp)
            )

        elif rank == 3:
            monster = random.choice(list(rank3.keys()))
            mon_data = rank3[monster]
            max_dmg = mon_dmg["RANK3_MAX_DMG"]
            max_def = mon_def["RANK3_DEFENSE"]
            max_hp = mon_hp["RANK3_MAX_HP"]
            max_inish = mon_inish["RANK3_INITIATIVE"]
            item_drop = mon_drop_chance["RANK3_DROP_CHANCE"]
            max_xp = mon_xp["RANK3_XP"]

            print(f"Building {monster}")
            return Monster(
                name=monster,
                url=mon_data["url"],
                sp_atk=mon_data["text"],
                max_hp=random.randint(max_hp // 2, max_hp),
                atk=random.randint(max_dmg // 2, max_dmg),
                defense=random.randint(max_def // 2, max_def),
                inish=random.randint(max_inish // 2, max_inish),
                itm=self.item_generator.random_item(3, item_drop),
                xp=random.randint(max_xp - max_xp // 3, max_xp)
            )

        elif rank == 4:
            monster = random.choice(list(rank4.keys()))
            mon_data = rank4[monster]
            max_dmg = mon_dmg["RANK4_MAX_DMG"]
            max_def = mon_def["RANK4_DEFENSE"]
            max_hp = mon_hp["RANK4_MAX_HP"]
            max_inish = mon_inish["RANK4_INITIATIVE"]
            item_drop = mon_drop_chance["RANK4_DROP_CHANCE"]
            max_xp = mon_xp["RANK4_XP"]

            print(f"Building {monster}")
            return Monster(
                name=monster,
                url=mon_data["url"],
                sp_atk=mon_data["text"],
                max_hp=random.randint(max_hp // 2, max_hp),
                atk=random.randint(max_dmg // 2, max_dmg),
                defense=random.randint(max_def // 2, max_def),
                inish=random.randint(max_inish // 2, max_inish),
                itm=self.item_generator.random_item(4, item_drop),
                xp=random.randint(max_xp - max_xp // 3, max_xp)
            )

        elif rank == 5:
            monster = random.choice(list(rank5.keys()))
            mon_data = rank5[monster]
            max_dmg = mon_dmg["RANK5_MAX_DMG"]
            max_def = mon_def["RANK5_DEFENSE"]
            max_hp = mon_hp["RANK5_MAX_HP"]
            max_inish = mon_inish["RANK5_INITIATIVE"]
            item_drop = mon_drop_chance["RANK5_DROP_CHANCE"]
            max_xp = mon_xp["RANK5_XP"]

            print(f"Building {monster}")
            return Monster(
                name=monster,
                url=mon_data["url"],
                sp_atk=mon_data["text"],
                max_hp=random.randint(max_hp // 2, max_hp),
                atk=random.randint(max_dmg // 2, max_dmg),
                defense=random.randint(max_def // 2, max_def),
                inish=random.randint(max_inish // 2, max_inish),
                itm=self.item_generator.random_item(5, item_drop),
                xp=random.randint(max_xp - max_xp // 3, max_xp)
            )

        elif rank == 6:
            monster = random.choice(list(rank6.keys()))
            mon_data = rank6[monster]
            max_dmg = mon_dmg["RANK6_MAX_DMG"]
            max_def = mon_def["RANK6_DEFENSE"]
            max_hp = mon_hp["RANK6_MAX_HP"]
            max_inish = mon_inish["RANK6_INITIATIVE"]
            item_drop = mon_drop_chance["RANK6_DROP_CHANCE"]
            max_xp = mon_xp["RANK6_XP"]

            print(f"Building {monster}")
            return Monster(
                name=monster,
                url=mon_data["url"],
                sp_atk=mon_data["text"],
                max_hp=random.randint(max_hp // 2, max_hp),
                atk=random.randint(max_dmg // 2, max_dmg),
                defense=random.randint(max_def // 2, max_def),
                inish=random.randint(max_inish // 2, max_inish),
                itm=self.item_generator.random_item(6, item_drop),
                xp=random.randint(max_xp - max_xp // 3, max_xp)
            )

        elif rank == 7:
            monster = random.choice(list(rank7.keys()))
            mon_data = rank7[monster]
            max_dmg = mon_dmg["RANK7_MAX_DMG"]
            max_def = mon_def["RANK7_DEFENSE"]
            max_hp = mon_hp["RANK7_MAX_HP"]
            max_inish = mon_inish["RANK7_INITIATIVE"]
            item_drop = mon_drop_chance["RANK7_DROP_CHANCE"]
            max_xp = mon_xp["RANK7_XP"]

            print(f"Building {monster}")
            return Monster(
                name=monster,
                url=mon_data["url"],
                sp_atk=mon_data["text"],
                max_hp=random.randint(max_hp // 2, max_hp),
                atk=random.randint(max_dmg // 2, max_dmg),
                defense=random.randint(max_def // 2, max_def),
                inish=random.randint(max_inish // 2, max_inish),
                itm=self.item_generator.random_item(7, item_drop),
                xp=random.randint(max_xp - max_xp // 3, max_xp)
            )

        elif rank == 8:
            monster = random.choice(list(rank8.keys()))
            mon_data = rank8[monster]
            max_dmg = mon_dmg["RANK8_MAX_DMG"]
            max_def = mon_def["RANK8_DEFENSE"]
            max_hp = mon_hp["RANK8_MAX_HP"]
            max_inish = mon_inish["RANK8_INITIATIVE"]
            item_drop = mon_drop_chance["RANK8_DROP_CHANCE"]
            max_xp = mon_xp["RANK8_XP"]

            print(f"Building {monster}")
            return Monster(
                name=monster,
                url=mon_data["url"],
                sp_atk=mon_data["text"],
                max_hp=random.randint(max_hp // 2, max_hp),
                atk=random.randint(max_dmg // 2, max_dmg),
                defense=random.randint(max_def // 2, max_def),
                inish=random.randint(max_inish // 2, max_inish),
                itm=self.item_generator.random_item(8, item_drop),
                xp=random.randint(max_xp - max_xp // 3, max_xp)
            )

        elif rank == 9:
            monster = random.choice(list(rank9.keys()))
            mon_data = rank9[monster]
            max_dmg = mon_dmg["RANK9_MAX_DMG"]
            max_def = mon_def["RANK9_DEFENSE"]
            max_hp = mon_hp["RANK9_MAX_HP"]
            max_inish = mon_inish["RANK9_INITIATIVE"]
            item_drop = mon_drop_chance["RANK9_DROP_CHANCE"]
            max_xp = mon_xp["RANK9_XP"]

            print(f"Building {monster}")
            return Monster(
                name=monster,
                url=mon_data["url"],
                sp_atk=mon_data["text"],
                max_hp=random.randint(max_hp // 2, max_hp),
                atk=random.randint(max_dmg // 2, max_dmg),
                defense=random.randint(max_def // 2, max_def),
                inish=random.randint(max_inish // 2, max_inish),
                itm=self.item_generator.random_item(9, item_drop),
                xp=random.randint(max_xp - max_xp // 3, max_xp)
            )

        elif rank == 10:
            monster = random.choice(list(rank10.keys()))
            mon_data = rank10[monster]
            max_dmg = mon_dmg["RANK10_MAX_DMG"]
            max_def = mon_def["RANK10_DEFENSE"]
            max_hp = mon_hp["RANK10_MAX_HP"]
            max_inish = mon_inish["RANK10_INITIATIVE"]
            max_xp = mon_xp["RANK10_XP"]

            print(f"Building {monster}")
            return Monster(
                name=monster,
                url=mon_data["url"],
                sp_atk=mon_data["text"],
                max_hp=random.randint(max_hp // 2, max_hp),
                atk=random.randint(max_dmg // 2, max_dmg),
                defense=random.randint(max_def // 2, max_def),
                inish=random.randint(max_inish // 2, max_inish),
                itm=random.choice(self.legendary_generator.legends),
                xp=random.randint(max_xp - max_xp // 3, max_xp)
            )
