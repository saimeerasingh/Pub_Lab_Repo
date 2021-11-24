import unittest

from src.customer import Customer
from src.pub import Pub
from src.drink import Drink


class TestPub(unittest.TestCase):

    def setUp(self):
        self.drink1 = Drink("Martini", 10.00, True)
        self.drink2 = Drink("Mojito", 7.50, True)
        self.drink3 = Drink("Apple Fizz", 3.20, False)
        self.drink_menu = [self.drink1, self.drink2, self.drink3]
        self.pub = Pub("The Prancing Pony", 100.00, self.drink_menu)


    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)


    def test_pub_has_cash(self):
        self.assertEqual(100.00, self.pub.till)


    def test_get_menu(self):
        self.pub.get_menu()
        self.assertEqual(self.drink_menu, self.pub.drink_menu)

    def test_get_till(self):
        self.pub.get_till()
        self.assertEqual(100.00, self.pub.till)


    def test_add_cash_to_till(self):
        self.pub.add_cash_to_till(10.00)
        self.assertEqual(110.00, self.pub.get_till())

    # def test_can_get_drink_by_name(self):
    #     drink = self.pub.get_drink_by_name("Mojito")
    #     self.assertEqual(("Mojito", 7.50, True), drink[drink.name])



