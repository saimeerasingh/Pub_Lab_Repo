import unittest

from src.customer import Customer
from src.pub import Pub
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink1 = Drink("Martini", 10.00, True)

def test_check_if_drink_is_non_alcoholic(self):
    is_non_alcoholic = self.drink3.is_non_alcoholic_drink()
    self.assertEqual( False , is_non_alcoholic)