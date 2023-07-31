from tkinter import *
from PIL import ImageTk, Image

root=Tk()

img1=ImageTk.PhotoImage(Image.open('images/1.jpg'))
img2=ImageTk.PhotoImage(Image.open('images/2.jpg'))
img3=ImageTk.PhotoImage(Image.open('images/3.jpg'))
img4=ImageTk.PhotoImage(Image.open('images/4.jpg'))
img5=ImageTk.PhotoImage(Image.open('images/5.jpg'))
img6=ImageTk.PhotoImage(Image.open('images/6.jpg'))
img7=ImageTk.PhotoImage(Image.open('images/7.jpg'))
img8=ImageTk.PhotoImage(Image.open('images/8.jpg'))
img9=ImageTk.PhotoImage(Image.open('images/9.jpg'))
img10=ImageTk.PhotoImage(Image.open('images/10.jpg'))
img11=ImageTk.PhotoImage(Image.open('images/11.jpg'))
img12=ImageTk.PhotoImage(Image.open('images/12.jpg'))

list1=[img1,img2,img3,img4,img5,img6,img7,img8,img9,img10,img11,img12]
list2=[1,2,3,4,5,6,7,8,9,10,11,12]

label1=Label(image=img1, height=480, width=720)
label1.grid(row=0, column=0, columnspan=3)

label2=Label(root, text=("Image 1 of "+str(len(list1))) + "   ", bd=1, relief=SUNKEN, anchor=E)
label2.grid(row=3, column=0, columnspan=3, sticky=E+W)

count=0

def btnclick(val):
    global count, label1, label2 , button1, button2, button3
    if (val==0):
        count-=1
    elif (val==1):
        count+=1

    if (count==11) or (count==-12):
        count=0
    
    label1.grid_forget()
    label2.grid_forget()
    label1=Label(image=list1[count], height=480, width=720)
    label1.grid(row=0, column=0, columnspan=3)
    label2=Label(root, text=("Image "+ str(list2[count]) +" of "+str(len(list1))) + "   ", bd=1, relief=SUNKEN, anchor=E)
    label2.grid(row=3, column=0, columnspan=3, sticky=E+W)
    

    button1=Button(root,text="<<", command= lambda : btnclick(0)).grid(row=1, column=0)
    button2=Button(root,text="Exit",command=root.quit).grid(row=1, column=1)
    button3=Button(root,text=">>", command= lambda : btnclick(1)).grid(row=1, column=2)

button1=Button(root,text="<<", command= lambda : btnclick(0)).grid(row=1, column=0)
button2=Button(root,text="Exit",command=root.quit).grid(row=1, column=1)
button3=Button(root,text=">>", command= lambda : btnclick(1)).grid(row=1, column=2, pady=10)

root.mainloop()