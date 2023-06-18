# ВАРИАНТ 1
# list_num = [1,2,3,41,5,2,7,3,8,2]
# k = int(input('На какое количество элементов сдвинуть список: '))

# for i in range(k-1):
#     if i <= k:
#         list_num.insert(0, list_num.pop())
# print(list_num)


# ВАРИАНТ 2
# import random

# list_length = int(input('Сколько элементов в списке: '))
# k = int(input('На какое количество элементов сдвинуть список: '))

# list_numbers = []
# for i in range(list_length):
#     list_numbers.append(random.randint(0,6))

# print(list_numbers)

# for i in range(k):
#     list_numbers.insert(0, list_numbers.pop())
# print(list_numbers)

# ВАРИАНТ 3, самый оптимальный

list_numb = [1, 4, 2, 7, 4, 88, 32, 5, 1]
print(list_numb)

k = int(input('На какое количество элементов сдвинуть список: '))

list_numb = list_numb[-k:] + list_numb[:-k]
print(list_numb)