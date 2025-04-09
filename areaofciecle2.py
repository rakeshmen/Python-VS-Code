"""Area of Circle"""

from math import pi

r = input("Hi Rakesh, Enter Radius of the Circle: ")

try:
    r = float(r)
    if r > 0:
        area = pi * r * r
        print("Area of circle is", round(area, 2), "Square Units.")
    else:
        print(f"You have Entered '{r}', Radius can not be 0 or Negative.")
except ValueError:
    print(
        f"You have entered '{r}'.\nEnter Radius in Positive Integer or Decimal Fraction."
    )
# End of file - Rakesh Men
