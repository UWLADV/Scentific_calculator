import tkinter as tk
from math import *





class Calculator:
    def __init__(self, master):
        
        # setting frame for showing inputs and title
        top_frame = tk.Frame(master, width=650, height=20, bd=4, relief='flat', bg='#666666')
        top_frame.pack(side=tk.TOP)
        # setting frame for showing all buttons
        bottom_frame = tk.Frame(master, width=650, height=470, bd=4, relief='flat', bg='#666666')
        bottom_frame.pack(side=tk.BOTTOM)
        # name of calculator
        my_item = tk.Label(top_frame, text="Simple Scientific Calculator",
                           font=('arial', 14), fg='Grey', width=26, bg='#555555')
        my_item.pack()
        # UI for inputs
        display_text = tk.Entry(top_frame, font=('arial', 36), relief='flat',
                               bg='#666666', fg='Grey', width=60, bd=4, justify='right')
        display_text.pack()




root = tk.Tk()
b = Calculator(root)
root.title("Simple Scientific Calculator")
root.geometry("750x590+50+50")
root.resizable(False, False)
root.mainloop()
