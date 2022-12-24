'''
 FILE:     midterm_percentage_function.py
 AUTHOR:   Daniel Adeyelu
 CREATED:  November 9, 2022
 UPDATED:  November 11, 2022
 DESCRIPTION:
   This python script will output the users overall percentage 
   and the percentage for each assessment 

   TERMS USED
   PCA - Pre-Class Assignment
   ICE - In Class Exercise
'''
import statistics

# Function to Validate Input
def grade_validate(maximum:int, assessment_type):
    '''Returns Validated Assessment'''
    # Declaration
    # Constants
    MAX_RANGE = 100
    MIN_RANGE = 0
    # List
    assessment = []
    is_valid = False
    print("\nInput serially: Pre-Class Activity (4) -> In Class Exercise (4) -> Assignment")
    while not is_valid:
        for counter in range(maximum):
            # Validate if input is a number
            try:
                amount = float(input("input score #{} for {}: ".format(counter+1, assessment_type)))
                # Validate if input is within range of 0-100 inclusively
                if MIN_RANGE <= amount <= MAX_RANGE:
                    is_valid = True
                    # Update the array till the counter is met
                    assessment.append(amount)
                else:
                    print("\nPlease enter a value between {} and {}.".format(MIN_RANGE,MAX_RANGE))
            except:
                print("\nThe score must be a number \nTry Again!\n")
    # Return Value
    return assessment

# Fuction to Process Input
def processing():
    '''Returns Calculated Assessment'''
    # Declaration
    # Constants
    WEIGHT_PCA = 16
    WEIGHT_ICE = 16
    WEIGHT_ASSIGNMENT = 10
    MIDTERM_WEIGHT = 42
    # Use function to validate input where PCA loops 4x ICE loops 4x and Assignment loops once
    pca = grade_validate(4, 'Pre-Class Activity')
    ice = grade_validate(4, 'In Class Exercise')
    assignment = grade_validate(1, 'Assignment')
    # Process
    # Using the mean method to find the average for each assesment
    average_pca = statistics.mean(pca)
    average_ice = statistics.mean(ice)
    average_assignment = statistics.mean(assignment)
    # Output Each Average
    print("\nAverage of Pre-Class Activitiess: \t{}%".format(round(average_pca, 1)))
    print("Average of In Class Exercises: \t\t{}%".format(round(average_ice, 1)))
    print("Average of Assignments: \t\t{}%".format(round(average_assignment, 1)))
    # Find the total grade earned by multiplying the average by the weight and summing them altogether
    total_grade_weight_earned = (average_pca * WEIGHT_PCA) + (average_ice * WEIGHT_ICE) + (average_assignment * WEIGHT_ASSIGNMENT)
    # Find the total grade weight by summing all the weights of each assesment together
    total_grade_weight_possible = WEIGHT_PCA + WEIGHT_ICE + WEIGHT_ASSIGNMENT
    average_overall = total_grade_weight_earned / total_grade_weight_possible
    # Return Value
    return round(average_overall,1)

# Call the processing function assign the returned value to variable processing
processing = processing()
print("Average Overall: \t\t\t{}%".format(processing))
input("Press Enter to End Program......")