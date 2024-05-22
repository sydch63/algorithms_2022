"""
Задание 5. На закрепление навыков работы со стеком

Реализуйте собственный класс-структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стопок.
Создание новой стопки происходит при достижении предыдущим
стеком порогового значения.

После реализации структуры, проверьте ее работу на различных сценариях.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание новой стопки можно реализовать добавлением нового пустого массива
в массив стопок (lst = [[], [], [], [],....]).
"""

class StackPlates:
    def __init__(self):
        self.stacks = []

    def is_empty(self):
        return self.stacks == []

    def push_in(self,plate):
        if self.stacks == []:
            self.stacks.append([])
        for lst in self.stacks:
            if lst == []:
                lst.append(plate)
            elif lst != [] and len(lst) != 4:
                lst.append(plate)
                if len(lst) == 4:
                    self.stacks.append([])
                    break

    def pop_out(self):
        if self.stacks == []:
            print('Стопка пуста')
        else:
            if self.stacks[len(self.stacks) -1] == []:
                self.stacks.remove([])
                return self.stacks[len(self.stacks) - 1].pop()
            else:
                return self.stacks[len(self.stacks) - 1].pop()


    def get_val(self):
        return self.stacks[len(self.stacks) -1][::-1][0]

    def stack_size(self):
        return len(self.stacks[len(self.stacks) -1])

if __name__ == '__main__':

    SP = StackPlates()
    print(SP.is_empty())
    SP.push_in('1')
    SP.push_in('2')
    SP.push_in('1')
    SP.push_in('2')
    SP.push_in('1')
    SP.push_in('2')
    SP.push_in('4')
    SP.push_in('3')
    SP.push_in('6')
    SP.push_in('9')
    print(SP.stacks)