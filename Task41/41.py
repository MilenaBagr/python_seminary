import random

size = int(input('Введите размер списка: '))
list_1 = [random.randint(1,10) for i in range(size)]

def CountNumberNeighborsSmallerSize(list1):
    # count = 0
    # for i in range(1, len(list1)-1):
    #     if list1[i-1] < list1[i] and list1[i+1] < list1[i]:
    #         count += 1

    # То же самое, что я описала выше, только в одну строку: 

    count = [1 for i in range(1, len(list1)-1) if list1[i-1] < list1[i] > list1[i+1]]
    return len(count)

print(list_1)
print(CountNumberNeighborsSmallerSize(list_1))