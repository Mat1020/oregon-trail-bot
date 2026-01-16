import time, Bots

bots = {
    "start for speed running bot": 1
}

def loop_available_bots():
    for bot_name, bot_id in bots.items():
        print(f"{bot_name.title()}: {bot_id}")

def boot_bot():
    while True:
        id = input("Enter the ID of the bot you want to boot up: ")
        if id.isdigit():
            id = int(id)
            if 1 <= id <= len(bots):
                break
            else:
                print("Please enter a valid bot ID next time.")
                time.sleep(0.5)
        else:
            print("Please enter a number for a bot ID next time.")
            time.sleep(0.5)

        if id == 1:
            Bots.start_for_speed_running_bot.main()

def main():
    print("This is where you boot up a bot. These are the available bots: ")
    time.sleep(1)
    loop_available_bots()
    boot_bot()