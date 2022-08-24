from distutils.cmd import Command
from tkinter import*
from tkinter.ttk import Progressbar
import customtkinter
from tkinter import messagebox
from PIL import Image , ImageTk
import os
import subprocess
import tkinter.font as TKFont
from playsound import playsound 
import time 

root = customtkinter.CTk()
root.geometry('600x800')
root.title('Login')


def step():
        my_progress['value'] +=20
        prog_label['text']=my_progress['value'] ,'%'
       

       








my_progress = Progressbar(root , length=350)

my_progress.place(rely=0.10 , relx=0.20)

prog_label= customtkinter.CTkLabel(root , text='0%')
prog_label.place(rely=0.30 , relx=0.35)
login_btn = customtkinter.CTkButton(root , text="Login" , fg_color=None , command=step)
login_btn.place(rely=0.20 , relx=0.35 )

















root.mainloop()