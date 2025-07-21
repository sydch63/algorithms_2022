"""
Задание 1.

Реализуйте кодирование строки по алгоритму Хаффмана.
У вас два пути:
1) тема идет тяжело? тогда вы можете,
опираясь на примеры с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных,
выбор других коллекций, различные изменения
и оптимизации.

2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например,
через ООП или предложить иной подход к решению.
"""

from collections import Counter



"""
tree - {
0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 
1: {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}
}
"""

s = "beep boop beer!"

str_clt = Counter(s).items()
srt_lst = sorted(str_clt,key=lambda i: i[1])

tree = {}
tmp_lst = []

while len(srt_lst) != 1:
    tpl1 = srt_lst[0]
    tpl2 = srt_lst[1]
    if tpl1[len(tpl1)-1] <= tpl2[len(tpl2)-1]:
        srt_lst.pop(srt_lst.index(tpl1))
        srt_lst.pop(srt_lst.index(tpl2))
        comb = {0:tpl1[0],
                1:tpl2[0]}
        tpl_new1 = (comb,tpl1[len(tpl1)-1] + tpl2[len(tpl2)-1])
        srt_lst.insert(0, (tpl_new1))
    elif tpl1[len(tpl1)-1] >= tpl2[len(tpl2)-1]:
        srt_lst.pop(srt_lst.index(tpl1))
        for i in srt_lst:
            if tpl1[len(tpl1)-1] <= i[len(i)-1]:
                srt_lst.insert(srt_lst.index(i), tpl1)
                break
            elif tpl1[len(tpl1)-1] >= i[len(i)-1]:
                if srt_lst.index(i) == (len(srt_lst)-1):
                    srt_lst.append(tpl1)
                    break