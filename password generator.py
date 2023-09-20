# Password Generator

from tkinter import *
import string
import secrets

def generate_password():
    passlength = int(length_entry.get())
    letter = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation
    combine = letter + symbols + numbers
    password = "".join(secrets.choice(combine) for i in range(passlength))
    result_label.config(text="Generated Password: " + password)

# Create the main window
window = Tk()
window.title("Password Generator")
window.geometry("350x200")
# Create label for main text
length_label = Label(window, text="Enter the length of the password:",font=("Arial black",12,"bold"))
length_label.grid(row=0,column=0)

# Create an entry field for password length
length_entry = Entry(window,font=("Arial black",10,"bold"),width=25,borderwidth=12)
length_entry.grid(row=2)

# Create a button to generate the password
generate_button = Button(window, text="Generate Password",font=("Calibre",12,"bold"), command=generate_password)
generate_button.grid(row=3)

# Create a result label
result_label = Label(window, text="",font=("Arial black",12,"bold"))
result_label.grid(row=4)

# Start the tkinter main loop
window.mainloop()
