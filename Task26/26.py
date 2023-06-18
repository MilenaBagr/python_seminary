def WholeDegree(num_a, num_b) -> int:
    if num_b == 1:
        return num_a
    return num_a * (WholeDegree(num_a, num_b-1))

number_a = int(input('Введите число: '))
number_b = int(input('В какую степень возвести: '))

print(WholeDegree(number_a, number_b))
