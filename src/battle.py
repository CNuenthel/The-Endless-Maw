
# Apply buff/debuff to both parties
# Apply damage of party 1 to party 2
# If party 2 is still alive, apply damage of party 2 to party 1
# Apply post fight changes
from hero import Hero
from monster import Monster
import random


class Battle:
    def __init__(self, hero: Hero, monster: Monster):
        self.hero = hero
        self.hero_damage = 0
        self.monster = monster
        self.monster_damage = 0
        self.combat_order = []
        self.hero_flags = {"crit": False}
        self.monster_flags = {"crit": False}

    def roll_initiative(self):
        monster_initiative = random.randint(1, self.monster.initiative)
        hero_initiative = random.randint(1, self.hero.initiative)

        if hero_initiative >= monster_initiative:
            self.combat_order.extend([self.hero, self.monster])
        else:
            self.combat_order.extend([self.monster, self.hero])

    def roll_crit(self):
        if random.randint(1, self.monster.crit_chance) == 1:
            self.monster_flags["crit"] = True
        if random.randint(1, self.hero.crit_chance) == 1:
            self.hero_flags["crit"] = True

    def roll_damage(self):
        self.hero_damage = random.randint(self.hero.atk//2, self.hero.atk)
        self.monster_damage = random.randint(self.monster.atk//2, self.monster.atk)

    def apply_hero_stat_changes(self):
        if self.hero_flags["crit"]:
            self.hero_damage = int(self.hero_damage * self.hero.crit_multiplier)

    def apply_monster_stat_changes(self):
        if self.monster_flags["crit"]:
            self.monster_damage = int(self.monster_damage * self.monster.crit_multi)

    def apply_damage(self):
        # TODO
        """ Current problem, need to assign damage in the correct order and then reference the appropriate damage
        I currently believe this can be done by mapping the hero damage to the hero object in the attack order, and the
        monster damage to the monster object in the attack order."""