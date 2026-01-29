import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("360x520")
        self.root.configure(bg="black")
        self.root.resizable(False, False)

        self.expression = ""

        # Display
        self.display = tk.Entry(
            root,
            font=("Arial", 36),
            bg="black",
            fg="white",
            bd=0,
            justify="right"
        )
        self.display.insert(0, "0")
        self.display.pack(fill="both", ipadx=8, ipady=20, padx=10, pady=20)

        # Buttons frame
        btn_frame = tk.Frame(root, bg="black")
        btn_frame.pack()

        buttons = [
            ["C", "()", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["+/-", "0", ".", "="]
        ]

        for row in buttons:
            row_frame = tk.Frame(btn_frame, bg="black")
            row_frame.pack(expand=True, fill="both")
            for btn in row:
                self.create_button(row_frame, btn)

    def create_button(self, frame, text):
        bg = "#1C1C1C"
        fg = "white"

        if text in ["/", "*", "-", "+"]:
            bg = "#9E9E9E"
            fg = "black"
        elif text == "=":
            bg = "#4CAF50"
        elif text == "C":
            bg = "#5A5A5A"

        button = tk.Button(
            frame,
            text=text,
            font=("Arial", 18),
            bg=bg,
            fg=fg,
            bd=0,
            height=2,
            width=6,
            command=lambda t=text: self.on_click(t)
        )
        button.pack(side="left", expand=True, fill="both", padx=5, pady=5)

    def on_click(self, value):
        if value == "C":
            self.expression = ""
            self.display.delete(0, tk.END)
            self.display.insert(0, "0")

        elif value == "=":
            try:
                result = str(eval(self.expression))
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
                self.expression = result
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
                self.expression = ""

        elif value == "+/-":
            if self.expression:
                if self.expression.startswith("-"):
                    self.expression = self.expression[1:]
                else:
                    self.expression = "-" + self.expression
                self.display.delete(0, tk.END)
                self.display.insert(0, self.expression)

        else:
            if self.display.get() == "0":
                self.display.delete(0, tk.END)
            self.expression += value
            self.display.insert(tk.END, value)


# Run app
root = tk.Tk()
Calculator(root)
root.mainloop()
