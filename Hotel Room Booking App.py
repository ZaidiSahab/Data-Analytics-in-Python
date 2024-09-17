import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector

# Path to your background image
background_image_path = r"C:\Users\MY PC\Downloads\jpg2png\AI Images (4k) - Freepik (180124725189).png"

def connect_to_db():
    # Establish a connection to the MySQL database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",         # MySQL username (default for XAMPP is 'root')
        password="",         # MySQL password (leave empty if there's no password)
        database="hotel_booking_system"
    )
    return connection

def book_room_to_db(full_name, phone_number, checkin_date, checkout_date, guests, room_type):
    connection = connect_to_db()
    cursor = connection.cursor()

    # Insert booking details into the bookings table
    query = """
    INSERT INTO bookings (full_name, phone_number, checkin_date, checkout_date, guests, room_type)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (full_name, phone_number, checkin_date, checkout_date, guests, room_type))
    connection.commit()
    cursor.close()
    connection.close()

def fetch_room_data():
    connection = connect_to_db()
    cursor = connection.cursor()

    query = "SELECT full_name, room_type, checkin_date, checkout_date FROM bookings"
    cursor.execute(query)

    rooms = cursor.fetchall()

    cursor.close()
    connection.close()
    return rooms

def set_background(window):
    # Load the image and resize it to fit the window
    bg_image = Image.open(background_image_path)
    bg_image = bg_image.resize((window.winfo_screenwidth(), window.winfo_screenheight()), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Create a Canvas widget to hold the background image
    canvas = tk.Canvas(window, width=window.winfo_screenwidth(), height=window.winfo_screenheight())
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

    # Retain a reference to the image so it doesn't get garbage-collected
    window.bg_photo = bg_photo
    return canvas

def open_booking_form():
    def book_room():
        # Collect data from the form
        full_name = entry_name.get()
        phone_number = entry_phone.get()
        checkin_date = entry_checkin.get()
        checkout_date = entry_checkout.get()
        guests = entry_guests.get()
        room_type = combo_room_type.get()

        # Save booking details to the database
        book_room_to_db(full_name, phone_number, checkin_date, checkout_date, guests, room_type)

        # Show confirmation message
        messagebox.showinfo("Booking Confirmation", f"Room booked successfully!\n\nName: {full_name}\nRoom Type: {room_type}\nCheck-in: {checkin_date}\nCheck-out: {checkout_date}")
        booking_form.destroy()

    booking_form = tk.Toplevel(root)
    booking_form.title("Book a Room")
    booking_form.geometry("400x400")

    tk.Label(booking_form, text="Full Name:").pack(pady=5)
    entry_name = tk.Entry(booking_form)
    entry_name.pack(pady=5)

    tk.Label(booking_form, text="Phone Number:").pack(pady=5)
    entry_phone = tk.Entry(booking_form)
    entry_phone.pack(pady=5)

    tk.Label(booking_form, text="Check-in Date (YYYY-MM-DD):").pack(pady=5)
    entry_checkin = tk.Entry(booking_form)
    entry_checkin.pack(pady=5)

    tk.Label(booking_form, text="Check-out Date (YYYY-MM-DD):").pack(pady=5)
    entry_checkout = tk.Entry(booking_form)
    entry_checkout.pack(pady=5)

    tk.Label(booking_form, text="Number of Guests:").pack(pady=5)
    entry_guests = tk.Entry(booking_form)
    entry_guests.pack(pady=5)

    tk.Label(booking_form, text="Room Type:").pack(pady=5)
    combo_room_type = ttk.Combobox(booking_form, values=["Single", "Double", "Suite"])
    combo_room_type.pack(pady=5)

    tk.Button(booking_form, text="Book Now", command=book_room).pack(pady=10)

def view_bookings():
    view_window = tk.Toplevel(root)
    view_window.title("View Bookings")
    view_window.geometry("600x400")

    tree = ttk.Treeview(view_window, columns=("Name", "Room Type", "Check-in", "Check-out"), show='headings')
    tree.heading("Name", text="Customer Name")
    tree.heading("Room Type", text="Room Type")
    tree.heading("Check-in", text="Check-in Date")
    tree.heading("Check-out", text="Check-out Date")

    tree.pack(fill=tk.BOTH, expand=True)

    # Fetch and display bookings from the database
    bookings = fetch_room_data()
    for row in bookings:
        tree.insert("", tk.END, values=row)

def admin_login():
    def validate_admin():
        username = entry_username.get()
        password = entry_password.get()

        # Check if the entered admin credentials are correct
        if username == "admin" and password == "password":  # Replace with your own credentials or validation logic
            messagebox.showinfo("Login Successful", "Welcome Admin!")
            admin_login_window.destroy()  # Close the login window
            open_admin_panel()  # Open the admin panel for room management
        else:
            messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")

    admin_login_window = tk.Toplevel(root)
    admin_login_window.title("Admin Login")
    admin_login_window.geometry("300x200")

    tk.Label(admin_login_window, text="Admin Username:").pack(pady=5)
    entry_username = tk.Entry(admin_login_window)
    entry_username.pack(pady=5)

    tk.Label(admin_login_window, text="Admin Password:").pack(pady=5)
    entry_password = tk.Entry(admin_login_window, show="*")
    entry_password.pack(pady=5)

    tk.Button(admin_login_window, text="Login", command=validate_admin).pack(pady=20)

def open_admin_panel():
    # Admin panel where the admin can manage rooms
    admin_panel = tk.Toplevel(root)
    admin_panel.title("Admin Panel - Manage Rooms")
    admin_panel.geometry("400x400")

    tk.Button(admin_panel, text="Manage Rooms", command=manage_rooms).pack(pady=20)
    tk.Button(admin_panel, text="View Bookings", command=view_bookings).pack(pady=20)

def manage_rooms():
    def add_room():
        room_number = entry_room_number.get()
        room_type = combo_room_type.get()
        price = entry_price.get()
        capacity = entry_capacity.get()

        # Show confirmation message (simulating adding room without database)
        messagebox.showinfo("Room Management", f"Room added successfully!\n\nRoom Number: {room_number}\nRoom Type: {room_type}\nPrice: {price}\nCapacity: {capacity}")
        manage_form.destroy()

    manage_form = tk.Toplevel(root)
    manage_form.title("Manage Rooms")
    manage_form.geometry("400x400")

    tk.Label(manage_form, text="Room Number:").pack(pady=5)
    entry_room_number = tk.Entry(manage_form)
    entry_room_number.pack(pady=5)

    tk.Label(manage_form, text="Room Type:").pack(pady=5)
    combo_room_type = ttk.Combobox(manage_form, values=["Single", "Double", "Suite"])
    combo_room_type.pack(pady=5)

    tk.Label(manage_form, text="Price:").pack(pady=5)
    entry_price = tk.Entry(manage_form)
    entry_price.pack(pady=5)

    tk.Label(manage_form, text="Capacity:").pack(pady=5)
    entry_capacity = tk.Entry(manage_form)
    entry_capacity.pack(pady=5)

    tk.Button(manage_form, text="Add Room", command=add_room).pack(pady=10)

# Create the main window
root = tk.Tk()
root.title("Hotel Room Booking System")
root.geometry("800x600")

# Create a tabbed interface
tab_control = ttk.Notebook(root)

# Create frames for each tab
home_tab = ttk.Frame(tab_control)
book_tab = ttk.Frame(tab_control)
view_tab = ttk.Frame(tab_control)
manage_tab = ttk.Frame(tab_control)

tab_control.add(home_tab, text="Home")
tab_control.add(book_tab, text="Book a Room")
tab_control.add(view_tab, text="View Bookings")
tab_control.add(manage_tab, text="Manage Rooms")

tab_control.pack(expand=1, fill="both")

canvas = set_background(home_tab)


# Create frames within tabs for background colors
home_frame = tk.Frame(home_tab, background="#ADD8E6")
home_frame.pack(fill="both", expand=True)
book_frame = tk.Frame(book_tab, background="#FFE4B5")
book_frame.pack(fill="both", expand=True)
view_frame = tk.Frame(view_tab, background="#98FB98")
view_frame.pack(fill="both", expand=True)
manage_frame = tk.Frame(manage_tab, background="#FFB6C1")
manage_frame.pack(fill="both", expand=True)



# Home tab content
# Home tab content
home_label = tk.Label(canvas, text="Welcome to the Hotel Room Booking System", font=("Arial", 24), bg="white")
home_label.pack(pady=20)


# Book a Room tab content
book_button = tk.Button(book_frame, text="Book a Room", command=open_booking_form)
book_button.pack(pady=20)

# View Bookings tab content
view_button = tk.Button(view_frame, text="View Bookings", command=view_bookings)
view_button.pack(pady=20)

# Manage Rooms tab content
admin_button = tk.Button(manage_frame, text="Admin Login", command=admin_login)
admin_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
