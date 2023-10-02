from PIL import ImageGrab, ImageOps
import pytesseract,pynput,pyautogui
import MousePositionTracker
import os
import cv2

print("Select the area to scan: ")
MousePositionTracker.init()
scanPointS = MousePositionTracker.scanPoints[0]
scanPointE = MousePositionTracker.scanPoints[1]




while(True):
    imageObj = ImageGrab.grab(bbox=(scanPointS[0],scanPointS[1],scanPointE[0],scanPointE[1]))
    imageObj.save(os.getcwd() + "/ScreenGrab.jpeg")
    img = cv2.imread(os.getcwd() + "/ScreenGrab.jpeg")
    gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    txt = pytesseract.image_to_string(gry, config="--psm 6")
    res = ''.join(i for i in txt if i.isalnum())
    print(txt)