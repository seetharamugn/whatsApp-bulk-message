from tkinter import *
from tkinter.ttk import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import socket
from tkinter.filedialog import askopenfilename
import pandas as pd
from tkinter.ttk import *
from tkinter import ttk
import os

#-----------------------------------------------------------------
window = Tk()



window.geometry('400x300')

window.resizable(0,0) 
labelframe = LabelFrame(window, text="WHATSAPP BULK") 


background_image=PhotoImage(file=r"wha.png")
background_label =Label(labelframe, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


background_label1 =Label(labelframe, image=background_image)
background_label1.place(x=0, y=0, relwidth=1, relheight=1)

window.title("WhatsApp")
labelframe.pack(fill="both", expand="yes")

sto = Style()

def page1():
    os.system(r"C:\Users\Hp\Desktop\bulk_msg\Message_send.py")
def page2():
    os.system(r"C:\Users\Hp\Desktop\bulk_msg\Documents_send.py")


sto.configure('W.TButton', font= ('Arial Black', 9, ''),foreground='Green',background='Green')




btns = Button(labelframe, text='Message',style='W.TButton',command=page1,width=10)
btns.grid(column=2,row=0, padx=10)

btns1 = Button(labelframe, text='Docs',style='W.TButton',command=page2,width=10)
btns1.grid(column=2,row=2,padx=10)







