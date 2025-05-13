from memory_profiler import profile
from memory_profiler import memory_usage

def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff
    return wrapper


@profile
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

nums = [i for i in range(100000)]

func_1(nums)

@profile
def func_2(nums):
    new_arr = [i for i in nums if i%2 ==0 ]
    return new_arr

nums = [i for i in range(100000)]

func_2(nums)



@decor
def func_3(nums):
    for num in nums:
        if num % 2 == 0:
            yield num

nums = [i for i in range(100000)]

lst = []
gen,mem_diff = func_3(list(range(100000)))
for n in gen:
    lst.append(n)
print(f"Выполнение заняло {mem_diff} Mib")