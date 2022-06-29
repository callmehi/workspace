    # Import the tkinter module
import tkinter
  
# Create the default window
root = tkinter.Tk()
root.title("Thruster types")
#root.geometry('700x500')
  
# Create the list of options
options_list = 'Tunnel', 'Azimuth', 'Pod', 'Shaft Line', 'Cycloid'
  

  
#Create an empty list that I will fill with my inputs
Thruster=[None]*5

# list of all StringVars for each OptionMenu
values = []

# Create the optionmenu widget and passing 
# the options_list and value_inside to it.
for i in range (0, 5, 1):
    # Variable to keep track of the option selected in OptionMenu
    value_inside = tkinter.StringVar(root)
     # Set the default value of the variable
    value_inside.set("Thruster"+str(i+1))   
    question_menu = tkinter.OptionMenu(root, value_inside, *options_list)
    question_menu.pack()
    values.append(value_inside)

    
def print_answers():
    for val in values:
        print(val.get()) #Placing the inputs into the list Thruster
    return None
  
  
# Submit button
# Whenever we click the submit button, our submitted
# option is printed ---Testing purpose
submit_button = tkinter.Button(root, text='Submit', command=print_answers)
submit_button.pack()

root.mainloop()