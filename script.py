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
    
    def greet_customer(self):
        print("Well hello, my friend! Welcome to my humble potion shop."
              + " What can I help you with today?")

# This class represents the items in the potion shop.
class Item():
    def __init__(self, name: str, level: int, price: int, effect: str):
        self.name = name
        self.level = level
        self.price = price
        self.effect = effect
    
    def __repr__(self):
        return "This is a Level {level} {name}, priced at {price}".format(
            name = self.name,
            level = self.level,
            price = self.price
        ) + " gold pieces. When used: {effect}".format(
            effect = self.effect
        )

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
    
    def greet_potion_seller(self):
        print("Hello, potion seller, I'm heading into battle, and I want"
              + " only your strongest potions.")

# This class represents the potion shop itself.
class PotionShop:
    def __init__(self, name: str, owner: Shopkeeper, adventurer: Adventurer):
        self.name = name
        self.owner = owner
        self.adventurer = adventurer
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
    
    def print_chat_prefix(self, character):
        print("<{character}> ".format(character = character.name), end = "")

    def start_characters_interaction(self):
        # Adventurer arrives at the potion shop...
        print("{adventurer_name}, the fighter, arrives at the".format(
            adventurer_name = self.adventurer.name
        ) + " {potion_shop_name}...\n".format(
            potion_shop_name = self.name
        ))

        # The owner greets the adventurer...
        self.print_chat_prefix(self.owner)
        self.owner.greet_customer()

        # The adventurer greets the owner...
        self.print_chat_prefix(adventurer)
        self.adventurer.greet_potion_seller()

        # Continue from here...

# TESTING PHASE
print("\nInitializing Internal Testing...\n")

print("Testing '__init__' and '__repr__' methods...")
print("---\n")

shopkeeper = Shopkeeper("Guy", 50)
print(shopkeeper)

potion_of_health = Item("Potion of Health", 5, 50, "Recovers HP.")
print(potion_of_health)

adventurer = Adventurer("Chad", "Fighter", 100)
print(adventurer)

potion_shop = PotionShop("Potion Place", shopkeeper, adventurer)
print(potion_shop)

print("\n---")
print("Great success!")
print("---\n")

print("Testing the shop's inventory management...")
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

print("\n---")
print("Great success!")
print("---\n")

print("Testing the characters interaction...")
print("---\n")

potion_shop.start_characters_interaction()

print("\n---")
print("Great success!")
print("---\n")
