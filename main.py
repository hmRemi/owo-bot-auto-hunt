from util.stats import Statistics
from util.discord import Discord
from util.config import Config
from util.methods import Util
from util.elapse import Time
from colorama import Fore
import threading
import requests
import time
import os

os.system("cls")

# Start the title thread
title_thread = threading.Thread(target=Util.update_title)
title_thread.daemon = True
title_thread.start()

# Start the title thread
anti_bot_detection = threading.Thread(target=Util.check_for_bot_detection)
anti_bot_detection.daemon = True
anti_bot_detection.start()

# Print the logo
print(Discord.logo)

# Start the main loop
while True:
    # The delay between each command
    delay = Util.get_delay(Config.base_delay, Config.randomize_delay)

    # Send the request
    response = requests.post(Discord.url, headers=Discord.headers, json=Discord.message_body)

    # Print send command message and wait 1 second
    print(
        f'\n{Fore.LIGHTBLACK_EX}[{Time.current_time()}] | Sent command {Fore.LIGHTBLACK_EX}({Fore.LIGHTBLUE_EX}{Config.command}{Fore.LIGHTBLACK_EX}) {Fore.LIGHTBLACK_EX}({Fore.LIGHTBLUE_EX}{Config.channel_id}{Fore.LIGHTBLACK_EX}){Fore.RESET}')
    if Config.command == "wb":
        time.sleep(8)
    else:
        time.sleep(1)

    # Check if the response is 200
    if response.status_code == 200:
        # Increase the success counter
        Statistics.success += 1

        # Get the last message
        last_sent_message = Util.get_last_message()
        last_sent_message_color = Util.get_last_embed_color()

        # Check if the last message is not None
        if last_sent_message:
            # Extract the info from the message
            Util.extract_info_from_message(last_sent_message)
        else:
            if last_sent_message_color == 65280:
                print(f'{Fore.LIGHTBLACK_EX}[{Time.current_time()}] | You won the battle')
                Statistics.battle_wins += 1
            elif last_sent_message_color == 16711680:
                print(f'{Fore.LIGHTBLACK_EX}[{Time.current_time()}] | You lost the battle')
            else:
                # Print the error message
                print(f'{Fore.LIGHTBLACK_EX}[{Time.current_time()}] | {Fore.RED}Unable to fetch the last message.')
    else:
        # Print the error message
        print(
            f'{Fore.LIGHTBLACK_EX}[{Time.current_time()}] | {Fore.RED}Failed to send message. Status code: {response.status_code}')

        # Increase the errors counter
        Statistics.errors += 1

    # Print the delay message and wait the delay
    print(
        f'{Fore.LIGHTBLACK_EX}[{Time.current_time()}] | {Fore.LIGHTBLACK_EX}Waiting for {Fore.LIGHTBLUE_EX}{delay}{Fore.LIGHTBLACK_EX} seconds before sending the next message...{Fore.RESET}')
    time.sleep(delay)
