from memory_profiler import memory_usage
from pympler import asizeof
from numpy import array

data = [15 * 3,15 / 3,15 // 2,15 ** 2]

for i in data:
    print(type(i),"Полученный тип целое число: ",isinstance(i,int))

print(asizeof.asizeof(data))#240


data = array([15 * 3,15 / 3,15 // 2,15 ** 2])

for i in data:
    print(type(i),"Полученный тип целое число: ",isinstance(i,int))

print(asizeof.asizeof(data))#152
