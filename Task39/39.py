import random

size_1 = int(input('Введите размер первого массива: '))
size_2 = int(input('Введите размер второго массива: '))

list_1 = [random.randint(1, 15) for i in range(size_1)]
list_2 = [random.randint(1, 15) for i in range(size_2)]

def ElementsFirstList(list1, list2):
    # arr = list()
    # for i in range(len(list1)):
    #         if list1[i] not in list2:
    #               arr.append(list1[i])
    # Всё мною выше написанное одной строкой: комплихейшен
    arr = [i for i in list1 if i not in list2]
    return arr

print(list_1)
print(list_2)
print(ElementsFirstList(list_1, list_2))
