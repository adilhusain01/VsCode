from tkinter import *

root = Tk()

myInput = Entry(root, width=50, borderwidth=5)
myInput.pack()
#myInput.insert(0, "Enter your name ...")

def myFunction():
    text1="Hello"+myInput.get()
    myLabel = Label(root, text=text1)
    myLabel.pack()

myButton=Button(root, text="Click me!", command=myFunction)
myButton.pack()

root.mainloop()