import tkinter as tk
from tkinter import messagebox

# Initialize window
root = tk.Tk()
root.title("Colorful To-Do List")
root.geometry("500x500")
root.configure(bg="#f0f8ff")  # light blue background

# Task list
tasks = []

# Functions
def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def remove_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        task = listbox.get(index)
        tasks.remove(task)
        listbox.delete(index)
    else:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")

# Heading label
heading = tk.Label(root, text="🌟 My Colorful To-Do List 🌟", 
                   bg="#f0f8ff", fg="#2f4f4f", font=("Helvetica", 16, "bold"))
heading.pack(pady=15)

# Frame with border
frame = tk.Frame(root, bg="#add8e6", bd=5, relief=tk.RIDGE)
frame.pack(pady=10)

# Entry widget inside frame
entry = tk.Entry(frame, width=40, bg="#ffffff", fg="#333333", font=("Arial", 12))
entry.pack(pady=10)

# Add & Remove buttons
add_btn = tk.Button(frame, text="➕ Add Task", command=add_task,
                    bg="#90ee90", fg="#000000", font=("Arial", 12, "bold"))
add_btn.pack(pady=5)

remove_btn = tk.Button(frame, text="❌ Remove Selected Task", command=remove_task,
                       bg="#ffcccb", fg="#000000", font=("Arial", 12, "bold"))
remove_btn.pack(pady=5)

# Enlarged Listbox outside the frame
listbox = tk.Listbox(root, width=60, height=15,
                     bg="#fdfd96", fg="#000080", font=("Courier", 11))
listbox.pack(pady=10)

# Run the app
root.mainloop()