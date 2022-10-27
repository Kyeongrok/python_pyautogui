import pyautogui as pg
from time import sleep

for i in range(115, 240, 2):
    sleep(1)
    print(f"{i}찍을 준비 하세요.")
    sleep(2)
    pg.screenshot('{:03d}.png'.format(i), region=(259, 111, 1430, 847))
    print(f"{i}찍었습니다. {(i*2)-1}")

