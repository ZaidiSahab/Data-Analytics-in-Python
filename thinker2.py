import tkinter as tk
from tkinter import ttk, messagebox, filedialog, colorchooser

# Create the main window
root = tk.Tk()
root.title("Tkinter GUI Demo")
root.geometry("600x400")  # Window Geometry Management

# Label - Display text
label = tk.Label(root, text="Hello, Tkinter!", font=("Helvetica", 16))
label.pack(pady=10)

# Button - Add a button
def on_button_click():
    messagebox.showinfo("Button Clicked", "You clicked the button!")
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)

# Checkbutton - Add a check-box
check_var = tk.IntVar()
check_button = tk.Checkbutton(root, text="Check me!", variable=check_var)
check_button.pack(pady=5)

# Radiobutton - Add radio buttons
radio_var = tk.StringVar(value="Option 1")
radio1 = tk.Radiobutton(root, text="Option 1", variable=radio_var, value="Option 1")
radio2 = tk.Radiobutton(root, text="Option 2", variable=radio_var, value="Option 2")
radio1.pack(pady=5)
radio2.pack(pady=5)

# Menu - Add a menu bar
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=lambda: filedialog.askopenfilename())
file_menu.add_command(label="Save", command=lambda: filedialog.asksaveasfilename())
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

# Entry - Input field
entry = tk.Entry(root)
entry.pack(pady=10)

# Text Widget - Multi-line text input
text = tk.Text(root, height=4, width=40)
text.pack(pady=10)

# Slider - Add a slider
slider = tk.Scale(root, from_=0, to=100, orient="horizontal")
slider.pack(pady=10)

# Progressbar - Add a progress bar
progress = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
progress.pack(pady=10)
progress.start()

# Messagebox - Show different message boxes
def show_message_box():
    messagebox.showwarning("Warning", "This is a warning message!")
button_msg = tk.Button(root, text="Show Message Box", command=show_message_box)
button_msg.pack(pady=10)

# Color Chooser Dialog
def choose_color():
    colorchooser.askcolor(title="Choose a color")
button_color = tk.Button(root, text="Choose Color", command=choose_color)
button_color.pack(pady=10)

# Frame - Creating a frame
frame = tk.Frame(root, borderwidth=2, relief="sunken")
frame.pack(pady=20, fill="x")
label_in_frame = tk.Label(frame, text="Label inside a frame")
label_in_frame.pack(pady=10)

# Run the main loop
root.mainloop()
