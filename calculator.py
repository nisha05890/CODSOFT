import tkinter as tk
from tkinter import ttk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("680x370")  # Set fixed window size
        self.root.resizable(False, False)  # Disable window resizing

        self.result_var = tk.StringVar()
        self.result_var.set("")

        self.entry = ttk.Entry(root, textvariable=self.result_var, font=('Helvetica', 20))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        button_texts = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("C", 5, 0), ("←", 5, 1),  # Clear and Delete buttons
        ]

        for (text, row, col) in button_texts:
            button = ttk.Button(root, text=text, command=lambda t=text: self.on_button_click(t), style="CalculatorButton.TButton")
            button.grid(row=row, column=col, padx=5, pady=5)

        # Apply custom button style
        style = ttk.Style()
        style.configure("CalculatorButton.TButton", font=('Helvetica', 16), padding=10)

    def on_button_click(self, text):
        if text == "=":
            try:
                result = str(eval(self.result_var.get()))
                self.result_var.set(result)
            except:
                self.result_var.set("Error")
        elif text == "C":
            self.result_var.set("")  # Clear the entry
        elif text == "←":
            current_text = self.result_var.get()
            self.result_var.set(current_text[:-1])  # Delete the last character
        else:
            current_text = self.result_var.get()
            self.result_var.set(current_text + text)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
