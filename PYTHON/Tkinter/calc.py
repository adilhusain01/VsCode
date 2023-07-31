from tkinter import *

root = Tk()
root.title("Calci")

current_value = ""
memory_value = None
current_operation = None

def clear():
    global current_value, memory_value, current_operation
    current_value = ""
    memory_value = None
    current_operation = None
    update_display()

def perform_operation(operation):
    global current_value, memory_value, current_operation
    if current_operation:
        calculate()
    memory_value = int(current_value)
    current_operation = operation
    current_value = ""
    update_display()

def calculate():
    global current_value, memory_value, current_operation
    if current_value and memory_value and current_operation:
        if current_operation == "+":
            current_value = str(memory_value + int(current_value))
        elif current_operation == "-":
            current_value = str(memory_value - int(current_value))
        elif current_operation == "*":
            current_value = str(memory_value * int(current_value))
        elif current_operation == "/":
            if current_value == "0":
                current_value = "Error: Division by zero"
            else:
                current_value = str(memory_value / int(current_value))
        memory_value = None
        current_operation = None
        update_display()

def update_display():
    display_label.config(text=current_value)

# Create the display label
display_label = Label(root, width=20, font=("Arial", 20), anchor=E)
display_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create digit buttons
for i in range(9):
    digit = i + 1
    button = Button(root, text=str(digit), width=5, height=2, font=("Arial", 14),command=lambda digit=digit: insert_value(digit)).grid(row=(i // 3) + 1, column=i % 3)

# Create operator buttons
operators = ["+", "-", "*", "/"]
for i, operator in enumerate(operators):
    button = Button(root, text=operator, width=5, height=2, font=("Arial", 14),command=lambda operator=operator: perform_operation(operator)).grid(row=i + 4, column=3)

# Create the zero button
button_zero = Button(root, text="0", width=5, height=2, font=("Arial", 14),command=lambda: insert_value(0)).grid(row=4, column=0)

# Create the clear button
button_clear = Button(root, text="Clear", width=12, height=2, font=("Arial", 14),command=clear).grid(row=4, column=1, columnspan=2)

# Create the equals button
button_equals = Button(root, text="=", width=12, height=2, font=("Arial", 14),command=calculate).grid(row=5, column=1, columnspan=2)

root.mainloop()
