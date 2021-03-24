import pyautogui as pg
from time import sleep
import glob
from dho.scr_shot import screen_shot
import win32api, win32con

def click(x, y):
    try:
        r = win32api.SetCursorPos((x ,y))
        print('r:', r)
    except Exception as e:
        print(e)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def is_exsist(n, img_file_nm):
    '''
    이미지에 해당하는 영역이 화면에 있는지 여부
    :param n:
    :param img_file_nm:
    :return:
    '''
    pg.getWindowsWithTitle("대항해시대 온라인")[n].activate()
    sleep(0.2)
    b_dep = pg.locateOnScreen(img_file_nm, grayscale=True, confidence=0.9)
    if b_dep != None:
        # print(b_dep)
        return True
    else:
        return False

def click_area(n, img_file_nm):
    sleep(1)
    pg.getWindowsWithTitle("대항해시대 온라인")[n].activate()
    sleep(0.5)
    b_dep = pg.locateOnScreen(img_file_nm, grayscale=True, confidence=0.8)
    if b_dep != None:
        print(n, img_file_nm, 'can search', b_dep, type(b_dep.left))
        c = pg.center(b_dep)
        print('center:', c)
        sleep(0.5)
        click(int(c.x), int(c.y))
        print(pg.position())
        return 0
    else:
        print(img_file_nm, 'cannot search')
        return 1

def press_key(n, key_code):
    sleep(0.5)
    pg.getWindowsWithTitle("대항해시대 온라인")[n].activate()
    win32api.keybd_event(key_code, 0, 0, 0)
    sleep(.05)
    win32api.keybd_event(key_code, 0, win32con.KEYEVENTF_KEYUP, 0)


if __name__ == '__main__':
    click_area(0, '../screen_shot/departure.png')
    click_area(0, '../screen_shot/departure2.png')
# click_departure(1, 'departure.png')
# click_departure(1, 'departure2.png')
