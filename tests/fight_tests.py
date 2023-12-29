import unittest
from src.monster import MonsterBuilder
from src.hero import Hero
from src.battle import Battle

hero = Hero(hero_name="Test", player_id=1234, player_name="Discord_User")
monster = MonsterBuilder().generate_monster(rank=1)
battle = Battle(hero, monster)

class BattleTest(unittest.TestCase):
    # TODO