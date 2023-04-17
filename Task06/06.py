numb = int(input('Введите шестизначный номерок вашего билета: '))
if 1000000 > numb > 99999:
    sum_first_three_numb = 0
    sum_last_three_numb = 0
    temp = numb//1000
    while temp > 0:
        sum_first_three_numb += temp%10
        temp //= 10
    while numb > 999:
        sum_last_three_numb += numb%10
        numb //= 10
    if sum_first_three_numb == sum_last_three_numb:
        print('Ура! Поздравляем, у Вас счастливый билетик!')
    else:
        print('Увы, повезет в следующий раз :(')
else:
    print('Введен не шестизначный номерок.')