# Package imports
import unittest

# Local imports
from src.weapon import WeaponGenerator


class WeaponGeneratorTest(unittest.TestCase):
    def setUp(self):
        self.generator = WeaponGenerator()

    def test_random_weapon(self):

        for _ in range(100):
            rand_weapon = self.generator.random_weapon(rank=1)

            max_atk = 0
            max_def = 0

            for weapon in self.generator.weapons[1]:
                if weapon.name == rand_weapon.name:
                    max_atk = weapon.bonus_atk
                    max_def = weapon.bonus_defense

            self.assertGreaterEqual(rand_weapon.bonus_atk, max_atk//2,
                                    "Random weapon rolled a weapon with bonus atk stats less than expected minimum")
            self.assertGreaterEqual(rand_weapon.bonus_defense, max_def//2,
                                    "Random weapon rolled a weapon with bonus def stats less than expected minimum")
            self.assertLessEqual(rand_weapon.bonus_atk, max_atk,
                                 "Random weapon rolled a weapon with bonus atk greater than expected maximum")
            self.assertLessEqual(rand_weapon.bonus_defense, max_def,
                                 "Random weapon rolled a weapon with bonus defense greater than expected maximum")

