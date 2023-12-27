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
mon_crit = monster_configs["Monster_Crit"]
mon_crit_multi = monster_configs["Monster_Crit_Multiplier"]

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
                 crit_chance: int, crit_multi: float, itm: str, xp: int):
        self.name = name
        self.url = url
        self.sp_atk = sp_atk
        self.current_hp = max_hp
        self.atk = atk
        self.defense = defense
        self.initiative = inish
        self.crit_chance = crit_chance
        self.crit_multi = crit_multi
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

        rank_map = {
            1: rank1,
            2: rank2,
            3: rank3,
            4: rank4,
            5: rank5,
            6: rank6,
            7: rank7,
            8: rank8,
            9: rank9,
            10: rank10
        }

        monster = random.choice(list(rank_map[rank].keys()))
        mon_data = rank_map[rank][monster]
        max_dmg = mon_dmg[f"RANK{rank}_MAX_DMG"]
        max_def = mon_def[f"RANK{rank}_DEFENSE"]
        max_hp = mon_hp[f"RANK{rank}_MAX_HP"]
        max_inish = mon_inish[f"RANK{rank}_INITIATIVE"]
        crit_chance = mon_crit[f"RANK{rank}_CRIT"]
        crit_multi = mon_crit_multi[f"RANK{rank}_CRIT_MULTI"]
        item_drop = mon_drop_chance[f"RANK{rank}_DROP_CHANCE"]
        max_xp = mon_xp[f"RANK{rank}_XP"]

        print(f"Building {monster}")
        return Monster(
            name=monster,
            url=mon_data["url"],
            sp_atk=mon_data["text"],
            max_hp=random.randint(max_hp // 2, max_hp),
            atk=random.randint(max_dmg // 2, max_dmg),
            defense=random.randint(max_def // 2, max_def),
            inish=random.randint(max_inish // 2, max_inish),
            crit_chance=crit_chance,
            crit_multi=crit_multi,
            itm=self.item_generator.random_item(1, item_drop),
            xp=random.randint(max_xp - max_xp // 3, max_xp)
        )
