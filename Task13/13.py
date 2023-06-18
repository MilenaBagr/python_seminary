import random

length = 30
count = 0
max_count = 0
day = 0

for i in range(length):
    day += random.randint(-3,3)
    print(day, end = ' ')
    if day > 0:
        count += 1
        if count > max_count:
            max_count = count
    else:
        count = 0
print(f'\nМаксимальное число теплых дней подряд {max_count}.')

