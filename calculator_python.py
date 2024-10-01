import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Avanzada")
        self.expression = ""
        self.memory = 0
        
        self.input_field = tk.Entry(root, font=('Arial', 24), borderwidth=2, relief='ridge')
        self.input_field.grid(row=0, column=0, columnspan=4, sticky='nsew')
        
        self.create_buttons()
        
        # Configurar el grid para que se expanda
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        for i in range(1, 5):
            self.root.grid_rowconfigure(i, weight=1)

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+',
            'M+', 'MR', 'MC', '%',
            'x²', '√', '±', '.'
        ]
        
        row_val = 1
        col_val = 0
        
        for button in buttons:
            tk.Button(self.root, text=button, font=('Arial', 18),
                      command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val, sticky='nsew')
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, button):
        if button == 'C':
            self.expression = ""
            self.input_field.delete(0, tk.END)
        elif button == '=':
            try:
                self.expression = str(eval(self.expression))
                self.input_field.delete(0, tk.END)
                self.input_field.insert(0, self.expression)
            except Exception as e:
                self.input_field.delete(0, tk.END)
                self.input_field.insert(0, "Error")
        elif button == 'M+':
            try:
                self.memory += float(self.expression)
            except:
                pass
        elif button == 'MR':
            self.input_field.delete(0, tk.END)
            self.input_field.insert(0, str(self.memory))
        elif button == 'MC':
            self.memory = 0
        elif button == '%':
            try:
                self.expression = str(float(self.expression) / 100)
                self.input_field.delete(0, tk.END)
                self.input_field.insert(0, self.expression)
            except:
                self.input_field.delete(0, tk.END)
                self.input_field.insert(0, "Error")
        elif button == 'x²':
            try:
                self.expression = str(float(self.expression) ** 2)
                self.input_field.delete(0, tk.END)
                self.input_field.insert(0, self.expression)
            except:
                self.input_field.delete(0, tk.END)
                self.input_field.insert(0, "Error")
        elif button == '√':
            try:
                self.expression = str(math.sqrt(float(self.expression)))
                self.input_field.delete(0, tk.END)
                self.input_field.insert(0, self.expression)
            except:
                self.input_field.delete(0, tk.END)
                self.input_field.insert(0, "Error")
        elif button == '±':
            try:
                self.expression = str(-float(self.expression))
                self.input_field.delete(0, tk.END)
                self.input_field.insert(0, self.expression)
            except:
                self.input_field.delete(0, tk.END)
                self.input_field.insert(0, "Error")
        else:
            self.expression += str(button)
            self.input_field.delete(0, tk.END)
            self.input_field.insert(0, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()