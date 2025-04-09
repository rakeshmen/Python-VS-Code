"""
AREA OF CIRCLE
"""

import math


def calculate_circle_area():
    """Function to calculate the area of a circle"""

    while True:
        try:
            # Get the radius from the user
            radius = float(input("Enter the radius of the circle: "))
            # Check if the radius is negative
            if radius < 0:
                print(
                    "Error: Radius cannot be negative. Please enter a non-negative value."
                )
                continue  # Ask the user to input again
            # Calculate the area
            area = math.pi * (radius**2)
            # Round the area to 2 decimal places
            rounded_area = round(area, 2)
            # Print the result
            print(f"The area of the circle is: {rounded_area}")
            break  # Exit the loop if valid input is provided
        except ValueError:
            print("Error: Please enter a valid number.")


# Call the function
calculate_circle_area()
# End
