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

    def load_monster_configurations(self, file_path: str):
        with open(file_path, "r") as f:
            monster_configs = yaml.safe_load(f)

        self.mon_dmg = monster_configs.get("Monster_Damage", {})
        self.mon_def = monster_configs.get("Monster_Defense", {})
        self.mon_hp = monster_configs.get("Monster_HP", {})
        self.mon_drop_chance = monster_configs.get("Monster_Item_Drop_Chance", {})
        self.mon_xp = monster_configs.get("Monster_XP", {})
        self.mon_inish = monster_configs.get("Monster_Initiative", {})
        self.mon_crit = monster_configs.get("Monster_Crit", {})
        self.mon_crit_multi = monster_configs.get("Monster_Crit_Multiplier", {})

    def load_monster_profiles(self):
        for i in range(1, 11):
            with open(f"monster_profiles/rank{i}.json", "r") as f:
                self.monster_ranks[i] = json.load(f)

    def generate_monster(self, rank: int) -> Monster:
        if rank < 1 or rank > 10:
            raise ValueError("Monster rank must be between 1 and 10")

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
            xp=random.randint(max_xp - max_xp // 3, max_xp)
        )
