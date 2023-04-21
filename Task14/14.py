number = int(input('Введите положительное число: '))

result =  2
degree = 2

print(f'Все целые степени двойки, не превосзодящие {number}:')
while result < number:
    print(result, end = ' ')
    result *= degree