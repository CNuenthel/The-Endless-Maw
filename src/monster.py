# Package imports
import random
import json
import yaml

# Internal file imports
import item


class Monster:
    def __init__(self, name: str, url: str, sp_atk: str, max_hp: int, atk: int, defense: int, inish: int,
                 crit_chance: int, crit_multi: float, itm: str, xp: int, gold: int):
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
        self.gold = gold

    def __repr__(self):
        return self.name

    def roll_initiative(self):
        return random.randint(self.initiative // 2, self.initiative)

    def roll_damage(self):
        damage = random.randint(self.atk // 2, self.atk)

        if random.randint(1, self.crit_chance) == 1:
            damage = int(damage * self.crit_multi)
            return {"crit": True, "dmg": damage}

        return {"crit": False, "dmg": damage}

    def take_damage(self, damage: int) -> dict:
        net_damage = max(damage - self.defense, 0)
        self.current_hp = max(self.current_hp - net_damage, 0)

        if net_damage == 0:
            return {"dmg_mitigated": True, "current_hp": self.current_hp}
        return {"dmg_mitigated": False, "current_hp": self.current_hp}


class MonsterBuilder:
    def __init__(self):
        self.item_generator = item.Items()
        self.monster_ranks = {}
        self.mon_dmg = None
        self.mon_def = None
        self.mon_hp = None
        self.mon_drop_chance = None
        self.mon_xp = None
        self.mon_inish = None
        self.mon_crit = None
        self.mon_crit_multi = None

        self._load_monster_configurations()
        self._load_monster_profiles()

    def _load_monster_configurations(self):
        """
        Loads monster configurations from yaml file.
        """
        print("Loading monster configurations...")
        with open("monster_profiles/monster_config.yaml", "r") as f:
            monster_configs = yaml.safe_load(f)

        self.mon_dmg = monster_configs.get("Monster_Damage", {})
        self.mon_def = monster_configs.get("Monster_Defense", {})
        self.mon_hp = monster_configs.get("Monster_HP", {})
        self.mon_drop_chance = monster_configs.get("Monster_Item_Drop_Chance", {})
        self.mon_xp = monster_configs.get("Monster_XP", {})
        self.mon_inish = monster_configs.get("Monster_Initiative", {})
        self.mon_crit = monster_configs.get("Monster_Crit", {})
        self.mon_crit_multi = monster_configs.get("Monster_Crit_Multiplier", {})
        self.mon_gold = monster_configs.get("Monster_Gold", {})

    def _load_monster_profiles(self):
        """
        Loads monster data from rank json files. If additional ranks are added
        the range will need to be altered to accommodate loading that profile
        """
        print("Loading monster profiles...")
        for i in range(1, 11):
            with open(f"monster_profiles/rank{i}.json", "r") as f:
                self.monster_ranks[i] = json.load(f)

    def generate_monster(self, rank: int) -> Monster:
        rank_data = self.monster_ranks[rank]
        selected_monster = random.choice(list(rank_data.keys()))
        mon_data = rank_data[selected_monster]

        max_dmg = self.mon_dmg.get(f"RANK{rank}_MAX_DMG", 0)
        max_def = self.mon_def.get(f"RANK{rank}_DEFENSE", 0)
        max_hp = self.mon_hp.get(f"RANK{rank}_MAX_HP", 0)
        max_inish = self.mon_inish.get(f"RANK{rank}_INITIATIVE", 0)
        crit_chance = self.mon_crit.get(f"RANK{rank}_CRIT", 0)
        crit_multi = self.mon_crit_multi.get(f"RANK{rank}_CRIT_MULTI", 0)
        item_drop = self.mon_drop_chance.get(f"RANK{rank}_DROP_CHANCE", 0)
        max_xp = self.mon_xp.get(f"RANK{rank}_XP", 0)
        max_gold = self.mon_gold.get(f"RANK{rank}_GOLD", 0)

        return Monster(
            name=selected_monster,
            url=mon_data.get("url", ""),
            sp_atk=mon_data.get("text", ""),
            max_hp=random.randint(max_hp // 2, max_hp),
            atk=random.randint(max_dmg // 2, max_dmg),
            defense=random.randint(max_def // 2, max_def),
            inish=random.randint(max_inish // 2, max_inish),
            crit_chance=crit_chance,
            crit_multi=crit_multi,
            itm=self.item_generator.random_item(1, item_drop),
            xp=random.randint(max_xp - max_xp // 3, max_xp),
            gold=random.randint(max_gold//2, max_gold)
        )
