import pyautogui
import os
import time

while True:
    time.sleep(30)
    pyautogui.press('1')

    pyautogui.keyDown('w')
    time.sleep(1)
    pyautogui.keyUp('w')
    pyautogui.keyDown('s')
    time.sleep(1)
    pyautogui.keyUp('s')
    pyautogui.keyDown('a')
    time.sleep(1)
    pyautogui.keyUp('a')
    pyautogui.keyDown('d')
    time.sleep(1)
    pyautogui.keyUp('d')