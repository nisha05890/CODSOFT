import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Password Generator")
        self.root.geometry("400x300")  # Fixed size for the main window
        self.root.resizable(False, False)  # Disable window resizing

        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.pack()

        self.length_entry = tk.Entry(root)
        self.length_entry.pack()

        self.special_var = tk.IntVar()
        self.special_check = tk.Checkbutton(root, text="Use Special Characters", variable=self.special_var)
        self.special_check.pack()

        self.digits_var = tk.IntVar()
        self.digits_check = tk.Checkbutton(root, text="Use Digits", variable=self.digits_var)
        self.digits_check.pack()

        self.lower_var = tk.IntVar()
        self.lower_check = tk.Checkbutton(root, text="Use Lowercase Letters", variable=self.lower_var)
        self.lower_check.pack()

        self.upper_var = tk.IntVar()
        self.upper_check = tk.Checkbutton(root, text="Use Uppercase Letters", variable=self.upper_var)
        self.upper_check.pack()

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.password_label = tk.Label(root, text="Generated Password:")
        self.password_label.pack()

        self.password_viewer = tk.Text(root, width=40, height=5)
        self.password_viewer.pack()

    def generate_password(self):
        length_input = self.length_entry.get()

        if not length_input:
            messagebox.showwarning("Warning", "Please enter a password length.")
            return

        length = int(length_input)
        use_special = bool(self.special_var.get())
        use_digits = bool(self.digits_var.get())
        use_lower = bool(self.lower_var.get())
        use_upper = bool(self.upper_var.get())

        character_set = ""
        if use_special:
            character_set += string.punctuation
        if use_digits:
            character_set += string.digits
        if use_lower:
            character_set += string.ascii_lowercase
        if use_upper:
            character_set += string.ascii_uppercase

        if character_set:
            generated_password = ''.join(random.choice(character_set) for _ in range(length))
            self.password_viewer.delete('1.0', tk.END)
            self.password_viewer.insert(tk.END, generated_password)
        else:
            self.password_viewer.delete('1.0', tk.END)
            self.password_viewer.insert(tk.END, "Please select at least one character set.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
