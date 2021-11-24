class Pub:
    def __init__(self, name, cash, drink_menu):
        self.name = name
        self.cash = cash
        self.drink_menu = drink_menu
        self.drinks_sold = 0

    
    def get_menu(self):
        return self.drink_menu
