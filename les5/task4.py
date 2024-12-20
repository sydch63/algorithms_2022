"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from timeit import timeit
from collections import OrderedDict


keys = [1,2,3,4,5,6,7,8]
value = ['a','b','c','d','e','f','g','i']

dct = {}
ord_dct = OrderedDict()

def plus_dct():
    for i in keys:
        dct[i]=value[keys.index(i)]

def plus_ord_dct():
    for i in keys:
        ord_dct[i]=value[keys.index(i)]

print('Первый add dct: ',timeit('plus_dct()',globals=globals(),number=1000))
print('Первый add ord dct: ',timeit('plus_ord_dct()',globals=globals(),number=1000))

def dct_items():
    dct.items()

def items_ord_dct():
    ord_dct.items()

print()
print('Первый items dct: ',timeit('dct_items()',globals=globals(),number=1000))
print('Первый items ord dct: ',timeit('items_ord_dct()',globals=globals(),number=1000))


def dct_keys():
    dct.keys()

def keys_ord_dct():
    ord_dct.keys()

print()
print('Первый keys dct: ',timeit('dct_keys()',globals=globals(),number=1000))
print('Первый keys ord dct: ',timeit('keys_ord_dct()',globals=globals(),number=1000))

