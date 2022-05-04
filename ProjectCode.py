import tkinter as tk
from math import *


btn_params = {
    'padx': 16,
    'pady': 1,
    'bd': 4,
    'fg': 'black',
    'bg': '#888888',
    'font': ('arial', 15),
    'width': 2,
    'height': 2,
    'relief': 'flat',
    'activebackground': "#888888"
}


class Calculator:
    def clear_all_button(self):
            self.expression = ""
            self.input_text.set("")

    def equal_button(self):
            self.sum_up = str(eval(self.expression))
            self.input_text.set(self.sum_up)
            self.expression = self.sum_up
    def clear1_button(self):
        self.expression = self.expression[:-1]
        self.input_text.set(self.expression)

    def sign_change_button(self):
        self.expression = self.expression + '-'
        self.input_text.set(self.expression)

    def clear_memory(self):
        self.recall = ""

    

    def memory_add(self):
        self.recall = self.recall + '+' + self.expression

    

    def answer(self):
        self.answer = self.sum_up
        self.expression = self.expression + self.answer
        self.input_text.set(self.expression)

    

    def memory_recall(self):
        if self.expression == "":
            self.input_text.set('0' + self.expression + self.recall)
        else:
            self.input_text.set(self.expression + self.recall)
        
    
    def __init__(self, master):

        
        self.expression = ""
        
        self.recall = ""
        
        self.sum_up = ""
        
        self.input_text = tk.StringVar()
        
        self.master = master
        
        # setting frame for showing inputs and title
        top_frame = tk.Frame(master, width=650, height=20, bd=4, relief='flat', bg='#888888')
        top_frame.pack(side=tk.TOP)
        # setting frame for showing all buttons
        bottom_frame = tk.Frame(master, width=650, height=470, bd=4, relief='flat', bg='#888888')
        bottom_frame.pack(side=tk.BOTTOM)
        # name of calculator
        my_item = tk.Label(top_frame, text="Simple Scientific Calculator",
                           font=('arial', 13,'bold italic'), fg='Black', width=26, bg='#555555')
        my_item.pack()
        # UI for inputs
        display_text = tk.Entry(top_frame, font=('arial', 36,'bold'), relief='flat',
                               bg='#999999', fg='black',textvariable=self.input_text, width=60, bd=4, justify='right')
        display_text.pack()


        

        # row 0
        
        self.left_brac_button = tk.Button(bottom_frame, **btn_params, text="(", command=lambda: self.btn_click('('))
        self.left_brac_button.grid(row=0, column=0)
        
        self.right_brac_button = tk.Button(bottom_frame, **btn_params, text=")", command=lambda: self.btn_click(')'))
        self.right_brac_button.grid(row=0, column=1)
        
        self.expo_button = tk.Button(bottom_frame, **btn_params, text="exp", command=lambda: self.btn_click('exp('))
        self.expo_button.grid(row=0, column=2)
    
        self.pi_button = tk.Button(bottom_frame, **btn_params, text="π", command=lambda: self.btn_click('pi'))
        self.pi_button.grid(row=0, column=3)
        
        self.clear_button = tk.Button(bottom_frame, **btn_params, text="C", command=self.clear_all_button)
        self.clear_button.grid(row=0, column=4)
        
        self.del_button = tk.Button(bottom_frame, **btn_params, text="del", command=self.clear1_button)
        self.del_button.grid(row=0, column=5)
        
        self.btn_change_sign = tk.Button(bottom_frame, **btn_params, text="+/-", command=self.sign_change_button)
        self.btn_change_sign.grid(row=0, column=6)
        
        self.div_button = tk.Button(bottom_frame, **btn_params, text="/", command=lambda: self.btn_click('/'))
        self.div_button.grid(row=0, column=7)
        
        self.sqrt_button = tk.Button(bottom_frame, **btn_params, text="sqrt", command=lambda: self.btn_click('sqrt('))
        self.sqrt_button.grid(row=0, column=8)
        # row 1
        
       
        
        self.cube = tk.Button(bottom_frame, **btn_params, text=u"x\u00B3", command=lambda: self.btn_click('**3'))
        self.cube.grid(row=1, column=2)
        
        self.btn_abs = tk.Button(bottom_frame, **btn_params, text="abs", command=lambda: self.btn_click('abs' + '('))
        self.btn_abs.grid(row=1, column=3)
    
        self.number_7 = tk.Button(bottom_frame, **btn_params, text="7", command=lambda: self.btn_click(7))
        self.number_7.configure(activebackground="#5d5d5d", bg='#5d5d5d')
        self.number_7.grid(row=1, column=4)
        
        self.number_8 = tk.Button(bottom_frame, **btn_params, text="8", command=lambda: self.btn_click(8))
        self.number_8.configure(activebackground="#5d5d5d", bg='#5d5d5d')
        self.number_8.grid(row=1, column=5)
        
        self.number_9 = tk.Button(bottom_frame, **btn_params, text="9", command=lambda: self.btn_click(9))
        self.number_9.configure(activebackground="#5d5d5d", bg='#5d5d5d')
        self.number_9.grid(row=1, column=6)
        
        self.multi_buttton = tk.Button(bottom_frame, **btn_params, text="x", command=lambda: self.btn_click('*'))
        self.multi_buttton.grid(row=1, column=7)
        
        self.memory_clear_button = tk.Button(bottom_frame, **btn_params, text="MC", command=self.clear_memory)
        self.memory_clear_button.grid(row=1, column=8)
        # row 2
        
        self.sin_button = tk.Button(bottom_frame, **btn_params, text="sin", command=lambda: self.btn_click('fsin('))
        self.sin_button.grid(row=2, column=0)
        
        self.cos_button = tk.Button(bottom_frame, **btn_params, text="cos", command=lambda: self.btn_click('fcos('))
        self.cos_button.grid(row=2, column=1)
        
        self.tan_button = tk.Button(bottom_frame, **btn_params, text="tan", command=lambda: self.btn_click('ftan('))
        self.tan_button.grid(row=2, column=2)
        
        self.btn_log = tk.Button(bottom_frame, **btn_params, text="log", command=lambda: self.btn_click('log('))
        self.btn_log.grid(row=2, column=3)
        
        self.number_4 = tk.Button(bottom_frame, **btn_params, text="4", command=lambda: self.btn_click(4))
        self.number_4.configure(activebackground="#5d5d5d", bg='#5d5d5d')
        self.number_4.grid(row=2, column=4)
        
        self.number_5 = tk.Button(bottom_frame, **btn_params, text="5", command=lambda: self.btn_click(5))
        self.number_5.configure(activebackground="#5d5d5d", bg='#5d5d5d')
        self.number_5.grid(row=2, column=5)
        
        self.number_6 = tk.Button(bottom_frame, **btn_params, text="6", command=lambda: self.btn_click(6))
        self.number_6.configure(activebackground="#5d5d5d", bg='#5d5d5d')
        self.number_6.grid(row=2, column=6)
        
        self.sub_button = tk.Button(bottom_frame, **btn_params, text="-", command=lambda: self.btn_click('-'))
        self.sub_button.grid(row=2, column=7)
        
        self.memory_recall_button = tk.Button(bottom_frame, **btn_params, text="MR", command=self.memory_recall)
        self.memory_recall_button.grid(row=2, column=8)
        # row 3
        
        self.sin_inverse_button = tk.Button(bottom_frame, **btn_params, text=u"sin-\u00B9",
                                         command=lambda: self.btn_click('arcsin('))
        self.sin_inverse_button.grid(row=3, column=0)
        
        self.cos_inverse_button = tk.Button(bottom_frame, **btn_params, text=u"cos-\u00B9",
                                         command=lambda: self.btn_click('arcos('))
        self.cos_inverse_button.grid(row=3, column=1)
        
        self.tan_inverse_button = tk.Button(bottom_frame, **btn_params, text=u"tan-\u00B9",
                                         command=lambda: self.btn_click('arctan('))
        self.tan_inverse_button.grid(row=3, column=2)
        
        self.btn_ln = tk.Button(bottom_frame, **btn_params, text="ln", command=lambda: self.btn_click('log1p('))
        self.btn_ln.grid(row=3, column=3)
        
        self.number_1 = tk.Button(bottom_frame, **btn_params, text="1", command=lambda: self.btn_click(1))
        self.number_1.configure(activebackground="#5d5d5d", bg='#5d5d5d')
        self.number_1.grid(row=3, column=4)
        
        self.btn_2 = tk.Button(bottom_frame, **btn_params, text="2", command=lambda: self.btn_click(2))
        self.btn_2.configure(activebackground="#5d5d5d", bg='#5d5d5d')
        self.btn_2.grid(row=3, column=5)
        
        self.btn_3 = tk.Button(bottom_frame, **btn_params, text="3", command=lambda: self.btn_click(3))
        self.btn_3.configure(activebackground="#5d5d5d", bg='#5d5d5d')
        self.btn_3.grid(row=3, column=6)
        
        self.btn_add = tk.Button(bottom_frame, **btn_params, text="+", command=lambda: self.btn_click('+'))
        self.btn_add.grid(row=3, column=7)
        
        self.btn_M_plus = tk.Button(bottom_frame, **btn_params, text="M+", command=self.memory_add)
        self.btn_M_plus.grid(row=3, column=8)

        # row 4
        
        self.btn_fact = tk.Button(bottom_frame, **btn_params, text="n!", command=lambda: self.btn_click('factorial('))
        self.btn_fact.grid(row=4, column=0)
        
        self.btn_sqr = tk.Button(bottom_frame, **btn_params, text=u"x\u00B2", command=lambda: self.btn_click('**2'))
        self.btn_sqr.grid(row=4, column=1)
        
        self.btn_power = tk.Button(bottom_frame, **btn_params, text="x^y", command=lambda: self.btn_click('**'))
        self.btn_power.grid(row=4, column=2)
        
        self.btn_ans = tk.Button(bottom_frame, **btn_params, text="ans", command=self.answer)
        self.btn_ans.grid(row=4, column=3)
        
        self.number_0 = tk.Button(bottom_frame, **btn_params, text="0", command=lambda: self.btn_click(0))
        self.number_0.configure(activebackground="#5d5d5d", bg='#5d5d5d', width=7, bd=5)
        self.number_0.grid(row=4, column=4, columnspan=2)
        
        self.equals_button = tk.Button(bottom_frame, **btn_params, text="=", command=self.equal_button)
        self.equals_button.configure(bg='#999999', activebackground='#ff9980')
        self.equals_button.grid(row=4, column=6)
       
        self.decimal_button = tk.Button(bottom_frame, **btn_params, text=".", command=lambda: self.btn_click('.'))
        self.decimal_button.grid(row=4, column=7)
        
        self.btn_comma = tk.Button(bottom_frame, **btn_params, text=",", command=lambda: self.btn_click(','))
        self.btn_comma.grid(row=4, column=8)
        
        


    def btn_click(self, expression_val):
        if len(self.expression) >= 23:
            self.expression = self.expression
            self.input_text.set(self.expression)
        else:
            self.expression = self.expression + str(expression_val)
            self.input_text.set(self.expression)



        







root = tk.Tk()
b = Calculator(root)
root.title("Simple Scientific Calculator")
root.geometry("750x590+50+50")
root.resizable(False, False)
root.mainloop()
