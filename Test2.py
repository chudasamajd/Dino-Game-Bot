import numpy as np
import cv2
from mss import mss
import pyautogui

mon = {'top': 480, 'left': 200, 'width':98, 'height':40}

k = 1
while 1:
    img = mss().grab(mon)
    img = np.array(img)
    print(img)
    cv2.imshow('test',img)
    p_cac = img[28,:,0]

    p_bird = img[1,:,0]
    print(p_bird)
    p_cac_sum = np.sum(p_cac)
    p_bird_sum = np.sum(p_bird)

    print(p_cac_sum)

    if p_cac_sum < 24206:
        pyautogui.press('up')
    if p_bird_sum < 24206:
        pyautogui.keyDown('down')
        print(p_bird)
        print(p_bird_sum)
        k=1

    if p_bird_sum == 24206 and k==1:
        pyautogui.keyUp('down')
        k=0
    if cv2.waitKey(25) == 27:
        cv2.destroyAllWindows()
        break
