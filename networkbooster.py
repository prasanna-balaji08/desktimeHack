import pyautogui
import time
pyautogui.FAILSAFE = False

while True:
    time.sleep(60)
    for i in range(0,100):
        pyautogui.moveTo(0,i*5)
        pyautogui.scroll(20)
    pyautogui.keyDown('alt')
    for i in range(0,3):
        pyautogui.press('tab')
    pyautogui.keyUp('alt')