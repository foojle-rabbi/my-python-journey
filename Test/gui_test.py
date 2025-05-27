import tkinter as tk
from tkinter import messagebox

# Create the main window
window = tk.Tk()
window.title("My First GUI")
window.geometry("300x200")

# Function to run when button is clicked
def say_hello():
    messagebox.showinfo("Hello", "Welcome to Python GUI!")

# Create a button
btn = tk.Button(window, text="Click Me", command=say_hello)
btn.pack(pady=50)

# Start the GUI event loop
window.mainloop()

# I just first experienced a GUI based language first time. before that I never worked with GUI 
# I only just coded on cli so yeah its a good thing to start. that great.
