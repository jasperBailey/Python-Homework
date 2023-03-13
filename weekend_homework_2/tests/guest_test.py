import unittest
from src.karaoke import *

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest = Guest("Jasper", 20.0)

    def test_has_name(self):
        self.assertEqual("Jasper", self.guest.name)

    def test_can_afford_insufficient_funds(self):
        self.assertEqual(True, self.guest.can_afford(15.0))

    def test_can_afford_sufficient_funds(self):
        self.assertEqual(False, self.guest.can_afford(25.0))

    def test_deduct_cash(self):
        self.guest.deduct_cash(15.0)
        self.assertEqual(5.0, self.guest.cash)

    def test_deduct_cash_insufficient_funds(self):
        self.guest.deduct_cash(25.0)
        self.assertEqual(20.0, self.guest.cash)