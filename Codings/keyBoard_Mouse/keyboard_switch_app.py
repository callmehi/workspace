import pyautogui as pg
pg.PAUSE = 1 #pg.PAUSE=1 指的是每隔一秒執行一個操作指令
pg.keyDown('alt') # 一定要有對應的KeyUP, 要不然會鍵盤錯亂
pg.press('tab')
pg.press('tab')
pg.press('tab')
pg.keyUp('alt')