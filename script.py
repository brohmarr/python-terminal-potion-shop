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
# [X] (2) Each of those classes must have at least THREE attributes and
#             THREE methods;
# [X] (3) Your classes should be able to describe themselves (through a
#             __repr__() method);
# [X] (4) Test all of the methods you created on every one of your
#             classes;
# [X] (5) Create some methods, or additional attributes, that make two
#             Classes able to interact with each other.


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
    
    def respond_the_customer(self):
        print("Of course! This is what I have in stock today.")
    
    def try_to_sell(self):
        print("So, which one?")
    
    def ask_for_the_quantity(self):
        print("How many?")
    
    def sell_item(self, item_name: str, quantity: int):
        print("Here you go, {quantity}x [{item_name}]!".format(
                    quantity = quantity,
                    item_name = item_name
                ))

    def not_enough_in_stock(self, inventory: dict, item: Item):
        print("I can only sell you {quantity_in_stock}".format(
                    quantity_in_stock = inventory[item]
                ) + " of that item. Would that be enough, adventurer?")
    
    def item_not_in_stock(self):
        print("Unfortunatelly, I don't have that one.")

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
    
    def not_enough_gold(self):
        print("Wait... That's pretty expensive, I can't afford that...")
    
    def say_farewell(self):
        print("Thank you, potion seller! You're much better than the other fool I visited before coming here!")

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
        for potion in self.inventory:
            if item.name.lower() == potion.name.lower():
                return True
        return False

    def add_to_inventory(self, item: Item, quantity: int):
        if self.is_item_in_stock(item):
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity
        print("Added {quantity}x [{item_name}] to the stock!".format(
                quantity = quantity,
                item_name = item.name
            ))
    
    def remove_from_inventory(self, item: Item, quantity: int):
        if item in self.inventory:
            if self.inventory[item] >= quantity:
                if self.inventory[item] > quantity:
                    self.inventory[item] -= quantity
                else:
                    self.inventory.pop(item)
                self.owner.sell_item(item.name, quantity)
                
                return True
            
            else:
                self.owner.not_enough_in_stock(self.inventory, item)
                
                return False
        else:
            self.owner.item_not_in_stock()

            return False
    
    def check_if_adventurer_has_gold(self, cost: int):
        if self.adventurer.gold_owned >= cost:
            return True
        else:
            return False

    def ask_the_user_for_another_input(self):
        print("I'm sorry, I didn't quite understand that...")

    def display_inventory(self):
        print()
        for item in self.inventory:
            print("[{name}] - Level {level} ~ {price} G".format(
                name = item.name,
                level = item.level,
                price = item.price
            ))
        print()

    def display_chat_prefix(self, character):
        print("<{character}> ".format(character = character.name), end = "")

    def close_sale(self, final_cost: int):
        self.adventurer.gold_owned -= final_cost
        self.owner.gold_owned += final_cost

        self.display_chat_prefix(self.adventurer)
        self.adventurer.say_farewell()

    def start_characters_interaction(self):
        # Declaring available items...
        lesser_health_potion = Item("Lesser Health Potion", 5, 50, "Recovers a small amount of HP.")
        health_potion = Item("Health Potion", 15, 100, "Recovers a decent amount of HP.")
        greater_health_potion = Item("Greater Health Potion", 25, 200, "Recovers a large amount of HP.")
        
        # Restocking...
        self.add_to_inventory(lesser_health_potion, 2)
        self.add_to_inventory(health_potion, 2)
        self.add_to_inventory(greater_health_potion, 2)
        
        # The adventurer arrives at the potion shop.
        print("\n{adventurer_name}, the fighter, arrives at the".format(
            adventurer_name = self.adventurer.name
        ) + " {potion_shop_name}...\n".format(
            potion_shop_name = self.name
        ))

        # The owner greets the adventurer.
        self.display_chat_prefix(self.owner)
        self.owner.greet_customer()

        # The adventurer greets the owner.
        self.display_chat_prefix(self.adventurer)
        self.adventurer.greet_potion_seller()

        # The owner responds the adventurer.
        self.display_chat_prefix(self.owner)
        self.owner.respond_the_customer()

        # Displays the current inventory to the user.
        self.display_inventory()

        # The owner tries to sell his potions.
        self.display_chat_prefix(self.owner)
        self.owner.try_to_sell()

        # Starts the user interaction part.
        is_sale_done = False

        while not is_sale_done:
            # Asks the user to choose an item to buy.
            self.display_chat_prefix(self.adventurer)
            desired_potion = input("I want the ")
            
            if (desired_potion.lower() == "lesser health potion") or (desired_potion.lower() == "health potion") or (desired_potion.lower() == "greater health potion"):
                # Gets the corresponding Item object.
                if (desired_potion.lower() == "lesser health potion"):
                    desired_potion = lesser_health_potion
                elif (desired_potion.lower() == "health potion"):
                    desired_potion = health_potion
                else:
                    desired_potion = greater_health_potion
                
                # Finds the chosen Item object in the inventory
                #     dictionary.
                for key in self.inventory:
                    if key == desired_potion:
                        desired_potion = key
                
                while True:
                    # Asks the user how many of the chosen item they
                    #     want to buy.
                    self.display_chat_prefix(self.owner)
                    self.owner.ask_for_the_quantity()

                    while True:
                        self.display_chat_prefix(self.adventurer)
                        desired_quantity = input()

                        # Checks if the user typed a valid answer (positive integer).
                        if desired_quantity.isnumeric():
                            desired_quantity = int(desired_quantity)

                            # Checks if the adventurer has enough gold.
                            final_cost = desired_potion.price * desired_quantity

                            if self.check_if_adventurer_has_gold(final_cost):
                                self.display_chat_prefix(self.owner)
                                is_sale_done = self.remove_from_inventory(desired_potion, desired_quantity)

                                # Checks for the owner's answer.
                                if is_sale_done:
                                    self.close_sale(final_cost)
                                    
                                    break
                                else:
                                    answer = ""
                                    while True and answer.lower() != "no" and answer.lower() != "n":
                                        self.display_chat_prefix(self.adventurer)
                                        answer = input("(Yes/No) ")

                                        if answer.lower() == "yes" or answer.lower() == "y":
                                            self.close_sale(final_cost)
                                            is_sale_done = True
                                            
                                            break
                                        elif answer.lower() == "no" or answer.lower() == "n":
                                            break
                                        else:
                                            self.display_chat_prefix(self.owner)
                                            self.ask_the_user_for_another_input()
                                    
                                    break
                            else:
                                self.display_chat_prefix(self.adventurer)
                                self.adventurer.not_enough_gold()
                        else:
                            self.display_chat_prefix(self.owner)
                            self.ask_the_user_for_another_input()
                    
                    break
            else:
                self.display_chat_prefix(self.owner)
                self.owner.item_not_in_stock()
        
        print("\nTHE END\n")

