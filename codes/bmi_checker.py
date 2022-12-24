# File:     bmi.py - BMI demo for COSC 1100 week 3
# Author:   Kyle Chapman
# Created:  September 20, 2022
# Updated:  September 20, 2022
# This program has no validation, but it accepts
# a user's height in inches and weight in pounds,
# calculates a body-mass index (BMI) value, and then
# displays it.

import math

# Declarations.
# Set a value to convert the units for the calculation.
UNIT_CONVERSION = 703

# Input.
# Prompt the user for a height in inches as a floating point number.
height = float(input("Please enter the person's height in inches: "))
# Prompt the user for a weight in pounds as a floating point number.
weight = float(input("Please enter the person's weight in pounds: "))

# Process.
# Determine the BMI by dividing the weight in pounds, by
# (the height in inches squared), multiplied by the unit conversion constant of 703.
bmi = weight / (height * height) * UNIT_CONVERSION
# bmi = weight / (height ** 2) * UNIT_CONVERSION
# bmi = weight / (math.pow(height, 2)) * UNIT_CONVERSION

# Output.
# “The BMI for a “, display the height
# “tall person who weighs”, display the weight
# “is “, display the calculated BMI value.
print('\nThe BMI for a ' + str(round(height, 1)) + '\" tall person who weighs ' + str(round(weight, 1)) + 'lb. is ' + str(round(bmi, 1)))

# Accept user input before ending the program.
input("\nPress Enter to end the program...")