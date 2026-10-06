import tkinter as tk
from tkinter import messagebox


def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
            result = num1 / num2

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")


def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="Result: ")


# Main window
root = tk.Tk()
root.title("Python Calculator")
root.geometry("400x350")
root.resizable(False, False)

title_label = tk.Label(
    root,
    text="Python Calculator",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=20)

tk.Label(root, text="Enter First Number").pack()
entry1 = tk.Entry(root, width=30)
entry1.pack(pady=5)

tk.Label(root, text="Enter Second Number").pack()
entry2 = tk.Entry(root, width=30)
entry2.pack(pady=5)

operation_var = tk.StringVar(value="+")

tk.Label(root, text="Select Operation").pack(pady=5)

operation_menu = tk.OptionMenu(
    root,
    operation_var,
    "+",
    "-",
    "*",
    "/"
)
operation_menu.pack()

tk.Button(
    root,
    text="Calculate",
    command=calculate,
    width=15
).pack(pady=15)

result_label = tk.Label(
    root,
    text="Result: ",
    font=("Arial", 14, "bold")
)
result_label.pack(pady=5)

tk.Button(
    root,
    text="Clear",
    command=clear,
    width=15
).pack(pady=10)

root.mainloop()