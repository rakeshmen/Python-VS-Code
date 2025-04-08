"""
Docstring: This is python basics.
"""

import math

print(math.floor(2.5))
print(math.ceil(2.5))
print(math.sqrt(4))
print(math.pi)
print(math.floor(2.6))
print(math.ceil(78.9))
print(math.ceil(78.4))
print(math.ceil(math.sqrt(9)))
print("hello world")
A = 1
B = 2
C = "This os STRIng."
print(A + B)
print(A - B)
print(A)
print(type(A))
print(type(C))
print(type(B))
print(type(C))

STRI = "my STRIng is not long enough"
print(STRI.capitalize())
print(STRI.title())
print(STRI.lower())
print(STRI.upper())
print(STRI.index("my"))
print(STRI.index("STRIng"))
# Capitalize first character of the STRIng and make all other characters lower case.
print(STRI.capitalize())

# Convert the first character of each word to upper case
print(STRI.title())

# Get index of a subSTRIng
print(STRI.index("my"))
print(STRI.index("STRIng"))

# Get the length of the STRIng
print(STRI.lower())
print(STRI.upper())

# list
rooms = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(type(rooms))
print("ROOMS list is", rooms)

list10 = [10, 20, 30]
print(type(list10))
print(list10[1])
print(list10[0])

list11 = [100, 200, 300, 400]
print(type(list11))
print(list11[0])
list11[0] = 500
print(list11[0])
print(list11)
print(type(list11))


print(rooms[0])
print(rooms[1])

member = ["Ram", 18, 2.5]
print(member)

print(type(member))

print(member)

address1 = [17, "Ganga", "Nagpur"]
print(address1)
print(address1[1])
print(address1[2])

mylist = ["Ram", 1, 2, 5]
print(mylist)

mylist2 = ["Ram", 1, 2, 5, "hello", "world", 2.5]
print(mylist2)

mylist2[0] = "Shyam"
print(mylist2)

A = 10
B = 30
print(A + B)

list1 = [10, 15, 19]
print(type(list1))

print(type(list1))

list1[0] = "Lakhan"
print(list1)

list1[2] = "Laxman"
print(list1)

print(type(list1))

list2 = ["Shalikram", 25, 30]
print(list2)
print(list2[0])
list2[1] = "Raghavendra"
print(list2[1])
print(list2)
list2[2] = "Ravi"
print(list2)
list2[2] = "Rahul"
print(list2)

tuple1 = (1, 2, 3, 4, 5)
print(type(tuple1))
print(tuple1)
print(type(tuple1))
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
print(tuple1[3])
print(tuple1[4])
print(tuple1[0:3])
print(tuple1[1:4])
print(tuple1[0:5])
print(tuple1[0:2])
print(tuple1[0:1])
print(tuple1[0:0])
# tuple1[0] = 10 # TypeError: 'tuple' object does not support item assignment
print(tuple1[0])

tuple11 = (10, "Ram")
print(tuple11)
print(type(tuple11))

dic1 = {"name": "Ram", "age": 25, "height": 5.5}
print(dic1)

dic2 = {"name": "Shyam", "age": 30, "height": 6.0}
print(dic2)
print(dic2["name"])
print(dic2["name"])
print(dic2["age"])
print(len(dic2))

dic3 = dict(name="John", age=36, country="Norway")
print(dic3)

list3 = [1, 2, 3, 4, 4, 5, 6, 6]
set1 = set(list3)
print(set1)

list11 = [200, 33, 442, 342, 200]
print(type(list11))
set11 = set(list11)
print(type(set11))
print(list11, set11)

A = 10
B = 20
C = "Nagesh"

print(A + B)
print(str(A) + str(B) + C)

print("5+5 is", 5 + 5)

# Get input value from user.
print("enter value")
var = int(input())
if var > 5:
    print("greater than 5")
elif var == 5:
    print("you entered", var)
else:
    print("less than 5")

for i in range(1, 101):
    print(i)

for i in range(1, 4):
    print(i)

for i in range(11, 15):
    print(i)

for i in range(10, 20):
    print(i)

i = 0
while i < 100:
    print(i)
    i = i + 1


i = 8
while i <= 10:
    print(i)
    i = i + 1
print("here loop exists and value becomes", i)

print("Hello Hello")

print("Henko Hello")
