import unittest
from src.hero import Hero


class HeroTest(unittest.TestCase):

    def setUp(self):
        self.hero = Hero(hero_name="Test", player_id=1234, player_name="discord_user")

    def test_roll_initiative(self):
        max_init = self.hero.initiative
        min_init = self.hero.initiative // 2

        for _ in range(100):
            initiative = self.hero.roll_initiative()
            self.assertGreaterEqual(initiative, min_init, "Hero initiative was rolled less than expected minimum")
            self.assertLessEqual(initiative, max_init, "Hero initiative was rolled greater than expected maximum")

    def test_roll_damage(self):
        max_atk = self.hero.atk + self.hero.bonus_atk
        max_dmg = int(max_atk * (self.hero.crit_multiplier + self.hero.bonus_crit_multiplier))
        min_dmg = max_atk // 2

        for _ in range(100):
            result = self.hero.roll_damage()
            self.assertGreaterEqual(result["dmg"], min_dmg, "Hero damage was rolled less than expected minimum")
            self.assertLessEqual(result["dmg"], max_dmg, "Hero damage was rolled greater than expected maximum")

    def test_apply_damage(self):
        hero_max_hp = self.hero.current_hp + self.hero.bonus_hp
        hero_max_def = self.hero.defense + self.hero.bonus_def

        expected_hero_hp = hero_max_hp + hero_max_def - 15

        self.hero.apply_damage(15)
        self.assertEqual(self.hero.current_hp, expected_hero_hp, "Damage was not correctly applied to hero HP")


