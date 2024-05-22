"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""

lst1 = [10,2,3,4,5,6,9,1]
lst2 = [0,4,5,1,2,5]
lst3 = [126,4,10,2,15]
lst4 = [0,4,10,2,1500,3,-2,5]

def min_lst1(lst):
    minimum_lst = []
    for n in lst:
        for i in lst:
            if n > i:
                minimum_lst.append(i)
                if minimum_lst[0] > i:
                    minimum_lst[0] = i
    return print(minimum_lst[0])

min_lst1(lst1)
min_lst1(lst2)
min_lst1(lst3)
min_lst1(lst4)



# lst1 = [10,2,3,4,5,6,9,1]
# lst2 = [0,4,5,1,2,5]
# lst3 = [126,4,10,2,15]
#
# """
# №2
# перебор на +1 в списке меняя значение если оно меньше
# """
#
def mini_lst(lst):
    minimum_lst = []
    for n in lst:
        minimum_lst.append(n)
        if n < minimum_lst[0]: 
            minimum_lst[0] = n
    return print(minimum_lst[0])

mini_lst(lst1)
mini_lst(lst2)
mini_lst(lst3)
mini_lst(lst4)