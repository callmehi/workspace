# -*- coding:utf-8 -*-
# author: Tommy Lee time:20220627

import os
from shutil import copy2, copytree, ignore_patterns
import time, datetime
import glob
#GUI
import tkinter as tk
from tkinter import Label
from tkinter import Button
from tkinter import messagebox 


### [主程式碼]
def event_handler():
    #需要備份並"壓縮"的檔案目錄(1/2)
    source=r'D:/temp/daliy_backup/'
    #儲存"備份壓縮檔"的位置(1/2)
    target_dir=r'D:/temp/daliy_backup/'

    messagebox.showinfo("INFO", "Starting backup = " + myoptinDate.get(), detail="please wait for another window")
    backup_logs()
    messagebox.showinfo("INFO", "Backup done!", detail="backup date = " + myoptinDate.get() + '\n'+'backup path =' + target_dir + myoptinDate.get())

### [時間比對]
#抓出[這個目錄]的[所有檔案]:把[最後修改時間]和[自己選定的時間]配對檔案丟出
def checkFilesTime_selectDate(ab_dir):
    target_xxx = ab_dir
    global file_list
    file_list =[]
    for f in os.listdir(target_xxx):
        t = time.localtime(os.path.getmtime(f'{target_xxx}\{f}'))
        datetimeString = ''
        datetimeString += str(t.tm_year)
        datetimeString += str(t.tm_mon).zfill(2)
        datetimeString += str(t.tm_mday).zfill(2)
        # datetimeString += ' '
        # datetimeString += str(t.tm_hour).zfill(2)
        # datetimeString += ':'
        # datetimeString += str(t.tm_min).zfill(2)
        # datetimeString += ':'
        # datetimeString += str(t.tm_sec).zfill(2)
        myoptinDate_connect = "{Y}{m}{d}".format(Y=str(myoptinDate.get()[0:4]), m=str(myoptinDate.get()[5:7]), d=str(myoptinDate.get()[8:10]))  

        if datetimeString == myoptinDate_connect:         
            file_list += [f]
    return file_list

#抓出[這個目錄]的[所有檔案]:把[今天的檔案]丟出
def checkFilesTime_today(ab_dir):
    target_xxx = ab_dir
    global file_list
    file_list =[]
    for f in os.listdir(target_xxx):
        t = time.localtime(os.path.getmtime(f'{target_xxx}\{f}'))
        datetimeString = ''
        datetimeString += str(t.tm_year)
        datetimeString += str(t.tm_mon).zfill(2)
        datetimeString += str(t.tm_mday).zfill(2)
        # datetimeString += ' '
        # datetimeString += str(t.tm_hour).zfill(2)
        # datetimeString += ':'
        # datetimeString += str(t.tm_min).zfill(2)
        # datetimeString += ':'
        # datetimeString += str(t.tm_sec).zfill(2)
        myoptinDate_connect_tmp = str(datetime.date.today())
        myoptinDate_connect = "{Y}{m}{d}".format(Y=str(myoptinDate_connect_tmp[0:4]), m=str(myoptinDate_connect_tmp[5:7]), d=str(myoptinDate_connect_tmp[8:10]))  
        if datetimeString == myoptinDate_connect:         
            file_list += [f]
    return file_list

#[視窗]標題大小
mainWin = tk.Tk()
#[視窗]視窗標題
mainWin.title("備份Logs小幫手[5天内]")
#[視窗]視窗大小
mainWin.geometry("330x130")
mainWin['bg'] = 'white'
#[視窗]定義myoptionmenu為近5天的日期,成為一個list的5個選項
myoptionmenuList = []
for a in range(5):
    myoption_tmp = datetime.date.today() - datetime.timedelta(days=a)
    myoption_str = myoption_tmp.strftime("%Y-%m-%d")
    myoptionmenuList.append(myoption_str)
myoptinDate = tk.StringVar()
myoptinDate.set(myoptionmenuList[0])


#[視窗]GUI Layout
label1 = Label(mainWin, text="[Date] -- > ").grid(row=1,column=0)
myoptionmenu = tk.OptionMenu(mainWin, myoptinDate, *myoptionmenuList).grid(row=1,column=1)
#[視窗]注釋文字comment
label2 = Label(mainWin, text="[Comment] ---> ").grid(row=2,column=0)
myentry = tk.Entry(mainWin)
myentry.grid(row=2,column=1)
#[視窗]送出結果按鈕
submit_button = tk.Button(mainWin, text='[Start]', command=event_handler).grid(row=6,column=1)

