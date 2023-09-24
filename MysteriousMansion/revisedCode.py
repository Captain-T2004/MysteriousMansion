# PREREQUISTE CODE NEEDED TO INSTALL AND IMPORT ALL THE REQURIED PACKAGES

import sys
import subprocess
import pkg_resources
import pip

required = {'imagegrab', 'pillow', 'pynput', 'pytesseract', 'pyautogui'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed
if(missing):
    print("the listed required packages are not installed. Installing required packages in 5secs: ",missing)
    for i in missing:
        pip.main(['install', i])

print("ALL PACKAGES are installed, starting the program: ")

from PIL import ImageGrab, ImageOps
import pytesseract,pynput,pyautogui
import time
import os
import GameStoryLines
import MousePositionTracker

# IMPORTING AND SETTING UP PYTESSERACT

from sys import platform
if platform == "win32":
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" # DEFAULT INSTALL LOCATION OF PYTESSERACT

# STARTING THE GAME LOOP AND KEYBOARD CONTROLLER

GameRunning = True
theEnd = False
currentChoice = 0
keyboard = pynput.keyboard.Controller()

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

    imageObj = ImageOps.grayscale(imageObj)                             # GRAYSCALLING TO MAKE DETECTION EASIER
    
    # EXTRACTING THE TEXT FROM THE IMAGE AND FORMATTING IT
    stringFromImage = pytesseract.image_to_string(imageObj)
    iString = stringFromImage.split("\n") 
    iString = iString[0].split(" ")
    print(iString)

    # GAME FUNCTIONING
    if(theEnd == True and InPosition()):
        theEnd = False
        currentChoice = 0
        return GameStoryLines.Choices["End"]

    if(currentChoice == 7 and InPosition()): return GameStoryLines.Choices["8"]

    if(currentChoice == 8 and InPosition()):
        GameRunning = False
        return ""

    if(iString[0].lower() == GameStoryLines.correctChoices[currentChoice] and InPosition()):
        currentChoice = currentChoice + 1
        return GameStoryLines.Choices[str(currentChoice)]

    elif(iString[0].lower() == GameStoryLines.incorrectChoices[currentChoice] and InPosition()):
        theEnd = True
        return GameStoryLines.Choices[str(currentChoice)+"f"]

    return ""
def InPosition():
    width = 720
    height = 920
    if(pyautogui.position().x>width and pyautogui.position().y>height):
        return True
    return False

print("Select the area to scan: ")
MousePositionTracker.init()
scanPointS = MousePositionTracker.scanPoints[0]
scanPointE = MousePositionTracker.scanPoints[1]

while(GameRunning):
    keyOut(readInput())
    ## time.sleep act as a buffer for memory to not run out too fast.
    time.sleep(5)







### Written by your friendly neighbourhood C.T.###
