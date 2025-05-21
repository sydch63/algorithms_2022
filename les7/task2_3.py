"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

3) с помощью встроенной функции поиска медианы

сделайте замеры на массивах длиной 10, 100, 1000 элементов

В конце сделайте аналитику какой трех из способов оказался эффективнее
"""


from random import randint
from timeit import timeit
from statistics import median

man_input = int(input("Введите число: "))
lst = [randint(1,100) for i in range(2*man_input+1)]

print(
    timeit(
        "median(lst[:])",
        globals=globals(),
        number=10),median(lst[:]))

print(
    timeit(
        "median(lst[:])",
        globals=globals(),
        number=100),median(lst[:]))

print(
    timeit(
        "median(lst[:])",
        globals=globals(),
        number=1000),median(lst[:]))