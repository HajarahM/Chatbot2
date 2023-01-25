import tkinter as tk

'''
This code creates a simple UI with a label, an input field and a submit button. 
The input field allows the user to enter their question or statement, 
and the submit button calls the get_input_text() function when clicked, 
which retrieves the text entered in the input field using the get() method and prints it to the console.

The Tk() function creates the main window, and the title() method sets the title of the window. 
The Label, Entry, and Button widgets are used to create the label, input field, and submit button respectively. 
The pack() method is used to add the widgets to the window.
'''

def get_input_text():
    input_text = input_field.get()
    print(input_text)
    return input_text

# create the main window
root = tk.Tk()
root.title("Chatbot UI")

# create a label for the input field
input_label = tk.Label(root, text="Enter your question or statement:")
input_label.pack()

# create an input field
input_field = tk.Entry(root)
input_field.pack()

# create a submit button
submit_button = tk.Button(root, text="Submit", command=get_input_text)
submit_button.pack()

# run the main loop
root.mainloop()