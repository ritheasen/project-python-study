import pyautogui as pt
import time

amount = input("Enter amount of message need to be send:")
message = input("Write message:")
i = 1

time.sleep(5) # to delay timing from enter value

while i <= int(amount):

    pt.typewrite(message)
    pt.press("enter")

    i = i + 1