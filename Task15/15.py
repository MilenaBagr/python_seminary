import random

watermelon = int(input('Введите количество арбузов: '))

MAX_WEIGTH = 30000
MIN_WEIGTH = 1000

weigth = 0
max_weigth = MIN_WEIGTH
min_weigth = MAX_WEIGTH

for i in range(watermelon):
    weigth = random.randint(MIN_WEIGTH, MAX_WEIGTH)
    print(weigth, end = ' ')
    if weigth > max_weigth:
        max_weigth = weigth
    elif weigth< min_weigth:
        min_weigth = weigth
print(f'\nАрбуз для себя получился на {max_weigth} г, а для тещи {min_weigth} г.')