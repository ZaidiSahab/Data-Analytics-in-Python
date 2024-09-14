import tkinter as tk
from tkinter import messagebox




# Function to add a task
def add_task():
    task = task_entry.get()

    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")


#Updating Tasks
def edit_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(selected_task_index)
        task_entry.delete(0, tk.END)
        task_entry.insert(tk.END, task)
        tasks_listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Edit Error", "Please select a task to edit.")

# Function to delete a task
def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Delete Error", "Please select a task to delete.")

# Function to display all tasks (In the listbox itself)
def display_tasks():
    tasks_listbox.delete(0, tk.END)
    from asyncio import tasks
    for task in tasks:
        tasks_listbox.insert(tk.END, task)

# Styling configuration
def configure_ui(widget, bg_color, fg_color, font):
    widget.configure(bg=bg_color, fg=fg_color, font=font)

#Creating A Main Window For The program
root =tk.Tk()
root.title("Mustafa's Todo_Crud App")
root.geometry("400x500")
root.configure(bg="#2D2F33")  # Dark background to match the image

# Fonts and Colors
button_font = ('Arial', 12, 'bold')
label_font = ('Arial', 12, 'bold')
entry_font = ('Arial', 14)

bg_color = "#2D2F33"  # Dark background
task_color = "#A8FF00"  # Greenish color for text/buttons

# Creating a label and entry for task input
task_label = tk.Label(root, text="Enter a task:" ,  font=label_font, bg=bg_color, fg=task_color)
task_label.pack(pady=10)

task_entry = tk.Entry(root, width=40 ,font =entry_font)
task_entry.pack(pady=5)


# Creating button for adding
add_button= tk.Button(root, text='Add Task', width=15,command=add_task ,bg=task_color, fg=bg_color, font=button_font)
add_button.pack(pady=5)

# Create the listbox to display tasks
tasks_listbox = tk.Listbox(root, height=10, width=50, font=entry_font, bg=bg_color, fg=task_color)
tasks_listbox.pack(pady=10)


# Create Edit button
edit_button = tk.Button(root, text="Edit Task", width=15, command=edit_task, bg=task_color, fg=bg_color, font=button_font)
edit_button.pack(pady=5)

# Creating button for DELETING
delete_button= tk.Button(root, text='Delete Task', width=15,command=delete_task ,bg=task_color, fg=bg_color, font=button_font)
delete_button.pack(pady=5)



#RUN APPLICATION

root.mainloop()