from memory_profiler import profile

import hashlib

st = 'papa'
result = set()
check = 0

res = list()
res_set = set()


for i in range(len(st)):
        for j in range(i + 1, len(st) + 1):
            unic = st[i:j]
            if unic != st:
                hash_oj = hashlib.md5(bytes(unic,'utf-8')).hexdigest()
                res_set.add(hash_oj)
