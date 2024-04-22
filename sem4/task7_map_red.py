"""🐀 Напишите программу на Python, которая будет находить
сумму элементов массива из 1000000 целых чисел.
🐀 Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
🐀 Массив должен быть заполнен случайными целыми числами
от 1 до 100.
🐀 При решении задачи нужно использовать многопоточность,
многопроцессорность и асинхронность.
🐀 В каждом решении нужно вывести время выполнения
вычислений."""

import json, time
from random import randint
from functools import reduce



# array_num = []
#
# def fill_aray(size):
#     for _ in range(size):
#         array_num.append(randint(1,100))
#     return array_num
#
# with open('array_data.json', 'w',encoding='utf-8') as f:
#     data ={}
#     data['arr'] = fill_aray(1000000)
#     json.dump(data, f)
#
# print(len(array_num))

arr_data = []
with open('array_data.json', 'r', encoding='utf-8') as f:
    d = json.load(f)
    arr_data = d['arr']
    print(f'sum elem = {sum(arr_data)}')


# print(arr[:10])


def chunkify(arr: list, number_of_chunks=20):
    step = len(arr) // number_of_chunks
    if step != 0:
        for i in range(0, len(arr), step):
            yield arr[i: i + step]
    else:
        yield arr


def chunks_mapper(chunk):

    return sum(chunk)


def reducer(p, c):
    return p + c


def main():
    start_time = time.time()
    data_chunks = chunkify(arr_data, number_of_chunks=20)
    mapped = map(chunks_mapper, data_chunks)
    reduced = reduce(reducer, mapped)

    print(reduced)
    print(f'Total time = {time.time() - start_time:.2f} seconds')


if __name__ == '__main__':
    main()
