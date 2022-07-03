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
import sys
import subprocess
import threading 

# --- classes ---
class Redirect():

    def __init__(self, widget, autoscroll=True):
        self.widget = widget
        self.autoscroll = autoscroll

    def write(self, text):
        self.widget.insert('end', text)
        if self.autoscroll:
            self.widget.see("end")  # autoscroll
        
    def flush(self):
       pass
      
# --- functions ---
def run():
    threading.Thread(target=test).start()

def test():
    print("Thread: start")

    p = subprocess.Popen("ping stackoverflow.com".split(), stdout=subprocess.PIPE, bufsize=1, text=True)
    while p.poll() is None:
        msg = p.stdout.readline().strip() # read a line from the process output
        if msg:
            print(msg)

    print("Thread: end")




### [主程式碼] ###
def event_handler():
    #需要備份並"壓縮"的檔案目錄(1/2)
    source=r'D:/temp/daliy_backup/'
    #儲存"備份壓縮檔"的位置(1/2)
    target_dir=r'D:/temp/daliy_backup/'

    messagebox.showinfo("INFO", "Starting backup = " + myoptinDate.get(), detail="please wait for another window")
    backup_logs()
    messagebox.showinfo("INFO", "Backup done!", detail="backup date = " + myoptinDate.get() + '\n'+'backup path =' + target_dir + myoptinDate.get())

### [時間比對] ###
#抓出[這個目錄]的[所有檔案]:把[最後修改時間]和[自己選定的時間]配對檔案丟出
def checkFilesTime_selectDate(compare_dir):
    target_xxx = compare_dir
    global file_list_callmehi
    file_list_callmehi =[]
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
            file_list_callmehi += [f]
    return file_list_callmehi

#抓出[這個目錄]的[所有檔案]:把[今天的檔案]丟出
def checkFilesTime_today(compare_dir):
    target_xxx = compare_dir
    global file_list_callmehi
    file_list_callmehi =[]
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
            file_list_callmehi += [f]
    return file_list_callmehi





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




# - Frame with Text and Scrollbar -
frame = tk.Frame(mainWin)
frame.pack(expand=True, fill='both')

text = tk.Text(frame)
text.pack(side='left', fill='both', expand=True)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side='right', fill='y')

text['yscrollcommand'] = scrollbar.set
scrollbar['command'] = text.yview

old_stdout = sys.stdout    
sys.stdout = Redirect(text)

# - rest -
to_button = tk.Button(mainWin, text='TEST', command=run).grid(row=3,column=0)




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

### [備份位置] ###
    #[備份位置]Machine_configs
    Machine_configs_dir=r'/configurations/Machine_configs' 
    #[備份位置]DataServer_configs
    DataServer_configs_dir=r'/configurations/DataServer_configs'    
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
    sensors_dir=r'/E_logs/Sensors'
    #[備份位置]exposure
    exposure_dir=r'/E_logs/Exposure'
    #[備份位置]efficiency
    efficiency_dir=r'/E_logs/Efficiency'
    #[備份位置]ScalingService
    ScalingService_dir=r'/E_logs/ScalingService'
    #[備份位置]Screenshot
    screenShots_dir=r'/ScreenShots'
     #[備份位置]BeamDiameter
    BeamDiameter_dir=r'/E_logs/BeamDiameter'  
     #[備份位置]LaserPower
    LaserPower_dir=r'/E_logs/HWLogs' 
     #[備份位置]PlcCommunication
    PlcCommunication_dir=r'/E_logs/PlcCommunication'
     #[備份位置]Alarms
    Alarms_dir=r'/Alarms'
     #[備份位置]RegistrationResults
    RegistrationResults_dir=r'/RegistrationResults'
     #[備份位置]MeasureToolResults
    MeasureToolResults_dir=r'/RegistrationResults/MeasureTool' 
      


