'''
 FILE:     pizza_slicer.py
 AUTHOR:   Daniel Adeyelu
 CREATED:  October 4, 2022
 UPDATED:  October 19, 2022
 DESCRIPTION:
   This python script will output the amount of slices
   of pizza based on its diameter and the area of each slice
'''

# Importing the in-built mathematics library
import math

# DECLARATION
# Validation Constant 
is_valid = True

# Declared Diameters
MINIMUM_PIZZA_DIAMETER = 8
MAXIMUM_PIZZA_DIAMETER = 24
SECOND_DIAMETER = 12
THIRD_DIAMETER = 14
FOURTH_DIAMETER = 16
FIFTH_DIAMETER = 20

# Declared Amount of Slices 
FIRST_SLICES = 6
SECOND_SLICES = 8
THIRD_SLICES = 10
FOURTH_SLICES = 12
FIFTH_SLICES = 16

# Maths Constants
PI = math.pi 
TWO = 2

# Amount of Pizza Slice
pizza_slice = 0

# Validation if input is numerc
try:
    # INPUT
    # Prompt user to input diameter of a pizza in inches as a real number
    diameter = float(input("Diameter of a pizza in inches: "))

    # Check if diameter is ranged between 8 and 24 inclusive
    if diameter >= MINIMUM_PIZZA_DIAMETER and diameter <= MAXIMUM_PIZZA_DIAMETER:
        '''  
          If the diameter is in range it will check through the decision structure
          and print the amount of slices
        '''  
        # Diameters of 8” to < 12” cut in 6 slices. 
        if diameter >= MINIMUM_PIZZA_DIAMETER and diameter < SECOND_DIAMETER:
            # Assign 6 amount of slices in pizza slice
            pizza_slice = FIRST_SLICES

        # Diameters of 12” to < 14” cut in 8 slices. 
        elif diameter > SECOND_DIAMETER and diameter < THIRD_DIAMETER:
            # Assign 8 amount of slices in pizza slice
            pizza_slice = SECOND_SLICES

        # Diameters of 14” to < 16” cut in 10 slices.
        elif diameter > THIRD_DIAMETER and diameter < FOURTH_DIAMETER:
            # Assign 10 amount of slices in pizza slice
            pizza_slice = THIRD_SLICES
        
        # Diameters of 16” to < 20” cut in 12 slices. 
        elif diameter > FOURTH_DIAMETER and diameter < FIFTH_DIAMETER:
            # Assign 12 amount of slices in pizza slice
            pizza_slice = FOURTH_SLICES
        
        # Diameters of 20” to 24” cut in 16 slices.
        elif diameter > FIFTH_DIAMETER and diameter <= MAXIMUM_PIZZA_DIAMETER:
            # Assign 16 amount of slices in pizza slice
            pizza_slice = FIFTH_SLICES

        # PROCESS
        # To get the radius divide the diameter by 2
        radius = diameter / TWO

        # Find the area of a cirlce using the calculated radius
        area = PI * (radius**2)

        # Find the area per slice by diving the calculated area by the constant pizza_slice
        area_per_pizza_slice = area / pizza_slice

        # OUTPUT
        print("A {}\" pizza will yield {} slices".format(diameter,pizza_slice))
        print("Each slice will have an area of {} square inches.".format(round(area_per_pizza_slice,2)))
    else:
        # Validation Error: Error out of range diameter
        print("ENTRY ERROR:\nPizza must have a diameter in the range of {} to {} inclusive!\nPlease try again.".format(MINIMUM_PIZZA_DIAMETER,MAXIMUM_PIZZA_DIAMETER))
except:
    # Validation Error: Diameter entered is not numeric
    print("ENTRY ERROR:\nDiameter entered is not a number")

# To Exit the Program
input("Press Enter to exit the program...")