import pyautogui as pg
import time

def get_timer_seconds(MINIMUM_TIMER_SECONDS):
    while True:
        timer = input("What do you want the timer time (in seconds) be? ")
        if timer.isdigit():
            timer = int(timer)
            if timer >= MINIMUM_TIMER_SECONDS:
                break
            else:
                print(f"Please enter a number greater than {MINIMUM_TIMER_SECONDS} next time.")
        else:
            print(f"Please enter a number (in seconds) next time.")

    return timer

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

# Main code sequence
def main():
    timer = get_timer_seconds(5)
    for _ in range(timer):
        print(f"Starting in {timer}...")
        time.sleep(1)
        timer -= 1
    time.sleep(timer)

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

    time.sleep(2.80) # the ONLY necessary wait; depends hevaliy on your computer
    resume()

    change_pace()
    start_the_trail()
    resume()

if __name__ == "__main__":
    main()