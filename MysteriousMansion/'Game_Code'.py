## All library's used
from PIL import ImageGrab
import pytesseract,time,pynput,pyautogui
import GameStoryLines

keyboard = pynput.keyboard.Controller()
## Replace this with your local Tesseract-OCR install location
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

GameRunning = True
theEnd = False
currentChoice = 0
def WriteItDown(inpString):
    if(inpString!=""):
        if(pyautogui.position().x>720 and pyautogui.position().y>920):
            for k in inpString:
                keyboard.press(k)
                keyboard.release(k)
            keyboard.press(pynput.keyboard.Key.enter)
            keyboard.release(pynput.keyboard.Key.enter)
def readItAll():
    global currentChoice
    global theEnd
    global GameRunning
    imageObj = ImageGrab.grab(bbox=(655,830,785,870))
    imageObj.save("C:/Users/aksha/Desktop/ImageGrub/ScreenGrab.jpeg")
    stringFromImage = pytesseract.image_to_string(imageObj)
    temp = stringFromImage.split("\n")
    temp = temp[0].split(" ")
    print(temp)
    if(theEnd==False):
        if(currentChoice==0):
            if(temp[0] == "StartGame"):
                currentChoice = 1 
                return GameStoryLines.Choices["1"]
            else:
                return ""
        elif(currentChoice==1):
            if(temp[0].lower() == "yes"):
                currentChoice = 2
                return GameStoryLines.Choices["2"]
            elif(temp[0].lower() == "no"):
                theEnd = True
                return GameStoryLines.Choices["1f"]
            else:
                return ""
        elif(currentChoice==2):
            if(temp[0].lower() == "left"):
                currentChoice = 3
                return GameStoryLines.Choices["3"]
            elif(temp[0].lower() == "right"):
                theEnd = True
                return GameStoryLines.Choices["2f"]
            else:
                return ""
        elif(currentChoice==3):
            if(temp[0].lower() == "blue"):
                currentChoice = 4
                return GameStoryLines.Choices["4"]
            elif(temp[0].lower() == "red"):
                theEnd = True
                return GameStoryLines.Choices["3f"]
            else:
                return ""
        elif(currentChoice==4):
            if(temp[0].lower() == "yes"):
                currentChoice = 5
                return GameStoryLines.Choices["5"]
            elif(temp[0].lower() == "no"):
                theEnd = True
                return GameStoryLines.Choices["4f"]
            else:
                return ""
        elif(currentChoice==5):
            if(temp[0].lower() == "yes"):
                currentChoice = 6
                return GameStoryLines.Choices["6"]
            elif(temp[0].lower() == "no"):
                theEnd = True
                return GameStoryLines.Choices["5f"]
            else:
                return ""
        elif(currentChoice==6):
            if(temp[0].lower() == "yes"):
                currentChoice = 7
                return GameStoryLines.Choices["7"]
            elif(temp[0].lower() == "no"):
                theEnd = True
                return GameStoryLines.Choices["6f"]
            else:
                return ""
        elif(currentChoice==7):
            return GameStoryLines.Choices["8"]
    elif(theEnd == True):
        GameRunning=False
        return GameStoryLines.Choices["End"]
    return ""
while(GameRunning):
    WriteItDown(readItAll())
    time.sleep(5)




















### Written by your friendly neighbourhood C.T.