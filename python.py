'''
 FILE:     midterm_percentage.py
 AUTHOR:   Daniel Adeyelu
 CREATED:  November 3, 2022
 UPDATED:  November 4, 2022
 DESCRIPTION:
   This python script will output the users overall percentage and the percentage for each assessment 

   TERMS USED
   PCA - Pre-Class Assignment
   ICE - In Class Exercise
'''
# Import in-built statistic library for finding the mean
import statistics

# Declaration
# Constants
COUNTER_PCA = 4
COUNTER_ICE = 4
COUNTER_ASSIGNMENT = range(1,2)
WEIGHT_PCA = 4
WEIGHT_ICE = 4
WEIGHT_ASSIGNMENT = 10
MIN_RANGE = 0
MAX_RANGE = 100
MIDTERM_WEIGHT = 42

# Arrays
pca = [ ]
ice = [ ]
assignment = [ ]

# Variables
sum_of_weights = 0
amount_pca = 0
amount_ice = 0

is_valid = False

# Input
def pca():
    for pca_counter in range(COUNTER_PCA):
        # Validate if input is a number
        try:
            amount_pca = float(input("Input score for Pre-Class Activity #{}: ".format((pca_counter+1))))
            # Validate if input is within range of 0-100 inclusively
            if MIN_RANGE <= amount_pca <= MAX_RANGE:
                is_valid = True
                # Update the pca array till the counter is 4
                pca.append(amount_pca)
            else:
                print("Pre-Class Activity score is not within range (i.e. 0-100)")
        except:
            print("The score must be a number")

def ice():
    is_valid = True
    # If counter = 4 Stop
    for ice_counter in range(COUNTER_ICE):
        # Validate if input is a number
        try:
            amount_ice = float(input("Input score for In Class Exercise #{}: ".format((ice_counter+1))))
            # Validate if input is within range of 0-100 inclusively
            if MIN_RANGE <= amount_ice <= MAX_RANGE:
                is_valid = True
                # Update the ice array till the counter is 4
                ice.append(amount_ice)
            else:
                print("In Class Exercise score is not within range (i.e. 0-100)")
        except:
            print("The score must be a number")

def assignment():
    is_valid = True
    # If counter = 1 Stop
    for assignment_counter in COUNTER_ASSIGNMENT:
        # Validate if input is a number
        try:
            amount_assignment = float(input("Input score for Assignment #{}: ".format(assignment_counter)))
            # Validate if input is within range of 0-100 inclusively
            if MIN_RANGE <= amount_assignment <= MAX_RANGE:
                is_valid = True
                # Update the assignment array till the counter is 4
                assignment.append()
            else:
                print("Assignment score is not within range (i.e. 0-100)")
        except:
            print("The score must be a number")


while not is_valid:
    pca()
    ice()
    assignment()

# Process
# Using the mean method to find the average for each assesment
average_pca = statistics.mean(pca)
average_ice = statistics.mean(ice)
average_assignment = statistics.mean(assignment)
# Find the total grade earned by multiplying the average by the weight and summing them altogether
total_grade_weight_earned = (average_pca * WEIGHT_PCA) + (average_ice * WEIGHT_ICE) + (average_assignment * WEIGHT_ASSIGNMENT)
# Find the total grade weight by summing all the weights of each assesment together
average_overall = total_grade_weight_earned / MIDTERM_WEIGHT

# Output
print("\nAverage of Pre-Class Activitiess: \t{}%".format(round(average_pca, 1)))
print("Average of In Class Exercises: \t\t{}%".format(round(average_ice, 1)))
print("Average of Assignments: \t\t{}%".format(round(average_assignment, 1)))
print("Average Overall: \t\t\t{}%".format(round(average_overall, 1)))