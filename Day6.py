# String Slicing
# s[start:end:steps]
# steps can be +ve ( left to right) or -ve(right to left pointer movement)
'''
s = "Bangolore"
# Take out a substring of first 4 chars ( index 0 to 3 )
s1 = s[0:4:1]
print(s1)



st = "Bangolore"
# Take out a substring of last 4 chars
l = len(st)
s = l-4
e = l-1
s2 = st[s:e-1:1]
print(s2)

# print last 4 chars in reverse direction
print(s)
print(e)
print(st[e:s-1:-1])

# way 2
print(st[-1:-5:-1])



st1 = "BANGALORECITY"
# print from 4th ( index : 3 )to 10th character ( index : 9)
print(st1[3:10:1])

# # print from second last character(T : index -2) to 4th last character(end: -4 )
print(st1[-2:-5:-1])

# print the revrsed string
print(st1[::-1])

# print the the whole string
print(st1[::1])




st1 = "BANGALORECITY"

# Print C in the string
print(st1[9])
print(st1[-4])

# print me last charcater
print(st1[-1])

l = len(st1)
print(st1[l-1])



# Q1 : print the charcters from the string
city = "Hyderabad"

# way 1 using extended for ( advanced for loop )
for ch in city:
    #print(ch)
    pass

# way 2 using for indexed for loop
le = len(city)
for idx in range(0,le,1):
    #print(city[idx])
    pass

# way 3 using while loop
s = 0
e = le-1

while (s<=e):
    print(city[s])
    s = s+1

'''


# Q2 : Reverse the string
city = "Hyderabad"

# Way 1 using slicing
#print(city[::-1])

# Way 2 using for while
le = len(city)  # 9
ei = le -1  # 8
ans = ""
while ei >=0:
    ans = ans + city[ei]
    print(ans)
    ei = ei -1

