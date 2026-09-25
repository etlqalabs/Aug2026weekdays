'''
# Taking inputs from user
# input()

name = input("Enter your name : ")
print("Data type of name :",type(name))
print("name is : ",name)

age = input("Enter age of the person : ")
print("Data type of age :",type(age))  # age = "35"
print("age is : ",age)

age = int(age)
print("Data type of age :",type(age))  # age = "35"
print("age is : ",age)


# Control Statement : manage the flow of execution of your program

age = 15

# if statement
if age >= 18:
    print("Eligible for voting")
print("Program completed...")



age = 18
# if ... else statement
if age >= 18:
    print("Eligible for voting")
else:
    print("Not Eligible for voting")

print("Program completed...")



# Elif

age = int(input("Enter age of the person : "))
# if ... else statement
if age > 18:
    print("Eligible for voting")
elif age == 18:
    print("Near Eligible for voting")
else:
    print("Not Eligible for voting")

print("Program completed...")


# Looping Statements
# for & while loop

# range(20) => 0,1,2,3......,19 , starts with 0 and ends with number-1
# range(start_value,end_values,steps) , range(1,20,2) => 1,3,5,7......19
# range(2,20,3) => 2,5,8,11,14,17

name = "ETL"
if name:
    print("True")
else:
    print("False")




# for loop
# range(20) ~ range(0,10,1)
for num in range(10):
    print(num)


# print all the even number till 20 starting from 2
for num in range(2,21,2):
    print(num)

# print all the even number till 20 starting from 1
for num in range(1,20,2):
    print(num)


# while loop stops after evealuation of a condition as False

# print 1 to 10

start_val = 1
end_val = 10

while start_val <= end_val:
    print(start_val)
    start_val = start_val + 1



x = True
y = False

# Logical operation
ans1 = x and y
ans2 = x or y
print(ans1)
print(ans2)


# Q1. Record count validation between source and target
source_count = 1000
target_count = 980
if source_count == target_count:
    print("PASS - Record counts matched")
else:
    print("Failed - Record counts matched")
    missing_count = source_count - target_count
    print("Missing Record counts :",missing_count)



# Q2 . ETL job SLA validation, Job should be completed within 30 mins
# a) 30 mins/less -> SLA met
# b) 31-45 mins -> SLA warning
# a) more than 45 mins -> SLA breached

duration = 50

if duration <= 30:
    print("SLA met")
elif duration <=45:
    print("SLA warning")
else:
    print("SLA breached")



# Q3 . validation 10 ETL records
for record in range(1,11):
    print("Validating Record" ,record)
print("Validating completed ..")

'''

# Q4 . Identify failed ETL records
# 20 roecrds and i want to print every 5th records the failed records
# 1....20 => 5,10,15,20

for i in range(1,21,1):
    if i % 5 == 0:
        print("Failed record :",i)


