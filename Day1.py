'''
print("Hello ! Welcome to day 1 Python learning")

# Indentation : spaces before the line

age = 20

if age >=18:
    print("You are elligible")
    print("You can drive the car")
print("Program completed")



# Variables : container for storing data values
name = "ETL QA Labs !"
age = 18
weight = 50.6
print(name)
print(type(name))
print(type(age))
print(type(weight))




nameofmyyutubechannel = "ETL QA Labs !"
# naming convention for multi word variable names

#1. Camel Case : Start of every word should be uppercase except for the first word
nameOfMyYoutubeChannel = "ETL QA Labs !"

#2. Pascal Case : Start of every word should be uppercase
NameOfMyYoutubeChannel = "ETL QA Labs !"

#3. Snake Case : Eevry word should be seperated by underscore
name_of_my_youtube_channel = "ETL QA Labs !"




# Type Casting

age = 18
print("Age : ",age ," and data type is : ",type(age))

age_float = float(age)
print(age_float)

int(18) -> float(18.0) => upcasting

weight = 50.8
weight_int = int(weight)
print(weight_int)
float(18.0) -> int(18) => downcasting



age1 = 18
age2 = 12

sum1 = age1 + age2
print(sum1,type(sum1))
sum2 = str(age1) + str(age2)
print(sum2,type(sum2))



# Progamming paradigm (Style)
# 1. procedural programming => Execution happens only line by line
print("Hello")
print("Welcome to ETL QA Labs !")
print("Mr. ABC , how are you doing")
print("It was nice meeting you")
print("Bye")


print("Hello")
print("Welcome to ETL QA Labs !")
print("Mr. DEF , how are you doing")
print("It was nice meeting you")
print("Bye")



# 2. Functional programming (re-usability)

def greeting():
    print("Hello")
    print("Welcome to ETL QA Labs !")

def bye():
    print("It was nice meeting you")
    print("Bye")



# 3. OOP programming (encapsulation , inheritance, polymorphism, abstraction)

class WelcomeMessage:
    def greeting(self):
        print("Hello")
        print("Welcome to ETL QA Labs !")

    def bye(self):
        print("It was nice meeting you")
        print("Bye")


welcome = WelcomeMessage()
welcome.greeting()
print("Mr. ABC , how are you doing")
welcome.bye()


welcome.greeting()
print("Mr. DEF , how are you doing")
welcome.bye()


Procedural way => Functional way => Object Oriented way



status  = False
print(status,type(status))
status_str = str(status)
print(status_str,type(status_str))
print(int(status))



num_str = "1234"
num_int = int(num_str)
print(type(num_int))

num_str = "0234"
num_bool = bool(num_str)
print(num_bool,type(num_bool))
'''


print(ord("अ"))


s1  = "abc" # 65 + 25 = 90
sum = 0
for ch in s1:
    sum = sum +ord(ch)
    print(ord(ch))
print(sum)
