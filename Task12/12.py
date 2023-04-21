import os
sum = int(input('Введите сумму двух натуральных чисел, которые вы загадали: '))
multiplicate = int(input('Введите произведение этих же чисел: '))

for i in range(multiplicate):
    for j in range(sum):
        if sum == i+j and multiplicate == i*j:
            os.system('cls')
            print(i,j)
    
