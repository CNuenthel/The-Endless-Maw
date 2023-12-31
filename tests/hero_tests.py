# Package imports
import unittest

# Local imports
from src.hero import Hero
from src.armor import ArmorGenerator
from src.weapon import WeaponGenerator


class HeroTest(unittest.TestCase):

    def setUp(self):
        self.hero = Hero(hero_name="Test", player_id=1234, player_name="discord_user")
        self.armor = ArmorGenerator().random_armor(rank=1)
        self.weapon = WeaponGenerator().random_weapon(rank=1)

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

        self.hero.take_damage(15)
        self.assertEqual(self.hero.current_hp, expected_hero_hp, "Damage was not correctly applied to hero HP")

    def test_equip_armor(self):
        expected_def = self.hero.bonus_def + self.armor.bonus_defense
        expected_hp = self.hero.bonus_hp + self.armor.bonus_hp

        self.hero.armory.append(self.armor)

        self.hero.equip_armor(self.armor.unique_id)
        self.assertEqual(self.hero.bonus_def, expected_def, "Equip armor failed to add to an expected bonus defense")
        self.assertEqual(self.hero.bonus_hp, expected_hp, "Equip armor failed to add to an expected bonus hp")
        self.assertEqual(self.hero.armor, self.armor, "Equip armor failed to set to hero armor attribute")

    def test_remove_armor(self):
        self.hero.armory.append(self.armor)
        self.hero.equip_armor(self.armor.unique_id)

        expected_def = self.hero.bonus_def - self.armor.bonus_defense
        expected_hp = self.hero.bonus_hp - self.armor.bonus_hp

        self.hero.remove_armor()
        self.assertEqual(self.hero.bonus_def, expected_def,
                         "Remove armor failed to remove the expected bonus defense from hero")
        self.assertEqual(self.hero.bonus_hp, expected_hp,
                         "Remove armor failed to remove the expected bonus hp from hero")
        self.assertEqual(self.hero.armor, None, "Remove armor failed to remove armor from hero armor attribute")

    def test_equip_weapon(self):
        expected_atk = self.hero.bonus_atk + self.weapon.bonus_atk
        expected_def = self.hero.bonus_def + self.weapon.bonus_defense

        self.hero.armory.append(self.weapon)

        self.hero.equip_weapon(self.weapon.unique_id)
        self.assertEqual(self.hero.bonus_atk, expected_atk, "Equip weapon failed to add to an expected bonus atk")
        self.assertEqual(self.hero.bonus_def, expected_def, "Equip weapon failed to add to an expected bonus def")
        self.assertEqual(self.hero.weapon, self.weapon, "Equip weapon failed to set hero weapon attribute")

    def test_remove_weapon(self):
        self.hero.armory.append(self.weapon)
        self.hero.equip_weapon(self.weapon.unique_id)

        expected_atk = self.hero.bonus_atk - self.weapon.bonus_atk
        expected_def = self.hero.bonus_def - self.weapon.bonus_defense

        self.hero.remove_weapon()
        self.assertEqual(self.hero.bonus_atk, expected_atk,
                         "Remove weapon failed to remove the expected bonus atk from hero")
        self.assertEqual(self.hero.bonus_def, expected_def,
                         "Remove weapon failed to remove the expected bonus def from hero")
        self.assertEqual(self.hero.weapon, None, "Remove weapon failed to remove weapon from hero weapon attribute")

