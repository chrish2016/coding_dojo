import random

class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 2000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.display_all()
    
    def display_all(self):
        print 'Price: $' + str(self.price)
        print 'Speed: ' + str(self.speed) + 'mph'
        print 'Fuel: ' + str(self.fuel)
        print 'Mileage: ' + str(self.mileage)
        print 'Tax: ' + str(self.tax)
    

car1 = Car(2000, 35, 'Full', 15)
car2 = Car(2001, 5, 'Not Full', 105)
car3 = Car(1999, 15, 'Kind of Full', 95)
car4 = Car(2000, 25, 'Full', 25)
car5 = Car(2000, 45, 'Empty', 25)
