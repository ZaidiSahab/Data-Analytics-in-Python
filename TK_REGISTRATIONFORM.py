from tkinter import *
from tkinter import messagebox

def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    gender = gender_var.get()
    country = dropdown_var.get()
    selected_languages = [listbox_languages.get(i) for i in listbox_languages.curselection()]
    message = text_message.get("1.0", END)

    if not name or not email or not message.strip() or not gender or not country or not selected_languages:
        messagebox.showwarning("Input Error", "Please fill all fields")
    else:
        # Handle form submission logic (e.g., save data, send email)
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Gender: {gender}")
        print(f"Country: {country}")
        print(f"Languages: {', '.join(selected_languages)}")
        print(f"Message: {message}")
        messagebox.showinfo("Form Submitted", "Thank you for your inquiry!")
        clear_form()

def clear_form():
    entry_name.delete(0, END)
    entry_email.delete(0, END)
    text_message.delete("1.0", END)
    gender_var.set(None)
    dropdown_var.set(countries[0])
    listbox_languages.selection_clear(0, END)

root = Tk()
root.title("Enhanced Inquiry Form")

# Labels
Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky=E)
Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=5, sticky=E)
Label(root, text="Gender:").grid(row=2, column=0, padx=10, pady=5, sticky=E)
Label(root, text="Country:").grid(row=3, column=0, padx=10, pady=5, sticky=E)
Label(root, text="Languages:").grid(row=4, column=0, padx=10, pady=5, sticky=NE)
Label(root, text="Message:").grid(row=5, column=0, padx=10, pady=5, sticky=NE)

# Entry Widgets
entry_name = Entry(root, width=30)
entry_name.grid(row=0, column=1, padx=10, pady=5)

entry_email = Entry(root, width=30)
entry_email.grid(row=1, column=1, padx=10, pady=5)

# Gender Radio Buttons
gender_var = StringVar()
Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=2, column=1, sticky=W)
Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=2, column=1, padx=70, sticky=W)
Radiobutton(root, text="Other", variable=gender_var, value="Other").grid(row=2, column=1, padx=140, sticky=W)

# Country Dropdown
countries = ["Select Country", "United States", "Canada", "United Kingdom", "Australia", "India"]
dropdown_var = StringVar(root)
dropdown_var.set(countries[0])
OptionMenu(root, dropdown_var, *countries).grid(row=3, column=1, padx=10, pady=5, sticky=W)

# Languages Listbox
listbox_languages = Listbox(root, selectmode=MULTIPLE, height=5)
languages = ["Python", "Java", "C++", "JavaScript", "Ruby"]
for language in languages:
    listbox_languages.insert(END, language)
listbox_languages.grid(row=4, column=1, padx=10, pady=5, sticky=W)

# Message Textbox
text_message = Text(root, width=30, height=5)
text_message.grid(row=5, column=1, padx=10, pady=5)

# Submit Button
Button(root, text="Submit", command=submit_form).grid(row=6, column=1, padx=10, pady=10, sticky=E)

root.mainloop()
