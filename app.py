from tkinter import *
from tkinter import ttk
import os
import subprocess
from PIL import *
import PIL.Image
from PIL import ImageTk
import tkinter.messagebox as mbox
import time
import pyautogui as au
import pyautogui, sys
# Designing window for registration
 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    main_screen.destroy()
    root = Toplevel()
    root.title("OTESL")
    root.geometry("1366x768")
    frame1= Frame(root,highlightthickness=2,highlightbackground="black")
    image1 = PIL.Image.open("HHTCOJ.png")
    resize_image = image1.resize((100, 50))
    new_image= ImageTk.PhotoImage(resize_image)
    label1 = ttk.Label(frame1,image=new_image)
    label1.image = new_image
    label1.grid(row=0,column=0)
    title_1= Label(frame1,text="OTESL",font=35).grid(row=0,column=1)
    title_2 = Label(frame1,text="Name of websites:",font=20).grid(row=1,column=0)
    entry= Entry(frame1,width= 40).grid(row=1,column=1)
    def get_value():
        text= entry.get()
        print(text)
    Button(frame1, text= "Xac Nhan",width= 8,command=get_value).grid(row=2,column=1)
    title_3 = Label(frame1,text="Picture of websites:",font=20).grid(row=3,column=0)
    entry= Entry(frame1,width= 40).grid(row=3,column=1)
    def get_value_1():
        hq=Toplevel()
        hq.geometry("200x200")
        def cj():
            hq.destroy()
        Label(hq,text="tinh nang dang thu nghiem").pack()
        Button(hq,text="thoat",command=cj).pack()
    def get_value_2():
        hq=Toplevel()
        hq.geometry("200x200")
        def cj():
            hq.destroy()
        Label(hq,text="tinh nang dang thu nghiem").pack()
        Button(hq,text="thoat",command=cj).pack()
    def get_value_3():
        hq=Toplevel()
        hq.geometry("200x200")
        def cj():
            hq.destroy()
        Label(hq,text="tinh nang dang thu nghiem").pack()
        Button(hq,text="thoat",command=cj).pack()
    def get_value_4():
        hq=Toplevel()
        hq.geometry("200x200")
        def cj():
            hq.destroy()
        Label(hq,text="tinh nang dang thu nghiem").pack()
        Button(hq,text="thoat",command=cj).pack()
        Button(hq,text="thoat",command=cj).pack()
    def get_value_5():
        hq=Toplevel()
        hq.geometry("200x200")
        def cj():
            hq.destroy()
        Label(hq,text="tinh nang dang thu nghiem").pack()
        Button(hq,text="thoat",command=cj).pack()
        Button(hq,text="thoat",command=cj).pack()
    
    Button(frame1, text= "Xac Nhan",width= 8,command=get_value_1).grid(row=4,column=1)
    frame2 = Frame(frame1,highlightthickness=2,highlightbackground="black")
    Label(frame2, text="Tinh nang:").grid(row=0)
    var1 = IntVar()
    Checkbutton(frame2, text="Cham bai", variable=var1).grid(row=1,column=0,padx=20)
    var2 = IntVar()
    Checkbutton(frame2, text="User", variable=var2).grid(row=1,column=1)
    var3 = IntVar()
    Checkbutton(frame2, text="Toan", variable=var3,command=get_value_2).grid(row=2,column=0)
    var4 = IntVar()
    Checkbutton(frame2, text="Tin", variable=var4).grid(row=2,column=1)
    btn = Button(frame2, text = 'xac nhan').grid(row=5,sticky=E)
    var5 =IntVar()
    Checkbutton(frame2, text="BXH", variable=var5).grid(row=1,column=2)
    var6 =IntVar()
    Checkbutton(frame2, text="PYTHON", variable=var6,command=get_value_3).grid(row=2,column=2)
    var7 =IntVar()
    Checkbutton(frame2, text="C++", variable=var7,command=get_value_4).grid(row=1,column=3)
    var8 =IntVar()
    Checkbutton(frame2, text="JAVA", variable=var8,command=get_value_5).grid(row=2,column=3)
    frame2.grid(row=6)
    frame12 = Frame(frame1,highlightbackground="black",highlightthickness=2)
    def hideBG():
        global state
        if state == "Hidden":
            background_label.pack()
            state = "Showing"
        elif state == "Showing":
            background_label.pack_forget()
            state = "Hidden"
    background_image= PhotoImage(file="HHTCOJ.png")
    background_label = Label(frame12, image=background_image)
    hideBttn = Button(frame12,text="Hide Background",command=hideBG)
    state = "Showing"
    hideBttn.pack()
    background_label.pack()
    frame12.grid(row=7)
    frame1.pack(side=LEFT,fill="both")
    
    """frame 3"""
    frame3= Frame(root,highlightbackground="black",highlightthickness=2)
    def ket_noi():
        os.system("gnome-terminal -e 'bash -c \"sudo lsof -i tcp:80; exec bash\"'")
    def ket_noi_2():
        os.system("gnome-terminal -e 'bash -c \"sudo lsof -t -i tcp:80 -s tcp:listen | sudo xargs kill; exec bash\"'")
    def ket_noi_3():
        os.system("gnome-terminal -e 'bash -c \"sudo docker-compose up -d; exec bash\"'")
    def ket_noi_4():
        os.system("gnome-terminal -e 'bash -c \"ifconfig; exec bash\"'")
        root2.destroy()
        root3 = Toplevel()
        root3.geometry("400x400")
        t1 = Label(root3,text="chuc mung ban da thiet lap thanh cong",font=10).grid(row=0)
        t2 = Label(root3,text="dia chi trang web cua ban o dong \n Docker 0: inet:___",font=10).grid(row=1)
        def kill_():
            root3.destroy()
        Button(root3,text="thoat",command=kill_)
    title_1= Label(frame3,text="TIEN TRINH XAY DUNG TRANG WEB",font=15).grid(row=0)
    title_2= Label(frame3,text="Buoc 1: Xac dinh port 80",font=15).grid(row=1)
    nut_1= Button(frame3,text="xac nhan",command=ket_noi).grid(row=2)
    title_2= Label(frame3,text="Buoc 2: kill port 80",font=15).grid(row=3)
    nut_2= Button(frame3,text="xac nhan",command=ket_noi_2).grid(row=4)
    title_3= Label(frame3,text="Buoc 3: truy cap quyen root, Thu muc, Pull Image",font=15).grid(row=5)
    nut_3= Button(frame3,text="xac nhan",command=ket_noi_3).grid(row=6)
    title_4= Label(frame3,text="Buoc 4: lay dia chi trang website",font=15).grid(row=7)
    nut_4= Button(frame3,text="xac nhan",command=ket_noi_4).grid(row=8)
    frame3.pack(side=BOTTOM,expand=True)
    """frame4"""
    frame4 = Frame(frame3,highlightbackground="black",highlightthickness=2)
    def ket_noi():
        mbox.askyesnocancel(title="XAC NHAN LAI",message="BAN CO MUON TIEP TUC")
        au.hotkey('ctrl', 'alt', 't')
        au.moveTo(263,136,2)
        au.click
        au.press("F11")
        au.sleep("2")
        au.write('sudo lsof -i tcp:80',interval=0.25)
        au.press("enter")
        au.click()
        au.write("hq07092005",interval=0.25)
        au.press("enter")
        au.click()
        au.write("sudo lsof -t -i tcp:80 -s tcp:listen | sudo xargs kill",interval=0.25)
        au.press("enter")
        au.write("sudo -i",interval=0.25)
        au.press("enter")
        au.write("cd ..",interval=0.25)
        au.press("enter")
        au.write("cd home",interval=0.25)
        au.press("enter")
        au.write("cd haiquy",interval=0.25)
        au.press("enter")
        au.write("cd OnlineJudgeDeploy",interval=0.25)
        au.press("enter")
        au.write("docker-compose up -d",interval=0.25)
        au.press("enter")
        au.write("ifconfig",interval=0.25)
    def ket_noi_4():
        os.system("gnome-terminal -e 'bash -c \"ifconfig; exec bash\"'")
        root2.destroy()
        root3 = Toplevel()
        root3.geometry("400x400")
        t1 = Label(root3,text="chuc mung ban da thiet lap thanh cong",font=10).grid(row=0)
        t2 = Label(root3,text="dia chi trang web cua ban o dong \n Docker 0: inet:___",font=10).grid(row=1)
        def kill_():
            root3.destroy()
        Button(root3,text="thoat",command=kill_)
    title_1= Label(frame4,text="TIEN TRINH THIET LAP SEVERV WEB",font=15).grid(row=0)
    title_3= Label(frame4,text="Buoc 1: TU DONG HOA",font=15).grid(row=5)
    nut_3= Button(frame4,text="xac nhan",command=ket_noi).grid(row=6)
    title_4= Label(frame4,text="Buoc 2: DIA CHI WEB",font=15).grid(row=7)
    nut_4= Button(frame4,text="xac nhan",command=ket_noi_4).grid(row=8)
    frame4.grid(padx=50)


 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.title("Login or Register")
    main_screen.geometry("1366x768")

    def thong_tin_co_ngoc():
        k = Toplevel()
        def destroy_():
            k.destroy()
        k.title("thong tin co ngoc")
        t= Label(k,text="Thong tin co ngoc___________\n ___________").pack()
        b= Button(k,text="xong",command=destroy_).pack()
        k.mainloop()
    def thong_tin_hai_quy():
        k = Toplevel()
        def destroy_():
            k.destroy()
        k.title("thong tin hai quy")
        t= Label(k,text="Thong tin hai quy___________\n ___________").pack()
        b= Button(k,text="xong",command=destroy_).pack()
        k.mainloop()
    def thong_tin_duc_anh():
        k = Toplevel()
        def destroy_():
            k.destroy()
        k.title("thong tin duc anh")
        t= Label(k,text="Thong tin duc anh___________\n ___________").pack()
        b= Button(k,text="xong",command=destroy_).pack()
        k.mainloop()
        

    frame = Frame(main_screen,highlightthickness=2,highlightbackground="black")
    Label(frame,text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(frame,text="").pack()
    Button(frame,text="Login", height="2", width="30", command = login).pack()
    Label(frame,text="").pack()
    Button(frame,text="Register", height="2", width="30", command=register).pack()
    frame.pack()
    frame2 = Frame(main_screen,highlightthickness=2,highlightbackground="black")
    image1 = PIL.Image.open("profile.png")
    Label(frame2,text="CAC THANH VIEN TRONG DU AN OTESL:").place(x=50,y=0)
    resize_image = image1.resize((200,200))
    new_image= ImageTk.PhotoImage(resize_image)
    label1 = ttk.Label(frame2,image=new_image)
    label1.image = new_image
    label1.grid(row=1,pady=20,sticky=N)
    Nut_1 = Button(frame2,text="BOSS: CO NGOC :))",command=thong_tin_co_ngoc).grid(row=2)
    image2 = PIL.Image.open("profile.png")
    resize_image2 = image1.resize((200,200))
    new_image2= ImageTk.PhotoImage(resize_image)
    label2 = ttk.Label(frame2,image=new_image)
    label2.image = new_image
    label2.grid(row=3,column=0)
    image3 = PIL.Image.open("profile.png")
    resize_image3 = image1.resize((200,200))
    new_image3= ImageTk.PhotoImage(resize_image)
    label3 = ttk.Label(frame2,image=new_image)
    label3.image = new_image
    label3.grid(row=3,column=1)
    nut_3 = Button(frame2,text="Lang Tu Thoi Tien Su: Hai Quy :))",command=thong_tin_hai_quy).grid(row=4,column=0)
    Nut_4 = Button(frame2,text="Nam Vuong: Duc Anh :))",command=thong_tin_duc_anh).grid(row=4,column=1)
    frame2.pack(side=RIGHT)
    frame3= Frame(main_screen,highlightthickness=2,highlightbackground="black")
    image1 = PIL.Image.open("hht.jpeg")
    resize_image = image1.resize((905,500))
    new_image= ImageTk.PhotoImage(resize_image)
    label1 = ttk.Label(frame3,image=new_image)
    label1.image = new_image
    label1.pack()
    frame3.pack(side=LEFT)
 
 
 
    main_screen.mainloop()
 
 
main_account_screen()