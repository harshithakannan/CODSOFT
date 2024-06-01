import tkinter as tk
from tkinter import messagebox

def calculate(operation):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Division by Zero.")
                return
        else:
            messagebox.showerror("Error", "Invalid operation.")
            return

        result_var.set(f"Your answer is : {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

# Main window
root = tk.Tk()
root.title("My Calculator")
root.geometry("500x500")
root.config(bg="#FFE4E1")

tk.Label(root, text="Enter the first number:", bg="#FFE4E1", font=('Arial', 12)).pack(pady=5)
entry_num1 = tk.Entry(root, font=('Arial', 12))
entry_num1.pack(pady=5)

tk.Label(root, text="Enter the second number:", bg="#FFE4E1", font=('Arial', 12)).pack(pady=5)
entry_num2 = tk.Entry(root, font=('Arial', 12))
entry_num2.pack(pady=5)

# Frame for operation buttons
button_frame = tk.Frame(root, bg="#FFE4E1")
button_frame.pack(pady=10)

# Buttons for each operation
add_button = tk.Button(button_frame, text="+", command=lambda: calculate("Add"), bg="#4CAF50", fg="white", font=('Arial', 12, 'bold'), width=5)
add_button.grid(row=0, column=0, padx=5, pady=5)

subtract_button = tk.Button(button_frame, text="-", command=lambda: calculate("Subtract"), bg="#f44336", fg="white", font=('Arial', 12, 'bold'), width=5)
subtract_button.grid(row=0, column=1, padx=5, pady=5)

multiply_button = tk.Button(button_frame, text="*", command=lambda: calculate("Multiply"), bg="#2196F3", fg="white", font=('Arial', 12, 'bold'), width=5)
multiply_button.grid(row=1, column=0, padx=5, pady=5)

divide_button = tk.Button(button_frame, text="/", command=lambda: calculate("Divide"), bg="#FF9800", fg="white", font=('Arial', 12, 'bold'), width=5)
divide_button.grid(row=1, column=1, padx=5, pady=5)

result_var = tk.StringVar(value="Result: ")
result_label = tk.Label(root, textvariable=result_var, bg="#CD2990", font=('Arial', 12))
result_label.pack(pady=10)

root.mainloop()
