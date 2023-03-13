from src.food import Food
from src.drink import Drink

class Customer:
    
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = 0

    def deduct_from_wallet(self, amount):
        self.wallet -= amount

    def check_money(self, amount):
        return self.wallet >= amount
    
    def drink_drink(self, drink):
        self.drunkenness += drink.alcohol_level

    def eat_food(self, food):
        self.drunkenness = max(0,
            self.drunkenness - food.rejuvenation_level)
        
    def consume(self, item):
        if type(item) == Drink:
            self.drink_drink(item)
        elif type(item) == Food:
            self.eat_food(item)

    