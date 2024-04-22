"""🐀 Создать программу, которая будет производить подсчет
количества слов в каждом файле в указанной директории и
выводить результаты в консоль.
🐀 Используйте асинхронный подход."""

import os, asyncio
from pathlib import Path
from time import time


async def word_counter(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        count_word = len(content.split())
        print(f'{f.name} содержит {count_word} слов.')


async def main():
    dir_path = Path('../lec4_multitask')
    file_paths = os.walk(dir_path)
    for root, dirs, files in file_paths:
        for file in files:
            tasks = [asyncio.create_task(word_counter(os.path.join(root, file)))]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    start_time = time()
    asyncio.run(main())
    print(f'{time() - start_time: .2f}')

    # print(word_counter('test_dir/test3.html'))
