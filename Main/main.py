import pyautogui as pg
import time

TIMER_SECONDS = 5

def confirm():
    pg.write("y")
    pg.press("Enter")

def resume():
    pg.press("Space")


def travel_the_trail():
    pg.write("1")
    pg.press("Enter")

def banker_from_boston():
    pg.write("1")
    pg.press("Enter")

def names_of_members():
    pg.write("You")
    for _ in range(2):
        pg.press("Enter")

def month_of_independence(): # Select April
    pg.write("2")
    pg.press("Enter")

def buy_supplies():
    # buy 9 oxens
    time.sleep(1)
    pg.write("1") 
    pg.press("Enter")

    pg.write("9") 
    pg.press("Enter")
    time.sleep(1)

    # buy 2,000 pounds of food
    pg.write("2") 
    pg.press("Enter")

    pg.write("2000") 
    pg.press("Enter")
    time.sleep(1)

    # buy 13 sets of clothing
    pg.write("3") 
    pg.press("Enter")

    pg.write("13") 
    pg.press("Enter")
    time.sleep(1)

    # buy spare parts, 3 for each
    pg.write("5") 
    pg.press("Enter")

    for _ in range(3):
        pg.write("3") 
        pg.press("Enter")
        time.sleep(0.01)
    time.sleep(1)

def change_pace():
    pg.write("4") 
    pg.press("Enter")

    pg.write("3") 
    pg.press("Enter")

def start_the_trail():
    pg.write("1") 
    pg.press("Enter")

print(f"Starting in {TIMER_SECONDS} seconds...")
time.sleep(TIMER_SECONDS)

# execution
travel_the_trail()
banker_from_boston()
names_of_members()
confirm()
month_of_independence()

for _ in range(4):
    resume()

buy_supplies()

for _ in range(2):
    resume()

time.sleep(2.80)
resume()

change_pace()
start_the_trail()
resume()