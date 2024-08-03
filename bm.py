import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)
        messagebox.showinfo("BMI Result", f"Your BMI is {bmi}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x200")

# Create and place the weight label and entry
label_weight = tk.Label(root, text="Weight (kg):")
label_weight.pack(pady=5)
entry_weight = tk.Entry(root)
entry_weight.pack(pady=5)

# Create and place the height label and entry
label_height = tk.Label(root, text="Height (m):")
label_height.pack(pady=5)
entry_height = tk.Entry(root)
entry_height.pack(pady=5)

# Create and place the calculate button
button_calculate = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
button_calculate.pack(pady=20)

# Start the main event loop
root.mainloop()
