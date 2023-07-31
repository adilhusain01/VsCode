from tkinter import *
from PIL import ImageTk,Image

root= Tk()
root.title("Image,Exit")
root.iconbitmap('space5.ico')

button1=Button(root, text="Exit!", command=root.quit) 
button1.pack()

img=ImageTk.PhotoImage(Image.open("space5.png"))
label1=Label(root, image=img)
label1.pack()

root.mainloop()