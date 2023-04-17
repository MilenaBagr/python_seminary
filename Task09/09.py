number = int(input('Введите неотрицательное число: '))

i = 1
result = 1

while i <= number:
    result *= i
    i+=1

if number > 0:
    print(f'{number}! = {result}')
else:
    print('Введено отрицательное значение.')
