import pyautogui as pg
import time

def do_advanced_offense():
    pg.keyDown("w")
    pg.press("a")
    pg.keyUp("w")
    time.sleep(0.1)
    pg.press("down")
    pg.keyDown("up")
    pg.press("a")
    pg.keyUp("up")

while True:
    repeat = input("Would you like to repeat (y/n)? ").lower()
    if repeat == "y":
        time.sleep(3)
        do_advanced_offense()
    elif repeat == "n":
        print("Ok, bye!")
        quit()
    else:
        print("Please enter 'y' or 'n' next time.")