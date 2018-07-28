from decimal import getcontext, Decimal

getcontext().prec = 3
Decimal(1) / Decimal(3)

class Product(object):
    def __init__(self, price, item_name, weight, brand, status):
        
        self.price = price + (price * 0.15)
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = 'for sale'

    
    def display_all(self):
        print 'Price: $' + str(self.price)
        print 'Item: ' + self.item_name
        print 'Weight: ' + str(self.weight) + 'LB.'
        print 'Brand: ' + self.brand
        print 'Status: ' + str(self.status)
    

product1 = Product(1.99, 'Chicken Soup', 0.75, 'Campbells', 'box')
product1.sell()