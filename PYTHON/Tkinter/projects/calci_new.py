from tkinter import *

root = Tk()
root.title("Calci")

memory_value=""
current_value=""
current_operation=""

def clear():
    global memory_value, current_value, current_operation
    memory_value=0
    current_value=""
    current_operation=""
    update_display()

def perform_operation(operation):
    global memory_value, current_value, current_operation
    if current_operation:
        calculate()
    memory_value=int(current_value)
    current_operation=operation
    current_value=""
    update_display()

def calculate():
    global memory_value, current_value, current_operation

    if current_value and memory_value and current_operation:
        if (current_operation=="X"):
            current_value=str(memory_value*int(current_value))
        if (current_operation=="-"):
            current_value=str(memory_value-int(current_value))
        if (current_operation=="+"):
            current_value=str(memory_value+int(current_value))
        if (current_operation=="/"):
            if (current_value==0):
                current_value="Error: Division by zero"
            else:
                current_value=str(memory_value/int(current_value))
        current_operation=""
        current_value=None
        update_display()


def insertion(digit):
    global current_value
    current_value+=digit
    update_display()

def update_display():
    display_label.config(text=current_value)

display_label = Label(root, width=20, font=("Arial", 20), anchor=E)
display_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button1 = Button(root, text="7", padx=30, pady=20, command=lambda : insertion("7")).grid(row=2,column=0)
button2 = Button(root, text="8", padx=30, pady=20, command=lambda : insertion("8")).grid(row=2,column=1)
button3 = Button(root, text="9", padx=30, pady=20, command=lambda : insertion("9")).grid(row=2,column=2)
button4 = Button(root, text="4", padx=30, pady=20, command=lambda : insertion("4")).grid(row=3,column=0)
button5 = Button(root, text="5", padx=30, pady=20, command=lambda : insertion("5")).grid(row=3,column=1)
button6 = Button(root, text="6", padx=30, pady=20, command=lambda : insertion("6")).grid(row=3,column=2)
button7 = Button(root, text="1", padx=30, pady=20, command=lambda : insertion("1")).grid(row=4,column=0)
button8 = Button(root, text="2", padx=30, pady=20, command=lambda : insertion("2")).grid(row=4,column=1)
button9 = Button(root, text="3", padx=30, pady=20, command=lambda : insertion("3")).grid(row=4,column=2)
button10 = Button(root, text="0", padx=30, pady=20, command=lambda : insertion("0")).grid(row=5,column=0)
button11 = Button(root, text="Clear", padx=57.2, pady=20, command=clear).grid(row=5,column=1, columnspan=2)


button12 = Button(root, text="X", padx=30, pady=20, command=lambda : perform_operation("X")).grid(row=6,column=0)
button13 = Button(root, text="/", padx=30, pady=20, command=lambda : perform_operation("/")).grid(row=6,column=1)
button14 = Button(root, text="-", padx=30, pady=20, command=lambda : perform_operation("-")).grid(row=6,column=2)


button15 = Button(root, text="+", padx=30, pady=20, command=lambda : perform_operation("+")).grid(row=7,column=0)
button16 = Button(root, text="=", padx=66.499, pady=20, command=calculate).grid(row=7,column=1, columnspan=2)

root.mainloop()