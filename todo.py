import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        task_list.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Set window size and position
root.geometry("300x400")  # Width x Height

# Create widgets
task_entry = tk.Entry(root, width=30)
add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
task_list = tk.Listbox(root, selectmode=tk.SINGLE, height=15)  # Adjust the height

# Place widgets on the window
task_entry.pack(pady=10)
add_button.pack()
remove_button.pack()
task_list.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)  # Use fill and expand

# Run the application
root.mainloop()
