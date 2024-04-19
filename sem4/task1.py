"""Написать программу, которая считывает список из 10 URL-
адресов и одновременно загружает данные с каждого
адреса.
🐀 После загрузки данных нужно записать их в отдельные
файлы.
🐀 Используйте потоки."""

import requests
import threading
import time

urls = ['https://shashkovs.ru/vmsh/2023/n/##prob_29_%D0%BD_01/',
        'https://www.kaggle.com/datasets/',
        'https://flask-russian-docs.readthedocs.io/ru/latest/tutorial/',
        'https://www.python.org/',
        'https://blockly.games/',
        ]


def download(url):
    response = requests.get(url)

    filename = 'thread_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    with open(filename, "w", encoding='utf-8') as f:
        f.write(response.text)
    print(f"Downloaded {url} in {time.time()-start_time:.2f} seconds")


threads = []
start_time = time.time()

for url in urls:
    thread = threading.Thread(target=download, args=[url])
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
