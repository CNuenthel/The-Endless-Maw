import yaml
import random


# Load weapon configurations
with open("item_profiles/weapon_config.yaml", "r") as f:
    weapon_configs = yaml.safe_load(f)

wpn_ranks = {}
for rank_key, weapon in weapon_configs.items():
    wpn_ranks[rank_key] = list(weapon.keys())


# class Legendary:
#     def __init__(self):
#         self.legends = ["Rod Of Lordly Might", "Natures Mantle", "Vestige Blade", "Chidori",
#                         "Yamatos Training Katana", "Forbidden Fruit"]
