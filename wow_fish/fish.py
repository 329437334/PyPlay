import cv2 as cv
import pyautogui
import time
import threading
import mss
import numpy
import numpy as np
import pyscreenshot as ImageGrab


# 浮漂图片
fishImgPath = r'fishImg.png'
# 拿到最新的截图路径
imgSrc = r'wowFish.png'
print("截图路径:{}".format(imgSrc))



def screenShot():
    print('===截图===')
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

    print('检测结果{},{}'.format(top_left, bottom_right))
    x = (top_left[0] + bottom_right[0]) / 2
    y = (top_left[1] + bottom_right[1]) / 2
    print('中心点{},{}'.format(x, y))
    return (x,y)

def moveMouse(x,y):
    time.sleep(3)
    print('移动鼠标')
    pyautogui.moveTo(x, y,duration=0.25)

def start():
    while True:
        pyautogui.press('1')
        time.sleep(3)
        screenShot()
        x, y = findFishFloat()

        moveMouse(x / 2, y / 2)

        screen_record_efficient(x=x,y=y,w=200,h=200)


        time.sleep(2)
        pyautogui.rightClick()


def printPiexl():
    c = 0
    while True:
        img = pyautogui.screenshot('sound.png')
        x, y = pyautogui.position()
        # pix = pyautogui.pixel(x, y-30)
        print('{}'.format((x,y)))
        # print('{}'.format(pix))1
        # c = c + 1


def startSoundFish():
    t = threading.Thread(target=printPiexl, name='Piexl')
    t.start()
    t.join()

def screen_record_efficient(x,y,w,h):
    # 800x600 windowed mode
    mon = {"top": 240, "left": -2340, "width": 300, "height": 50}

    title = "[MSS] FPS benchmark"
    fps = 0
    sct = mss.mss()
    last_time = time.time()

    while time.time() - last_time < 60:
        img = numpy.asarray(sct.grab(mon))
        fps += 1

        cv.imshow(title, img)
        if cv.waitKey(25) & 0xFF == ord("q"):
            # cv.destroyAllWindows()
            break

    sct.close()
    return fps


time.sleep(2)
# start()
# startSoundFish()



screen_record_efficient(x=1931,y=362,w=200,h=200)



# screen_record()
# print("PIL:", screen_record())
# print("MSS:", screen_record_efficient())
