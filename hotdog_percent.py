'''
 FILE:     hotdog.py
 AUTHOR:   Daniel Adeyelu
 CREATED:  October 14, 2022
 DESCRIPTION:
   This python script will output the popular percentage
   of hotdogs sold
'''

# DECLARATION
# Variables
traditional_hotdog = 0
veggie_hotdog = 0
curry_hotdog = 0

# If Program is Continuing? 
is_continuing = True


# Loop when continuing is true
while is_continuing:    
    #Print Menu
    print("\nEnter the following")
    print("1: Tradional Hotdog")
    print("2: Vegitable Hotdog")
    print("3: Curry Hotdog")
    print("4: Display total \n")
    # INPUT
    menu = int(input("\nEnter your option: "))
    # Validate Menu Input
    if menu >=1 and menu <= 4:
        if menu == 1:
            # Increment the variable
            traditional_hotdog = int(input("Traditional Hotdog: "))
        elif menu == 2:
            # Increment the variable
            veggie_hotdog = int(input("Vegitable Hotdog: "))
        elif menu == 3:
            # Increment the variable
            curry_hotdog = int(input("Curry Hotdog: "))
        elif menu == 4:
            # Option to ask if user is done
            option = str(input("\nDo you want to end the program Y/N? "))
            if option == 'Y' or option == 'y' or option == 'Yes' or option == 'yes':
                is_continuing = False
                # PROCESS
                # Calculate Total Sum of Hotdogs Sold
                sum_of_hotdogs = traditional_hotdog + veggie_hotdog + curry_hotdog
                # Validate if sum is equal to zero
                if sum_of_hotdogs == 0:
                    print("Zero Error: Please Input Number of Hotdogs Sold")
                    is_continuing = True
                # Else continue with process
                else:
                    # Calculate Percentage of Each
                    percent_traditional = ((traditional_hotdog / sum_of_hotdogs) * 100)
                    percent_veggie = ((veggie_hotdog / sum_of_hotdogs) * 100)
                    percent_curry = ((curry_hotdog / sum_of_hotdogs) * 100)

                    # OUTPUT
                    # print("\nThe total sum of hotdogs is {}%".format(sum_of_hotdogs))
                    print("Traditional Hotdog: \t{} \t {}%".format(traditional_hotdog, round(percent_traditional,2)))
                    print("Vegitable Hotdog: \t{} \t {}%".format(veggie_hotdog, round(percent_veggie,2)))
                    print("Curry Hotdog: \t\t{} \t {}%".format(curry_hotdog, round(percent_curry,2)))
            else: 
                print('')
                is_continuing = True

    # Validation Error for Menu Range
    else:
        print("\nInput is not within the menu range (1-4)")
        is_continuing = True
    

input("Press Enter to End........")