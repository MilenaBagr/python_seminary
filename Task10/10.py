import random

number = int(input('Сколько монеток лежат на столе: '))



eagle = 0
tails = 0

for i in range(number):
    coin = random.randint(0,1)
    print(coin, end = ' ')
    if coin == 1:
        eagle+=1
    else:
        tails+=1
if eagle < tails:
    print(f'\nМинимальное количество монеток, которые нужно перевернуть, чтоб все монетки были повернуты вверх одной и той же стороной --> {eagle}')
else:
    print(f'\nМинимальное количество монеток, которые нужно перевернуть, чтоб все монетки были повернуты вверх одной и той же стороной --> {tails}')
