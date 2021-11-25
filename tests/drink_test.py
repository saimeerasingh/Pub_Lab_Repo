import unittest

from src.customer import Customer
from src.pub import Pub
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink1 = Drink("Martini", 10.00, True)
        self.drink2 = Drink("Mojito", 7.50, True)
        self.drink3 = Drink("Apple Fizz", 3.20, False)
        self.drink_menu = [self.drink1, self.drink2, self.drink3]
        

    def test_check_if_drink_is_non_alcoholic(self):
         self.assertEqual(False, self.alcohol_status)