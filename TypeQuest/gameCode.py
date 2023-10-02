# PREREQUISTE CODE NEEDED TO INSTALL AND IMPORT ALL THE REQURIED PACKAGES

import sys
import subprocess
import pkg_resources
import pip

required = {'imagegrab', 'pillow', 'pynput', 'pytesseract', 'pyautogui', 'cvzone'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed
if(missing):
    print("the listed required packages are not installed. Installing required packages in 5secs: ",missing)
    for i in missing:
        pip.main(['install', i])

print("ALL PACKAGES are installed, starting the program: ")

from PIL import ImageGrab, ImageOps
import pytesseract, pynput, pyautogui, MousePositionTracker, time
import os, random, cv2
import GameStoryLines
# IMPORTING AND SETTING UP PYTESSERACT

from sys import platform
if platform == "win32":
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" # DEFAULT INSTALL LOCATION OF PYTESSERACT

# STARTING THE GAME LOOP AND KEYBOARD CONTROLLER

GameRunning = True
theEnd = False
currentChoice = 0
keyboard = pynput.keyboard.Controller()
storyIndex = randint(0,2)

print(GameStoryLines.correct)
# FUNCTION TO TYPEOUT A STRING TO A TEXT FIELD
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

# FUNCTION TO READ THE INPUT TEXT AND ALSO TO READ FROM STORY LINES....
def readInput():
    global currentChoice
    global theEnd
    global GameRunning
    # TAKING A SCREENSHOT OF SELECTED REGION AND SAVING IN CURRENT WORKING DIRECTORY
    imageObj = ImageGrab.grab(bbox=(scanPointS[0],scanPointS[1],scanPointE[0],scanPointE[1]))
    imageObj.save(os.getcwd() + "/ScreenGrab.jpeg")

    img = cv2.imread(os.getcwd() + "/ScreenGrab.jpeg")
    gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    txt = pytesseract.image_to_string(gry, config="--psm 6")
    iString = ''.join(i for i in txt if i.isalpha())
    print(iString.lower())

    # GAME FUNCTIONING
    if(theEnd == True and InPosition()):
        theEnd = False
        currentChoice = 0
        return GameStoryLines.Choices[storyIndex]["End"]

    if(currentChoice == len(GameStoryLines.Choices[storyIndex])-1 and InPosition()):
        GameRunning = False
        return ""

    if((GameStoryLines.correct[storyIndex][currentChoice] in iString.lower()) and InPosition()):
        currentChoice = currentChoice + 1
        return GameStoryLines.Choices[storyIndex][str(currentChoice)]

    elif((GameStoryLines.incorrect[storyIndex][currentChoice] in iString.lower()) and InPosition()):
        theEnd = True
        return GameStoryLines.Choices[storyIndex][str(currentChoice)+"f"]

    return ""
def InPosition():
    width = scanPointS[0]
    height = scanPointE[1]
    if(pyautogui.position().x>width and pyautogui.position().y>height):
        return True
    return False

print("Select the area to scan: ")
MousePositionTracker.init()
scanPointS = MousePositionTracker.scanPoints[0]
scanPointE = MousePositionTracker.scanPoints[1]

while(GameRunning):
    keyOut(readInput())
    time.sleep(5)# time.sleep act as a buffer for memory to not run out too fast.







### Written by your friendly neighbourhood C.T.###