import cv2 as cv
import pyautogui
import os
import time
import glob

# WOW截图文件夹路径
scrnShotPath = r'/Users/mccree/Desktop/Blizzard/World of Warcraft/_classic_/Screenshots/*.jpg'
# 拿到最新的截图路径
imgSrc = glob.glob(scrnShotPath)[-1]
print("截图路径:{}".format(imgSrc))
src = cv.imread(imgSrc)






# while True:
#     time.sleep(30)
#     pyautogui.press('1')
#
#     pyautogui.keyDown('w')
#     time.sleep(1)
#     pyautogui.keyUp('w')
#     pyautogui.keyDown('s')
#     time.sleep(1)
#     pyautogui.keyUp('s')
#     pyautogui.keyDown('a')
#     time.sleep(1)
#     pyautogui.keyUp('a')
#     pyautogui.keyDown('d')
#     time.sleep(1)
#     pyautogui.keyUp('d')