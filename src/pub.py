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


    # def get_drink_by_name(self, drink_name):
    #     for drink in self.drink_menu:
    #         if drink_name == drink.name:
    #             return drink
    #         else:
    #             return None