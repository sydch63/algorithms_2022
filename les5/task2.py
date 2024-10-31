"""
Задание 2.

Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Попытайтесь решить это задание в двух вариантах
1) через collections

defaultdict(list)
int(, 16)
reduce

2) через ООП

вспомните про перегрузку методов

__mul__
__add__
"""

from collections import defaultdict
from functools import reduce



def hex_do():
    number = input('Введите два шеснадцатеричных числа через пробел: ')
    dct_number = defaultdict(int)
    dct_number['1'] = [i for i in number.split()[0]]
    dct_number['2'] = [i for i in number.split()[1]]
    summary = reduce(lambda x,y:int(''.join(x),16) + int(''.join(y),16),dct_number.values())
    multi = reduce(lambda x,y:int(''.join(x),16) * int(''.join(y),16),dct_number.values())
    print(f'Сумма чисел: {[i for i in format(summary, "X")]}')
    print(f'Произведение чисел: {[i for i in format(multi, "X")]}')

hex_do()


class Hex_Do():
    def __init__(self):
        self.numbers = input('Введите два шеснадцатеричных числа через пробел: ')
        self.dct = {'1': [i for i in self.numbers.split()[0]], '2': [i for i in self.numbers.split()[1]]}

    def dct_numbers(self):
        print(self.dct)

    def __mul__(self):
        multi = int(self.numbers.split()[0],16)*int(self.numbers.split()[1],16)
        return print(f'Произведение чисел: {[i for i in format(multi, "X")]}')

    def __add__(self):
        summary = int(self.numbers.split()[0],16)+int(self.numbers.split()[1],16)
        return print(f'Сумма чисел: {[i for i in format(summary, "X")]}')

C = Hex_Do()
C.dct_numbers()
C.__mul__()
C.__add__()