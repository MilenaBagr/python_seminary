fibonacci = int(input('Введите число фибоначчи: '))

number1 = 0
number2 = 1
k = 2

while number2 < fibonacci:
    number1, number2 = number2, number2+number1
    k+=1
if number2 == fibonacci:
    print(f'Число {fibonacci} имеет индекс {k}.')
else:
    print(-1)


