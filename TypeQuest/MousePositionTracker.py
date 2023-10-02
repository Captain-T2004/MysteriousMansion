from pynput import mouse

scanPoints = []

def on_click(x, y, button, pressed):
    scanPoints.append((x,y))
    return False

def init():
    for i in range(2):
        listener = mouse.Listener(on_click=on_click)
        listener.start()
        listener.join()