### [原檔位置] ###
    # #[原檔位置][Product.Config] ori_Machine_configs_dir_1
    #ori_Machine_configs_dir_1=r'D:/Program Files/Orbotech Ltd/Roll2Roll'
    ori_Machine_configs_dir_1=r'D:/temp/Test_folder'
    # #[原檔位置][Ves.exe.config] ori_Machine_configs_dir_2
    #ori_Machine_configs_dir_2=r'D:/Program Files/Orbotech Ltd/Toolcommander/Spirit/System/System32/Release'
    ori_Machine_configs_dir_2=r'D:/temp/Test_folder'
    # #[原檔位置][SpiritShell.exe.config] ori_Machine_configs_dir_3
    #ori_Machine_configs_dir_3=r'D:/Program Files/Orbotech Ltd/Roll2Roll'
    ori_Machine_configs_dir_3=r'D:/temp/Test_folder'
    # #[原檔位置][ComponentDatastore] ori_Machine_configs_dir_4
    #ori_Machine_configs_dir_4=r'D:/Program Files/Orbotech Ltd/Roll2Roll'
    ori_Machine_configs_dir_4=r'D:/temp/Test_folder'   
    # #[原檔位置][ipedrunkernel_FPSS_measure.ini] ori_Machine_configs_dir_5
    #ori_Machine_configs_dir_5=r'D:/Program Files/Orbotech Ltd/Toolcommander/IPED/config'
    ori_Machine_configs_dir_5=r'D:/temp/Test_folder'
    # #[原檔位置][AIS.TC.ApplicationStarter.log] ori_Machine_configs_dir_6
    #ori_Machine_configs_dir_6=r'D:/Program Files/Orbotech Ltd/Toolcommander/ApplicationStarter'
    ori_Machine_configs_dir_6=r'D:/temp/Test_folder'
    # #[原檔位置][SystemInfo.txt & Spirit.ini] ori_Machine_configs_dir_7
    #ori_Machine_configs_dir_7=r'D:/Program Files/Orbotech Ltd/Toolcommander/Spirit'
    ori_Machine_configs_dir_7=r'D:/temp/Test_folder/Spirit'



    # #[原檔位置][DataServer.config] ori_DataServer_configs_dir_1
    #ori_DataServer_configs_dir_1=r'Z:'
    ori_DataServer_configs_dir_1=r'D:/temp/Test_folder'



    # #[原檔位置]Automatic_PLogs_1
    #ori_P_logs_dir=r'E:/Logs/Exported-Plogs-Automatic'
    ori_P_logs_dir_1=r'D:/temp/Test_folder'
    # #[原檔位置]Manual_PLogs_2
    #ori_P_logs_dir=r'D:/Logs/ProductionLog'
    ori_P_logs_dir_2=r'D:/temp/Test_folder'
    # #[原檔位置]E_logs/GPU
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
    #[原檔位置]exposure
    # ori_exposure_dir=r'E:/Logs/Exposure'
    ori_exposure_dir=r'D:/temp/Test_folder/Exposure'
    #[原檔位置]efficiency
    # ori_efficiency_dir=r'E:/Logs/Efficiency'
    ori_efficiency_dir=r'D:/temp/Test_folder/Efficiency'
    #[原檔位置]ScalingService
    # ori_ScalingService_dir=r'E:/Logs/ScalingService'
    ori_ScalingService_dir=r'D:/temp/Test_folder/ScalingService'
    # #[原檔位置]Screenshot
    # ori_screenShots_dir=r'C:/Users/DLine/Pictures/Screenshots'
    ori_screenShots_dir=r'D:/temp/Test_folder/Screenshot'
    #[原檔位置]BeamDiameter
    # ori_BeamDiameter_dir=r'E:/Logs/BeamDiameter'
    ori_BeamDiameter_dir=r'D:/temp/Test_folder/BeamDiameter'
    #[原檔位置]LaserPower
    # ori_LaserPower_dir=r'E:/Logs/HWLogs'
    ori_LaserPower_dir=r'D:/temp/Test_folder/HWLogs'
    #[原檔位置]PlcCommunication
    # ori_PlcCommunication_dir=r'E:/Logs/PlcCommunication'
    ori_PlcCommunication_dir=r'D:/temp/Test_folder/PlcCommunication'    
    #[原檔位置][Alarms yyMMDD.txt & Alarms yyMMDD.xml] ori_Alarms_dir
    #ori_Alarms_dir=r'D:/Program Files/Orbotech Ltd/Toolcommander/Spirit/VCTC_InternalLogging'
    ori_Alarms_dir=r'D:/temp/Test_folder/Spirit/VCTC_InternalLogging'
    #[原檔位置][RegistrationResults] ori_RegistrationResults_dir
    #ori_RegistrationResults_dir=r'D:/Program Files/Orbotech Ltd/Roll2Roll/RegistrationResults'
    ori_RegistrationResults_dir=r'D:/temp/Test_folder/RegistrationResults'
    #[原檔位置][MeasureToolResults] ori_MeasureToolResults_dir
    #ori_MeasureToolResults_dir=r'D:/Program Files/Orbotech Ltd/Roll2Roll/RegistrationResults/MeasureTool'
    ori_MeasureToolResults_dir=r'D:/temp/Test_folder/RegistrationResults/MeasureTool'




    # myoptinDate的格式轉換
    myoptinDate_underLine = "{Y}{c}{m}{c}{d}".format(c="_", Y=str(myoptinDate.get()[0:4]), m=str(myoptinDate.get()[5:7]), d=str(myoptinDate.get()[8:10]))
    myoptinDate_connect = "{Y}{m}{d}".format(Y=str(myoptinDate.get()[0:4]), m=str(myoptinDate.get()[5:7]), d=str(myoptinDate.get()[8:10]))  
    myoptinDate_connect_yy = "{y}{m}{d}".format(y=str(myoptinDate.get()[2:4]), m=str(myoptinDate.get()[5:7]), d=str(myoptinDate.get()[8:10])) 
    myoptinDate_yyyy = "{Y}".format(Y=str(myoptinDate.get()[0:4]))     
    myoptinDate_mm = "{m}".format(m=str(myoptinDate.get()[5:7])) 

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
    # configuration main-folder create
    if not os.path.exists(today+"/configurations"):
        os.mkdir(today+"/configurations")

    # Machine configs
    if not os.path.exists(today+Machine_configs_dir):
        os.mkdir(today+Machine_configs_dir)

     # configuration sub-folder create
    if not os.path.exists(today+Machine_configs_dir+"/Orbotech Ltd"):
        os.mkdir(today+Machine_configs_dir+"/Orbotech Ltd")
    if not os.path.exists(today+Machine_configs_dir+"/Orbotech Ltd"+"/IPED"):
        os.mkdir(today+Machine_configs_dir+"/Orbotech Ltd"+"/IPED")
    if not os.path.exists(today+Machine_configs_dir+"/Orbotech Ltd"+"/IPED"+"/config"):
        os.mkdir(today+Machine_configs_dir+"/Orbotech Ltd"+"/IPED"+"/config") 
    if not os.path.exists(today+Machine_configs_dir+"/Orbotech Ltd"+"/ToolCommander"):
        os.mkdir(today+Machine_configs_dir+"/Orbotech Ltd"+"/ToolCommander")   
    if not os.path.exists(today+Machine_configs_dir+"/Orbotech Ltd"+"/ToolCommander"+"/ApplicationStarter"):
        os.mkdir(today+Machine_configs_dir+"/Orbotech Ltd"+"/ToolCommander"+"/ApplicationStarter")
    if not os.path.exists(today+Machine_configs_dir+"/Orbotech Ltd"+"/ToolCommander"+"/Spirit"):
        os.mkdir(today+Machine_configs_dir+"/Orbotech Ltd"+"/ToolCommander"+"/Spirit")                 


    # [Product.Config] = ori_Machine_configs_dir_1
    try:    copy2(ori_Machine_configs_dir_1+"/Product.Config", today+Machine_configs_dir)
    except  IOError: print("Error:w/o"+" Product.Config")
    else:   print("Product.Config"+" --- [Copy OK!]")
    # [Ves.exe.config] = ori_Machine_configs_dir_2
    try:    copy2(ori_Machine_configs_dir_2+"/Ves.exe.config", today+Machine_configs_dir)
    except  IOError: print("Error:w/o"+" Ves.exe.config")
    else:   print("Ves.exe.config"+" --- [Copy OK!]")
    # [SpiritShell.exe.config] = ori_Machine_configs_dir_3
    try:    copy2(ori_Machine_configs_dir_3+"/SpiritShell.exe.config", today+Machine_configs_dir)
    except  IOError: print("Error:w/o"+" SpiritShell.exe.config")
    else:   print("SpiritShell.exe.config"+" --- [Copy OK!]")
    # [ComponentDatastore] = ori_Machine_configs_dir_4 
    try:    copytree(ori_Machine_configs_dir_4+"/ComponentDatastore/", today+Machine_configs_dir+"/ComponentDatastore")
    except  IOError: print("Error:w/o"+" ComponentDatastore")
    else:   print("ComponentDatastore"+" --- [Copy OK!]") 
    # [ipedrunkernel_FPSS_measure.ini] = ori_Machine_configs_dir_5
    try:    copy2(ori_Machine_configs_dir_5+"/ipedrunkernel_FPSS_measure.ini", today+Machine_configs_dir+"/Orbotech Ltd"+"/IPED"+"/config")
    except  IOError: print("Error:w/o"+" ipedrunkernel_FPSS_measure.ini")
    else:   print("ipedrunkernel_FPSS_measure.ini"+" --- [Copy OK!]")
    # [AIS.TC.ApplicationStarter.log] = ori_Machine_configs_dir_6
    try:    copy2(ori_Machine_configs_dir_6+"/AIS.TC.ApplicationStarter.log", today+Machine_configs_dir+"/Orbotech Ltd"+"/ToolCommander"+"/ApplicationStarter")
    except  IOError: print("Error:w/o"+" AIS.TC.ApplicationStarter.log")
    else:   print("AIS.TC.ApplicationStarter.log"+" --- [Copy OK!]") 
    # [SystemInfo.txt] = ori_Machine_configs_dir_7
    try:    copy2(ori_Machine_configs_dir_7+"/SystemInfo.txt", today+Machine_configs_dir+"/Orbotech Ltd"+"/ToolCommander"+"/Spirit")
    except  IOError: print("Error:w/o"+" SystemInfo.txt")
    else:   print("SystemInfo.txt"+" --- [Copy OK!]") 
    # [Spirit.ini] = ori_Machine_configs_dir_7
    try:    copy2(ori_Machine_configs_dir_7+"/Spirit.ini", today+Machine_configs_dir+"/Orbotech Ltd"+"/ToolCommander"+"/Spirit")
    except  IOError: print("Error:w/o"+" Spirit.ini")
    else:   print("Spirit.ini"+" --- [Copy OK!]")     
    
    # Alarms folder create
    if not os.path.exists(today+Alarms_dir):
        os.mkdir(today+Alarms_dir) 
    # [Alarms yyMMDD.txt] = ori_Alarms_dir
    # 備份所有的Alarms yymmdd.txt/xml
    alarmLogCopyFiles = glob.glob(os.path.join(ori_Alarms_dir+"/"+myoptinDate_yyyy+"/"+myoptinDate_mm+"/Alarms *.*"))
    for f in alarmLogCopyFiles:
        try:    copy2(f, today+Alarms_dir)
        except  IOError: print("Error:w/o"+" "+f)
        else:   print(f+" --- [Copy OK!]") 

    # RegistrationResults folder create
    if not os.path.exists(today+RegistrationResults_dir):
        os.mkdir(today+RegistrationResults_dir) 
    # [RegistrationResults_dir] = ori_RegistrationResults_dir
    # 備份所選日期的RegistrationFile_RollSystem檔案
    regResultsLogCopyFiles = glob.glob(os.path.join(ori_RegistrationResults_dir+"/RegistrationFile_RollSystem_"+myoptinDate_underLine+"*.tsv"))
    for f in regResultsLogCopyFiles:
        try:    copy2(f, today+RegistrationResults_dir)
        except  IOError: print("Error:w/o"+" "+f)
        else:   print(f+" --- [Copy OK!]") 
    # [ContinuousRegistrationResults.tsv]
    try:    copy2(ori_RegistrationResults_dir+"/ContinuousRegistrationResults.tsv", today+RegistrationResults_dir)
    except  IOError: print("Error:w/o"+" ContinuousRegistrationResults.tsv")
    else:   print("ContinuousRegistrationResults.tsv"+" --- [Copy OK!]") 

    # MeasureToolResults folder create
    if not os.path.exists(today+MeasureToolResults_dir):
        os.mkdir(today+MeasureToolResults_dir) 
    # [MeasureToolResults_dir] = ori_MeasureToolResults_dir
    # 備份所選日期的MeasureToolResults檔案
    measureToolLogCopyFiles = glob.glob(os.path.join(ori_MeasureToolResults_dir+"/MeasureToolFile_RollSystem_"+myoptinDate_underLine+"*.tsv"))
    for f in measureToolLogCopyFiles:
        try:    copy2(f, today+MeasureToolResults_dir)
        except  IOError: print("Error:w/o"+" "+f)
        else:   print(f+" --- [Copy OK!]") 


    # DataServer configs
    if not os.path.exists(today+DataServer_configs_dir):
        os.mkdir(today+DataServer_configs_dir)
    # [DataServer.config] = ori_Machine_configs_dir_1    
    try:    copy2(ori_DataServer_configs_dir_1+"/DataServer.config", today+DataServer_configs_dir)
    except  IOError: print("Error:w/o"+" DataServer.config")
    else:   print("DataServer.config"+" --- [Copy OK!]")


    # E disk logs folder = E_logs_dir #創建E_logs目錄
    if not os.path.exists(today+E_logs_dir):
        os.mkdir(today+E_logs_dir)
    
    # Production logs folder = P_logs
    if not os.path.exists(today+P_logs_dir):
        os.mkdir(today+P_logs_dir)
    # Python 的標準函式「glob」可以使用名稱與路徑的方式，查找出匹配條件的檔案或資料夾，
    # 查找出檔案後，搭配其他函式庫 (例如 os 標準函式庫) ，就能做到像是批次重新命名、批次刪除...等的動作。
    pLogCopyFiles = glob.glob(os.path.join(ori_P_logs_dir_2+'/', "Export - "+str(myoptinDate.get())+"-*.csv"))
    for f in pLogCopyFiles:
        try:    copy2(f, today+P_logs_dir)
        except  IOError: print("Error:w/o"+" "+f)
        else:   print(f+" --- [Copy OK!]") 

    # GPU logs folder = GPU_dir
    if not os.path.exists(today+GPU_dir):
        os.mkdir(today+GPU_dir)
    gpuLogCopyFiles_1 = glob.glob(os.path.join(ori_GPU_dir+'/', "GPUTransformer_"+myoptinDate_underLine+".*"))
    for f in gpuLogCopyFiles_1:
        try:    copy2(f, today+GPU_dir)
        except  IOError: print("Error:w/o"+" "+f)
        else:   print(f+" --- [Copy OK!]") 
    gpuLogCopyFiles_2 = glob.glob(os.path.join(ori_GPU_dir+'/', "GPUTransformerCorrectionGrid_"+str(myoptinDate.get())+".log"))
    for f in gpuLogCopyFiles_2:
        try:    copy2(f, today+GPU_dir)
        except  IOError: print("Error:w/o"+" "+f)
        else:   print(f+" --- [Copy OK!]")   
    gpuLogCopyFiles_3 = glob.glob(os.path.join(ori_GPU_dir+'/', "GRPCCommandstream_"+myoptinDate_underLine+".bin"))
    for f in gpuLogCopyFiles_3:
        try:    copy2(f, today+GPU_dir)
        except  IOError: print("Error:w/o"+" "+f)
        else:   print(f+" --- [Copy OK!]")    

    # IPED logs folder = IPED_dir
    if not os.path.exists(today+IPED_dir):
        os.mkdir(today+IPED_dir)
    # 備份IPED/archive裏的備份檔
    dirPathPattern = ori_IPED_dir_1+r"/IPEDRK_Errors_" + myoptinDate_connect + r"-*"  
    ipedLogCopyFiles_1 = glob.glob(dirPathPattern)
    for f in ipedLogCopyFiles_1:
        # f[-29:] 用來截取IPEDRK的目錄名稱
        try:    copytree(f, today+IPED_dir+"/"+f[-29:])
        except  IOError: print("Error:w/o"+" "+f)
        else:   print(f+" --- [Copy OK!]")
    # 備份IPED裏的檔案
    ipedLogCopyFiles_2 = glob.glob(os.path.join(ori_IPED_dir_2, "*.txt"))
    for f in ipedLogCopyFiles_2:
        try:    copy2(f, today+IPED_dir)
        except  IOError: print("Error:w/o"+" "+f)
        else:   print(f+" --- [Copy OK!]")

    # ToolKit logs folder = TK_dir
    if not os.path.exists(today+TK_dir):
        os.mkdir(today+TK_dir)
    tkLogCopyFiles = glob.glob(os.path.join(ori_TK_dir+'/', str(myoptinDate.get())+"_spirit.*"))
    for f in tkLogCopyFiles:
        try:    copy2(f, today+TK_dir)
        except  IOError: print("Error:w/o"+" "+f)
        else:   print(f+" --- [Copy OK!]")

    # SpiritConsole logs folder = SC_dir
    if not os.path.exists(today+SC_dir):
        os.mkdir(today+SC_dir)
    scLogCopyFiles = glob.glob(os.path.join(ori_SC_dir+'/', str(myoptinDate.get())+"_Spirit_*"))
    for f in scLogCopyFiles:
        try:    copy2(f, today+SC_dir)
        except  IOError: print("Error:w/o"+" "+f)
        else:   print(f+" --- [Copy OK!]")

    # ScalingService folder = ScalingService_dir
    if not os.path.exists(today+ScalingService_dir):
        os.mkdir(today+ScalingService_dir)
    # 備份選定日期的所有screenshots
    checkFilesTime_selectDate(ori_ScalingService_dir)
    for f in file_list_callmehi:
        copy2(ori_ScalingService_dir+"/"+f, today+ScalingService_dir)
        try:    copy2(ori_ScalingService_dir+"/"+f, today+ScalingService_dir)
        except  IOError: print("Error:w/o"+" "+f)
        else:   print(f+" --- [Copy OK!]")
        
    # Screenshots folder = screenShots_dir
    if not os.path.exists(today+screenShots_dir):
        os.mkdir(today+screenShots_dir)
    # 備份選定日期的所有screenshots
    checkFilesTime_selectDate(ori_screenShots_dir)
    for f in file_list_callmehi:
        copy2(ori_screenShots_dir+"/"+f, today+screenShots_dir)
        try:    copy2(ori_screenShots_dir+"/"+f, today+screenShots_dir)
        except  IOError: print("Error:w/o"+" "+f)
        else:   print(f+" --- [Copy OK!]")
    # 備份今天的所有screenshots
    checkFilesTime_today(ori_screenShots_dir)
    for f in file_list_callmehi:
        try:    copy2(ori_screenShots_dir+"/"+f, today+screenShots_dir)
        except  IOError: print("Error:w/o"+" "+f)
        else:   print(f+" --- [Copy OK!]")

    # sensors folder = sensors_dir
    if not os.path.exists(today+sensors_dir):
        os.mkdir(today+sensors_dir)
    try:    copy2(ori_sensors_dir+"/sensors.tsv", today+sensors_dir)
    except  IOError: print("Error:w/o"+" sensors.tsv")
    else:   print("sensors.tsv"+" --- [Copy OK!]")
    try:    copy2(ori_sensors_dir+"/measurewheel.tsv", today+sensors_dir)
    except  IOError: print("Error:w/o"+" measurewheel.tsv")
    else:   print("measurewheel.tsv"+" --- [Copy OK!]")
    # exposure folder = exposure_dir
    if not os.path.exists(today+exposure_dir):
        os.mkdir(today+exposure_dir)
    try:    copy2(ori_exposure_dir+"/ExposureParameterSetup.log", today+exposure_dir)
    except  IOError: print("Error:w/o"+" ExposureParameterSetup.log")
    else:   print("ExposureParameterSetup.log"+" --- [Copy OK!]")
    # efficiency folder = efficiency_dir
    if not os.path.exists(today+efficiency_dir):
        os.mkdir(today+efficiency_dir)
    try:    copy2(ori_efficiency_dir+"/EfficiencyMeasurement.log", today+efficiency_dir)
    except  IOError: print("Error:w/o"+" EfficiencyMeasurement.log")
    else:   print("EfficiencyMeasurement.log"+" --- [Copy OK!]")
    # BeamDiameter folder = BeamDiameter_dir
    if not os.path.exists(today+BeamDiameter_dir):
        os.mkdir(today+BeamDiameter_dir)
    try:    copy2(ori_BeamDiameter_dir+"/BeamDiameterCalibration.log", today+BeamDiameter_dir)
    except  IOError: print("Error:w/o"+" BeamDiameterCalibration.log")
    else:   print("BeamDiameterCalibration.log"+" --- [Copy OK!]")
    # LaserPower folder = LaserPower_dir
    if not os.path.exists(today+LaserPower_dir):
        os.mkdir(today+LaserPower_dir)
    try:    copy2(ori_LaserPower_dir+"/LaserPower.log", today+LaserPower_dir)
    except  IOError: print("Error:w/o"+" LaserPower.log")
    else:   print("LaserPower.log"+" --- [Copy OK!]")
    # PlcCommunication folder = PlcCommunication_dir
    if not os.path.exists(today+PlcCommunication_dir):
        os.mkdir(today+PlcCommunication_dir)
    try:    copy2(ori_PlcCommunication_dir+"/"+myoptinDate.get()+"_plccommunication.xml", today+PlcCommunication_dir)
    except  IOError: print("Error:w/o"+myoptinDate.get()+"_plccommunication.xml")
    else:   print(myoptinDate.get()+"_plccommunication.xml"+" --- [Copy OK!]")




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

# - after close window -
sys.stdout = old_stdout