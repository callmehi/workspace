#!/usr/bin/env python

# coding: utf-8


import os


import datetime


import shutil


# confluence資料備份，因為confluence不能保留7天備份，並且每天全備份，佔用空間很大，所以寫指令碼，保留7天備份檔案。


backup_directory = "/backup/"


# backup file name: backup-2019_02_24.zip


today_backup_file = "backup-" + str(datetime.date.today() + datetime.timedelta(days = -1)).replace("-", "_") + ".zip"


day_list = 


for i in range(1, 8):
    day = str(datetime.date.today() + datetime.timedelta(days = -i)).replace("-", "_")


filename = "backup-" + day + ".zip"


if os.path.exists(data_directory) and os.path.exists(backup_directory):


# 迴圈資料目錄，將7天的資料檔案保留，其他的刪除，並將最新的資料備份包，拷貝到其他的盤上


for file in os.listdir(data_directory):
    filepath = os.path.join(data_directory, file)


if file == today_backup_file:
    shutil.copy(filepath, backup_directory)
elif file not in day_list:
    file = os.remove(filepath)