'''
# Primitive data types : int, float,string,boolean
# Non primitive data types (Collection data types) : list, tuple,set, dictionary

name = "ETL"
name_ch = "E"
print("Name is :",name,"and data type is :",type(name))
print("Name_ch is :",name,"and data type is :",type(name_ch))



# List : An ordered collection of items that can be changed (mutable).
# you can store different type of data in a list

# ordered : Insertion order preservered
# Mutable : can add or remove some items from the list


name_list = ["Ram", "Shyam","Ghanshyam",25,20,40]
print("Original lists :",name_list,":   :" ,type(name_list))
name_list.append("Thomas")
print("Updated lists :",name_list,":   :" ,type(name_list))



name_list = ["Ram", "Shyam","Ghanshyam"]
# Indexes
# name_list = ["Ram"(0), "Shyam"(1),"Ghanshyam"(2)]

print(name_list[0])
print(name_list[2])

name_list.remove("Shyam")
# name_list = ["Ram"(0),"Ghanshyam"(1)]
print(name_list[0])
print(name_list[2])




name_list = ["Ram", "Shyam","Ghanshyam","Thomas","Ali"]
print(name_list)

print(name_list[0])
print(name_list[4])
print(name_list[3])
print(name_list[2])
print(name_list[1])

name_list = ["Ram", "Shyam","Ghanshyam","Thomas","Ali"]

# using for loop

# Way 1
for idx in range(0,5,1):
    #print("Hello :" ,name_list[idx])
    pass

# Way 2 Advanced for loop
for item in name_list:
    #print("Hello : ",item,"How are you?")
    pass

# Create a smaller list from 3rd(end index) to 5th item in the list

# Way 1 using for loop
ans_list = []
for idx in range(2,5,1):
    print("Hello :" ,name_list[idx])
    ans_list.append(name_list[idx])
print("Answer list : ",ans_list)

# Way 2 using List Slicing
ans_list2 = name_list[2:5:1]
print("Answer list 2 :",ans_list2)

# get me 1st , 3rd and 5th element(items) from name_list
# name_list = ["Ram"(0), "Shyam"(1),"Ghanshyam"(2),"Thomas"(3),"Ali"(4)]

print(name_list[0:5:2])



# Tuple : An ordered collection of items that can NOT be changed (immutable).
# you can store different type of data in a tuple

# ordered : Insertion order preserved
# Immutable : can NOT add or remove some items from the Tuple


name_tuple = ("Ram", "Shyam","Ghanshyam",25,20,40)
print("Tuple is :",name_tuple," and data type is :",type(name_tuple))
# Fstring way of printing
print(f"Tuple is {name_tuple} and data type is : {type(name_tuple)}")



# Set : an Un-ordered collection of unique items ( set does not allow duplicates) and its mutable
name_tuple = ("Ram", "Shyam","Ghanshyam","Ram")
#print(name_tuple)

name_set = {"Ram", "Shyam","Ghanshyam","Ram"}
#print(f"Set  is {name_set} and data type is : {type(name_set)}")

name_set.add("Mohan")
print(name_set)



# print all the element from the set
for item in name_set:
    print(item)



 # Special method applicale to set
 # union, intersection, difference(minus/except)

num1_set = {1,2,3,4}
num2_set = {5,6,3,7}

# Union ( | (or) )
print("Union operator: ")
ans = num1_set | num2_set
print("ans is :",ans," and type is :",type(ans))
ans = num1_set.union(num2_set)
print("ans is :",ans," and type is :",type(ans))

# Intersection ( & (and) )
print("Intersection operator: ")
ans = num1_set & num2_set
print("ans is :",ans," and type is :",type(ans))
ans = num1_set.intersection(num2_set)
print("ans is :",ans," and type is :",type(ans))

# Difference ( - (minus) )
print("Difference operator: ")
ans = num1_set - num2_set
print("ans is :",ans," and type is :",type(ans))
ans = num1_set.difference(num2_set)
print("ans is :",ans," and type is :",type(ans))

# symmtreic Difference ( - (minus) )
print("symmetric Difference operator: ")
ans = num1_set^num2_set
print("ans is :",ans," and type is :",type(ans))
ans = num1_set.symmetric_difference(num2_set)
print("ans is :",ans," and type is :",type(ans))



num1_list = [1,2,3,4]
num2_list = [5,6,3,7]

#print(num1_list|num2_list)

num1_set = {1,2,3,4}
num2_set = {5,6,3,7}

# print(num1_set.union(num2_set))
# print(num1_set|num2_set)

'''


list1 = [1,5.6,"Ram"]
print(type(list1))

for ele in list1:
    print(f"values is : {ele} and data type is: {type(ele)}")


