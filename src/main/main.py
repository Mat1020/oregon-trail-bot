import time, bots.start_for_speed_running_bot

dict_of_bots = {
    "start for speed running bot": 1
}

def loop_available_bots():
    for bot_name, bot_id in dict_of_bots.items():
        print(f"{bot_name.title()}: {bot_id}")

def boot_bot():
    while True:
        id = input("Enter the ID of the bot you want to boot up: ")
        if id.isdigit():
            id = int(id)
            if 1 <= id <= len(dict_of_bots):
                break
            else:
                print("Please enter a valid bot ID next time.")
                time.sleep(0.5)
        else:
            print("Please enter a number for a bot ID next time.")
            time.sleep(0.5)

    return id

def main():
    print("This is where you boot up a bot. These are the available bots: ")
    time.sleep(1)
    loop_available_bots()
    id = boot_bot()
    if id == 1:
        bots.start_for_speed_running_bot.main()

if __name__ == "__main__":
    main()