number = int(input('Введите трехзначное число: '))
result = 0
if number > 99 and number < 1000:
    while number>0:
        result += number%10
        number //=10
    print(f'Сумма цифр трехзначного числа: {result}')
else:
    print('Введено не трехзначное число.')