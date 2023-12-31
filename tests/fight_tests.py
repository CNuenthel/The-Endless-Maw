# Package imports
import unittest

# Local imports
from src.monster import MonsterBuilder
from src.hero import Hero
from src.battle import Battle


class BattleTest(unittest.TestCase):
    def setUp(self):
        self.hero = Hero(hero_name="Test", player_id=1234, player_name="discord_user")
        self.monster = MonsterBuilder().generate_monster(rank=1)
        self.battle = Battle(self.hero, self.monster)

    def test_roll_hero_damage(self):
        max_atk = self.hero.atk + self.hero.bonus_atk
        max_crit = self.hero.crit_multiplier + self.hero.bonus_crit_multiplier

        min_dmg = int(max_atk // 2)
        max_dmg = int(max_atk * max_crit)

        for _ in range(50):
            self.battle.roll_hero_damage()
            self.assertGreaterEqual(self.battle.hero_damage, min_dmg, "Hero damage was less than expected minimum")
            self.assertLessEqual(self.battle.hero_damage, max_dmg, "Hero damage was greater than expected maximum")

    def test_roll_monster_damage(self):
        min_dmg = self.monster.atk // 2
        max_dmg = int(self.monster.atk * self.monster.crit_multi)

        for _ in range(100):
            self.battle.roll_monster_damage()
            self.assertGreaterEqual(self.battle.monster_damage, min_dmg,
                                    "Monster damage was less than expected minimum")
            self.assertLessEqual(self.battle.monster_damage, max_dmg,
                                 "Monster damage was greater than expected maximum")

    def test_roll_hero_initiative(self):
        min_initiative = self.hero.initiative // 2
        max_initiative = self.hero.initiative

        for _ in range(100):
            self.battle.roll_hero_initiative()
            self.assertGreaterEqual(self.battle.hero_initiative, min_initiative,
                                    "Hero initiative was lower than expected minimum")
            self.assertLessEqual(self.battle.hero_initiative, max_initiative,
                                 "Hero initiative was greater than expected maximum")

    def test_roll_monster_initiative(self):
        min_initiative = self.monster.initiative // 2
        max_initiative = self.monster.initiative

        for _ in range(100):
            self.battle.roll_monster_initiative()
            self.assertGreaterEqual(self.battle.monster_initiative, min_initiative,
                                    "Monster initiative was lower than expected minimum")
            self.assertLessEqual(self.battle.monster_initiative, max_initiative,
                                 "Monster initiative was greater than expected maximum")

    def test_set_attack_order(self):
        self.battle.hero_initiative = 1
        self.battle.monster_initiative = 2

        self.battle.set_attack_order()
        self.assertEqual(self.battle.first_attacker, "monster", "Attack order was improperly set")

        self.battle.hero_initiative = 2
        self.battle.monster_initiative = 1

        self.battle.set_attack_order()
        self.assertEqual(self.battle.first_attacker, "hero", "Attack order was improperly set")

    def test_apply_damage(self):
        self.battle.hero_damage = 15
        self.battle.monster_damage = 15

        expected_damage_to_hero = 15 - self.battle.hero.defense - self.battle.hero.bonus_def
        expected_hero_hp = self.battle.hero.current_hp + self.battle.hero.bonus_hp - expected_damage_to_hero

        expected_damage_to_monster = 15 - self.battle.monster.defense
        expected_monster_hp = self.battle.monster.current_hp - expected_damage_to_monster

        self.battle.apply_damage()
        self.assertEqual(self.battle.hero.current_hp, expected_hero_hp,
                         "Damage calculation against hero is not accurate")
        self.assertEqual(self.battle.monster.current_hp, expected_monster_hp,
                         "Damage calculation against monster is not accurate")









