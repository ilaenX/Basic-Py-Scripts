'''
 FILE:     kmtomiles_ui.py
 AUTHOR:   Daniel Adeyelu
 CREATED:  November 24, 2022
 UPDATED:  November 29, 2022
 DESCRIPTION:
   This python script will outputs the user interface where
   it converts the user input to either miles or kilometers
   depending on the users choice.
'''

# Import modules and packages 
from tkinter import *
# from tkinter.tix import *
import sys
  
# Tk Instances and Variables
window = Tk()
radio_button_input = StringVar()
radio_button_output = StringVar() 

# Variable to display tooltips 
# tooltip = Balloon(window)

# Function for the Reset button 
def clear(_event=None):
    input_label.delete(0, 'end')
    output_label.configure(text="")
    status_label.configure(text="")
    # Once cleared, the pointer goes back to the first input box
    input_label.focus()
    radio_button_km.set()

# Function for the Convert button
def convert(_event=None):
    FORMULA_KM = 0.62137119
    FORMULA_MILES = 0.62137119   
    try:
        value = float(input_label.get())
        # If radio button is set to mi and km, convert to kilometers
        if radio_button_input.get() == "mi" and radio_button_output.get() == "km":
            value_km = value * FORMULA_KM
            output_label.configure(text="{} Kilometers".format(round(value_km,2)))
            status_label.configure(text="Convertion Successful")
        # If radio button is set to km and mi, convert to miles
        elif radio_button_input.get() == "km" and radio_button_output.get() == "mi":
            value_miles = value / FORMULA_MILES
            output_label.configure(text="{} Miles".format(round(value_miles,2)))
            status_label.configure(text="Convertion Successful")
        # If radio button is set to km and km, display error
        elif radio_button_input.get()  == "km" and radio_button_output.get()  == "km":
            status_label.configure(text="ERROR: Wrong Conversion")
        # If radio button is set to mi and mi, display error
        elif radio_button_input.get()  == "mi" and radio_button_output.get()  == "mi":
            status_label.configure(text="ERROR: Wrong Conversion")
        # If user has not selected an option, display error
        else:
            status_label.configure(text="ERROR: Select Conversion")
    # User Input must be numeric
    except:
        status_label.configure(text="ERROR: Please enter a numeric distance to convert.")

# Function for the Exit button
def exits(_event=None):
    sys.exit()

# Window properties
window.geometry("500x400")
window.minsize(width=400, height=300)
window.title("Km to Mi")

# Row 0 widget
input_label_prompt = Label(window,text="Value:")
input_label_prompt.grid(row=0, column=0, sticky=W, padx=3, pady=3)
input_label = Entry(width=23)
input_label.grid(row=0, column=1)
# tooltip.bind_widget(input_label, msg = "Input value to be converted")
radio_button_km = Radiobutton(text="km", value="km", variable=radio_button_input)
radio_button_km.grid(row=0, column=2)
radio_button_miles = Radiobutton(text="mi", value="mi", variable=radio_button_input)
radio_button_miles.grid(row=0, column=3)

# Row 1 widget
output_label_prompt = Label(window, text="Converted value:")
output_label_prompt.grid(row=1, column=0, sticky=W, padx=3, pady=3)
output_label = Label(relief = SUNKEN, width=20)
output_label.grid(row=1,column=1)
# tooltip.bind_widget(output_label, msg = "Conversion output")
output_radio_button_km = Radiobutton(text="km", value="km", variable=radio_button_output)
output_radio_button_km.grid(row=1, column=2)
output_radio_button_miles = Radiobutton(text="mi", value="mi", variable=radio_button_output)
output_radio_button_miles.grid(row=1, column=3)

# Row 2 widget
status_label_prompt = Label(window, text="Status:")
status_label_prompt.grid(row=2,column=0, sticky=W, padx=3, pady=3)
status_label = Label(relief = SUNKEN, width=20)
status_label.grid(row=2,column=1)
# tooltip.bind_widget(status_label, msg = "Display Status Messages")

# Row 3 widget
convert_button = Button(text="Convert", command=convert)
convert_button.grid(row=3,column=1)
# tooltip.bind_widget(convert_button, msg = "Click to Convert")
clear_button = Button(window,text="Reset",command=clear)
clear_button.grid(row=3,column=0)
# tooltip.bind_widget(clear_button, msg = "Click to Reset")
exit_button = Button(window,text="Exit",command=exits)
exit_button.grid(row=3,column=2)
# tooltip.bind_widget(exit_button, msg = "Click to Exit")

# Add hotkey support for the three main buttons.
window.bind("<Alt-c>", clear)
window.bind("<Return>", convert)
window.bind("<Escape>", exits)

window.mainloop()