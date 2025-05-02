from memory_profiler import profile


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