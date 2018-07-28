import random

class Bike(object):
    def __init__(self, price, max_speed, miles):
        
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    
    def displayInfo(self):
        print 'Price is: $' + str(self.price)
        print 'Max speed: ' + str(self.max_speed) + 'mph'
        print 'Total miles: ' + str(self.miles) + ' miles'
    
    def ride(self):
        self.miles = self.miles + random.randint(1,10)
        print 'I rode ' + str(self.miles) + ' miles.'

    def reverse(self):
        self.miles = self.miles - random.randint(1, 10)
        print 'I reversed ' + str(self.miles) + ' miles.'
    

bike1 = Bike(99.99, 12, 0)
bike1.displayInfo()
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()

bike2 = Bike(5, 2, 0)
bike2.displayInfo()
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()