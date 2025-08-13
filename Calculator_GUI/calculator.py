import tkinter as tk
from math import sin, cos, sqrt, radians
import os

class Calculator:
    def __init__(self, root):
        self.root = root
        icon_path = os.path.join(os.path.dirname(__file__), "icon.ico")
        self.root.iconbitmap(icon_path)
        self.root.title("Calculator")
        self.root.geometry("350x450")
        self.expression = ""
        self.entry = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, pady=10)

        self.create_buttons()
        
    def add_to_expression(self, value):
        self.expression += str(value) #Appends all the clicked button values to the expression
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def clear(self):
        self.expression = ""
        self.entry.delete(0, tk.END)

    def calculate(self):
        try:
            result = eval(self.expression)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
            self.expression = str(result)
        except:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")
            self.expression = ""

    def calculate_sin(self):
        try:
            angle = radians(float(self.expression))
            result = sin(angle)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
            self.expression = str(result)
        except:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")
            self.expression = ""

    def calculate_cos(self):
        try:
            angle = radians(float(self.expression))
            result = cos(angle)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
            self.expression = str(result)
        except:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")
            self.expression = ""

    def calculate_sqrt(self):
        try:
            result = sqrt(float(self.expression))
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
            self.expression = str(result)
        except:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")
            self.expression = ""

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('sin', 5, 1), ('cos', 5, 2), ('√', 5, 3),
        ]

        for (text, row, col) in buttons:
            if text == '=':
                action = self.calculate
            elif text == 'C':
                action = self.clear
            elif text == 'sin':
                action = self.calculate_sin
            elif text == 'cos':
                action = self.calculate_cos
            elif text == '√':
                action = self.calculate_sqrt
            else:
                action = lambda val=text: self.add_to_expression(val)

            tk.Button(self.root, text=text, width=5, height=2, font=("Arial", 14), command=action)\
                .grid(row=row, column=col, padx=5, pady=5)

# Run the calculator
if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
