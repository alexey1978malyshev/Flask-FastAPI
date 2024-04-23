"""🐀 Напишите программу на Python, которая будет находить
сумму элементов массива из 1000000 целых чисел.
🐀 Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
🐀 Массив должен быть заполнен случайными целыми числами
от 1 до 100.
🐀 При решении задачи нужно использовать многопоточность,
многопроцессорность и асинхронность.
🐀 В каждом решении нужно вывести время выполнения
вычислений."""

import asyncio
import json, time

with open('array_data.json', 'r', encoding='utf-8') as f:
    d = json.load(f)
    arr_data = d['arr']
# print(f'sum elem = {sum(arr_data)}')

result = 0

def chunkify(arr: list, number_of_chunks=20):
    step = len(arr) // number_of_chunks
    if step != 0:
        for i in range(0, len(arr), step):
            yield arr[i: i + step]
    else:
        yield arr


async def chunks_counter(chunk):
    global result
    result += sum(chunk)
    return result

async def main():
    start_time = time.time()
    data_chunks = chunkify(arr_data, number_of_chunks=20)
    tasks = []
    for el in data_chunks:
        task = asyncio.ensure_future(chunks_counter(el,))
        tasks.append(task)
    await asyncio.gather(*tasks)
    print(f"Сумма элементов списка: {result}")
    print(f'Total time = {time.time() - start_time:.2f} seconds')




if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())


"""Сумма элементов списка: 50492727
Total time = 0.57 seconds"""


