class Animal(object):
    def __init__(self, name, health):
        super(Animal, self).__init__()   # use super to call the Human __init__ method
        self.name = name
        self.health = health
    
    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_info(self, comment):
        print 'Name: ' + str(self.name)
        print 'Health: ' + str(self.health)
        print comment
        return self

manny = Animal('Manimal', 50)
manny.display_info('Manimal begins workout.').walk().walk().walk().run().run().display_info('Manimal is done with workout.')

  
class Dog(Animal):
    def __init__(self, name, health):
        super(Dog, self).__init__(name, health)
        
    
    def pet(self):
        self.health += 5
        return self

dog = Dog('Rover', 100)
dog.display_info('Rover starts workout session.').walk().walk().walk().run().run().pet().display_info('Rover ends his workout.')

class Dragon(Animal):
    def __init__(self, name, health):
        super(Dragon, self).__init__(name, health)  # use super to call the Human __init__ method
        

    def fly(self):
        self.health -= 10
        return self

dragon = Dragon('Igor', 150)
dragon.display_info('Igor goes on a trip.').fly().fly().display_info('Igor comes home.')