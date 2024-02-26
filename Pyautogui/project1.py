# Spiral Drawing

import pyautogui as pyt
import time


# Code for Taking Screenshots

time.sleep(3)
photo = pyt.screenshot()
photo.save("demo.png")
photo.show()


# Code for Spiral drawing

time.sleep(3)
distance = 300
while(distance > 0):
    pyt.dragRel(distance, 0, 1,button="left")
    distance -= 20
    pyt.dragRel(0, distance, 1,button="left")
    pyt.dragRel(-distance, 0, 1,button="left")
    distance -= 20
    pyt.dragRel(0, -distance, 1,button="left")
    time.sleep(2)
    
    