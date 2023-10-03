## TypeQuest 
is a command-line application that allows you to host a virtual bot on your PC for any text-based chatting platform. It uses OCR (optical character recognition) to read messages you receive on these platforms and automatically replies by sending a response to the person who sent the message. In this specific example, **TypeQuest** is used to host a text-based video game that can be played on these text-based chatting platforms.

## Technologies Used

* Python: The programming language used to develop TypeQuest
* Pytesseract: A Python module used to handle OCR
* OpenCV: A library used to perform basic image manipulation (thresholding, grayscaling)
* pyautogui, pynput: Libraries used to track the mouse and write to the keyboard, respectively

## How to Set Up TypeQuest

To set up TypeQuest, you will need to have Python installed on your system, along with the PIP (Python package management tool).

To install Python and PIP:

* Windows: Use the Microsoft Store to install the latest version of Python.
* Linux: Both Python and PIP are already installed in almost all major Linux distributions. Search the internet if you cannot find them on your system.<br/>

**Once you have Python and PIP installed**, go to the download destination of the TypeQuest repository and open a terminal window (Command Line window) there.

Then, **run the following command**:
~~~
python3 GameCode.py
~~~
This will install the rest of the packages required by the program automatically.

After all of this, you will need to select the exact area on the screen where the OCR will run. To do this, simply move your mouse to the required area and drag from the start point of the scan area to the end point.

**That's it! You have successfully set up your own virtual bot.**

Now, just ask your friends to text you <em>"Startgame"</em> to start the game.

## How TypeQuest Works

After you have selected the scan area, the program will capture a screenshot of the selected area every 5 seconds. After a little modification to the captured image, it will ask **Pytesseract** to perform OCR on the image. **Pytesseract** will extract the text from the captured image, and then the game logic will come into play.

The game logic will compare the input message to the stored game storylines and correct and incorrect choices inside the **GameStoryLines.py** file. Based on the response being correct or incorrect, the program will return the output accordingly.

If the mouse pointer of your PC is close to the position of the text box of the chatting application, the program will write the output to the chatbot automatically using the pynput module, which creates a virtual keyboard controller in Python.

After sending the message, the program will wait for the next response and so on. When the game ends (either by winning or losing the game), the program is basically reset and the game can be played again by inputing Startgame once again.

## Note

* The tracking of the mouse pointer is done by the Pyautogui module.
* There are 3 stories that will be played randomly.
* This is a personal project that I have used to learn more about different technologies. I am also working on adding more interesting features, such as automatic story generation using the Google PaLM API. Stay tuned for updates!
* This project can easily be used to integrate AI to your chatting platforms also like Whatsapp Web, Discord etc..
