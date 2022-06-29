#!/usr/bin/python

# 步驟一：匯入 tkinter 模組。
from tkinter import Tk
from tkinter import Label
from tkinter import Button
from datetime import datetime
from clipboard import copy

# 步驟二：建立主視窗
mainWin = Tk()
# 視窗標題
mainWin.title("KLA DLINE 小幫手")
# 視窗大小
mainWin.geometry("330x130")
mainWin['bg'] = 'white'

# 按鈕 Click 事件處理函式
def cal_date_time():
    tonow = datetime.now()
    copy(tonow.strftime("%y%m%d%H%M%S"))

def cal_date_time_t():
    tonow = datetime.now()
    copy(tonow.strftime("%y%m%d%H%M%S"+"-t"))

def cal_date_time_b():
    tonow = datetime.now()
    copy(tonow.strftime("%y%m%d%H%M%S"+"-b"))    

# 步驟四： 進入事件處理迴圈。
dateLabel = Label(mainWin, text="[日期][Date]+[時間][Time] ")
dateButton1 = Button(mainWin, text="按這個, 將""左邊的條件""拷貝",bg="black", fg="white", command=cal_date_time)
emptyLabell = Label(mainWin, text="")
dateLabe2 = Label(mainWin, text="[日期][Date]+[時間][Time]+T面 ")
dateButton2 = Button(mainWin, text="按這個, 將""左邊的條件""拷貝",bg="black", fg="white", command=cal_date_time_t)
emptyLabel2 = Label(mainWin, text="")
dateLabe3 = Label(mainWin, text="[日期][Date]+[時間][Time]+B面 ")
dateButton3 =Button(mainWin, text="按這個, 將""左邊的條件""拷貝",bg="black", fg="white", command=cal_date_time_b)


# 版面配置
dateLabel.grid(row=10,column=0)
dateButton1.grid(row=10,column=1)
emptyLabell.grid(row=50,column=1)
dateLabe2.grid(row=110,column=0)
dateButton2.grid(row=110,column=1)
emptyLabel2.grid(row=150,column=1)
dateLabe3.grid(row=210,column=0)
dateButton3.grid(row=210,column=1)

mainWin.mainloop()