import random

min_range = int(input('Введите минимум диапазона: '))
max_range = int(input('Введите максимум диапазона: '))

def CreateList(min_, max_, count):
    my_list = [random.randint(min_, max_) for i in range(count)]
    return my_list

def SearchElementinRange(min_r, max_r, my_list = list):
    for i in range(len(my_list)):
        if min_r<=my_list[i]<=max_r:
            print(i, end = ' ')

list_my = CreateList(1, 500, 20)
print(list_my)
print('Индексы элементов списка, значения которых принадлежат заданному диапазону:')
SearchElementinRange(min_range, max_range, list_my)