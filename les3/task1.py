"""
Задание 1.

Реализуйте функции:

a) заполнение списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   заполнение словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени
"""
import time

def dec_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        time.sleep(1)
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Затраченное время: {end - start}')
        return result
    return wrapper

@dec_time
def lst_gen(k,n,lst=[]):
    for i in range(k,n):
        lst.append(i)
    return lst

@dec_time
def dct_gen(k,n,dct={}):
    for i in range(k,n):
        dct.setdefault(i,i)
    return dct


lst = lst_gen(0,10)
dct = dct_gen(0,10)
"""
b) получение элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   получение элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени
   
"""

@dec_time
def put_lst(a=2,b=0,c=0):
    lst = lst_gen(b,c,[])
    for i in range(len(lst)):
        if i == a:
            return print(lst[i])

put_lst(3,0,15)

@dec_time
def put_dct(a=2,b=0,c=0):
    dct = dct_gen(b,c,{})
    for i in dct.keys():
        if i == a:
            return print(dct[i])

put_dct(3,0,15)

"""
с) удаление элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   удаление элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени


ВНИМАНИЕ: в задании три пункта
НУЖНО выполнить каждый пункт
обязательно отделяя каждый пункт друг от друга

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""

@dec_time
def pop_lst(a=3,b=0,c=0):
    lst = lst_gen(b,c,[])
    for i in range(len(lst)):
        if i == a:
            return print(lst.pop(i)),print(lst)

pop_lst(3,0,15)

@dec_time
def pop_dct(a=3,b=0,c=0):
    dct = dct_gen(0,15,{})
    for i in dct.keys():
        if i == a:
            return print(dct.pop(i)),print(dct)

pop_dct(3,0,15)