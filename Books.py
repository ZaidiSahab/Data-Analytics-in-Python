import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk, Image
import mysql.connector


# Function to connect to the database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="mustafazaidi"
        )
        return connection
    except mysql.connector.Error as err:
        messagebox.showerror("Connection Error", f"Error: {err}")
        return None


# Function to insert data into the database (Create)
def insert_data():
    isbn = entry_isbn.get()
    bookTitle = entry_bookTitle.get()
    author = entry_author.get()
    year = entry_year.get()

    if isbn and bookTitle and author and year:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute("INSERT INTO books (ISBN, BookTitle, Author, Year) VALUES (%s, %s, %s, %s)",
                               (isbn, bookTitle, author, year))
                connection.commit()
                messagebox.showinfo("Success", "Data inserted successfully!")
                clear_fields()
                fetch_data()  # Refresh the data in Treeview
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Failed to insert data: {err}")
            finally:
                cursor.close()
                connection.close()
        else:
            messagebox.showerror("Error", "Failed to connect to the database.")
    else:
        messagebox.showwarning("Input Error", "All fields are required!")


# Function to fetch data from the database (Read)
def fetch_data():
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM books")
            rows = cursor.fetchall()
            tree.delete(*tree.get_children())  # Clear the Treeview
            for row in rows:
                tree.insert("", "end", values=row)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to fetch data: {err}")
        finally:
            cursor.close()
            connection.close()


# Function to update a selected record (Update)
def update_data():
    selected_item = tree.selection()
    if selected_item:
        isbn = entry_isbn.get()
        bookTitle = entry_bookTitle.get()
        author = entry_author.get()
        year = entry_year.get()

        if isbn and bookTitle and author and year:
            connection = connect_to_database()
            if connection:
                cursor = connection.cursor()
                try:
                    current_title = tree.item(selected_item, 'values')[0]  # Correct column index for Book Title

                    cursor.execute("""
                        UPDATE books
                        SET  ISBN=%s ,BookTitle=%s, Author=%s, Year=%s
                        WHERE BookTitle=%s
                    """, (isbn, bookTitle, author, year, current_title))

                    connection.commit()
                    messagebox.showinfo("Success", "Data updated successfully!")
                    clear_fields()
                    fetch_data()  # Refresh the data in Treeview
                except mysql.connector.Error as err:
                    messagebox.showerror("Error", f"Failed to update data: {err}")
                finally:
                    cursor.close()
                    connection.close()
            else:
                messagebox.showerror("Error", "Failed to connect to the database.")
        else:
            messagebox.showwarning("Input Error", "All fields are required!")
    else:
        messagebox.showwarning("Selection Error", "Please select a record to update.")


# Function to delete a selected record (Delete)
def delete_data():
    selected_item = tree.selection()
    if selected_item:
        selected_title = tree.item(selected_item, 'values')[0]  # Correct column index for Book Title
        if selected_title:
            connection = connect_to_database()
            if connection:
                cursor = connection.cursor()
                try:
                    print(f"Deleting record with BookTitle: {selected_title}")  # Debugging

                    cursor.execute("DELETE FROM books WHERE BookTitle=%s", (selected_title,))
                    connection.commit()

                    if cursor.rowcount > 0:
                        messagebox.showinfo("Success", "Data deleted successfully!")
                    else:
                        messagebox.showwarning("Warning", "No record found with the provided title.")

                    fetch_data()  # Refresh the data in Treeview
                except mysql.connector.Error as err:
                    messagebox.showerror("Error", f"Failed to delete data: {err}")
                finally:
                    cursor.close()
                    connection.close()
            else:
                messagebox.showerror("Error", "Failed to connect to the database.")
        else:
            messagebox.showwarning("Selection Error", "No title selected.")
    else:
        messagebox.showwarning("Selection Error", "Please select a record to delete.")


# Function to clear input fields
def clear_fields():
    entry_isbn.delete(0, tk.END)
    entry_bookTitle.delete(0, tk.END)
    entry_author.delete(0, tk.END)
    entry_year.delete(0, tk.END)


# Function to fill entry fields with selected row data
def fill_fields(event):
    selected_item = tree.selection()
    if selected_item:
        selected = tree.item(selected_item, 'values')
        entry_bookTitle.delete(0, tk.END)
        entry_bookTitle.insert(0, selected[0])  # Correct column index for Book Title
        entry_author.delete(0, tk.END)
        entry_author.insert(0, selected[1])
        entry_year.delete(0, tk.END)
        entry_year.insert(0, selected[2])
        entry_isbn.delete(0, tk.END)
        entry_isbn.insert(0, selected[3])


# Create the main window
root = tk.Tk()
root.title("CRUD App")
root.geometry("600x500")

# Load the background image
bg_image = Image.open(r"C:\Users\MY PC\Desktop\books-1617327_640.jpg")

bg_photo = ImageTk.PhotoImage(bg_image)

# Create a Canvas to hold the background image
canvas = tk.Canvas(root, width=600, height=500)
canvas.pack(fill="both", expand=True)

# Display the background image on the Canvas
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Create a Frame for the entry fields and buttons
frame = tk.Frame(canvas, bg="white")
canvas.create_window((300, 200), window=frame, anchor="center")

# Create entry fields on the frame
tk.Label(frame, text="Book Title:", bg="white").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
entry_bookTitle = tk.Entry(frame)
entry_bookTitle.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame, text="Author:", bg="white").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
entry_author = tk.Entry(frame)
entry_author.grid(row=2, column=1, padx=10, pady=5)

tk.Label(frame, text="Year:", bg="white").grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
entry_year = tk.Entry(frame)
entry_year.grid(row=3, column=1, padx=10, pady=5)

tk.Label(frame, text="ISBN:", bg="white").grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
entry_isbn = tk.Entry(frame)
entry_isbn.grid(row=0, column=1, padx=10, pady=5)

# Create CRUD buttons on the frame
submit_button = tk.Button(frame, text="Add Book", command=insert_data)
submit_button.grid(row=4, column=0, pady=10)

update_button = tk.Button(frame, text="Update Book", command=update_data)
update_button.grid(row=4, column=1, pady=10)

delete_button = tk.Button(frame, text="Delete Book", command=delete_data)
delete_button.grid(row=4, column=2, pady=10)

clear_button = tk.Button(frame, text="Clear", command=clear_fields)
clear_button.grid(row=4, column=3, pady=10)

# Create Treeview to display data (Read) and add to the canvas
tree = ttk.Treeview(root, columns=("ISBN", "Book Title", "Author", "Year",), show="headings")
tree.heading("ISBN", text="ISBN")
tree.heading("Book Title", text="Book Title")
tree.heading("Author", text="Author")
tree.heading("Year", text="Year")

tree.column("ISBN", width=100)
tree.column("Book Title", width=150)
tree.column("Author", width=150)
tree.column("Year", width=100)

canvas.create_window((300, 400), window=tree, anchor="center")

# Bind the Treeview select event to fill entry fields
tree.bind("<<TreeviewSelect>>", fill_fields)

# Fetch and display data in Treeview
fetch_data()

# Run the application
root.mainloop()
