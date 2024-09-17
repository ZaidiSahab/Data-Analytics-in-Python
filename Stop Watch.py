import tkinter as tk
import time

# Create the main window
root = tk.Tk()
root.title("Mustafa's Stopwatch")
root.geometry("400x500")
root.configure(bg="black")

# Variables
start_time = 0
elapsed_time = 0
running = False
laps = []

# Function to format time
def format_time(ms):
   # hours = int(ms / 3600000)
    minutes = int((ms % 3600000) / 60000)
    seconds = int((ms % 60000) / 1000)
    milliseconds = int(ms % 1000 / 10)
    return f"{minutes:02}:{seconds:02}.{milliseconds:02}"

# Update the display every 10 milliseconds
def update_time():
    if running:
        global elapsed_time
        elapsed_time = int(time.time() * 1000) - start_time
        time_label.config(text=format_time(elapsed_time))
        root.after(10, update_time)

# Start the stopwatch
def start_stop():
    global running, start_time, elapsed_time
    if running:
        running = False
        start_button.config(text="Start", fg="green")
    else:
        running = True
        start_button.config(text="Stop", fg="red")
        if elapsed_time == 0:
            start_time = int(time.time() * 1000)
        else:
            start_time = int(time.time() * 1000) - elapsed_time
        update_time()

# Reset the stopwatch
def reset():
    global elapsed_time, running, laps
    running = False
    elapsed_time = 0
    laps = []
    lap_list.delete(0, tk.END)
    time_label.config(text="00:00.00")
    start_button.config(text="Start", fg="green")

# Record lap
def lap():
    if running:
        laps.append(format_time(elapsed_time))
        lap_list.insert(0, f"Lap {len(laps)}: {laps[-1]}")

# UI Elements

mustafa_label = tk.Label(root, text="Zaidi's StopWatch", font=("Helvetica", 30), fg="#feed3b", bg="black")
mustafa_label.pack(pady=20)

time_label = tk.Label(root, text="00:00.00", font=("Helvetica", 40), fg="white", bg="black")
time_label.pack(pady=20)

# Buttons for Start/Stop, Reset, and Lap
button_frame = tk.Frame(root, bg="#feed3b")
button_frame.pack(pady=10)

start_button = tk.Button(button_frame, text="Start", command=start_stop, font=("Helvetica", 16), fg="green", bg="black", width=8)
start_button.grid(row=0, column=0, padx=5)

reset_button = tk.Button(button_frame, text="Reset", command=reset, font=("Helvetica", 16), fg="white", bg="black", width=8)
reset_button.grid(row=0, column=1, padx=5)

lap_button = tk.Button(button_frame, text="Lap", command=lap, font=("Helvetica", 16), fg="#75957B", bg="black", width=8)
lap_button.grid(row=0, column=2, padx=5)

# Listbox to show laps
lap_list = tk.Listbox(root, font=("Helvetica", 20), bg="#353128", fg="#feed3b", height=5, width=25)
lap_list.pack(pady=10)

# Run the application
root.mainloop()
