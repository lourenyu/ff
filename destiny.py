import pyautogui
import pydirectinput
import time
m = 0
for i in range(0,1000):
    m = m + 1
    print(m)
    time.sleep(2)
    pydirectinput.press('a')
    time.sleep(2)
    pydirectinput.press('d')
    time.sleep(2)
    pydirectinput.click()
    # time.sleep(2)
    # pydirectinput.click('&nbsp')


