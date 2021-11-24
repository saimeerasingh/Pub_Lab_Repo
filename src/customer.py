class Customer:
    def __init__(self, name, wallet,age):
        self.name = name
        self.intake = []
        self.wallet = wallet
        self.age = age

    def add_drink_to_customer(self, drink):
        self.intake.append(drink)

    
    def reduce_cash(self,amount):
        self.wallet -= amount

    
        

