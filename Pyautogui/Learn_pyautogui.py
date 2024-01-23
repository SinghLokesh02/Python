# Import the Relavant Modules
import pyautogui as pya
import time


# Give the python file some time before running
time.sleep(3) # Delay execution for a given number of seconds. The argument may be a floating point number for subsecond precision.

# Mouse Functions

print(pya.size()) #Returns the width and height of the screen as a two-integer tuple.
# Output -> Size(width=1920, height=1080)


print(pya.position()) #Returns the current xy coordinates of the mouse cursor as a two-integer tuple.
# Output -> Point(x=822, y=505)

# Moves the mouse cursor to a point on the screen. (x,y,time_in_secs)
pya.moveTo(18,115,1)
pya.leftClick()


# Move mouse relative to its current position
pya.moveRel(100,200,3)


# click (X, Y, Number_of_click, time, button_to_click)
pya.click(18,115,3,3,button="left")


# Python Scroll Up 500
pya.scroll(500)

# Python Scroll Up 500
pya.scroll(-500)

# Example of mouse up and down (Program Number - 1)

x1,y1 = 300,400

while y1!=1000:
    pya.mouseDown(x1,y1,button="left")
    pya.moveTo(800,y1,3)
    pya.mouseUp()
    y1+=100

# Program Number - 2

num1 = 200
num2 = 200
count = 0
while count != 5:
    pya.mouseDown(num1,num2,button="left")
    pya.moveTo(num1+100,num2,2)
    num1+= 100
    pya.mouseUp()
    pya.moveTo(num1+50,num2,2)
    num1+=50
    count += 1


# # Program -3 to make Rectangle

l1,l2 = 400,400
pya.mouseDown(l1,l2,button="left")
pya.moveTo(l1+300,l2,1)
l1+=300
pya.mouseUp()
pya.mouseDown(l1,l2,button="left")
pya.moveTo(l1,l2+200,1)
l2+=200
pya.mouseUp()
pya.mouseDown(l1,l2,button="left")
pya.moveTo(l1-300,l2,1)
l1-=300
pya.mouseUp()
pya.mouseDown(l1,l2,button="left")
pya.moveTo(l1,l2-200,1)
l2-=200
pya.mouseUp()


# Program - 4 (Print three rectangle)

count = 0
l1, l2 = 400, 400
while count != 3:
    pya.mouseDown(l1, l2, button="left")
    pya.moveTo(l1 + 300, l2, 1)
    l1 += 300
    pya.mouseUp()
    pya.mouseDown(l1, l2, button="left")
    pya.moveTo(l1, l2 + 200, 1)
    l2 += 200
    pya.mouseUp()
    pya.mouseDown(l1, l2, button="left")
    pya.moveTo(l1 - 300, l2, 1)
    l1 -= 300
    pya.mouseUp()
    pya.mouseDown(l1, l2, button="left")
    pya.moveTo(l1, l2 - 200, 1)
    l2 -= 200
    pya.mouseUp()
    l1 += 400    
    count+=1


"""
# Perform a left mouse click
pyautogui.click()
pya.leftClick()
pya.rightClick()
pya.doubleClick()
pya.tripleClick()
pya.middleClick()

# Perform a double click with a 0.5-second interval
pyautogui.click(clicks=2, interval=0.5) 

"""
