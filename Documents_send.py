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
import time


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
txt = Text(rightFrame1, width = 30, height = 2, takefocus=0)
txt.grid(row=2, column=0, padx=10, pady=2)

#-----------------------------------------------------------------------



d=[]
m=[]

def import_csv_data():
    csv_file_path = askopenfilename()
    print(csv_file_path)
    txt1.insert('1.0',csv_file_path)
    df = pd.read_csv(csv_file_path)
    data=df['mobile_number']
    for i in range(len(data)):
        d.append(data[i])

def file():
    csv_file_path = askopenfilename()
    print(csv_file_path)
    txt.insert('1.0',csv_file_path)
    m.append(csv_file_path)


sto.configure('W.TButton', font= ('Arial Black', 9, ''),foreground='Green',background='Green')

#Button with style
btns = Button(labelframe, text='Browse',style='W.TButton',command=import_csv_data,width=10)
btns.grid(column=2,row=0, padx=10)

btns1 = Button(labelframe, text='Docs',style='W.TButton',command=file,width=10)
btns1.grid(column=2,row=2,padx=10)



btns3 = Button(labelframe, text='Send>>>',style='W.TButton',command=window.destroy,width=15)
btns3.grid(column=0,row=8, padx=10)




window.mainloop()

message_text=m[-1]

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

def send_whatsapp_msg(phone_no,message_text):
    driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no))
    try:
        driver.switch_to_alert().accept()
    except Exception as e:
        pass
    WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//div[@title = "Menu"]')))
    try:
        attachment_box = driver.find_element_by_xpath('//div[@title="Attach"]')
        attachment_box.click()
        time.sleep(1)

        image_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        image_box.send_keys(message_text)
        time.sleep(2)

        send_btn = driver.find_element_by_xpath('//span[@data-icon="send"]')
        send_btn.click()
        time.sleep(2)
    except IndexError:
        pass
for moblie_no in d:
    try:
        send_whatsapp_msg(moblie_no,message_text)

    except Exception as e:
        sleep(10)
        is_connected()


