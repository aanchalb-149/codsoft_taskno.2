import tkinter as tk
from tkinter import messagebox

# Function to perform calculation
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operator.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero!")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid Operation!")
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

# GUI setup
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("500x350")
window.configure(bg="lightblue")

# Entry fields
tk.Label(window, text="Enter first number:", bg="lightblue").pack(pady=5)
entry1 = tk.Entry(window)
entry1.pack()

tk.Label(window, text="Enter second number:", bg="lightblue").pack(pady=5)
entry2 = tk.Entry(window)
entry2.pack()

tk.Label(window, text="Choose operation (+, -, *, /):", bg="lightblue").pack(pady=5)
operator = tk.Entry(window)
operator.pack()

# Calculate button
tk.Button(window, text="Calculate", command=calculate, bg="green", fg="white").pack(pady=10)

# Result label
result_label = tk.Label(window, text="Result: ", bg="lightblue", font=("Arial", 12))
result_label.pack(pady=10)

# Run the GUI
window.mainloop()