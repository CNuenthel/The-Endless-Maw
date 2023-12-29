import random


# TODO TEST ALL THIS

class Battle:
    def __init__(self, hero, monster):
        self.first_attacker = None

        self.hero = hero
        self.monster = monster

        self.hero_damage = 0
        self.hero_flags = {"crit": False,
                           "dmg_mitigated": False}

        self.monster_damage = 0
        self.monster_flags = {"crit": False,
                              "dmg_mitigated": False}

    def roll_hero_damage(self):
        damage_roll = self.hero.roll_damage()
        self.hero_flags["crit"] = damage_roll["crit"]
        self.hero_damage = damage_roll["dmg"]

    def roll_monster_damage(self):
        damage_roll = self.monster.roll_damage()
        self.monster_flags["crit"] = damage_roll["crit"]
        self.monster_damage = damage_roll["dmg"]
    
    def set_attack_order(self):
        if self.hero.roll_initiative() >= self.monster.roll_initiative():
            self.first_attacker = "hero"
        else:
            self.first_attacker = "monster"

    def apply_damage(self):
        if self.first_attacker == "hero":

            mon_result = self.monster.apply_damage(self.hero_damage)
            self.monster_flags["dmg_mitigated"] = mon_result["dmg_mitigated"]

            if mon_result["current_hp"] == 0:
                self.victory()
                return

            hero_result = self.hero.apply_damage(self.monster_damage)
            self.hero_flags["dmg_mitigated"] = hero_result["dmg_mitigated"]

            if hero_result["current_hp"] == 0:
                self.defeat()
                return  # Hero is dead

        else:
            hero_result = self.hero.apply_damage(self.monster_damage)
            self.hero_flags["dmg_mitigated"] = hero_result["dmg_mitigated"]

            if hero_result["current_hp"] == 0:
                self.defeat()
                return

            mon_result = self.monster.apply_damage(self.hero_damage)
            self.monster_flags["dmg_mitigated"] = mon_result["dmg_mitigated"]

            if mon_result["current_hp"] == 0:
                self.victory()
                return

    def victory(self):
        # Issue item/xp/gold to hero signalling death of monster
        pass

    def defeat(self):
        # Advise hero is dead/incapacitated
        pass