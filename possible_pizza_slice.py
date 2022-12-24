'''
 FILE:     possible_pizza_slice.py
 AUTHOR:   Daniel Adeyelu
 CREATED:  October 18, 2022
 UPDATED:  October 19, 2022
 DESCRIPTION:
   This python script will output the possible number of slices
   of pizza based on its diameter and the area of each slice
'''

# Import in-buit libraries
import math

# DECLARATION
# Loop Variable 
is_continuing = True

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

# Amount of Pizza Slice Variable
pizza_slice = 0
    
while is_continuing:
    # INPUT
    # Prompt user to input diameter of a pizza in inches as a real number
    try:
        diameter = float(input("Diameter of a pizza in inches (0 to end Program): "))
        # If input is 0 End Program
        if diameter == 0:
            is_continuing = False
        # Check if diameter is ranged between 8 and 24 inclusive
        elif diameter >= MINIMUM_PIZZA_DIAMETER and diameter <= MAXIMUM_PIZZA_DIAMETER:
            '''  
            If the diameter is in range it will check through the decision structure
            and print the amount of slices
            '''  
            # Diameters of 8” to < 12” cut in 6 slices. 
            if diameter >= MINIMUM_PIZZA_DIAMETER and diameter < SECOND_DIAMETER:
                # Assign 6 amount of slices in pizza slice
                pizza_slice = FIRST_SLICES
                            
            # Diameters of 12” to < 14” cut in 8 slices. 
            elif diameter >= SECOND_DIAMETER and diameter < THIRD_DIAMETER:
                # Assign 8 amount of slices in pizza slice
                pizza_slice = SECOND_SLICES            

            # Diameters of 14” to < 16” cut in 10 slices.
            elif diameter >= THIRD_DIAMETER and diameter < FOURTH_DIAMETER:
                # Assign 10 amount of slices in pizza slice
                pizza_slice = THIRD_SLICES
                                
            # Diameters of 16” to < 20” cut in 12 slices. 
            elif diameter >= FOURTH_DIAMETER and diameter < FIFTH_DIAMETER:
                # Assign 12 amount of slices in pizza slice
                pizza_slice = FOURTH_SLICES
                
            # Diameters of 20” to 24” cut in 16 slices.
            elif diameter >= FIFTH_DIAMETER and diameter <= MAXIMUM_PIZZA_DIAMETER:
                # Assign 16 amount of slices in pizza slice
                pizza_slice = FIFTH_SLICES
                 
            # PROCESS
            # To get the radius divide the diameter by 2
            radius = diameter / TWO

            # Find the area of a cirlce using the calculated radius
            area = PI * (radius**TWO)

            # Find the area per slice by diving the calculated area by the constant pizza_slice
            area_first_slices = area/FIRST_SLICES
            area_second_slices = area/SECOND_SLICES
            area_third_slices = area/THIRD_SLICES
            area_fourth_slices = area/FOURTH_SLICES
            area_fifth_slices = area/FIFTH_SLICES
   
            # OUTPUT
            # Possible Amount of Pizza Based on it's diameter
            # Area will be divided by the s
            if pizza_slice >= FIRST_SLICES:
                print("Pizza Diameter: {}".format(diameter))
                print("Cut in {} slices results in an area of {}\" per slice.".format(FIRST_SLICES, round(area_first_slices,2)))
            if pizza_slice >= SECOND_SLICES:
                print("Cut in {} slices results in an area of {}\" per slice.".format(SECOND_SLICES, round(area_second_slices,2)))
            if pizza_slice >= THIRD_SLICES:
                print("Cut in {} slices results in an area of {}\" per slice.".format(THIRD_SLICES, round(area_third_slices,2)))
            if pizza_slice >= FOURTH_SLICES:
                print("Cut in {} slices results in an area of {}\" per slice.".format(FOURTH_SLICES, round(area_fourth_slices,2)))
            if pizza_slice >= FIFTH_SLICES:
                print("Cut in {} slices results in an area of {}\" per slice.".format(FIFTH_SLICES, round(area_fifth_slices,2)))  

        else:
            # Validation Error: Error out of range diameter
            print("ENTRY ERROR:\nPizza must have a diameter in the range of {} to {} inclusive!\nPlease try again.".format(MINIMUM_PIZZA_DIAMETER,MAXIMUM_PIZZA_DIAMETER))
    except:
        # Validation Error: Diameter entered is not numeric
        print("ENTRY ERROR:\nDiameter entered is not a number")