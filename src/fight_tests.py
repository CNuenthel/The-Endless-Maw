import unittest
from src.monster import MonsterBuilder
from src.hero import Hero
from src.battle import Battle

hero = Hero(hero_name="Test", player_id=1234, player_name="Discord_User")
monster = MonsterBuilder().generate_monster(rank=1)
battle = Battle(hero, monster)
print(monster.initiative)

class BattleTest(unittest.TestCase):
    def test_roll_initiative(self):
        for _ in range(10):
            battle.roll_initiative()
            self.assertGreaterEqual(battle.hero_initiative, hero.initiative // 2)
            self.assertLessEqual(battle.hero_initiative, hero.initiative)
            self.assertGreaterEqual(battle.monster_initiative, monster.initiative // 2)
            self.assertLessEqual(battle.monster_initiative, monster.initiative)
