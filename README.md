# Oregon Trail Bot
A collection of bots that automate and control gameplay behavior for [The Oregon Trail](https://www.pcjs.org/software/pcx86/game/other/1991/oregon_trail/) video game from 1991.

These bots are using the **Python** programming language, with 3 third-party libraries such as [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/), [OpenCV](https://opencv.org/), and [MSS](https://python-mss.readthedocs.io/) (or Multiple ScreenShots) are the core of these game bots. 

This is also **cross-platform**, which means it works for all operating systems (Windows/MacOS/Linux), and it's **open source**, which means that anyone can use my code. 

This project is licensed under the [MIT License](LICENSE.txt).

## Want to Contribute?
See [CONTRIBUTING.md](https://github.com/Mat1020/oregon-trail-bot?tab=contributing-ov-file) for details.

## The Oregon Trail "Gaming Website" Copyright
[pcjs.org](https://www.pcjs.org/software/pcx86/game/other/1991/oregon_trail/#pcjs-machines) © 2012-2026 [Jeff Parsons](https://github.com/jeffpar) <br>
[PCjs](https://github.com/jeffpar/pcjs) is released under an [MIT License](https://www.pcjs.org/LICENSE.txt)

The Oregon Trail video game itself is **open source**, but, however, the link that I include in this repo (that opens up a new window to play it in your web browser) is not own by me, as it's work from another person. This is just a notice to avoid being Copyrighted.

## Installing
1. Open Git and copy & paste this command. Open it with your preferred code editor after doing so.

```bash
git clone https://github.com/Mat1020/oregon-trail-bot.git
```

2. If you haven't already done so, install the official latest version at [Python.org](https://www.python.org/), choose **your OS**, and follow the downloading instructions.

![Screenshot of Python.org](images/readme/downloads-python-org.png)

> [!IMPORTANT]
> Latest Python version (e.g. Python 3.13+) is strongly recommended.

3. Open the terminal and install your virtual environment (.venv/) within your cloned version of this repository:

```bash
python -m venv .venv
```

4. Activate your virtual environment.

i. _For Windows:_ Use either the Command Prompt, PowerShell, or Git Bash.

**Command Prompt:** <br>
```bash
.venv\Scripts\Activate.ps1
```

**PowerShell:** <br>
```bash
.venv\Scripts\activate
```

**Git Bash:** <br>
```bash
source .venv/Scripts/activate
```

ii. _For macOS/Linux_: Use bash / zsh.

```bash
source .venv/bin/activate
```

5. Lastly, on the terminal, install the dependencies found on requirements.txt by copying & pasting this command:

```bash
pip install -r requirements.txt
```

# Start for Speedrunning Bot
An autonomous bot that sets up the start for speedrunning in **under 15 seconds**.
<br>

![Bot running](videos/readme/start-for-speedrunning.gif)

**Full run:** Download the full [MP4 video](https://github.com/Mat1020/oregon-trail-bot/blob/main/videos/readme/start-for-speedrunning.mp4) or watch in [YouTube](https://www.youtube.com/watch?v=k9FTH87C5b8).

> [!WARNING]
> This bot manipulates **keyboard input**. Make sure the bot **IS NOT** running somewhere else besides The Oregon Trail.

## Running
To run the bot, you need to first open [The Oregon Trail](https://www.pcjs.org/software/pcx86/game/other/1991/oregon_trail/) video game. Then, go under the _Main_ folder and then run _main.py_. Next, boot up the assigned ID # for _Start for Speedrunning Bot_. Finally, go back to The Oregon Trail since the bot runs when you **first boot the game**.

### Bot Actions
Essentially, the purpose for _Start for Speedrunning Bot_ is to **initiate your oregon trail in a specific manner for a speedrun**; by establishing everything you need without the need to remember it or to do it yourself at all!

There's more detailed information about what the bot does in the comments from the [code](https://github.com/Mat1020/oregon-trail-bot/blob/main/Main/Bots/start_for_speed_running_bot.py).

### User Actions
After the bot is done with its job, the rest of the speedrun consists:

1. Enter "n" every time you are at a landmark.
2. Spam the space bar: Sometimes you get messages that can slow you down.
3. Near the end, there's a specific part of the trail where you want to:

When you get to choose where to go next, select "1".

When you get to choose where to go next again, select "2".

When you are at "2", select "2" again and enter "y".

You should finish _your_ speedrun afterwards!
