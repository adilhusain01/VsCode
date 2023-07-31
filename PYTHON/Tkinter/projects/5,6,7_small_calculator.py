from tkinter import *

root = Tk()
root.title("Calci")

addition=0
substraction=0
multiplication=0
division=0

def insertion(x):
    y = input1.get() + x
    input1.delete(0,END)
    input1.insert(0,y)

def clear():
    global addition
    global division
    global multiplication
    global substraction

    input1.delete(0,END)
    addition=0
    substraction=0
    multiplication=0
    division=0


def add():
    if (input1.get()!=""):
        global addition
        addition += int(input1.get())
        input1.delete(0,END)


def divide():
    if (input1.get()!=""):
        global division
        if (division==0):
            division = int(input1.get())
        else:
            division/=int(input1.get())
        input1.delete(0,END)

def substract():
    if (input1.get()!=""):
        global substraction
        if (substraction==0):
            substraction = int(input1.get())
        else:
            substraction -= int(input1.get())
        input1.delete(0,END)

def multiply():
    if (input1.get()!=""):
        global multiplication
        if (multiplication==0):
            multiplication = int(input1.get())
        else:
            multiplication *= int(input1.get())
        input1.delete(0,END)


def calculate():
    global division
    global multiplication
    global addition
    global substraction

    if (input1.get()!=""):
        if (division!=0) or (multiplication!=0) or (substraction!=0) or (addition!=0):
            if ((division!=0) and (multiplication==0) and (substraction==0) and (addition==0)):
                division/=int(input1.get())
                input1.delete(0, END)
                input1.insert(0, division)


            if ((multiplication!=0) and (division==0) and (addition==0) and (substraction==0)):
                multiplication*=int(input1.get())
                input1.delete(0, END)
                input1.insert(0, multiplication)

            if ((addition!=0) and (substraction==0) and (multiplication==0) and (division==0)):
                addition+=int(input1.get())
                input1.delete(0, END)
                input1.insert(0, addition)

            if ((division==0) and (addition==0) and (substraction!=0) and (multiplication==0)):
                substraction-=int(input1.get())
                input1.delete(0, END)
                input1.insert(0, substraction)



input1 = Entry(root, width=36)
input1.grid(row=0, column=0, columnspan=3, pady=20)

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


button12 = Button(root, text="X", padx=30, pady=20, command=multiply).grid(row=6,column=0)
button13 = Button(root, text="/", padx=30, pady=20, command=divide).grid(row=6,column=1)
button14 = Button(root, text="-", padx=30, pady=20, command=substract).grid(row=6,column=2)


button15 = Button(root, text="+", padx=30, pady=20, command=add).grid(row=7,column=0)
button16 = Button(root, text="=", padx=66.499, pady=20, command=calculate).grid(row=7,column=1, columnspan=2)

root.mainloop()