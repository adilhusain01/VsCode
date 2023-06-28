from tkinter import *

root = Tk()

mylabel1=Label(root, text="Hello world")
mylabel2=Label(root, text="This isnt fair")

mylabel1.grid(row=0,column=0)
mylabel2.grid(row=1,column=1)


## OR
  
'''
mylabel1=Label(root, text="Hello world").grid(row=0,column=0)
mylabel2=Label(root, text="This isnt fair").grid(row=1,column=1)
'''

root.mainloop()