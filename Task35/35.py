def CheckingPrimeNumber(num):
    count = 0
    for i in range(1, (num+1)):
        if num % i == 0:
            count += 1
    if count <= 2 :
        return 1
    return 0

number = int(input('Enter a number to check for a prime: '))
result = CheckingPrimeNumber(number)
print(f'{number} --> ' + ('Yes, this is a prime number.' if result else "No, it's not a prime number."))

# Второй вариант решения, хороший, оптимизированный:

def is_simple(num: int) -> bool:
    if num in [1, 2]:
        return True
    elif not num % 2:
        return False
    else:
        for i in range(3, num//2 +1, 2):
            if num % i == 0:
                return False
    return True

result_2 = is_simple(number)
print(f'{number} --> ' + ('Yes, this is a prime number.' if result_2 else "No, it's not a prime number."))
