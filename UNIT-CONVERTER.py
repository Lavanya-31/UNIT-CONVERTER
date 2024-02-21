import tkinter as tk

def convert_units(conversion_factor):
    try:
        value = float(entry.get())
        result = value * conversion_factor
        result_label.config(text=f"Result: {result:.2f}")
    except ValueError:
        result_label.config(text="Invalid input")

# GUI setup
root = tk.Tk()
root.title("Simple Unit Converter")

# Label and Entry for user input
label = tk.Label(root, text="Enter Value:")
label.pack()
entry = tk.Entry(root)
entry.pack()

# Buttons for conversions
buttons = [
    ("Convert to Feet", 0.0328084),
    ("Convert to Inches", 12),
    ("Convert to Sqm", 0.092903),
    ("Convert to Hectare / Acres", 0.0000092903),
]

for btn_text, factor in buttons:
    tk.Button(root, text=btn_text, command=lambda f=factor: convert_units(f)).pack()

# Result display
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
