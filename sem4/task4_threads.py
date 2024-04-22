"""🐀 Создать программу, которая будет производить подсчет
количества слов в каждом файле в указанной директории и
выводить результаты в консоль.
🐀 Используйте потоки."""

import time, threading, logging, os
from pathlib import Path

logger = logging.getLogger()


def word_counter(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        count_word = len(content.split())
        # logger.info(f'{f.name} содержит {count_word} слов')
        print(f'{f.name} содержит {count_word} слов.')


def main():
    dir_path = Path('../lec4_multitask')
    file_paths = os.walk(dir_path)
    threads = []
    for root, dirs, files in file_paths:
        for file in files:
            t = threading.Thread(target=word_counter(os.path.join(root, file)))
            threads.append(t)
            t.start()

if __name__ == '__main__':
    start_time = time.time()
    main()
    print(f'{time.time() - start_time: .2f}')

# print(word_counter('test_dir/test3.html'))
