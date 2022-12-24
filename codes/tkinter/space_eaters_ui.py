'''
 FILE:     space_eaters_ui.py
 AUTHOR:   Daniel Adeyelu
 CREATED:  November 23, 2022
 UPDATED:  November 25, 2022
 DESCRIPTION:
   This python script will outputs the user interface where
   it calculates the perimeter and area of a rectangle with 
   length and width being inputted by the user.
'''

# Import in-buit libraries
from tkinter import *
# from tkinter.tix import *
import sys

# Function to exit the program
def exit_button():
    sys.exit()

# Function to calculate the perimeter and area of a rectangle
def calculate_button():
    # Constant for perimeter
    TWO = 2
    try:
        # User input entered assigned to variable length and width
        length = float(length_input.get())
        width = float(width_input.get())
        if length > 0 and width > 0:
            perimeter = TWO * (length + width)
            area = length * width
            output_perimeter.configure(text = perimeter)
            output_area.configure(text = area)
            output_status.configure(text="Completed")
        else:
            output_status.configure(text = "ERROR: Entry must both be positive.")
    except:
        output_status.configure(text = "ERROR: Entry must both be a number.")

# Function to clear all inputs
def reset_button():
    length_input.delete(0, 'end')
    width_input.delete(0, 'end')
    output_perimeter.configure(text="")
    output_area.configure(text="")
    output_status.configure(text="")
    # Takes the cursor back to the length input
    length_input.focus()

# Define a Tk Instance
window = Tk()
# Window properties
window.geometry("400x300")
window.minsize(width=300, height=200)
window.title("Space Eaters")

# Row 0 widget
length_label = Label(text = "Length:")
length_label.grid(row=0,column=0)
length_input = Entry() 
length_input.grid(row=0,column=1)

# Row 1 widget
width_label = Label(text="Width")
width_label.grid(row=1,column=0)
width_input = Entry()
width_input.grid(row=1,column=1)

# Row 2 widget
calculate_button = Button(text="Calculate", width=15, command=calculate_button)
calculate_button.grid(row=2,column=4,padx=5,pady=5)

# Row 3 widget
reset_button = Button(text="Reset",width=15, command=reset_button)
reset_button.grid(row=3,column=4)
output_perimeter = Label(width = 15, borderwidth = 2, relief = SUNKEN)
output_perimeter.grid(row=3,column=1)
perimeter_label = Label(text="Perimeter:")
perimeter_label.grid(row=3,column=0)

# Row 4 widget
exit_button = Button(text="Exit",width=15,command=exit_button)
exit_button.grid(row=4,column=4)
output_area = Label(width = 15, borderwidth = 2, relief = SUNKEN)
output_area.grid(row=4,column=1)
area_label = Label(text="Area:")
area_label.grid(row=4,column=0)

# Row 5 widget
output_status = Label(width = 15, borderwidth = 2, relief = SUNKEN)
output_status.grid(row=5,column=1)
status_label = Label(window,text="Status:")
status_label.grid(row=5,column=0)

# Add hotkey support for the three main buttons.
window.bind("<Alt-c>", calculate_button)
window.bind("<Alt-r>", reset_button)
window.bind("<Return>", calculate_button)
window.bind("<Escape>", exit_button)

# Run the main loop
window.mainloop()