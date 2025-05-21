"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""

from random import randint
from timeit import timeit


man_input = int(input("Введите число: "))
lst = [randint(1,100) for i in range(2*man_input+1)]



def shellsort(a):
    def new_increment(a):
        i = int(len(a) / 2)
        yield i
        while i != 1:
            if i == 2:
                i = 1
            else:
                i = int(round(i/2.2))
            yield i
    for increment in new_increment(a):
        for i in range(increment, len(a)):
            for j in range(i, increment-1, -increment):
                if a[j - increment] < a[j]:
                    break
                a[j],a[j - increment] = a[j - increment],a[j]
    return a

print(
    timeit(
        "shellsort(lst[:])",
        globals=globals(),
        number=10),shellsort(lst[:])[man_input])

print(
    timeit(
        "shellsort(lst[:])",
        globals=globals(),
        number=100),shellsort(lst[:])[man_input])

print(
    timeit(
        "shellsort(lst[:])",
        globals=globals(),
        number=1000),shellsort(lst[:])[man_input])