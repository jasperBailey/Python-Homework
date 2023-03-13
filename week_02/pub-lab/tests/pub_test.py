from src.pub import *
from src.drink import *
from src.food import *
from src.customer import *
import unittest

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Caley Sample Room", 1000.00)
        self.tennents = Drink("Tennent's", 3.80, 3)
        self.guinness = Drink("Guinness", 5.20, 2)
        self.customer = Customer("Sarah", 10.00, 21)

    def test_has_name(self):
        self.assertEqual("The Caley Sample Room", self.pub.name)

    def test_has_till(self):
        self.assertEqual(1000.00, self.pub.till)

    def test_add_drink(self):
        self.pub.add_item_to_stock(self.tennents)
        self.assertEqual(1, len(self.pub.get_drinks()))

    def test_add_money_to_till(self):
        self.pub.add_money_to_till(5.80)
        self.assertEqual(1005.80, self.pub.till)

    def test_find_drink_by_name(self):
        self.pub.add_item_to_stock(self.tennents)
        expected = self.tennents
        actual = self.pub.find_drink_by_name("Tennent's")
        self.assertEqual(expected, actual)

    def test_find_drink_by_name_not_found(self):
        expected = None
        actual = self.pub.find_drink_by_name("Tennent's")
        self.assertEqual(expected, actual)

    def test_request_serve_drink(self):
        self.pub.add_item_to_stock(self.tennents)
        self.pub.take_order(self.customer, "Tennent's")
        self.assertEqual(6.20, self.customer.wallet)
        self.assertEqual(1003.80, self.pub.till)

    def test_request_serve_drink_not_found(self):
        self.pub.take_order(self.customer, "Tennent's")
        self.assertEqual(10.00, self.customer.wallet)
        self.assertEqual(1000.00, self.pub.till)

    def test_request_serve_drink_insufficient_funds(self):
        customer = Customer("Jasper", 1.00, 24)
        self.pub.add_item_to_stock(self.tennents)
        self.pub.take_order(customer, "Tennent's")
        self.assertEqual(1.00, customer.wallet)
        self.assertEqual(1000.00, self.pub.till)
    
    def test_request_serve_drink_too_drunk(self):
        customer = Customer("Jasper", 50.00, 18)
        self.pub.add_item_to_stock(self.tennents)
        for i in range(7):
            self.pub.take_order(customer, "Tennent's")
        self.assertAlmostEqual(27.20, customer.wallet, 2)
        self.assertAlmostEqual(1022.80, self.pub.till, 2)
        self.assertEqual(18, customer.drunkenness)

    def test_request_serve_drink_underage(self):
        customer = Customer("Jasper", 10.00, 16)
        self.pub.add_item_to_stock(self.tennents)
        self.pub.take_order(customer, "Tennent's")
        self.assertEqual(10.00, customer.wallet)
        self.assertEqual(1000.00, self.pub.till)