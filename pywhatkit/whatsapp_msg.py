# Send WhatsApp messages.


import pywhatkit, pyautogui as pya

num1 = "9625655166"
num2 = "7985218361"
num3 = "6386481355"
num4 = "8319172589"
num5 = "9329622116"
num6 = "8840806945"
# phone = input("Enter the Phone Number : ")
msg = "Lunch kr liya tha na ??"


# pywhatkit.sendwhatmsg(number,msg,hour,mins,wa)
pywhatkit.sendwhatmsg("+91" + num1, msg, 17, 11, 10)
pya.press("enter")


"""
User Manual

Syntax: pywhatkit.sendmsg(“receiver mobile number”,”message”,hours,minutes)

Parameters:

Receiver mobile number: The Receiver’s mobile number must be in string format and the country code must be mentioned before the mobile number.
Message: Message to be sent(Must be in string format).
Hours: This module follows the 24 hrs time format.
Minutes: Mention minutes of the scheduled time for the message(00-59).
"""
