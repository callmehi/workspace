#!/usr/bin/python

# 步驟一：匯入 tkinter 模組。
import tkinter
import datetime
import pyautogui
import clipboard as pc


# 步驟二：建立主視窗。
mainWin = tkinter.Tk()
# 視窗標題
mainWin.title("KLA DLINE 小幫手")
# 視窗大小
mainWin.geometry("600x200")

# 按鈕 Click 事件處理函式
def cal_date():
    tonow = datetime.datetime.now()
    pc.copy(tonow.strftime("%Y%m%d"))

def cal_time():
    tonow = datetime.datetime.now()
    pc.copy(tonow.strftime("%H%M%S"))

# 步驟四： 進入事件處理迴圈。
dateLabel = tkinter.Label(mainWin, text="[日期][Date]  ")


dateButton = tkinter.Button(mainWin, text="按這個, 將""日期""拷貝", command=cal_date)


timeLabel = tkinter.Label(mainWin, text="[時間][Time]  ")


timeButton = tkinter.Button(mainWin, text="按這個, 將""時間""拷貝", command=cal_time)



# 版面配置
dateLabel.grid(row=1,column=0)
dateButton.grid(row=1,column=1)
timeLabel.grid(row=2,column=0)
timeButton.grid(row=2,column=1)

mainWin.mainloop()