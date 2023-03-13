from src.food import *
import unittest

class TestFood(unittest.TestCase):
    
    def setUp(self):
        self.food = Food("chips", 3.00, 3)

    def test_has_name(self):
        self.assertEqual("chips", self.food.name)

    def test_has_price(self):
        self.assertEqual(3.00, self.food.price)

    def test_rejuvenation_level(self):
        self.assertEqual(3, self.food.rejuvenation_level)
