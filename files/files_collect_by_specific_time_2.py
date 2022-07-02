#coding=utf-8
import os
import datetime
import time
import shutil

#设定base_dir,确保该目录为需要删除的文件路径
base_dir = ('D:/temp/TK_logs_for_all')
os.chdir(base_dir)
filename = os.listdir(base_dir)
length = len(filename)
todaytime = time.time()



i = 0

for i in range(length):
  #各備份檔案的時間
  filetime = os.path.getctime(filename[i])
  #各備份檔案與目前的時間的時間差, /60 = 分鐘, /3600 = 小時.
  differencetime = (todaytime - os.path.getctime(filename[i]))/60
  #各備份檔案的日期
  filedate = datetime.datetime.fromtimestamp(filetime)

  if differencetime > 3:

    os.remove(filename[i])

  #print (filedate)

  #print (differencetime)

    print ('delete ', filename[i])

    i+=1

  else:

    print ('Nothing deleted')
