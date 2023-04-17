length = int(input('Введите количество долек шоколадки в длину: '))
width = int(input('Введите количество долек шоколадки в ширину: '))
break_off = int(input('Сколько долек вы хотите отломать: '))

b = False

if break_off > length*width:
    print('В вашей шоколадке нет столько долек :(')
else:
    if break_off > length:
        if break_off % length == 0 or break_off % width == 0:
            b = True
    else:
        if length == break_off or break_off % width == 0:
            b = True
    print(f'{length} {width} {break_off} --> {b}')
