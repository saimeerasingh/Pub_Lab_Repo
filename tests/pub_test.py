import unittest

from src.customer import Customer
from src.pub import Pub
from src.drink import Drink


class TestPub(unittest.TestCase):

    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)

    

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)


    def test_pub_has_cash(self):
        self.assertEqual(100.00, self.pub.cash)




    