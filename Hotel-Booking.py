import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk




# Function to open the booking form window
def open_booking_form():
    def book_room():
        # Collect data from the form
        full_name = entry_name.get()
        phone_number = entry_phone.get()
        checkin_date = entry_checkin.get()
        checkout_date = entry_checkout.get()
        guests = entry_guests.get()
        room_type = combo_room_type.get()

        # Show confirmation message (simulating booking without database)
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

# Function to view bookings
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

    # Simulate viewing bookings with sample data
    sample_data = [
        ("John Doe", "Single", "2024-10-01", "2024-10-05"),
        ("Jane Smith", "Double", "2024-11-10", "2024-11-15"),
    ]
    for row in sample_data:
        tree.insert("", tk.END, values=row)

# Function to manage rooms (Admin functionality)
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


# Load and set the background image
image_path = r"C:\Users\YouExcel\Downloads\istockphoto-2152193820-1024x1024.png"  # Replace with your image path
image = Image.open(image_path)
background_image = ImageTk.PhotoImage(image)
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)  # Fill the entire window


# Create a tabbed interface
tab_control = ttk.Notebook(root)
home_tab = ttk.Frame(tab_control)
book_tab = ttk.Frame(tab_control)
view_tab = ttk.Frame(tab_control)
manage_tab = ttk.Frame(tab_control)

tab_control.add(home_tab, text="Home")
tab_control.add(book_tab, text="Book a Room")
tab_control.add(view_tab, text="View Bookings")
tab_control.add(manage_tab, text="Manage Rooms")

tab_control.pack(expand=1, fill="both")

# Home Tab
tk.Label(home_tab, text="Welcome to the Hotel Room Booking System", font=("Arial", 24)).pack(pady=20)
# Add an image or logo here (optional)
# Example: img = tk.PhotoImage(file="logo.png")
# tk.Label(home_tab, image=img).pack(pady=20)

# Book a Room Tab
tk.Button(book_tab, text="Book a Room", command=open_booking_form).pack(pady=20)

# View Bookings Tab
tk.Button(view_tab, text="View Bookings", command=view_bookings).pack(pady=20)

# Manage Rooms Tab
tk.Button(manage_tab, text="Manage Rooms", command=manage_rooms).pack(pady=20)

# Start the main event loop
root.mainloop()
