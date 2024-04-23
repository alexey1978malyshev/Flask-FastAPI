"""🐀 Напишите программу на Python, которая будет находить
сумму элементов массива из 1000000 целых чисел.
🐀 Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
🐀 Массив должен быть заполнен случайными целыми числами
от 1 до 100.
🐀 При решении задачи нужно использовать многопоточность,
многопроцессорность и асинхронность.
🐀 В каждом решении нужно вывести время выполнения
вычислений."""
import multiprocessing
from random import randint
import json,time

with open('../array_data.json', 'r', encoding='utf-8') as f:
    d = json.load(f)
    arr_data = d['arr']
#print(f'sum elem = {sum(arr_data)}')

result = multiprocessing.Value('i', 0)

def chunkify(arr: list, number_of_chunks=20):
    step = len(arr) // number_of_chunks
    if step != 0:
        for i in range(0, len(arr), step):
            yield arr[i: i + step]
    else:
        yield arr

def chunks_counter(chunk, res):
    with res.get_lock():
        res.value += sum(chunk)
    return res


start_time = time.time()
processes = []

if __name__ == '__main__':
    start_time = time.time()
    processes = []
    data_chunks = chunkify(arr_data, number_of_chunks=2)


    for el in data_chunks:
        process = multiprocessing.Process(target=chunks_counter, args=(el, result))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()


    print(f"Сумма элементов списка: {result.value}")
    print(f'Total time = {time.time() - start_time:.2f} seconds')

"""Сумма элементов списка: 50492727
Total time = 0.57 seconds"""
