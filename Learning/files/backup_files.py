#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: xulinjie time:2017/10/12
##1.匯入os和time模組
##2.備份與儲存位置
##3.定義儲存備份zip的資料夾
##4.輸入對儲存的檔案加註釋(標記備份檔案)並判斷輸入的標籤註釋是否長度為0,以確定備份檔名
##5.判斷是否有儲存備份檔案的資料夾名(即today資料夾)
##6.定義zip命令,將檔案打包成zip格式
##7.執行備份
##8.使zip命令從系統中執行,執行成功返回0,執行失敗返回錯誤程式碼
import os
import time
#需要備份的檔案
source=r'D:/python'
#儲存備份檔案的位置
target_dir=r'D:/Python/backup/'
#os.path.exists是判斷檔案是否存在
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
#today即在target_dir路徑下的資料夾名,用來存放當天的備份檔案
#time.strftime是將建立的zip歸檔檔案的名字由當前日期和時間構成
today=target_dir+time.strftime('%Y%m%d')
#now指備份檔名字
now=time.strftime('%H%M%S')
#target=today+os.sep+now+'.zip'
#comment這裡是需要你輸入對備份檔案的標籤,方便以後查詢
comment=input('input comment-->')
#判斷是否有標籤鍵入,解釋下這裡為什麼是today+os.sep+now,而不是now
#因為today指的是你將要生成檔案的路徑,而os.sep是根據你的作業系統給出的分隔符
#(linux:/,win://,mac::),所以使用os.sep而非直接使用這些字元,是提高了程式可移植性
if len(comment)==0:
    target=today+'/'+now+'.zip'
else:
    target=today+'/'+now+'_'+comment.replace(' ','_')+'.zip'
#判斷是否生成了名為today的資料夾
if not os.path.exists(today):
    os.mkdir(today)
print('ok create:',today)
#建立一串字串,包含了要執行的命令,我下面兩種方法都是可以的
#這裡的a命令代表新增檔案到壓縮檔案中

# 下面三種方法可以在python中正確執行7z命令：
#   方法1： 拷貝 7z.exe 和7z.dll 到當前python檔案所在的目錄下。 否則，不認識7z 命令。
#       zip_command = '7z a -tzip {0} {1} -r'.format(target,' '.join(source))
#   方法2： os.system() 裡面執行的是同目錄下的exe,使用如下os.chdir() 命令切換 path。
os.chdir('C:/Program Files/7-Zip')
print('切換當前路徑為：',os.getcwd())
zip_command = '7z a -tzip {0} {1}'.format(target,''.join(source))
#   方法3：在cmd 命令中寫入7z.exe所在的目錄
#       zip_command = '"C:\\Program Files\\7-Zip\\7z.exe" a -tzip {0} {1} '.format(target,' '.join(source))

# zip_command=r"7z a %s %s" %(target,source)
# zip_command=r'7z a {0} {1}'.format(target,‘’.join(source))
print('zip command is:')
print(zip_command)
print('running:')

#是os.system函式是使zip_command命令從系統中執行,執行成功返回0,執行失敗返回錯誤程式碼
if os.system(zip_command)==0:
    print('success')
else:
    print('error')
