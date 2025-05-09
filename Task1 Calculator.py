
import tkinter as tk

def on_click(value):
    display.set(display.get() + str(value))  # Append clicked number

def calculate():
    try:
        display.set(str(eval(display.get())))  # Replace input with evaluated result
    except:
        display.set("Error")  

def clear():
    display.set("")  # Clear input field

def backspace():
    display.set(display.get()[:-1])  # Remove last character

# Create GUI window
window = tk.Tk()
window.title("Calculator")
window.configure(bg="lightgray")

display = tk.StringVar()

# Display Box (Now Shows Result Inside)
entry = tk.Entry(window, textvariable=display, font=("Arial", 24), justify="right", bd=10, relief="ridge")
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Buttons Layout
buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('0', 5, 1)
]

for text, row, col in buttons:
    tk.Button(window, text=text, font=("Arial", 20), width=5, height=2, command=lambda t=text: on_click(t)).grid(row=row, column=col)

# Operator Buttons
ops = [('+', 2, 3), ('-', 3, 3), ('*', 4, 3), ('/', 5, 3)]
for text, row, col in ops:
    tk.Button(window, text=text, font=("Arial", 20), width=5, height=2, command=lambda t=text: on_click(t)).grid(row=row, column=col)

# Function Buttons
tk.Button(window, text="C", font=("Arial", 20), fg="red", width=5, height=2, command=clear).grid(row=5, column=0)
tk.Button(window, text="←", font=("Arial", 20), width=5, height=2, command=backspace).grid(row=5, column=2)
tk.Button(window, text="=", font=("Arial", 20), bg="green", width=10, height=2, command=calculate).grid(row=6, column=0, columnspan=4, pady=10)

# Run the GUI
window.mainloop()
