import random

size = int(input('Какой длины будет наш массив: '))
number = int(input('Введите натуральное число: '))
random_list = [random.randint(1, 15) for _ in range(size)]

print(random_list)

count = random_list.count(number)
min_difference = random_list[0]

for item in random_list:
    if abs(number - item) < abs(number - min_difference):
        min_difference = item

print(f'Число {number} встречается в списке {count} раз.' if count != 0 else f'Число {number} не встречается в списке, однако самый близкий по величине элемент --> {min_difference}')