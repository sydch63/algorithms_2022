"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""

def sum(a=None,ryad = 1,result = 0):
    if a is None:
        a = int(input('Введите число, которое требуется перевернуть: '))
    if str(a) == '1':
        return result+1
    return sum(str(int(a)-1),ryad/-2,result+ryad/-2)

