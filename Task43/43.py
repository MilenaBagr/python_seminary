import random

size = int(input('Введите разммер списка: '))

print(my_list := [random.randint(1, 5) for _ in range(size)])

def UniqPairs(list_1: list):
    count_pairs = sum([list_1.count(i)//2 for i in set(list_1)])
    return count_pairs

print(UniqPairs(my_list))