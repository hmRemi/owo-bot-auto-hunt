from colorama import Fore
import threading
import datetime
import requests
import ctypes
import time
import os
import re


class Statistics:
    start_time = time.time()
    total_xp = 0
    success = 0
    errors = 0
    author = "Devuxious"


os.system("cls")

logo = f'''{Fore.LIGHTBLUE_EX}
                             ██████╗ ██╗    ██╗ ██████╗     ██████╗  ██████╗ ████████╗
                            ██╔═══██╗██║    ██║██╔═══██╗    ██╔══██╗██╔═══██╗╚══██╔══╝
                            ██║   ██║██║ █╗ ██║██║   ██║    ██████╔╝██║   ██║   ██║   
                            ██║   ██║██║███╗██║██║   ██║    ██╔══██╗██║   ██║   ██║   
                            ╚██████╔╝╚███╔███╔╝╚██████╔╝    ██████╔╝╚██████╔╝   ██║   
                             ╚═════╝  ╚══╝╚══╝  ╚═════╝     ╚═════╝  ╚═════╝    ╚═╝   
'''

# Settings
channel_id = ''  # Your channel id here to send commands to
url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
command = 'wh'  # Command to send
delay = 15  # Delay between each command
token = ''  # Your token here

# Message body for the request
message_body = {
    'content': command
}

# Headers for the request
headers = {
    'authorization': token,
    'authority': 'discord.com',
    'accept': '*/*',
    'accept-language': 'en-US',
    'content-type': 'application/json',
    'origin': 'https://discord.com',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9024 Chrome/108.0.5359.215 Electron/22.3.26 Safari/537.36',
    'x-debug-options': 'bugReporterEnabled',
    'x-discord-locale': 'en-US',
    'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDI0Iiwib3NfdmVyc2lvbiI6IjEwLjAuMjI2MjEiLCJvc19hcmNoIjoieDY0IiwiYXBwX2FyY2giOiJpYTMyIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV09XNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIGRpc2NvcmQvMS4wLjkwMjQgQ2hyb21lLzEwOC4wLjUzNTkuMjE1IEVsZWN0cm9uLzIyLjMuMjYgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjIyLjMuMjYiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyNDk1NjEsIm5hdGl2ZV9idWlsZF9udW1iZXIiOjQwMDEwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsLCJkZXNpZ25faWQiOjB9',
}

exit_flag = False

# Update the title of the console
def update_title():
    while True:
        # Update the title
        ctypes.windll.kernel32.SetConsoleTitleW(
            f'OWO Bot | Total XP: {Statistics.total_xp} | Success: {Statistics.success} | Errors: {Statistics.errors} | Elapsed Time: {round(time.time() - Statistics.start_time)}s | Author: {Statistics.author}')


def check_for_bot_detection():
    global exit_flag
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    while True:
        time.sleep(20)
        print(f'\n{Fore.LIGHTBLACK_EX}[{current_time}] | {Fore.LIGHTBLACK_EX}Checking for bot detection...{Fore.RESET}')
        owo_bot_id = 408785106942164992
        direct_messages_url = f'https://discord.com/api/v9/users/@me/channels'

        params = {
            'limit': 50
        }

        response = requests.get(direct_messages_url, headers=headers, params=params)

        if response.status_code == 200:
            messages = response.json()

            for message in messages:
                recipients = message.get('recipients', [])
                owo_recipients = [recipient for recipient in recipients if recipient.get('id') == str(owo_bot_id)]
                if owo_recipients:
                    channel_id = message.get('id')
                    channel_url = f'https://discord.com/api/v9/channels/{channel_id}/messages'

                    response = requests.get(channel_url, headers=headers, params=params)
                    if response.status_code == 200:
                        messages = response.json()
                        for bot_message in messages:
                            if bot_message.get('author', {}).get('id') == str(owo_bot_id):
                                if "Beep Boop. Are you a real human?" in bot_message.get('content'):
                                    print(f'{Fore.LIGHTBLACK_EX}[{current_time}] | {Fore.RED}Bot detected. Exiting...')
                                    exit_flag = True
                                    break
                                else:
                                    print(f'{Fore.LIGHTBLACK_EX}[{current_time}] | {Fore.GREEN}Bot not detected.')
                                    exit_flag = False
                                    break


# Get the last message from the channel
def get_last_message():
    # Send the request
    response = requests.get(url, headers=headers)

    # Check if the response is 200
    if response.status_code == 200:
        # Get the messages
        messages = response.json()

        # Check if the messages is not empty
        if messages:
            # Get the last message
            last_message = messages[0]

            # Return the content of the last message
            return last_message['content']
    return None


# Extract the info from the message
def extract_info_from_message(message):
    # Search for the emojis and xp
    emojis_match = re.search(r'(?<=You found: )(.*?)(?=\n)', message)
    xp_match = re.search(r'gained \*\*(\d+)xp\*\*', message)

    # Define the emojis and xp
    emojis = emojis_match.group(1) if emojis_match else "Not found"
    xp = xp_match.group(1) if xp_match else "Not found"

    # Increase the total xp
    if xp != "Not found":
        Statistics.total_xp += int(xp)

    print(
        f'{Fore.LIGHTBLACK_EX}[{current_time}] | Gathered Items (Emojis: {Fore.LIGHTBLUE_EX}{emojis}{Fore.LIGHTBLACK_EX} | XP: {Fore.LIGHTBLUE_EX}{xp}{Fore.LIGHTBLACK_EX}){Fore.RESET}')


# Start the title thread
title_thread = threading.Thread(target=update_title)
title_thread.daemon = True
title_thread.start()

# Start the title thread
anti_bot_detection = threading.Thread(target=check_for_bot_detection)
anti_bot_detection.daemon = True
anti_bot_detection.start()

# Print the logo
print(logo)

# Start the main loop
while True:
    if exit_flag:
        break

    # Send the request
    response = requests.post(url, headers=headers, json=message_body)

    # Get the current time
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Print send command message and wait 1 second
    print(
        f'\n{Fore.LIGHTBLACK_EX}[{current_time}] | Sent command {Fore.LIGHTBLACK_EX}({Fore.LIGHTBLUE_EX}{command}{Fore.LIGHTBLACK_EX}) {Fore.LIGHTBLACK_EX}({Fore.LIGHTBLUE_EX}{channel_id}{Fore.LIGHTBLACK_EX}){Fore.RESET}')
    time.sleep(1)

    # Check if the response is 200
    if response.status_code == 200:
        # Increase the success counter
        Statistics.success += 1

        # Get the last message
        last_sent_message = get_last_message()

        # Check if the last message is not None
        if last_sent_message:
            # Extract the info from the message
            extract_info_from_message(last_sent_message)
        else:
            # Print the error message
            print(f'{Fore.LIGHTBLACK_EX}[{current_time}] | {Fore.RED}Unable to fetch the last message.')
    else:
        # Print the error message
        print(
            f'{Fore.LIGHTBLACK_EX}[{current_time}] | {Fore.RED}Failed to send message. Status code: {response.status_code}')

        # Increase the errors counter
        Statistics.errors += 1

    # Print the delay message and wait the delay
    print(
        f'{Fore.LIGHTBLACK_EX}[{current_time}] | {Fore.LIGHTBLACK_EX}Waiting for {Fore.LIGHTBLUE_EX}{delay}{Fore.LIGHTBLACK_EX} seconds before sending the next message...{Fore.RESET}')
    time.sleep(delay)
