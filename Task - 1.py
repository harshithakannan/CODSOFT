import tkinter as tk
from tkinter import messagebox

# Main window
root = tk.Tk()
root.title("My To-Do List")
root.geometry("1000x500")
root.config(bg="#CDC0B0")

tasks = []

def add_task():
    task = task_entry.get()
    priority = priority_var.get()
    if task != "" and priority != "Select Priority":
        tasks.append((task, priority))
        update_task_listbox()
        task_entry.delete(0, tk.END)
        priority_var.set("Select Priority")
    else:
        messagebox.showwarning("Warning", "You must enter a task and select a priority.")

def remove_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        tasks.pop(selected_task_index[0])
        update_task_listbox()
    else:
        messagebox.showwarning("Warning", "You must select a task to remove.")

def update_task_listbox():
    task_listbox.delete(0, tk.END)
    priority_order = {"High": 1, "Medium": 2, "Low": 3}
    for task, priority in sorted(tasks, key=lambda x: priority_order[x[1]]):
        task_listbox.insert(tk.END, f"{task} ({priority} priority)")

# Frame for the task entry and buttons
input_frame = tk.Frame(root, bg="#f5f5f5")
input_frame.pack(pady=20)

# Entry box for new tasks
task_entry = tk.Entry(input_frame, width=30, font=('Arial', 14), bd=2)
task_entry.pack(side=tk.LEFT, padx=10)

# Dropdown menu for task priority
priority_var = tk.StringVar(value="Select Priority")
priority_options = ["High", "Medium", "Low"]
priority_menu = tk.OptionMenu(input_frame, priority_var, *priority_options)
priority_menu.config(width=12, bg="#5F9EA0", font=('Arial', 12), bd=2)
priority_menu.pack(side=tk.LEFT, padx=10)

# ADD task button
add_task_button = tk.Button(input_frame, text="Add Task", command=add_task, bg="#757575", fg="white", font=('Arial', 12, 'bold'), bd=0, padx=10, pady=5)
add_task_button.pack(side=tk.LEFT)

# Listbox to display tasks
task_listbox = tk.Listbox(root, width=50, height=15, font=('Arial', 12), bd=2, selectbackground="#FFB6C1")
task_listbox.pack(pady=10)

# REMOVE task button
button_frame = tk.Frame(root, bg="#f5f5f5")
button_frame.pack(pady=10)
remove_task_button = tk.Button(button_frame, text="Remove Task", command=remove_task, bg="#f85757", fg="white", font=('Arial', 12, 'bold'), bd=0, padx=10, pady=5)
remove_task_button.pack()

# Main loop
root.mainloop()
