class Car:

    # Class Attribute
    car_tag = 1234

    # Initializer / Instance attributes
    def __init__(self, name, year):
        self.name = name
        self.year = year

    # instance method
    def description(self):
        return '{} is {} years old'.format(self.name, self.year)

# description from parent class
class Honda(Car):
    def maxspeed(self,speed):
        return '{} max speed is {}'.format(self.name, speed)
    
    def new_car_tag(self,newtag):
        self.car_tag = newtag

if __name__ == '__main__':
    car = Car('Jazz','2018')
    print(car.description())

    # modify a method in a child class that it has inherited from the parent class
    accord = Honda('Accord9997','1999')
    print(accord.description())
    