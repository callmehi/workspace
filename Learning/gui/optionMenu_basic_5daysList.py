#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time, datetime
import tkinter as tk
from tkinter import messagebox 
 
root = tk.Tk()
root.title('my window')
root.geometry('200x150')

myoptionmenuList = []

for a in range(5):
    myoption_tmp = datetime.date.today() - datetime.timedelta(days=a)
    myoption_str = myoption_tmp.strftime("%Y-%m-%d")
    myoptionmenuList.append(myoption_str)
    print(myoptionmenuList, type(myoptionmenuList))

myoptinDate = tk.StringVar()
myoptinDate.set(myoptionmenuList[0])
myoptionmenu = tk.OptionMenu(root, myoptinDate, *myoptionmenuList)
myoptionmenu.pack(pady=10)

def event_handler():
    messagebox.showinfo("INFO", "Starting backup = " + myoptinDate.get(), detail="please wait...")
    messagebox.showinfo("INFO", "Backup done!", detail="backup date = " + myoptinDate.get())

submit_button = tk.Button(root, text='Submit', command=event_handler)
submit_button.pack()

root.mainloop()