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


#-----------------------------------------------------------------
window = Tk()



window.geometry('400x300')
window.resizable(0,0)
labelframe = LabelFrame(window, text="BULK MASSAGE")

background_image=PhotoImage(file=r"wha.png")
background_label =Label(labelframe, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

window.title("WhatsApp")
labelframe.pack(fill="both", expand="yes")
sto = Style()
#---------------------------------------------------------------------

rightFrame = Frame(labelframe, width=200, height = 600)
rightFrame.grid(row=0, column=0, padx=10, pady=2)
txt1 = Text(rightFrame, width = 30, height = 2, takefocus=0)
txt1.grid(row=2, column=0, padx=10, pady=2)




rightFrame1 = Frame(labelframe, width=200, height = 600)
rightFrame1.grid(rows=2, column=0,rowspan=5, padx=10, pady=2)
txt = Text(rightFrame1, width = 30, height = 10, takefocus=0)
txt.grid(row=2, column=0, padx=10, pady=2)

#-----------------------------------------------------------------------

d=[]
l=[]
def clicked():
    msg=txt.get('1.0', END)
    l.append(msg)

   

def import_csv_data():
    csv_file_path = askopenfilename()
    print(csv_file_path)
    txt1.insert('1.0',csv_file_path)
    df = pd.read_csv(csv_file_path)
    data=df['mobile_number']
    for i in range(len(data)):
        d.append(data[i])
def clear():
    txt.delete('1.0', END)
    l.clear()
sto.configure('W.TButton', font= ('Arial Black', 9, ''),foreground='Green',background='Green')

#Button with style
btns = Button(labelframe, text='Browse',style='W.TButton',command=import_csv_data,width=10)
btns.grid(column=2,row=0, padx=10)

btns1 = Button(labelframe, text='Save',style='W.TButton',command=clicked,width=10)
btns1.grid(column=2,row=2,padx=10)

btns2 = Button(labelframe, text='Clear',style='W.TButton',command=clear,width=10)
btns2.grid(column=2,row=4, padx=10)


btns3 = Button(labelframe, text='Send>>>',style='W.TButton',command=window.destroy,width=15)
btns3.grid(column=0,row=8, padx=10)



window.mainloop()
print(l[:])
print(l[-1])
print(d)
msg=l[-1]
message_text=msg







no_of_message=1 # no. of time you want the message to be send
moblie_no_list=d # list of phone number can be of any length

def element_presence(by,xpath,time):
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)

def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except :
        is_connected()

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://web.whatsapp.com")
sleep(10) #wait time to scan the code in second

def send_whatsapp_msg(phone_no,text):
    driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no))
    try:
        driver.switch_to_alert().accept()
    except Exception as e:
        pass

    try:
        element_presence(By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]',30)
        txt_box=driver.find_element(By.XPATH , '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        global no_of_message
        for x in range(no_of_message):
            txt_box.send_keys(text)
            txt_box.send_keys("\n")

    except Exception as e:
        print("invailid phone no :"+str(phone_no))
for moblie_no in moblie_no_list:
    try:
        send_whatsapp_msg(moblie_no,message_text)

    except Exception as e:
        sleep(10)
        is_connected()
