import win32api
import time
from datetime import datetime
import os
import getpass

user_name = getpass.getuser()
file_name = (user_name + '-' + (str(datetime.now()))[:10])
state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128
keyboard_state = win32api.GetKeyboardState()

resolution_file = './ActivityData/MainScreenResolution.csv'
try:
    os.stat('./ActivityData')
except:
    os.mkdir('./ActivityData')
if os.path.exists(resolution_file):
    pass
else:
    file = open(resolution_file, 'w')
    monitors = win32api.EnumDisplayMonitors()

    main_monitor = 0

    for i in range(len(monitors)):
        if (monitors[i][2][0] == 0) and (monitors[i][2][1] == 0):
            main_monitor = i


    file.write(str(main_monitor) + ';' + str(monitors[main_monitor][2]) + '\n')
    file.close()



def try_write_mousekey():
    try:
        file = open('./ActivityData/' + file_name + '.txt', 'a')
        file.write(str(datetime.now()) + ',' + str(win32api.GetCursorPos()) + '\n')
        file.close()
    except IOError:

        file = open('./ActivityData/' + file_name + '.txt', 'w')
        file.write(str(datetime.now()) + ',' + str(win32api.GetCursorPos()) + '\n')
        file.close()


def try_write_keyboard():
    try:
        file = open('./ActivityData/' + file_name + '.txt', 'a')
        file.write(str(datetime.now()) + '\n')
        file.close()
    except IOError:

        file = open('./ActivityData/' + file_name + '.txt', 'w')
        file.write(str(datetime.now()) + '\n')
        file.close()

while True:
    mouse_l_click = win32api.GetKeyState(0x01)
    mouse_r_click = win32api.GetKeyState(0x02)
    current_keyboard_state = win32api.GetKeyboardState()

    if current_keyboard_state[7:] != keyboard_state[7:]:
        keyboard_state = current_keyboard_state
        try_write_keyboard()
        #print(keyboard_state)

    if mouse_l_click != state_left or mouse_r_click != state_right:
        state_left = mouse_l_click
        state_right = mouse_r_click
        if mouse_l_click < 0 or mouse_r_click < 0:
            try_write_mousekey()
    time.sleep(0.01)

