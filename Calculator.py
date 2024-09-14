import tkinter as tk
from tkinter import messagebox, ttk

# Function to update the entry field with button presses
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

# Function to clear the entry field
def clear_entry():
    entry.delete(0, tk.END)

# Function to perform the calculation
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

# Create the main window
root = tk.Tk()
root.title("Calculator App")
root.config(bg="black")
root.geometry("350x500")

# Styling using ttk
style = ttk.Style()
style.configure('TButton', font=('Arial', 14), background="#FDE047", foreground="black", borderwidth=1)
style.map('TButton', background=[('active', '#FDE047'), ('!active', '#333333')],
          relief=[('pressed', 'groove'), ('!pressed', 'flat')])
style.configure('TEntry', font=('Arial', 24), fieldbackground="#333333", foreground="black")

# Create an Entry widget for the display (right aligned)
entry = ttk.Entry(root, width=12, font=('Arial', 28), justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=20)

# Create digit and operation buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Loop through buttons list to create and position buttons in the grid
for (text, row, col) in buttons:
    if text == '=':
        ttk.Button(root, text=text, command=calculate).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    elif text == 'C':
        ttk.Button(root, text=text, command=clear_entry).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    else:
        ttk.Button(root, text=text, command=lambda t=text: button_click(t)).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Configure grid weight for resizing
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Run the application
root.mainloop()
