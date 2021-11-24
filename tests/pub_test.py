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


    def test_add_drink_to_menu(self):
        new_drink = ("Diet Coke", 2.50, False)
        self.pub.add_drink_to_menu(new_drink)
        self.assertEqual(4, len(self.drink_menu))

    def test_remove_drink_from_menu(self):
        removed_drink = self.drink_menu[1]
        self.pub.remove_drink_from_menu(removed_drink)
        self.assertEqual(2, len(self.drink_menu))

    
    def test_can_get_drink_by_name(self):
        drink = self.pub.get_drink_by_name("Mojito")
        self.assertEqual("Mojito", drink.name)

    def test_can_get_drink_price(self):
        drink = self.pub.get_drink_price("Martini")
        self.assertEqual(10.00, drink)


    def test_can_customer_buy_drink(self):
        customer = Customer("George Bowen", 120.00)
        self.pub.sell_drink_to_customer(customer, "Mojito")
        self.assertEqual(1, len(customer.intake))
        self.assertEqual(112.50, customer.wallet)
        self.assertEqual(107.50, self.pub.get_till())


    
        



