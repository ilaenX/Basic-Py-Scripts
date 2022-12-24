'''
 FILE:     Caesar_crypto.py
 AUTHOR:   Daniel Adeyelu
 CREATED:  November 13, 2022
 UPDATED:  November 16, 2022
 DESCRIPTION:
   This python script uses caesers cryptography algorithm to
   encrypt or decrypt cipher texts
REFERENCE:
    https://teachen.info/cspp/unit4/lab04-02.html
'''

is_continuing = True

# Function to encode where text is the parameter with a string data type
def encode(text:str):
    '''To encode text input'''
    # Declaration
    # Constant
    # Default key
    KEY = 4
    # Variable
    encrypted_string = ""
    # Process
    for i in range(len(text)):
        # Break the input into characters
        character = text[i]
        # Gets the number representation of the character
        number_representation = ord(character)
        # Using the encoding formular
        calculate_encode = number_representation + KEY
        # Returns the number representation back to the characters 
        unicode = chr(calculate_encode)
        # Concatenate to the empty string
        encrypted_string += unicode
    return encrypted_string

# Function to decode where text is the parameter with a string data type
def decode(text:str):
    '''To Decode Text Input'''
    # Declaration
    # Constant
    KEY = 4
    # Variable
    decrypted_string = ""
    for i in range(len(text)):
        # Break the input into characters
        character = text[i]
        # Represent the characters to numbers and remove ord("A") or 65
        number_representation = ord(character) #- ord("A")
        # Using the decoding formular
        calculate_upper = number_representation - KEY
        # Convert interger to string
        unicode = chr(calculate_upper)
        # Concatenate to the empty string
        decrypted_string += unicode  
    return decrypted_string

# Continue to re-prompt untill loop breaks
while is_continuing:
    print("\n1: Encode \n2: Decode \n3: Exit")
    menu = input("Menu Selection: ")
    # Menu 1: Encode
    if menu == '1':
        # Input
        text = input("Input text: ")
        # Call the encoding function
        text_encrypt = encode(text)
        print("Encoded text: {}".format(text_encrypt))
    # Menu 2: Decode
    elif menu == '2':
        # Input
        text = input("Input encrypted text: ")
        # Call the decoding function
        text_decrypt = decode(text)
        print("Decoded text: {}".format(text_decrypt))
    # Menu 3: Exit
    elif menu == '3':
        print("\n....Exiting....\n")
        # End Loop
        is_continuing = False
    else:
        # If menu input is not between 1-3
        # Re-prompt
        print("Please select a valid option (1-3)")