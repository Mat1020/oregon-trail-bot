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

def fire_the_riffle():
    pg.press("Space")

def point_the_riffle():
    pg.write(">")

def go_hunting():
    pg.press("Enter")
    pg.press("8")
    pg.press("Enter")

# Main sequence
def main():
    timer = get_timer_seconds(5)
    for _ in range(timer):
        print(f"Starting in {timer}...")
        time.sleep(1)
        timer -= 1
    time.sleep(timer)
    go_hunting()
    x = 10000

    while x > 1:
        fire_the_riffle()
        point_the_riffle()
        x -= 1

main()
