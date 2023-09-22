# Project: Python CLI Potion Shop
# by: @Brohmarr

# Welcome! You should now be equipped with everything you need to make a
#     complicated program that uses multiple classes that interact with
#     each other. This is where we turn the creativity over to you.
# 
# For this project, we want you to create a fully functional system that
#     involves multiple classes. We’ll give more details on the specific
#     requirements below.
# 
# We know that it can sometimes be hard to come up with an idea on your
#     own. Take some time to think of what you want to create — it truly
#     can be anything. This step is important! We want you to feel
#     motivated to complete this project, so pick something you’re
#     excited to make.

# Requirements:
# 
# [X] (1) You must create at least TWO classes;
# [ ] (2) Each of those classes must have at least THREE attributes and
#             THREE methods;
# [ ] (3) Your classes should be able to describe themselves (through a
#             __repr__() method);
# [ ] (4) Test all of the methods you created on at least TWO instances
#             of every one of your classes;
# [ ] (5) Create some methods, or additional attributes, that make your
#             two Classes able to interact with each other.


# This class represents the owner of the potion shop.
class ShopKeeper:
    def __init__(self, name: str, gold_owned: int):
        self.name = name
        self.gold_owned = gold_owned

# This class represents the potion shop itself.
class PotionShop:
    def __init__(self, name: str, owner: ShopKeeper):
        self.name = name
        self.owner = owner
        # {(key = item_name: str): (value = quantity_in_stock: int)}
        self.inventory = {}

# This class represents the items in the potion shop.
class Item():
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

# This class represents an adventurer (basically a client).
class Adventurer:
    def __init__(self, name: str, gold_owned: int):
        self.name = name
        self.gold_owned = gold_owned
