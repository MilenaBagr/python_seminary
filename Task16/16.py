import random

size = int(input('Какой длины будет наш массив: '))
number = int(input('Введите натуральное число: '))
random_list = [random.randint(1, 5) for _ in range(size)]
count = 0

count = random_list.count(number)

print(random_list)
print(f'Число {number} встречается в списке {count} раз.')