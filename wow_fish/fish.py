import cv2 as cv
import pyautogui
import os
import time
import glob

# WOW截图文件夹路径
fishImgPath = r'/Users/mccree/Desktop/Blizzard/fishImg/fishImg.png'
# 拿到最新的截图路径
# scrnShotPath = r'wowFish.png'
# imgSrc = glob.glob(scrnShotPath)[-1]
imgSrc = r'wowFish.png'
print("截图路径:{}".format(imgSrc))



def screenShot():
    print('截图')
    time.sleep(3)
    img = pyautogui.screenshot('wowFish.png')


def findFishFloat():

    # 大图
    imgBig = cv.imread(
        imgSrc,
        0
    )
    # 鱼漂图
    imgTemplate = cv.imread(
        fishImgPath,
        0
    )
    # 得到鱼漂图宽高
    w, h = imgTemplate.shape[::-1]
    # 模板匹配操作
    res = cv.matchTemplate(imgBig, imgTemplate, cv.TM_SQDIFF_NORMED)
    # 得到最大和最小值得位置
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    top_left = min_loc  # 左上角的位置
    bottom_right = (top_left[0] + w, top_left[1] + h)  # 右下角的位置
    # 在原图上画矩形
    print('检测结果{},{}'.format(top_left,bottom_right))
    x = (top_left[0]+bottom_right[0])/2
    y = (top_left[1]+bottom_right[1])/2
    print('中心点{},{}'.format(x,y))
    pyautogui.move(x, y)
    cv.rectangle(imgBig, top_left, bottom_right, (0, 0, 255), 2)
    # 显示原图和处理后的图像
    cv.imshow("processed", imgBig)
    cv.waitKey(0)
    cv.destroyAllWindows()

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


screenShot()
findFishFloat()