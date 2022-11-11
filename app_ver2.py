from tkinter import *
from tkinter import ttk
from tkinter.colorchooser import askcolor
from PIL import *
import PIL.Image
from PIL import ImageTk
import tkinter.messagebox as mbox
root = Tk()
root.geometry("500x500")
root.title("OTESL")
image1 = PIL.Image.open("HHTCOJ.png")
resize_image = image1.resize((100, 50))
new_image= ImageTk.PhotoImage(resize_image)
label1 = ttk.Label(root,image=new_image)
label1.image = new_image
label1.place(x=0, y=0)
title_1= Label(root,text="OTESL",font=25)
title_2 = Label(root,text="Name of websites:",font=20)
title_1.place(x=225,y=0)
title_2.place(x=0,y=40)
entry= Entry(root, width= 40)
entry.focus_set()
entry.place(x=150,y=60)
def get_value():
    text= entry.get()
    print(text)
ttk.Button(root, text= "Xac Nhan",width= 8,command=get_value).place(x=400,y=85)
title_3 = Label(root,text="Picture of websites:",font=20)
title_3.place(x=0,y=120)
entry2= Entry(root, width= 40)
entry2.focus_set()
entry2.place(x=150,y=150)
def get_value():
    text= entry.get()
    print(text)
ttk.Button(root, text= "Xac Nhan",width= 8,command=get_value).place(x=400,y=180)    
frame = Frame(root)
frame.place(x=200,y=250)
Label(frame, text="Tinh nang:").grid(row=0,padx=0,pady=0)
var1 = IntVar()
Checkbutton(frame, text="Cham bai", variable=var1).grid(row=1, sticky=W)
var2 = IntVar()
Checkbutton(frame, text="User", variable=var2).grid(row=2, sticky=W)
var3 = IntVar()
Checkbutton(frame, text="Toan", variable=var3).grid(row=3, sticky=W)
var4 = IntVar()
Checkbutton(frame, text="Tin", variable=var4).grid(row=4, sticky=W)
btn = Button(frame, text = 'xac nhan',command = root.destroy)
btn.grid(row=5)
def mebox():
    mbox.askokcancel(title="xac nhan thiet lap websites",message="hay dam bao cac tinh nang da duoc chon!!")
btn2 = Button(root, text = 'thiet lap websites',command = mebox).place(x=350,y=450)
root.mainloop()

