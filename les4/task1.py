"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""

from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

nums = [1,3,4,5,6,7,10]

print('Первый замер: ',timeit('func_1(nums)',globals=globals(),number=1000))


def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 ==0]
    return new_arr

nums = [1,3,4,5,6,7,10]

print('Второй , оптимизированный , замер: ',timeit('func_2(nums)',globals=globals(),number=1000))