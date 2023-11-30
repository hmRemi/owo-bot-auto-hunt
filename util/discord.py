from colorama import Fore
from util.config import Config

class Discord:
    logo = f'''{Fore.LIGHTBLUE_EX}
                                     ██████╗ ██╗    ██╗ ██████╗     ██████╗  ██████╗ ████████╗
                                    ██╔═══██╗██║    ██║██╔═══██╗    ██╔══██╗██╔═══██╗╚══██╔══╝
                                    ██║   ██║██║ █╗ ██║██║   ██║    ██████╔╝██║   ██║   ██║   
                                    ██║   ██║██║███╗██║██║   ██║    ██╔══██╗██║   ██║   ██║   
                                    ╚██████╔╝╚███╔███╔╝╚██████╔╝    ██████╔╝╚██████╔╝   ██║   
                                     ╚═════╝  ╚══╝╚══╝  ╚═════╝     ╚═════╝  ╚═════╝    ╚═╝   

                                            {Fore.LIGHTBLACK_EX}Author: {Fore.LIGHTBLUE_EX}Devuxious{Fore.LIGHTBLACK_EX} | {Fore.LIGHTBLACK_EX}Version: {Fore.LIGHTBLUE_EX}1.0.0{Fore.LIGHTBLACK_EX}
    '''

    # Settings
    url = f'https://discord.com/api/v9/channels/{Config.channel_id}/messages'

    # Message body for the request
    message_body = {
        'content': Config.command
    }

    # Headers for the request
    headers = {
        'authorization': Config.token,
        'authority': 'discord.com',
        'accept': '*/*',
        'accept-language': 'en-US',
        'content-type': 'application/json',
        'origin': 'https://discord.com',
        'referer': 'https://discord.com/channels/1096857148820045905/1098718428086419497',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9024 Chrome/108.0.5359.215 Electron/22.3.26 Safari/537.36',
        'x-debug-options': 'bugReporterEnabled',
        'x-discord-locale': 'en-US',
        'x-discord-timezone': 'Europe/Berlin',
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDI0Iiwib3NfdmVyc2lvbiI6IjEwLjAuMjI2MjEiLCJvc19hcmNoIjoieDY0IiwiYXBwX2FyY2giOiJpYTMyIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV09XNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIGRpc2NvcmQvMS4wLjkwMjQgQ2hyb21lLzEwOC4wLjUzNTkuMjE1IEVsZWN0cm9uLzIyLjMuMjYgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjIyLjMuMjYiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyNDk1NjEsIm5hdGl2ZV9idWlsZF9udW1iZXIiOjQwMDEwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsLCJkZXNpZ25faWQiOjB9',
    }
