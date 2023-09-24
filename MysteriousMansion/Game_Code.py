## All library's used
from PIL import ImageGrab, ImageOps
import pytesseract,pynput,pyautogui
import time
import os
import GameStoryLines

from sys import platform
if platform == "win32":
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
keyboard = pynput.keyboard.Controller()

## Replace this with your local Tesseract-OCR install location


GameRunning = True
theEnd = False
InPosition() = False
currentChoice = 0

def keyOut(inpString):
    print(inpString)
    if(inpString!=""):
        if(InPosition()):
            print('yes')
            for k in inpString:
                keyboard.press(k)
                keyboard.release(k)
            keyboard.press(pynput.keyboard.Key.enter)
            keyboard.release(pynput.keyboard.Key.enter)
def readInput():
    global currentChoice
    global theEnd
    global GameRunning
    global InPosition()
    imageObj = ImageGrab.grab(bbox=(655,850,785,895))
    imageObj.save("C:/Users/aksha/Desktop/ImageGrub/ScreenGrab.jpeg")
    imageObj = ImageOps.grayscale(imageObj)
    stringFromImage = pytesseract.image_to_string(imageObj)
    iString = stringFromImage.split("\n")
    iString = iString[0].split(" ")
    print(iString)
    
    if(theEnd==False):
        if(currentChoice==0):
            if(iString[0] == "StartGame"):
                if(InPosition()):
                    currentChoice = 1 
                    return GameStoryLines.Choices["1"]
            else:
                return ""
        elif(currentChoice==1):
            if(iString[0].lower() == "yes"):
                if(InPosition()):
                    currentChoice = 2
                    return GameStoryLines.Choices["2"]
            elif(iString[0].lower() == "no"):
                if(InPosition()):
                    theEnd = True
                    return GameStoryLines.Choices["1f"]
            else:
                return ""
        elif(currentChoice==2):
            if(iString[0].lower() == "left"):
                if(InPosition()):
                    currentChoice = 3
                    return GameStoryLines.Choices["3"]
            elif(iString[0].lower() == "right"):
                if(InPosition()):
                    theEnd = True
                    return GameStoryLines.Choices["2f"]
            else:
                return ""
        elif(currentChoice==3):
            if(iString[0].lower() == "blue"):
                if(InPosition()):
                    currentChoice = 4
                    return GameStoryLines.Choices["4"]
            elif(iString[0].lower() == "red"):
                theEnd = True
                return GameStoryLines.Choices["3f"]
            else:
                return ""
        elif(currentChoice==4):
            if(iString[0].lower() == "yes"):
                if(InPosition()):
                    currentChoice = 5
                    return GameStoryLines.Choices["5"]
            elif(iString[0].lower() == "no"):
                if(InPosition()):
                    theEnd = True
                    return GameStoryLines.Choices["4f"]
            else:
                return ""
        elif(currentChoice==5):
            if(iString[0].lower() == "yes"):
                if(InPosition()):
                    currentChoice = 6
                    return GameStoryLines.Choices["6"]
            elif(iString[0].lower() == "no"):
                if(InPosition()):
                    theEnd = True
                    return GameStoryLines.Choices["5f"]
            else:
                return ""
        elif(currentChoice==6):
            if(iString[0].lower() == "yes"):
                if(InPosition()):
                    currentChoice = 7
                    return GameStoryLines.Choices["7"]
            elif(iString[0].lower() == "no"):
                if(InPosition()):
                    theEnd = True
                    return GameStoryLines.Choices["6f"]
            else:
                return ""
        elif(currentChoice==7):
            if(InPosition()):
                return GameStoryLines.Choices["8"]
    elif(theEnd == True):
        if(InPosition()):
            theEnd=False
            currentChoice = 0
            return GameStoryLines.Choices["End"]
    return ""
while(GameRunning):
    ## Here 720 is the starting x position of whatsapp chatbox and y is starting y position of whatsapp chatbox.
    if(pyautogui.position().x>720 and pyautogui.position().y>920):
        InPosition()=True
    else:
        InPosition()=False
    keyOut(readInput())
    ## time.sleep act as a buffer for memory to not run out too fast.
    time.sleep(5)




### Written by your friendly neighbourhood C.T.###