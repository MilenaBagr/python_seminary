first_element = int(input('Введите первый элемент арифметической прогрессии: '))
difference = int(input('Введите разность: '))
limit_prog = int(input('Введите количество элементов: '))

def ArithmeticProgression(first_elem, dif, limit):
    list_progression = [first_elem]
    last_elem = list_progression[0]
    for i in range(limit-1):
        last_elem = last_elem + dif
        list_progression.append(last_elem)
    return list_progression

print(*ArithmeticProgression(first_element, difference, limit_prog))