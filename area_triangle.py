#!/usr/bin/env python3
# Created by Marc Coffi
# Created in May 2022
# # This program calculates the area of a triangle


# Defining the function that calculates the area of a triangle
def calc_area(height, base):
    area = (height * base) / 2
    print("The area of the triangle is {}cm\u00b2.".format(area))


if __name__ == "__main__":
    # Getting the height and base from the user
    height_from_user = input("Enter a height: ")
    base_from_user = input("Enter a base: ")

    try:
        # Trying to convert the user input to integers
        base_int = int(base_from_user)
        height_int = int(height_from_user)
        # Checking to see if the input is bigger than 0
        if base_int > 0 and height_int > 0:
            calc_area(height_int, base_int)
        else:
            print(
                "Invalid input. Please enter a natural number to calculate the Area of a triangle."
            )
    except:
        print("Invalid input. Please enter a valid number.")
