class Drink:
    def __init__(self, name, price, alcohol_status):
        self.name = name
        self.price = price
        self.alcohol_status = alcohol_status
    
    def is_non_alcoholic_drink(self):
        if self.alcohol_status == False:
            return self.name