# # TESTING PHASE
# print("\nInitializing Internal Testing...\n")

# print("Testing '__init__' and '__repr__' methods...")
# print("---\n")

# shopkeeper = Shopkeeper("Guy", 100)
# print(shopkeeper)

# potion_of_health = Item("Potion of Health", 5, 50, "Recovers HP.")
# print(potion_of_health)

# adventurer = Adventurer("Chad", "Fighter", 500)
# print(adventurer)

# potion_shop = PotionShop("Potion Place", shopkeeper, adventurer)
# print(potion_shop)

# print("\n---")
# print("Great success!")
# print("---\n")

# print("Testing the shop's inventory management...")
# print("---\n")

# potion_shop.add_to_inventory(potion_of_health, 1)
# print()
# potion_shop.remove_from_inventory(potion_of_health, 2)
# print()
# potion_shop.add_to_inventory(potion_of_health, 1)
# print()
# print(potion_shop.inventory)
# print()
# potion_shop.remove_from_inventory(potion_of_health, 2)
# print()
# print(potion_shop.inventory)

# print("\n---")
# print("Great success!")
# print("---\n")

shopkeeper = Shopkeeper("Guy", 100)
adventurer = Adventurer("Chad", "Fighter", 200)
potion_shop = PotionShop("Potion Place", shopkeeper, adventurer)

potion_shop.start_characters_interaction()
