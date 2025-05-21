"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

2) без сортировки

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""


from random import randint
from timeit import timeit


man_input = int(input("Введите число: "))
lst = [randint(1,100) for i in range(2*man_input+1)]



def find_median(lst):
    n = man_input
    while n > 0:
        lst.pop(lst.index(max(lst)))
        n -= 1
    return max(lst)

print(find_median(lst[:]))


print(
    timeit(
        "find_median(lst[:])",
        globals=globals(),
        number=10),find_median(lst[:]))

print(
    timeit(
        "find_median(lst[:])",
        globals=globals(),
        number=100),find_median(lst[:]))

print(
    timeit(
        "find_median(lst[:])",
        globals=globals(),
        number=1000),find_median(lst[:]))