# Oregon Trail Bot
This repo contains bots made by me for [The Oregon Trail](https://www.pcjs.org/software/pcx86/game/other/1991/oregon_trail/) video game from 1991.


This bot is written in **Python**, with the **pyautogui module**. This is also **cross-platform**, which means it works for all operating systems (Windows/MacOS/Linux), and it's **open source**.

## Contributing
Feel free to open issues or pull requests. See [CONTRIBUTING.md](contributing.md) for details.

## The Oregon Trail Rights

# Start for Speedrunning Bot
An autonomous bot that sets up the start for speedrunning in under 15 seconds.
<br>

![Bot running](GIFs/start-for-speedrunning.gif)

Full run: Download the full [MP4 video](https://github.com/Mat1020/oregon-trail-bot/blob/main/GIFs/start-for-speedrunning.mp4) or watch in YouTube (link to YouTube).

## Requirements
I assume that you've already installed Python. Otherwise, go to [python.org](https://www.python.org/) and follow the downloading instructions.

**Pyautogui:** <br>
This bot consists of using the [pyautogui module](https://pyautogui.readthedocs.io/en/latest/) (or library) from Python, which is **cross-platform** (works in Windows/MacOS/Linux).

If you don't have it already installed, you need to **pip install it**.

Copy & paste this on your **terminal (cmd)**:
```bash
pip install pyautogui
```

## Bot Actions
Essentially, this bot employs a predefined set of actions to initiate your trail in a specific manner, by establishing your speedrun when you first boot the game. It would type _quickly real quick_ through the steps and wait once when necessary.

I actually forgot where I got these steps from (but I guess it's pretty easy to find them). There's more information about what the bot does in commets from the code.

## User Actions
After the bot is done with its job, the rest of the speedrun consists:

1. Enter "n" every time you are at a landmark.
2. Spam the space bar: Sometimes you get messages that can slow you down.
3. Near the end, there's a specific part of the trail where you want to:

When you get to choose where to go next, select "1".

When you get to choose where to go next again, select "2".

When you are at "2", select "2" again and enter "y".
