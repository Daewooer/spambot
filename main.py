import time
import pyautogui

def sendSpamBot():
    time.sleep(5)

    text = open('beemovie')
    for each_line in text:
        pyautogui.typewrite(each_line)
        pyautogui.press('enter')


sendSpamBot()



