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
# [X] (3) Your classes should be able to describe themselves (through a
#             __repr__() method);
# [ ] (4) Test all of the methods you created on at least TWO instances
#             of every one of your classes;
# [ ] (5) Create some methods, or additional attributes, that make your
#             two Classes able to interact with each other.


# This class represents the owner of the potion shop.
class Shopkeeper:
    def __init__(self, name: str, gold_owned: int):
        self.name = name
        self.job = "Potion Seller"
        self.gold_owned = gold_owned
    
    def __repr__(self):
        return "This is {name}, the {job}.".format(
            name = self.name,
            job = self.job
        )

# This class represents the items in the potion shop.
class Item():
    def __init__(self, name: str, level: int, price: int):
        self.name = name
        self.level = level
        self.price = price
    
    def __repr__(self):
        return "This is a Level {level} {name}, priced at {price}".format(
            name = self.name,
            level = self.level,
            price = self.price
        ) + " gold pieces."

# This class represents the potion shop itself.
class PotionShop:
    def __init__(self, name: str, owner: Shopkeeper):
        self.name = name
        self.owner = owner
        # {(key = item_name: str): (value = quantity_in_stock: int)}
        self.inventory = {}
    
    def __repr__(self):
        return "This is {owner}'s potion shop, {name}!".format(
            owner = self.owner.name,
            name = self.name
        )
    
    def is_item_in_stock(self, item:Item):
        if item.name in self.inventory:
            return True
        else:
            return False

    def add_to_inventory(self, item: Item, amount: int):
        if self.is_item_in_stock(item):
            self.inventory[item.name] += amount
        else:
            self.inventory[item.name] = amount
        print("Added {amount}x [{item_name}] to the stock!".format(
                amount = amount,
                item_name = item.name
            ))
    
    def remove_from_inventory(self, item: Item, amount: int):
        if item.name in self.inventory:
            if self.inventory[item.name] >= amount:
                if self.inventory[item.name] > amount:
                    self.inventory[item.name] -= amount
                else:
                    self.inventory.pop(item.name)
                print("Here you go, {amount}x [{item_name}]!".format(
                    amount = amount,
                    item_name = item.name
                ))
            else:
                print("I can only sell you {inventory_amount}".format(
                    inventory_amount = self.inventory[item.name]
                ) + " of that item. Would that be enough, adventurer?")
        else:
            print("Unfortunatelly, I'm out of that one.")

# This class represents an adventurer (basically a client).
class Adventurer:
    def __init__(self, name: str, job: str, gold_owned: int):
        self.name = name
        self.job = job
        self.gold_owned = gold_owned
    
    def __repr__(self):
        return "This is {name}, the {job},".format(
            name = self.name,
            job = self.job
        ) + " and he is heading into battle!"

# TESTING PHASE
print("\nInitializing Internal Testing...\n")

print("Testing '__init__' and '__repr__' methods...\n")
print("---\n")

shopkeeper = Shopkeeper("Guy", 50)
print(shopkeeper)

potion_of_health = Item("Potion of Health", 99, 500)
print(potion_of_health)

potion_shop = PotionShop("Potion Place", shopkeeper)
print(potion_shop)

adventurer = Adventurer("Chad", "Fighter", 500)
print(adventurer)

print("\nGreat success!\n")
print("---\n")

print("Testing the shop's inventory management...\n")
print("---\n")

potion_shop.add_to_inventory(potion_of_health, 1)
print()
potion_shop.remove_from_inventory(potion_of_health, 2)
print()
potion_shop.add_to_inventory(potion_of_health, 1)
print()
print(potion_shop.inventory)
print()
potion_shop.remove_from_inventory(potion_of_health, 2)
print()
print(potion_shop.inventory)

print("\nGreat success!\n")
print("---\n")
