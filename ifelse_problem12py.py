"""
Docstring:
Program that grants access only to kids aged between 4-17
and find largest among them.
"""

age = int(input("Enter Age: "))

if age >= 4 and age <= 17:
    print("Welcome")
else:
    print("Sorry, you are not allowded.")
