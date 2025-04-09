"""
Docstring: Program to find grades based on average of 3 subjects.
"""

sub1 = int(input("Enter Subject 1 Marks:"))
sub2 = int(input("Enter Subject 2 Marks:"))
sub3 = int(input("Enter Subject 3 Marks:"))

average = (sub1 + sub2 + sub3) / 3
print(average)

if average >= 90:
    print("Grade A")
elif average >= 80 and average < 90:
    print("Grade B")
elif average >= 70 and average < 80:
    print("Grade C")
elif average >= 60 and average < 70:
    print("Grade D")
else:
    print("Grade F")
