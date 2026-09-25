'''
# Q1 . Write a function that prints maximum number from the list.
# numbers = [1,5,7,99,10] , O/p : 99

def get_maximum(list1):
    max = list1[0]
    length = len(list1)
    for idx in range(1,length,1):
        if list1[idx] > max:
            max = list1[idx]
    print(max)


numbers = [1,5,7,99,10]
ans1 = get_maximum(numbers)
print(ans1)

# Q2 . Write a function that returns maximum number from the list and add 100 to the retruned value and print
# numbers = [1,5,7,99,10] , O/p : 99

def get_max(list1):
    max = list1[0]
    length = len(list1)
    for idx in range(1,length,1):
        if list1[idx] > max:
            max = list1[idx]
    return max

numbers = [1,5,7,99,10]
ans = get_max(numbers)
print(ans+100)

# Class assigment : Solve above problems using extended (advanced for loop ) and while loop



# Q3. Write a script which return the list of prime numbers using function
# prime numbers : having 2 factors ( 1 or number itself except 1 )
# 2 => 2 % 1 ==0, 2%2 == 0 (1,2) prime
#3 => (1,3) prime
#4 => (1,2,4) not a prime
# 9 => (1,3,9) - not a prime
# 1 => (1) not a prime numbers

# you to get all the prime numbers between 2 to 20

def getPrimeNumbers(min_num,max_num):
    primes = []
    for num in range(min_num,max_num+1):
        count = 0
        for num1 in range(1,num+1):
            if num % num1 == 0:
                count = count +1
        if count == 2:
            primes.append(num)
    print(primes)

min_num = 2
max_num = 20
getPrimeNumbers(min_num,max_num)



# Strings
channel_name = "ETL QA Labs"
s_idx = 0
#print(channel_name[s_idx])
e_idx = len(channel_name)-1
#print(channel_name[e_idx])

sL_nun = 1
for idx in range(s_idx,e_idx+1):
    print(sL_nun,". ",channel_name[idx])
    sL_nun = sL_nun+1

'''

channel_name = "ETL QA Labs"
# String slicing
# Get me fisrt 3 chavaters form the string
#print(channel_name[0:3:1])

# Get me charaters at 5 and 6 form the string
#print(channel_name[4:6:1])

# Get me charaters from 0 to end index form the string
#print(channel_name[::2])

# Strings functions

# len
# print(len(channel_name))

print(channel_name.upper())
print(channel_name.lower())

print(channel_name.replace("Labs","Company"))

print(channel_name.find("Labs"))

print(channel_name.count("L"))

ans_list = channel_name.split()
print(ans_list)

email = "etl.qa.labs@gmail.com"
print(email.split("."))

print(email.split("@"))



