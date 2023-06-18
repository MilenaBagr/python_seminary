array = [1, 1, 2, 0, -1, 3, 4, 4, 11, 3, 9, 5, 5, 7, 4]

# ВАРИАНТ 1

# list_unic_numbers = set(array)
# print(array)
# # print(list_unic_numbers)
# print(len(list_unic_numbers))

# ВАРИАНТ 2

# print(len(set(array)))

# ВАРИАНТ 3

list_n = list(input('Введите числа: '))

unic_list = []

for item in list_n:
    if not item in unic_list:
        unic_list.append(item)

print(list_n)
print(len(unic_list))