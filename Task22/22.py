import random

first_numbers = int(input('Введите какого размера будет первый набор целых чисел: '))
second_numbers = int(input('Введите какого размера будет второй набор целых чисел: '))

random_list1 = [random.randint(1, 20) for _ in range(first_numbers)]
random_list2 = [random.randint(1, 20) for _ in range(second_numbers)]

print(random_list1)
print(random_list2)

result = list((set(random_list1).intersection(set(random_list2))))
result.sort()
print(*result)