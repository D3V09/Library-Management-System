import tkinter as tk
from tkinter import messagebox
import csv

# Function to handle the "Submit" button click event
def submit_button_click():
    text = entry.get()
    messagebox.showinfo("Submitted Text", f"You entered: {text}")
    
    # Append the submitted data to a CSV file
    with open('data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([text])

# Function to handle the Enter key press in the text box
def on_enter_key(event):
    submit_button_click()  # Simulate a click on the "Submit" button

# Function to handle the "Close" button click event
def close_button_click():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Barcode Scanner GUI")

# Create a label
label = tk.Label(root, text="Scan the barcode:")
label.pack()

# Create a text box
entry = tk.Entry(root)
entry.pack()

# Bind the Enter key press event to the text box
entry.bind('<Return>', on_enter_key)

# Create the "Submit" button
submit_button = tk.Button(root, text="Submit", command=submit_button_click)
submit_button.pack()

# Create the "Close" button
close_button = tk.Button(root, text="Close", command=close_button_click)
close_button.pack()

# Start the main loop
root.mainloop()