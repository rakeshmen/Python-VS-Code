"""Area of Circle"""

from math import pi

r = input("Enter Radius of the Circle: ")

if float(r) > 0:
    area = pi * float(r) * float(r)
    print("Area of circle is", round(area, 2))
elif float(r) <= 0:
    print(f"You have Entered '{r}', Radius can not be 0 or Negative.")
elif str(r) != True:
    print(f"You have entered '{r}'.\nPlease Enter Radius in Positive Integer or Decimal Fraction")

# End of file
