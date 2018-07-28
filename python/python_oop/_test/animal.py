class Vehicle(object):
    def __init__(self, wheels, capacity, make, model):
        self.wheels = wheels
        self.capacity = capacity
        self.make = make
        self.model = model
        self.mileage = 0
    def drive(self,miles):
        self.mileage += miles
        return self
    def reverse(self,miles):
        self.mileage -= miles
        return self
class Bike(Vehicle):
    def vehicle_type(self):
        return "Bike"
class Car(Vehicle):
    def set_wheels(self):
        self.wheels = 4
        return self
class Airplane(Vehicle):
    def fly(self, miles):
        self.mileage += miles
        return self
v = Vehicle(4,8,"dodge","minivan")
print v.make
b = Bike(2,1,"Schwinn","Paramount")
print b.vehicle_type()
c = Car(8,5,"Toyota", "Matrix")
c.set_wheels()
print c.wheels
a = Airplane(22,853,"Airbus","A380")
a.fly(580)
print a.mileage

from animal import Animal
class Animal(Animal):
    def __init__(self):
        super(Animal, self).__init__()   # use super to call the Human __init__ method
        self.name = 'Animal'
        self.health = 0
    def walk(self):
        self.health += 10
    def run(self):
        self.health += 10
    def display_health(self):
        print self.name
        print self.health()
        return self

class Dog(Animal):
    def __init__(self):
        super(Dog, self).__init__()
        self.name = 'Dog'
        self.health = 150
    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self):
        super(Dragon, self).__init__()  # use super to call the Human __init__ method
        self.name = 'Dragon'
        self.health = 170              # every Samurai starts off with 10 strength
    def fly(self):
        self.health -= 10
        return self

a = Animal('Animal', 0)
d = Dog('Dog', 1500)
dr = Dragon('Dragon', 170)