#[備份/壓縮]備份程式碼
def backup_logs():

    # 在Python的string前面加上‘r’， 是為了告訴編譯器這個string是個raw string，
    # 不要轉意backslash '\' 。 例如，\n 在raw string中，是兩個字元，\和n， 
    # 而不會轉意為換行符。由於正則表示式和 \ 會有衝突，因此，當一個字串使用了正則表示式後，
    # 最好在前面加上'r'

    #需要備份並"壓縮"的檔案目錄(2/2)
    source=r'D:/temp/daliy_backup/'
    #儲存"備份壓縮檔"的位置(2/2)
    target_dir=r'D:/temp/daliy_backup/'
    
    #[備份位置]P_logs
    P_logs_dir=r'/P_logs'
    #[備份位置]E_logs
    E_logs_dir=r'/E_logs'
    #[備份位置]E_logs/GPU
    GPU_dir=r'/E_logs/GPU'
    #[備份位置]E_logs/IPED
    IPED_dir=r'/E_logs/IPED'
    #[備份位置]E_logs/TK
    TK_dir=r'/E_logs/ToolKit'
    #[備份位置]E_logs/SC
    SC_dir=r'/E_logs/SpiritConsole'
    #[備份位置]sensors
    sensors_dir=r'/Sensors'
    #[備份位置]exposure
    exposure_dir=r'/exposure'
    #[備份位置]efficiency
    efficiency_dir=r'/efficiency'

    #[備份位置]Screenshot
    screenShots_dir=r'/ScreenShots'
    

    #[原檔位置]P_logs
    #ori_P_logs_dir=r'Z:/???'
    ori_P_logs_dir=r'D:/temp/Test_folder'

    #[原檔位置]E_logs/GPU
    # ori_GPU_dir=r'E:/Logs/Gpu'
    ori_GPU_dir=r'D:/temp/Test_folder'

    # #[原檔位置]E_logs/IPED_1
    # ori_IPED_dir=r'E:/Logs/IPED'
    ori_IPED_dir_1=r'D:/temp/Test_folder/archive'

    # #[原檔位置]E_logs/IPED_2
    # ori_IPED_dir=r'E:/Logs/IPED/archive'
    ori_IPED_dir_2=r'D:/temp/Test_folder/'

    #[原檔位置]E_logs/TK
    # ori_TK_dir=r'E:/Logs/Toolkit'
    ori_TK_dir=r'D:/temp/Test_folder'

    #[原檔位置]E_logs/SC
    # ori_SC_dir=r'E:/Logs/SpiritConsole'
    ori_SC_dir=r'D:/temp/Test_folder'

    # #[原檔位置]sensors
    # ori_sensors_dir=r'E:/Logs/Sensors'
    ori_sensors_dir=r'D:/temp/Test_folder/Sensors'

    # #[原檔位置]exposure
    # ori_exposure_dir=r'E:/Logs/Exposure'
    # ori_exposure_dir=r'/exposure'

    # #[原檔位置]efficiency
    # ori_efficiency_dir=r'E:/Logs/Efficiency'
    # ori_efficiency_dir=r'/efficiency'

    # #[原檔位置]Screenshot
    # ori_screenShots_dir=r'C:/Users/DLine/Pictures/Screenshots'
    ori_screenShots_dir=r'D:/temp/Test_folder/Screenshot'



    # myoptinDate的格式轉換
    myoptinDate_underLine = "{Y}{c}{m}{c}{d}".format(c="_", Y=str(myoptinDate.get()[0:4]), m=str(myoptinDate.get()[5:7]), d=str(myoptinDate.get()[8:10]))
    myoptinDate_connect = "{Y}{m}{d}".format(Y=str(myoptinDate.get()[0:4]), m=str(myoptinDate.get()[5:7]), d=str(myoptinDate.get()[8:10]))  

    #os.path.exists是判斷檔案是否存在
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    #today即在target_dir路徑下的資料夾名,用來存放當天的備份檔案
    #time.strftime是將建立的zip歸檔檔案的名字由當前日期和時間構成
    today=target_dir+myoptinDate.get()
    #now指備份檔名字
    now=time.strftime('%H%M%S')

    if len(myentry.get())==0:
        target=today+'/'+ myoptinDate.get() + '_' + now+'.zip'
    else:
        target=today + '/' + myoptinDate.get() + '_' + now + '_' + myentry.get().replace(' ','_')+'.zip'
    #判斷是否生成了名為today的資料夾
    if not os.path.exists(today):
        os.mkdir(today)

    # ===========================================================================================
    # E disk logs folder = E_logs_dir #創建E_logs目錄
    if not os.path.exists(today+E_logs_dir):
        os.mkdir(today+E_logs_dir)
    
    # Production logs folder = P_logs
    if not os.path.exists(today+P_logs_dir):
        os.mkdir(today+P_logs_dir)
    # Python 的標準函式「glob」可以使用名稱與路徑的方式，查找出匹配條件的檔案或資料夾，
    # 查找出檔案後，搭配其他函式庫 (例如 os 標準函式庫) ，就能做到像是批次重新命名、批次刪除...等的動作。
    pLogCopyFiles = glob.glob(os.path.join(ori_P_logs_dir+'/', "Export - "+str(myoptinDate.get())+"-*.csv"))
    for f in pLogCopyFiles:
        copy2(f, today+P_logs_dir)

    # GPU logs folder = GPU_dir
    if not os.path.exists(today+GPU_dir):
        os.mkdir(today+GPU_dir)
    # Python 的標準函式「glob」可以使用名稱與路徑的方式，查找出匹配條件的檔案或資料夾，
    # 查找出檔案後，搭配其他函式庫 (例如 os 標準函式庫) ，就能做到像是批次重新命名、批次刪除...等的動作。
    gpuLogCopyFiles_1 = glob.glob(os.path.join(ori_GPU_dir+'/', "GPUTransformer_"+myoptinDate_underLine+".*"))
    for f in gpuLogCopyFiles_1:
        copy2(f, today+GPU_dir)
    gpuLogCopyFiles_2 = glob.glob(os.path.join(ori_GPU_dir+'/', "GPUTransformerCorrectionGrid_"+str(myoptinDate.get())+".log"))
    for f in gpuLogCopyFiles_2:
        copy2(f, today+GPU_dir)   
    gpuLogCopyFiles_3 = glob.glob(os.path.join(ori_GPU_dir+'/', "GRPCCommandstream_"+myoptinDate_underLine+".bin"))
    for f in gpuLogCopyFiles_3:
        copy2(f, today+GPU_dir)    

    # IPED logs folder = IPED_dir
    if not os.path.exists(today+IPED_dir):
        os.mkdir(today+IPED_dir)
    # Python 的標準函式「glob」可以使用名稱與路徑的方式，查找出匹配條件的檔案或資料夾，
    # 查找出檔案後，搭配其他函式庫 (例如 os 標準函式庫) ，就能做到像是批次重新命名、批次刪除...等的動作。

    # 備份IPED/archive裏的備份檔
    dirPathPattern = ori_IPED_dir_1+r"/IPEDRK_Errors_" + myoptinDate_connect + r"-*"  
    ipedLogCopyFiles_1 = glob.glob(dirPathPattern)
    for f in ipedLogCopyFiles_1:
        # f[-29:] 用來截取IPEDRK的目錄名稱
        copytree(f, today+IPED_dir+"/"+f[-29:])

    # 備份IPED裏的檔案
    ipedLogCopyFiles_2 = glob.glob(os.path.join(ori_IPED_dir_2, "IPEDRK_*.*"))
    for f in ipedLogCopyFiles_2:
        copy2(f, today+IPED_dir)

    # ToolKit logs folder = TK_dir
    if not os.path.exists(today+TK_dir):
        os.mkdir(today+TK_dir)
    # Python 的標準函式「glob」可以使用名稱與路徑的方式，查找出匹配條件的檔案或資料夾，
    # 查找出檔案後，搭配其他函式庫 (例如 os 標準函式庫) ，就能做到像是批次重新命名、批次刪除...等的動作。
    tkLogCopyFiles = glob.glob(os.path.join(ori_TK_dir+'/', str(myoptinDate.get())+"_spirit.*"))
    for f in tkLogCopyFiles:
        copy2(f, today+TK_dir)

    # SpiritConsole logs folder = SC_dir
    if not os.path.exists(today+SC_dir):
        os.mkdir(today+SC_dir)
    scLogCopyFiles = glob.glob(os.path.join(ori_SC_dir+'/', str(myoptinDate.get())+"_Spirit_*"))
    for f in scLogCopyFiles:
        copy2(f, today+SC_dir)

    # Screenshots folder = screenShots_dir
    if not os.path.exists(today+screenShots_dir):
        os.mkdir(today+screenShots_dir)
    # 備份選定日期的所有screenshots
    checkFilesTime_selectDate(ori_screenShots_dir)
    for f in file_list:
        copy2(ori_screenShots_dir+"/"+f, today+screenShots_dir)
    # 備份今天的所有screenshots
    checkFilesTime_today(ori_screenShots_dir)
    for f in file_list:
        copy2(ori_screenShots_dir+"/"+f, today+screenShots_dir)    

    # sensors folder = sensors_dir
    if not os.path.exists(today+sensors_dir):
        os.mkdir(today+sensors_dir)
    copy2(ori_sensors_dir+"/sensors.tsv", today+sensors_dir)
    copy2(ori_sensors_dir+"/measurewheel.tsv", today+sensors_dir)

    # exposure folder = exposure_dir
    if not os.path.exists(today+exposure_dir):
        os.mkdir(today+exposure_dir)
    copy2('C:/installAgent.log', today+exposure_dir)

    # efficiency folder = efficiency_dir
    if not os.path.exists(today+efficiency_dir):
        os.mkdir(today+efficiency_dir)
    copy2('C:/installAgent.log', today+efficiency_dir)

    # Copy檔案到要備份的目錄裏
    # files = ['sensors.csv', 'file2.txt', 'file3.txt']
    # for f in files:
    #     shutil.copy(f, 'my_new_folder')

    #   方法3：在cmd 命令中寫入7z.exe所在的目錄
    #       zip_command = '"C:\\Program Files\\7-Zip\\7z.exe" a -tzip {0} {1} '.format(target,' '.join(source))
    os.chdir('C:/Program Files/7-Zip')
    zip_command = '7z a -tzip {0} {1}{2}'.format(target,''.join(source),''.join(myoptinDate.get()))
    print(zip_command)

    #是os.system函式是使zip_command命令從系統中執行,執行成功返回0,執行失敗返回錯誤程式碼
    if os.system(zip_command)==0:
        print('success')
    else:
        print('error')

mainWin.mainloop()