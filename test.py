from dho.click_area import click_area
from dho.click_area import press_key
from time import sleep
# 'F5':0x74 https://gist.github.com/chriskiehl/2906125
# 'F6':0x75,
'''
'spacebar':0x20,
'''
# press_key(0, 0x74)
# click_area(0, './screen_shot/port_icon.png') # 항구로 가기
# sleep(1)
# press_key(0, 0x09)
# press_key(0, 0x09)
# press_key(0, 0x20) # space로 항구안내원 선택
# # 항구안내원이 나올때까지 tab누르기
# click_area(0, './screen_shot/goto_port.png')
print(click_area(0, './screen_shot/here_is_a_port.png'))
