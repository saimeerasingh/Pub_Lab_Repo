import unittest

from src.customer import Customer
from src.pub import Pub
from src.drink import Drink


class TestPub(unittest.TestCase):

    def setUp(self):
        self.drink1 = Drink("Martini", 10.00, True)
        self.drink2 = Drink("Mojito", 7.50, True)
        self.drink3 = Drink("Apple Fizz", 3.20, False)
        drink_menu = [self.drink1, self.drink2, self.drink3]
        self.pub = Pub("The Prancing Pony", 100.00, drink_menu)


    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)


    def test_pub_has_cash(self):
        self.assertEqual(100.00, self.pub.cash)


    def test_get_menu(self):
        drink_menu = ["Martini", 10.00, True, "Apple Fizz", 3.20, False, "Apple Fizz", 3.20, False]
        self.pub.get_menu()
        self.assertEqual(drink_menu, self.pub.drink_menu)



    # "Martini", 10.00, True, "Apple Fizz", 3.20, False, "Apple Fizz", 3.20, False