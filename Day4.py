'''
# eno : ename
# Dictionary (map) -
# Dictionary stores key and value
# unordered, mutable where key must be unique and immutable


eno =[1,2,3]
ename =["Ajay","Vijay","Thomas"]

employees_details = {1:"Ajay",2:"Vijay",3:"Thomas",4:"Ajay"}

#print(employees_details)

# Get all the keys ( eno)
for key in employees_details.keys():
    print(key)

# Get all the values ( ename)
for val in employees_details.values():
    print(val)

# Get all the keys, values ( eno, ename) - item
for item in employees_details.items():
    print(item," : ",type(item))


employees_details = {1:"Ajay",2:"Vijay",3:"Thomas",4:"Ajay"}
for item in employees_details.items():
    eno = item[0]
    ename = item[1]
    #print(eno ,"  :  ",ename)

for k,v in employees_details.items():
    print(k, "  :  ", v)

# To get a value of a specific key ( eno = 4 )
print(employees_details[4])
print(employees_details.get(4))


# add one more item to the dictionary
employees_details[5]="Ali"

# update ename of eno: 1
employees_details[1]="Suraj"
print(employees_details)




# Remove items form the dictionary
employees_details = {1:"Ajay",2:"Vijay",3:"Thomas",4:"Ajay"}
print("Before removal : ",employees_details)
removed_value = employees_details.pop(1)
print("After removal : ",employees_details)
print("Removed values :",removed_value)

removed_popitem = employees_details.popitem()
print("After removal : ",employees_details)
print("Removed values popitem :",removed_popitem)


# Function contains a block of code to put together
# It supports modularization

# defining a function and running
# Function that does not return any value
def display():
    print(1)
    print(2)
    print(3)
    print(4)

display()
display()
display()


# Function that returns the value
def print_name():
    name = "ETL QA Labs"
    print(name)
    return name

ans = print_name()
print(ans)

'''

# Why set is faster than list and tuple?

eno_list = [1,2,3,4]
eno_set = {1,2,3,4}
print(hash("ETL"))





