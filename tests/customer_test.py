import unittest

from src.customer import Customer
from src.pub import Pub
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer1 = Customer("George Bowen", 120.00, 29)
        self.customer2 = Customer("Harry Smiles", 24.30, 15)
        self.customer3 = Customer("Boris Johnson", 500.00,54)

        self.customers = [self.customer1, self.customer2, self.customer3]


    def test_can_add_drink_to_customer(self):
        drink1 = Drink("Martini", 10.00, True)
        self.customer1.add_drink_to_customer(drink1)
        self.assertEqual(1,len(self.customer1.intake))

              
    def test_can_reduce_customer_cash(self):
        self.customer1.reduce_cash(10.00)
        self.assertEqual(110,self.customer1.wallet)

    def test_can_check_for_age(self):
        is_customer_of_legal_age = self.customer2.is_of_legal_age()
        self.assertEqual(False , is_customer_of_legal_age)

    