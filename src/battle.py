import random


# TODO TEST ALL THIS

class Battle:
    def __init__(self, hero, monster):
        self.first_attacker = None
        self.hero = hero
        self.monster = monster

        self.hero_attack = hero.atk + hero.bonus_atk
        self.hero_damage = 0
        self.hero_initiative = 0
        self.hero_defense = hero.defense + hero.bonus_def
        self.hero_flags = {"crit": False,
                           "dmg_mitigated": False}

        self.monster_attack = monster.atk
        self.monster_damage = 0
        self.monster_initiative = 0
        self.monster_flags = {"crit": False,
                              "dmg_mitigated": False}
        self.monster_defense = monster.defense

    def roll_initiative(self):
        self.hero_initiative = self.hero.roll_initiative()
        # TODO Add roll initiative to monster class

    def roll_hero_damage(self):
        self.hero_damage = self.hero.roll_damage()

    def roll_monster_damage(self):
        pass
        # TODO add roll damage to monster class
    
    def set_attack_order(self):
        if self.hero_initiative > self.monster_initiative:
            self.first_attacker = "Hero"
        else:
            self.first_attacker = "Monster"

    def check_damage_mitigation(self):
        if (self.hero_damage <= self.monster.defense or
                self.first_attacker == "Monster" and self.monster_damage - self.hero_defense >= self.hero.current_hp or
                self.hero_flags["dmg_mitigated"]):
            self.hero_flags["dmg_mitigated"] = True
            self.hero_damage = 0

        if (self.monster_damage <= self.hero_defense or
                self.first_attacker == "Hero" and self.hero_damage - self.monster.defense >= self.monster.current_hp or
                self.monster.current_hp <= 0 or
                self.monster_flags["dmg_mitigated"]):
            self.monster_flags["dmg_mitigated"] = True
            self.monster_damage = 0

    def apply_damage(self):
        if not self.hero_flags["dmg_mitigated"]:
            self.hero_damage -= self.monster.defense
            self.monster.current_hp -= self.hero_damage
            if self.monster.current_hp < 0:
                self.monster.current_hp = 0
        else:
            print("hero_damage_mitigated")

        if not self.monster_flags["dmg_mitigated"]:
            self.monster_damage -= self.hero_defense
            self.hero.current_hp -= self.monster_damage
        else:
            print("monster damage mitigated")
