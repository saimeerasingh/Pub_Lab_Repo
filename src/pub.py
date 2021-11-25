from src.customer import Customer
from src.drink import Drink


class Pub:
    def __init__(self, name, till, drink_menu):
        self.name = name
        self.till = till
        self.drink_menu = drink_menu
        self.drinks_sold = 0

    
    def get_menu(self):
        return self.drink_menu

    def get_till(self):
        return self.till

    def add_cash_to_till(self, amount):
        self.till += amount

    def add_drink_to_menu(self, new_drink):
        self.drink_menu.append(new_drink)

    def remove_drink_from_menu(self, removed_drink):
        self.drink_menu.remove(removed_drink)


    def get_drink_by_name(self, drink_name):
        for drink in self.drink_menu:
            if drink_name == drink.name:
                return drink.name


    def get_drink_price(self,drink_name):
        for drink in self.drink_menu:
            if drink_name == drink.name:
                return drink.price
                
    
    def sell_drink_to_customer(self, customer, drink):
        drink_price = self.get_drink_price(drink)
        customer.add_drink_to_customer(drink)
        customer.reduce_cash(drink_price)
        self.add_cash_to_till(drink_price)
   
    def find_alcoholic_drink(self,drink_name):
        for drink in self.drink_menu:
            if drink.name == drink_name:
                return drink.alcohol_status

    def find_non_alcoholic_drink(self):
        for drink in self.drink_menu:
            if drink.alcohol_status == False:
                return drink.name

    def can_buy_alcohol(self,customer,drink):
        customer.is_of_legal_age()    
        drink.is_non_alcoholic_drink()
        return self.find_non_alcoholic_drink()
