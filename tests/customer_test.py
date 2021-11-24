import unittest

from src.customer import Customer
from src.pub import Pub
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer1 = Customer("George Bowen", 120.00)
        self.customer2 = Customer("Harry Smiles", 24.30)
        self.customer3 = Customer("Boris Johnson", 500.00)

    # def test_buy_drink_from_pub(self):
    #     customer = self.customer1
        
    #     self.buy_a_drink(customer, )       