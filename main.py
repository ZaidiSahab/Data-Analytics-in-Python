import tkinter as tk
win=tk.Tk()
win.title("Youexcel")
win.iconbitmap(r"E:\ADVANCE-PYTHON-YOUEXCEL\thinker\thinker\174855.png")
win.attributes('-alpha',0.9)
win.config(bg="yellow")
win["bg"]="yellow"
win.geometry("300x500-100-100")


width=300
height=500
sys_width=win.winfo_screenwidth()
sys_height=win.winfo_screenheight()
c_x=int(sys_width/2-width/2)
c_y=int(sys_height/2-height/2)
win.geometry(f"{width}x{height}+{c_x}+{c_y}")


width=300
height=500
win.maxsize(500,500)
win.minsize(200,200)
win.resizable(False,False)





win.mainloop()

