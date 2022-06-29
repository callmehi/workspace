import datetime
import pyautogui
import clipboard as pc

tonow = datetime.datetime.now()
pc.copy(tonow.strftime("%Y%m%d"))
