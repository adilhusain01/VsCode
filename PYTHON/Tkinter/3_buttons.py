from tkinter import *

root = Tk()

def myFunction():
    myLabel=Label(root, text="button is clicked")
    myLabel.pack()

myButton1 = Button(root, text="Click Me!")
myButton2 = Button(root, text="Click Me!", state=DISABLED)
myButton3 = Button(root, text="Click Me!", padx=20,pady=20, bg="blue", fg="red")
myButton4 = Button(root, text="Click Me!", command=myFunction)


myButton1.pack()
myButton2.pack()
myButton3.pack()
myButton4.pack()

root.mainloop()
