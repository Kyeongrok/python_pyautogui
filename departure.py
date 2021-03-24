from dho.click_area import click_area
from dho.click_area import press_key
from dho.click_area import is_exsist
from time import sleep
# 'F5':0x74 https://gist.github.com/chriskiehl/2906125
# 'F6':0x75,
'''
'spacebar':0x20,
'''
def select_port_guide():
    for _ in range(10):
        if is_exsist(0, './screen_shot/port_guide.png') or is_exsist(0, './screen_shot/port_manager.png'):
            break
        press_key(0, 0x09)

def which_screen():
    '''
    어떤 화면인지 여부
    :return:
    '''
    if is_exsist(0, './screen_shot/port_guide.png') or is_exsist(0, './screen_shot/port_manager.png'):
        #항구안내원 또는 항구 관리
        return 3
    elif is_exsist(0, './screen_shot/here_is_a_port.png'):  # 항구
        return 2
    elif is_exsist(0, './screen_shot/is_before_depart.png'): # 출항 누르기 전
        return 1
    else:
        return 4

# 현재 화면이 광장인지, 항구안내원 또는 항구 관리인지, 항구인지, 출항눌렀을때인지
screen_no = which_screen()
print('screen_no:', screen_no)

if screen_no == 4: # 도시
    press_key(0, 0x74)
    click_area(0, './screen_shot/port_icon.png') # 항구로 가기
    sleep(1)
    select_port_guide()
    sleep(1)
    press_key(0, 0x20) # space로 항구안내원(관리) 선택
    # 항구안내원이 나올때까지 tab누르기

if screen_no == 3: # 항구안내원 또는 관리
    r = click_area(0, './screen_shot/goto_port.png') # 항구로
    if r == 0:
        screen_no = 2

if screen_no == 2: # 항구
    click_area(0, './screen_shot/departure.png')
    r = click_area(1, './screen_shot/departure.png')
    if r == 0:
        screen_no = 1

if screen_no == 1: # 출항 누르기 전
    click_area(0, './screen_shot/departure2.png')
    click_area(1, './screen_shot/departure2.png')

print('screen_no:', screen_no)