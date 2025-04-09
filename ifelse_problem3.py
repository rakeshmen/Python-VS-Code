"""
Docstring: Find LARGEST int in three integers.
"""

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))
LARGEST = 0
if num1 > num2 and num1 > num3:
    LARGEST = num1
elif num2 > num1 and num2 > num3:
    LARGEST = num2
else:
    LARGEST = num3
print("Largest is:", LARGEST)
