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
def hideBG():
    global state
    if state == "Hidden":
        background_label.pack()
        state = "Showing"

    elif state == "Showing":
        background_label.pack_forget()
        state = "Hidden"




window = Tk()

background_image= PhotoImage(file="HHTCOJ.png")
background_label = Label(window, image=background_image)

hideBttn = Button(window, text="Hide Background", command=hideBG)
state = "Showing"

hideBttn.pack()
background_label.pack()

window.mainloop()