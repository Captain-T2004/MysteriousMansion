## All library's used
from PIL import ImageGrab, ImageOps
import pytesseract,time,pynput,pyautogui
import GameStoryLines
keyboard = pynput.keyboard.Controller()

## Replace this with your local Tesseract-OCR install location
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

GameRunning = True
theEnd = False
inPosition = False
currentChoice = 0

def writeItDown(inpString):
    print(inpString)
    if(inpString!=""):
        if(inPosition):
            print('yes')
            for k in inpString:
                keyboard.press(k)
                keyboard.release(k)
            keyboard.press(pynput.keyboard.Key.enter)
            keyboard.release(pynput.keyboard.Key.enter)
def readItAll():
    global currentChoice
    global theEnd
    global GameRunning
    global inPosition
    imageObj = ImageGrab.grab(bbox=(655,850,785,895))
    imageObj.save("C:/Users/aksha/Desktop/ImageGrub/ScreenGrab.jpeg")
    imageObj = ImageOps.grayscale(imageObj)
    stringFromImage = pytesseract.image_to_string(imageObj)
    temp = stringFromImage.split("\n")
    temp = temp[0].split(" ")
    print(temp)
    
    if(theEnd==False):
        if(currentChoice==0):
            if(temp[0] == "StartGame"):
                if(inPosition):
                    currentChoice = 1 
                    return GameStoryLines.Choices["1"]
            else:
                return ""
        elif(currentChoice==1):
            if(temp[0].lower() == "yes"):
                if(inPosition):
                    currentChoice = 2
                    return GameStoryLines.Choices["2"]
            elif(temp[0].lower() == "no"):
                if(inPosition):
                    theEnd = True
                    return GameStoryLines.Choices["1f"]
            else:
                return ""
        elif(currentChoice==2):
            if(temp[0].lower() == "left"):
                if(inPosition):
                    currentChoice = 3
                    return GameStoryLines.Choices["3"]
            elif(temp[0].lower() == "right"):
                if(inPosition):
                    theEnd = True
                    return GameStoryLines.Choices["2f"]
            else:
                return ""
        elif(currentChoice==3):
            if(temp[0].lower() == "blue"):
                if(inPosition):
                    currentChoice = 4
                    return GameStoryLines.Choices["4"]
            elif(temp[0].lower() == "red"):
                theEnd = True
                return GameStoryLines.Choices["3f"]
            else:
                return ""
        elif(currentChoice==4):
            if(temp[0].lower() == "yes"):
                if(inPosition):
                    currentChoice = 5
                    return GameStoryLines.Choices["5"]
            elif(temp[0].lower() == "no"):
                if(inPosition):
                    theEnd = True
                    return GameStoryLines.Choices["4f"]
            else:
                return ""
        elif(currentChoice==5):
            if(temp[0].lower() == "yes"):
                if(inPosition):
                    currentChoice = 6
                    return GameStoryLines.Choices["6"]
            elif(temp[0].lower() == "no"):
                if(inPosition):
                    theEnd = True
                    return GameStoryLines.Choices["5f"]
            else:
                return ""
        elif(currentChoice==6):
            if(temp[0].lower() == "yes"):
                if(inPosition):
                    currentChoice = 7
                    return GameStoryLines.Choices["7"]
            elif(temp[0].lower() == "no"):
                if(inPosition):
                    theEnd = True
                    return GameStoryLines.Choices["6f"]
            else:
                return ""
        elif(currentChoice==7):
            if(inPosition):
                return GameStoryLines.Choices["8"]
    elif(theEnd == True):
        if(inPosition):
            theEnd=False
            currentChoice = 0
            return GameStoryLines.Choices["End"]
    return ""
while(GameRunning):
    ## Here 720 is the starting x position of whatsapp chatbox and y is starting y position of whatsapp chatbox.
    if(pyautogui.position().x>720 and pyautogui.position().y>920):
        inPosition=True
    else:
        inPosition=False
    writeItDown(readItAll())
    ## time.sleep act as a buffer for memory to not run out too fast.
    time.sleep(5)




### Written by your friendly neighbourhood C.T.###