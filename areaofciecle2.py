"""Area of Circle"""

from math import pi

# r = input("Enter Radius of the Circle: ")

try:
    r = float(input("Enter Radius of the Circle: "))
    #    r = float(r)
    if r > 0:
        area = pi * r * r
        print("Area of circle is", round(area, 2))
    else:
        print(f"You have Entered '{r}', Radius can not be Negative.")
except ValueError:
    print(
        f"You have entered '{r}'.\nPlease Enter Radius in Positive Integer or Decimal Fraction"
    )
# End of file
