# Oregon Trail Bot (Start for Speedrunning)
An atonomous bot that sets-up the start of speedrunning for [The Oregon Trail](https://www.pcjs.org/software/pcx86/game/other/1991/oregon_trail/) video game from 1991.

 It takes about less than **17 seconds** (maybe even faster on another computer) to start the trail, which is very impressive.
[![Oregon Trail Bot Video](https://img.youtube.com/vi/ia_NPJsQM_o/0.jpg)](https://www.youtube.com/watch?v=ia_NPJsQM_o)

This bot is written in **Python, with the pyautogui module**. This is also **cross-platform**, which means it works for all OS (Windows/MacOS/Linux).

## Contributing
Feel free to open issues or pull requests. See [CONTRIBUTING.md](contributing.md) for details.

## Bot Actions
Basically, this bot uses a specifc sets of actions in order to start your trail in a a specific way to set your speedrun at the beggining. It would type quickly through the steps, and wait when neccesary.

I actually forgot where I got these steps from (but I guess it's pretty easy to find them). There's more information of what the bot does in the code.

## User Actions
After the bot is done with its job, the rest of the speedrun consists:

1. Enter "n" everytime you are at a landmark.
2. Spam the space bar: sometimes you get messages which can slow you down.
3. Near the end, there's a specific part of the trail where you want to:

When you get to choose where to go next, select "1".

When you get to choose where to go next again, select "2".

When you are at "2", select "2" again and enter "y".

# Requirements
I assume that you've already Python installed. Otherwise, go to [python.org](https://www.python.org/) and follow the downloading instructions.

## Pyautogui
This bot consistes of using the [pyautogui module](https://pyautogui.readthedocs.io/en/latest/) (or library) from Python, which is **cross-platform** (works in Windows/MacOS/Linux).

If you don't have it already installed, need to **pip install it**.

Copy & paste this on your **terminal (cmd)**:
```bash
pip install pyautogui
```
