"""Задание №9
🐀 Написать программу, которая скачивает изображения с заданных URL-адресов и
сохраняет их на диск. Каждое изображение должно сохраняться в отдельном
файле, название которого соответствует названию изображения в URL-адресе.
🐀 Например URL-адрес: https://example/images/image1.jpg -> файл на диске:
image1.jpg
🐀 Программа должна использовать многопоточный, многопроцессорный и
асинхронный подходы.
🐀 Программа должна иметь возможность задавать список URL-адресов через
аргументы командной строки.
🐀 Программа должна выводить в консоль информацию о времени скачивания
каждого изображения и общем времени выполнения программы."""

import requests
from pathlib import Path
from time import time

start_time = time()

urls = ['https://w.forfun.com/fetch/71/7111142d25bd0f62d5078b68bbfe40a0.jpeg',
        'https://w.forfun.com/fetch/5d/5d572d697e41c82ac511549420ebcf44.jpeg',
        'https://images.unsplash.com/photo-1712135595180-f3902e325574?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        'https://images.unsplash.com/photo-1711972964911-ddf34f5955c3?q=80&w=2071&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        'https://images.unsplash.com/photo-1712194295920-a7e01399bf9f?q=80&w=2079&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D]'
        ]

for url in urls:
    response = requests.get(url)
    filename = url[-10:-5] + '.jpeg'
    with open(filename, "bw") as f:
        f.write(response.content)
    print(f"Downloaded {url} in {time() - start_time:.2f} seconds")

print(f'Total time = {time() - start_time:.2f} seconds')

"""Downloaded https://w.forfun.com/fetch/71/7111142d25bd0f62d5078b68bbfe40a0.jpeg in 0.98 seconds
Downloaded https://w.forfun.com/fetch/5d/5d572d697e41c82ac511549420ebcf44.jpeg in 1.96 seconds
Downloaded https://images.unsplash.com/photo-1712135595180-f3902e325574?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D in 3.77 seconds
Downloaded https://images.unsplash.com/photo-1711972964911-ddf34f5955c3?q=80&w=2071&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D in 4.80 seconds
Downloaded https://images.unsplash.com/photo-1712194295920-a7e01399bf9f?q=80&w=2079&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D] in 5.28 seconds
Total time = 5.28seconds"""

