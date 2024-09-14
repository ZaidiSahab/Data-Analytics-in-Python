import tkinter as tk
from textwrap import fill

from tkinter import *
win=tk.Tk()

win.title("Zaidi File")
win.config(bg="blue")
lab1=tk.Label(win, text="Mustafa Zaidi",font=("arial",16),bg="white")
lab1.pack(padx=30,pady=20)

lab2=tk.Label(win, text="Age",font=("arial",12))
lab2.pack(padx=10,pady=20,side="left")
lab2=tk.Label(win, text="22",font=("arial",12))
lab2.pack(padx=10,pady=20,side="right")


win.mainloop()




