# Oregon Trail Bot
Contains bots created by me for [The Oregon Trail](https://www.pcjs.org/software/pcx86/game/other/1991/oregon_trail/) video game from 1991.

These bots are written in **Python**, with the **pyautogui module**. This is also **cross-platform**, which means it works for all operating systems (Windows/MacOS/Linux), and it's **open source**, which means that anyone can use my code as long as they put my name if anyone uses it. See [LICENSE.txt](LICENSE.txt) for details.

## Contributing
See [CONTRIBUTING.md](contributing.md) for details.

## The Oregon Trail Game Rights
[pcjs.org](https://www.pcjs.org/software/pcx86/game/other/1991/oregon_trail/#pcjs-machines) © 2012-2025 [Jeff Parsons](https://github.com/jeffpar) <br>
[PCjs](https://github.com/jeffpar/pcjs) is released under an [MIT License](https://www.pcjs.org/LICENSE.txt)

The link that goes to The Oregon Trail video game is not owned by me nor contributed by me, as it's work from another person. See above for more details. 

# Start for Speedrunning Bot
An autonomous bot that sets up the start for speedrunning in **under 15 seconds**.
<br>

![Bot running](GIFs/start-for-speedrunning.gif)

**Full run:** Download the full [MP4 video](https://github.com/Mat1020/oregon-trail-bot/blob/main/GIFs/start-for-speedrunning.mp4) or watch in YouTube (link to YouTube).

## Requirements
1. Clone This Repository <br>
Open Git and copy & paste this command:

```bash
git clone https://github.com/Mat1020/oregon-trail-bot.git
```

After you clone it, open with your **code editor/IDE**; examples of them for this project are Visual Studio Code, PyCharm, Sublime Text, Vim, Kite, Adam, or really any that can execute and compile **Python** code. 

2. Install and Activate a Virtal Enviroment (.venv/) <br>
Within the repository you just cloned, open the terminal and **create your virtual enviroment**:  

```bash
python -m venv .venv
```

4. Install the dependencies on requirements.txt <br>
On Git, and copy & paste this command:

```bash
pip install -r requirements.txt
```

4. Install the latest Python version on your machine <br>
If you haven't already done so, install the official latest version at [Python.org](https://www.python.org/), choose **your OS**, and follow the downloading instructions.

This bot in particular is compatible with **Python 3.10** and so on.

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
