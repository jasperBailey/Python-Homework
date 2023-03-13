from src.drink import Drink
from src.food import Food

class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.stock = []

    def add_item_to_stock(self, item):
        self.stock.append(item)

    def add_money_to_till(self, amount):
        self.till += amount

    def find_item_by_name(self, item_name):
        for item in self.stock:
            if item.name == item_name:
                return item
            
    def take_order(self, customer, item_name):
        # check customer_age
        # check find_drink_by_name
        # check customer has enough money
        # if all True, call serve drink function

        item = self.find_item_by_name(item_name)
        if item and self.can_serve(customer, item):
            customer.deduct_from_wallet(item.price)
            self.add_money_to_till(item.price)
            customer.consume(item)
        else:
            print("GET OUT OF MY PUB!")

    def can_serve(self, customer, item):
        if type(item) == Drink:
            if self.customer_too_drunk(customer):
                return False
            if self.customer_underage(customer):
                return False
        if not self.customer_can_afford(customer):
            return False
        return True

    def customer_too_drunk(self, customer):
        return customer.drunkenness > 15
    
    def customer_underage(self, customer):
        return customer.age < 18
    
    def customer_can_afford(self, customer, amount):
        return customer.check_money(amount)
    