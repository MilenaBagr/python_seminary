from random import *

def Same_by(characteristic, objects : list):
    my_set = set(map(characteristic, objects))
    return len(my_set) == 1 or len(my_set) == 0

num = int(input('Введите длину списка: '))
my_list =[randint(1, 10) for i in range(num)]
print(my_list) 
print(Same_by(lambda x: x%2==0, my_list))
