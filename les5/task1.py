"""
Задание 1.

Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего

Подсказка:
Для решения задачи обязательно примените коллекцию из модуля collections
Для лучшего освоения материала можете сделать
несколько варианто решения этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235      346159

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34          956

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога
Предприятия, с прибылью ниже среднего значения: Копыта
"""

from collections import ChainMap,defaultdict,Counter


dct_company = defaultdict(int)
average_profit = 0
profit_high = []
profit_low = []

count = int(input('Введите количество предприятий для расчета прибыли: '))

while count != 0:
    name_company = input('Введите название предприятия: ')
    profit_company = input('Введите через пробел, прибыль данного предприятия за каждый квартал(Всего 4 квартала):')
    dct_company[name_company] = {'profit':[int(i) for i in profit_company.split()]} #прибыль по кварталам в виде списка, значения инт
    dct_company[name_company].update({'summary_profit':sum(dct_company[name_company]['profit'])}) #суммарная прибыль за все кварталы
    #all_profit = Counter(sum(dct_company[name_company]['profit']))
    average_profit += dct_company[name_company]['summary_profit']
    count -= 1

average_profit_year = average_profit/len(dct_company)

for company in dct_company.keys():
    if average_profit_year < dct_company[company]['summary_profit']:
        profit_high.append(company)
    else:
        profit_low.append(company)


print()
print(f'Средняя годовая прибыль всех предприятий: {average_profit_year}')
print(f"Предприятия, с прибылью выше среднего значения:", *profit_high,sep=" ")
print(f"Предприятия, с прибылью ниже среднего значения:", *profit_low,sep=" ")



    