import pyautogui as pag
import random
import time
import keyboard

while True:
    x = random.randint(600, 700)
    y = random.randint(200, 600)
    print(x)
    time.sleep(0.5)
    pag.moveTo(x, y, 0.5)

    if keyboard.is_pressed('e'):
        break