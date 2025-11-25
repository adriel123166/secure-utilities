import tkinter as tk

class Calculator(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Calculator")
        self.geometry("320x420")
        self.config(bg="#f0f5f9")

        self.expression = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        entry = tk.Entry(self, textvariable=self.expression, font=("Arial", 20), bd=10, insertwidth=2, width=17, borderwidth=4, justify='right')
        entry.grid(row=0, column=0, columnspan=4, pady=20)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('÷', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('×', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
            ('=', 5, 0, 4)
        ]

        for btn in buttons:
            text = btn[0]
            row = btn[1]
            col = btn[2]
            colspan = btn[3] if len(btn) > 3 else 1
            cmd = self.clear if text == "C" else self.equal if text == "=" else lambda x=text: self.press(x)
            tk.Button(self, text=text, padx=20, pady=20, bd=5, fg="black", font=("Arial", 14), bg="#d0e1f9", command=cmd).grid(row=row, column=col, columnspan=colspan, sticky="nsew")

        for i in range(6):
            self.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)

    def press(self, num):
        self.expression.set(self.expression.get() + str(num))

    def clear(self):
        self.expression.set("")

    def equal(self):
        expr = self.expression.get()
        try:
            result = str(eval(expr.replace("×", "*").replace("÷", "/")))
            self.expression.set(f"{expr} = {result}")
        except Exception:
            self.expression.set("Error")