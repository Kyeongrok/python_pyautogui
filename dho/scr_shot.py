import pyautogui as pg
def screen_shot(x_loc, y_loc, x_size, y_size, filename='departure.png'):
    # pg.getWindowsWithTitle("대항해시대 온라인")[0].activate()
    pg.screenshot(filename, region=(x_loc, y_loc, x_size,y_size))
    print('take screen shot')

if __name__ == '__main__':
    # screen_shot(2514, 1191, 40, 20, 'departure.png')
    # screen_shot(1657, 999, 40, 25, 'departure2.png')
    # x = 2587, y = 1236
    # screen_shot(2587, 1236, 40, 20, '../screen_shot/square.png')
    # x = 2071, y = 470
    # screen_shot(2066, 472, 22, 24, '../screen_shot/port_icon.png')
    screen_shot(2517, 1195, 45, 26, '../screen_shot/goto_port.png') #항구안내원 항구로

