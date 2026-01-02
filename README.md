# Oregon Trail Bot
Contains bots created by me for [The Oregon Trail](https://www.pcjs.org/software/pcx86/game/other/1991/oregon_trail/) video game from 1991.

These bots are written in **Python**, with the **pyautogui module**. This is also **cross-platform**, which means it works for all operating systems (Windows/MacOS/Linux), and it's **open source**, which means that anyone can use my code as long as they put my name if anyone uses it. See [LICENSE.txt](LICENSE.txt) for details.

## Want to Contribute?
See [CONTRIBUTING.md](contributing.md) for details.

## The Oregon Trail Game Rights
[pcjs.org](https://www.pcjs.org/software/pcx86/game/other/1991/oregon_trail/#pcjs-machines) © 2012-2025 [Jeff Parsons](https://github.com/jeffpar) <br>
[PCjs](https://github.com/jeffpar/pcjs) is released under an [MIT License](https://www.pcjs.org/LICENSE.txt)

The link that goes to The Oregon Trail video game is not owned by me, as it's work from another person. See above for more details. 

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

After you clone it, open it with your **code editor/IDE**; examples of these for this project include Visual Studio Code, PyCharm, Sublime Text, Vim, Kite, or any other that can execute and compile **Python** code.

2. Install Python on Your Computer <br>
If you haven't already done so, install the official latest version at [Python.org](https://www.python.org/), choose **your OS**, and follow the downloading instructions.

This bot is particularly compatible with **Python 3.10** and later versions.

3. Install and Activate a Virtual Environment (.venv/) <br>
Within the repository you just cloned, open the terminal and **create your virtual environment**: <br>
```bash
python -m venv .venv
```

***For Windows:*** To activate the virtual environment, you're going to use either the **Command Prompt**, **PowerShell**, or **Git Bash**.

**Command Prompt:** <br>
```bash
.venv\Scripts\activate
```

**PowerShell:** <br>
```bash
.venv\Scripts\activate
```

**Git Bash:** <br>
```bash
source .venv/Scripts/activate
```

***For macOS/Linux:*** For macOS or Linux, you're going to activate it using **bash / zsh**. <br>
```bash
source .venv/bin/activate
```

4. Install the Dependencies on requirements.txt <br>
Lastly, on the same terminal, copy & paste this command: <br>
```bash
pip install -r requirements.txt
```

## Bot Actions
Essentially, this bot employs a predefined set of actions to initiate your trial in a specific manner, by establishing your speed run when you first boot the game. It would type _quickly real quick_ through the steps and wait once when necessary.

There's more detailed information about what the bot does in the comments from the [code](https://github.com/Mat1020/oregon-trail-bot/blob/main/Main/start_for_speed_running_bot.py).

## User Actions
After the bot is done with its job, the rest of the speedrun consists:

1. Enter "n" every time you are at a landmark.
2. Spam the space bar: Sometimes you get messages that can slow you down.
3. Near the end, there's a specific part of the trail where you want to:

When you get to choose where to go next, select "1".

When you get to choose where to go next again, select "2".

When you are at "2", select "2" again and enter "y".
