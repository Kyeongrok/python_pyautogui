import pyautogui as pg
from time import sleep
import pyperclip

pg.doubleClick(x=1722, y=314)
sleep(1)
pyperclip.copy("아름")
pg.hotkey('ctrl', 'v')
pg.doubleClick(x=1743, y=383)
