class Sneakers:
        def __init__(self, name, price, size):
            self.name = name
            self.price = price
            self.size = size
        def set_price (self, price):
             if price < 0:
                print("Price cannot be below zero.")
             else:
                  self.price = price 
