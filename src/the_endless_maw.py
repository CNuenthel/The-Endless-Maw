# Package imports
import yaml
import random

# Local imports
from monster import MonsterBuilder, Monster


class TheEndlessMaw:
    def __init__(self):
        self.monsters = {}
        self.pool_sizes = {}
        self.monster_generator = MonsterBuilder()
        self.spawn_chances = {}
        self._load_configs()
        self._build_monsters()

    def _load_configs(self):
        print("Building the Maw...")
        with open("gameplay_profiles/the_endless_maw_config.yaml", "r") as f:
            maw_configs = yaml.safe_load(f)

        self.shard_drop_chance = maw_configs.get("Shard_Drop_Chance")
        for i in range(1, 10):
            self.pool_sizes[i] = maw_configs.get(f"Rank{i}_Pool", 0)
        for i in range(1, 10):
            self.spawn_chances[i] = maw_configs.get(f"Rank{i}_Spawn_Chance", 0)

    def _build_monsters(self):
        print("Flooding the maw...")

        for rank, count in self.pool_sizes.items():
            self.monsters[rank] = []
            for i in range(count):
                self.monsters[rank].append(self.monster_generator.generate_monster(rank))

    def roaming_monster(self):
        selected_rank = random.choices(
            list(self.spawn_chances.keys()),
            weights=list(self.spawn_chances.values())
        )[0]

        if len(self.monsters[selected_rank]) < self.pool_sizes[selected_rank]:
            roaming_monster = self.monster_generator.generate_monster(selected_rank)
            self.monsters[selected_rank].append(roaming_monster)

    def pull_random_monster(self, rank: int) -> Monster | None:
        if self.monsters[rank]:
            random_monster = random.choice(self.monsters[rank])
            index = self.monsters[rank].index(random_monster)
            return self.monsters[rank].pop(index)
        return None
