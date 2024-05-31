def get_sum(lst):
    if len(lst) == 1:
        return lst[0]
    return lst[0] + get_sum(lst[1:])

a = [1, 2 ,3]
get_sum(a)

#1 + 3 = L