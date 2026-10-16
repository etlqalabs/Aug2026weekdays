# Print "Hello" 10 times

'''
# Procedural way
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Goof Bye")


# Functional way
def print_hello():
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")

def print_bye():
    print("Goof Bye")

print_hello()
print_hello()
print_bye()


# Object oriented programming way

class PrintClass:
    name = "ETL QA Labs"
    def print_hello(self):
        print("Hello")
        print("Hello")
        print("Hello")
        print("Hello")
        print("Hello")

    def print_bye(self):
        print("Good Bye")

obj1 = PrintClass()
obj1.print_hello()
obj1.print_bye()
print(obj1.name)

print(type(obj1))

name = "ETL"
print(type(name))
age = 4

print(type(age))


class Car:
    def start(self):
        print("Car starts...")
    def stop(self):
        print("Car stops...")
    color = "Black"
    seating_capacity = 4

car1 = Car()
car2 = Car()
car1.start()
car1.stop()
print(car1.color)

car2.start()
car2.stop()
print(car2.color)


# Constructor:
class Car:
    def __init__(self):
        print("I am constructor..")
        color = "Black"
        seating_capacity = 4

    def start(self):
        print("Car starts...")
    def stop(self):
        print("Car stops...")


c1 = Car()

# Parametrizied constrcutor

class Car:

    def __init__(self, color, seating_capacity):
        self.color = color
        self.seating_capacity = seating_capacity
        print("I am constructor..")

    def __init__(self, color, seating_capacity, car_type):
        self.color = color
        self.seating_capacity = seating_capacity
        self.car_type = car_type
        print("I am constructor..")

    def start(self):
        print("Car starts...")
    def stop(self):
        print("Car stops...")


c1 = Car("Red",4,"Hackback")
print(c1.color)
print(c1.seating_capacity)
print(c1.car_type)

c2 = Car("Black",6,"SuV")
print(c2.color)
print(c2.seating_capacity)
print(c2.car_type)


# c1.start() => start(c1)
# c2.start() =< start(c2))

'''

class Vehicle:
    def start(self):
        print("Vehicle starts..")
    def stop(self):
        print("Vehicle starts..")
    color ="Red"

v1 = Vehicle()
v1.color

