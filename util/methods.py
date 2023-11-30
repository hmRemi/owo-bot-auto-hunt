from util.stats import Statistics
from util.discord import Discord
from util.config import Config
from plyer import notification
from util.elapse import Time
from colorama import Fore
import requests
import random
import ctypes
import time
import re

class Util:
    author = "Devuxious"

    # Function to display Windows notification
    @staticmethod
    def send_notification(title, message):
        notification.notify(title=title, message=message, app_name="OWO Bot", app_icon="assets/logo.ico", timeout=10)

    # Update the title of the console
    @staticmethod
    def update_title():
        while True:
            # Update the title
            ctypes.windll.kernel32.SetConsoleTitleW(
                f'OWO Bot | Total XP: {Statistics.total_xp} | Total Emojis: {Statistics.total_emojis} | Success: {Statistics.success} | Errors: {Statistics.errors} | Elapsed Time: {round(time.time() - Time.start_time)}s | Author: {Util.author}')

    # Check for bot detection
    @staticmethod
    def check_for_bot_detection():
        while True:
            time.sleep(20)
            print(
                f'\n{Fore.LIGHTBLACK_EX}[{Time.current_time}] | {Fore.LIGHTBLACK_EX}Checking for verification...{Fore.RESET}')

            owo_bot_id = 408785106942164992
            direct_messages_url = f'https://discord.com/api/v9/users/@me/channels'

            params = {
                'limit': 50
            }

            # Get the last message
            last_sent_message = Util.get_last_message()

            # Check if the bot is asking for verification
            if "Please complete your captcha" in last_sent_message or "are you a real human?" in last_sent_message:
                Util.send_notification("OWO Automation | Verification Detected",
                                       "Please complete the captcha to continue.")
                print(
                    f'{Fore.LIGHTBLACK_EX}[{Time.current_time}] | {Fore.RED}Verification detected in channel. Exiting...')
                Discord.exit_flag = True
                break
            else:
                print(f'{Fore.LIGHTBLACK_EX}[{Time.current_time}] | Verification not detected in channel.')

            # Send the request to get the direct messages
            dm_check = requests.get(direct_messages_url, headers=Discord.headers, params=params)

            # Check if the response is 200
            if dm_check.status_code == 200:
                messages = dm_check.json()

                # Loop through the recipients
                for message in messages:
                    recipients = message.get('recipients', [])

                    # Search for the bot in the recipients
                    owo_recipients = [recipient for recipient in recipients if recipient.get('id') == str(owo_bot_id)]

                    # Check if the bot is in the recipients
                    if owo_recipients:
                        channel_id = message.get('id')
                        channel_url = f'https://discord.com/api/v9/channels/{channel_id}/messages'

                        response = requests.get(channel_url, headers=Discord.headers, params=params)
                        if response.status_code == 200:
                            messages = response.json()

                            # Loop through the messages
                            for bot_message in messages:

                                # Check if the message is from the bot
                                if bot_message.get('author', {}).get('id') == str(owo_bot_id):

                                    # Check if the bot is asking for verification
                                    if "Beep Boop. Are you a real human?" in bot_message.get('content'):
                                        Util.send_notification("OWO Automation | Verification Detected",
                                                               "Please complete the captcha to continue.")
                                        print(
                                            f'{Fore.LIGHTBLACK_EX}[{Time.current_time}] | {Fore.RED}Verification detected in dms. Exiting...')
                                        Discord.exit_flag = True
                                        break
                                    else:
                                        print(
                                            f'{Fore.LIGHTBLACK_EX}[{Time.current_time}] | Verification not detected in dms.')
                                        Discord.exit_flag = False
                                        break

    # Get the last message from the channel
    @staticmethod
    def get_last_message():
        # Send the request
        response = requests.get(Discord.url, headers=Discord.headers)

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

    # Get the last embed color from the channel
    @staticmethod
    def get_last_embed_color():
        # Send the request
        response = requests.get(Discord.url, headers=Discord.headers)

        # Check if the response is 200
        if response.status_code == 200:
            # Get the messages
            messages = response.json()

            # Check if the messages is not empty
            if messages:
                # Get the last message
                last_message = messages[0]

                # Extract the embeds
                embeds = last_message.get('embeds')

                if embeds:
                    # Get the color from the first embed (assuming there's only one)
                    embed_color = embeds[0].get('color')
                    return embed_color

        return None

    # Get the delay
    @staticmethod
    def get_delay(base, randomized):
        return base + random.randint(Config.min_random_delay, Config.max_random_delay) if randomized else base

    # Extract the info from the message
    @staticmethod
    def extract_info_from_message(message):
        # Search for the emojis and xp
        emojis_match = re.search(r'(?<=You found: )(.*?)(?=\n)', message)
        xp_match = re.search(r'gained \*\*(\d+)xp\*\*', message)

        # Define the emojis and xp
        emojis = emojis_match.group(1) if emojis_match else "Not found"
        xp = xp_match.group(1) if xp_match else "Not found"

        # Increase the total emojis
        Statistics.total_emojis += len(emojis.split()) if emojis != "Not found" else 0

        # Increase the total xp
        Statistics.total_xp += int(xp) if xp != "Not found" else 0

        print(
            f'{Fore.LIGHTBLACK_EX}[{Time.current_time}] | Gathered Items (Emojis: {Fore.LIGHTBLUE_EX}{emojis}{Fore.LIGHTBLACK_EX} | XP: {Fore.LIGHTBLUE_EX}{xp}{Fore.LIGHTBLACK_EX}){Fore.RESET}')
