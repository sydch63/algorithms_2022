"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее

2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее

3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""

####1####

from timeit import timeit
from collections import deque

lst = [1,3,51,46236,12,325,6,1,26343,646453]
dq = deque([1,3,51,46236,12,325,6,1,26343,646453])

def pop_lst():
    count = len(lst)
    while count != 0:
        lst.pop()
        count -= 1

def pop_deque():
    count = len(dq)
    while count != 0:
        dq.pop()
        count -= 1

print('Первый замер pop lst: ',timeit('pop_lst()',globals=globals(),number=1000))
print('Первый замер pop deque: ',timeit('pop_deque()',globals=globals(),number=1000))

# +- Чуть быстрее list


def append_lst():
    example = [1,2,3,5,1,12,325,56,1]
    for i in example:
        lst.append(i)

def append_deque():
    example = [1,2,3,5,1,12,325,56,1]
    for i in example:
        dq.append(i)

print('Первый замер append lst: ',timeit('append_lst()',globals=globals(),number=1000))
print('Первый замер append deque: ',timeit('append_deque()',globals=globals(),number=1000))

# +- Чуть быстрее deque


lst_ex = [228,322]

def extend_lst():
    example = [1,2,3,5,1,12,325,56,1]
    example.extend(lst_ex)

def append_deque():
    example = [1,2,3,5,1,12,325,56,1]
    example.extend(lst_ex)

print('Первый замер extend lst: ',timeit('extend_lst()',globals=globals(),number=1000))
print('Первый замер extend deque: ',timeit('append_deque()',globals=globals(),number=1000))

# +- Чуть быстрее deque


####2####

#2) сравнить операции
#appendleft, popleft, extendleft дека и соответствующих им операций списка
#и сделать выводы что и где быстрее


def appendleft_lst():
    example = [1,2,3,5,1,12,325,56,1]
    for i in example:
        lst.insert(0,i)


def appendleft_deque():
    example = [1,2,3,5,1,12,325,56,1]
    for i in example:
        dq.appendleft(i)

print('Первый замер append left lst: ',timeit('appendleft_lst()',globals=globals(),number=1000))
print('Первый замер appendleft deque: ',timeit('appendleft_deque()',globals=globals(),number=1000))

#Сильно быстрее у deque

def popleft_lst():
    example = [1,2,3,5,1,12,325,56,1]
    lst.pop(0)

def popleft_deque():
    example = [1,2,3,5,1,12,325,56,1]
    dq.popleft()

print('Первый замер pop left lst: ',timeit('popleft_lst()',globals=globals(),number=1000))
print('Первый замер popleft deque: ',timeit('popleft_deque()',globals=globals(),number=1000))

#Сильно быстрее у deque

def extendleft_lst():
    example = [1,2,3,5,1,12,325,56,1]
    result = example + lst

def extendleft_deque():
    example = [1,2,3,5,1,12,325,56,1]
    dq.extendleft(example)

print('Первый замер extend left lst: ',timeit('extendleft_lst()',globals=globals(),number=1000))
print('Первый замер extendleft deque: ',timeit('extendleft_deque()',globals=globals(),number=1000))

#Сильно быстрее у deque

####3####

#3) сравнить операции получения элемента списка и дека
#и сделать выводы что и где быстрее

def take_lst():
    example = [1,2,3,5,1,12,325,56,1]
    lst[0]

def take_deque():
    example = [1,2,3,5,1,12,325,56,1]
    dq[0]

print('Первый замер take lst: ',timeit('take_lst()',globals=globals(),number=1000))
print('Первый замер take deque: ',timeit('take_deque()',globals=globals(),number=1000))

#Заметно дольше