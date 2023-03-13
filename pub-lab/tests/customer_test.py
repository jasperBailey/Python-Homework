from src.customer import *
from src.drink import *
from src.food import *
import unittest

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer("Sarah", 10.00, 21)
        self.tennents = Drink("Tennent's", 3.80, 3)
        self.guinness = Drink("Guinness", 5.20, 2)
        self.chips = Food("chips", 3.00, 3)
        self.pizza = Food("pizza", 9.00, 6)

    def test_has_name(self):
        self.assertEqual("Sarah", self.customer.name)

    def test_has_wallet(self):
        self.assertEqual(10.00, self.customer.wallet)

    def test_deduct_from_wallet(self):
        self.customer.deduct_from_wallet(4.40)
        self.assertEqual(5.60, self.customer.wallet)

    def test_check_money(self):
        expected = True
        actual = self.customer.check_money(.50)
        self.assertEqual(expected, actual)

    def test_check_money_insufficient_funds(self):
        expected = False
        actual = self.customer.check_money(100)
        self.assertEqual(expected, actual)

    def test_drink_drink(self):
        self.customer.drink_drink(self.guinness)
        self.assertEqual(2, self.customer.drunkenness)

    def test_eat_food_not_drunk(self):
        self.customer.eat_food(self.chips)
        self.assertEqual(0, self.customer.drunkenness)

    def test_eat_food_slightly_drunk(self):
        self.customer.eat_food(self.pizza)
        self.assertEqual(0, self.customer.drunkenness)

    def test_eat_food_more_drunk(self):
        self.customer.drink_drink(self.guinness)
        self.customer.drink_drink(self.guinness)
        self.customer.eat_food(self.chips)
        self.assertEqual(1, self.customer.drunkenness)