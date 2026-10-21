'''
# Polymorphism: Greek worlds ( Poly => Many, Morph => Forms ) => Many forms
# It refers to the ability to use a single interface ( method, class ) to represent different underlying forms

# Can be implemented in different ways:
# 1. Method OverLoading : having multiple methods with the same name ( Directly not supported in Python)

class Maths:

    def add_numbers(self,a,b):
        return a+b

    def add_numbers(self,a,b,c):
        return a+b+c

    def add_numbers(self,a,b,c,d):
        return a+b+c+d

obj = Maths()
sum1 = obj.add_numbers(10,20)
print(sum1) # error needing c and d as well

sum2 = obj.add_numbers(10,20,30,40)
print(sum2) # works


Solution:
class Maths:

    def add_numbers(self,a,b,c=0,d=0):
        return a+b+c+d

obj = Maths()
sum1 = obj.add_numbers(10,20,30,40)
print(sum1)

sum2 = obj.add_numbers(10,20)
print(sum2)



# 2. Method Overriding (using the same method in parent and child class)
class Vehicle:
    def start(self):
        print("Vehicle starts...")

    def stops(self):
        print("Vehicle stops...")

class Car(Vehicle):

    def start(self):
        print("Car starts...")

    def honk(self):
        print("Car beeps..")


c = Car()
c.start()
c.stops()
c.honk()

v = Vehicle()
v.start()
v.stops()


#3. Operator overloading

class OperatorOverLoading:
    def __init__(self,num1,num2,str1,str2):
        self.sum_num = num1 + num2
        self.concatenate_strings=str1 + str2

    def printMethod(self):
        print(self.sum_num)
        print(self.concatenate_strings)

o1 = OperatorOverLoading(10,20,"ETL","QA Labs")
o2 = OperatorOverLoading(10,20,"10","20")
#o1.printMethod()
o2.printMethod()


# 4. Class Polymorphism in Python

class Circle:
    def area(self):
        return 3.14*5*5

class Square:
    def area(self):
        return 5*5

class Triangle:
    def area(self):
        return 0.5*5*4

c = Circle()
s = Square()
t = Triangle()
shapes = [c,s,t]

for obj in shapes:
    print(obj.area())


# Abstraction : Hiding complexity of the system from end user
# Abstract class : we can't create an object of abstract
# Abstract Method : Missing implementation

# Concrete class
class Vehicle:
    def start(self):
        print("Starts Vehicle")

    def stop(self):
        print("stops Vehicle")

v = Vehicle()
v.start()
v.stop()

'''


# Abstract class
from abc import ABC,abstractmethod
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def honk(self):
        print("Vehicle honks..")

class Car(Vehicle):
    def start(self):
        print("Car starts...")

    def stop(self):
        print("Car stops...")

class Bike(Vehicle):
    def start(self):
        print("Bike starts..")

    def stop(self):
        print("Bike stops..")


c = Car()
c.start()
c.stop()
c.honk()

b = Bike()
b.start()
b.honk()