import random

n = int(input('Сколько всего кустов на вашей грядке: '))
arr = [random.randint(10, 20) for i in range(n)]
i = 1
for item in arr:
    print(f'На {i} грядке {item} черник')
    i += 1

arr_count = list()
for i in range(len(arr) - 1):
    arr_count.append(arr[i-1] + arr[i] +arr[i+1])
arr_count.append(arr[-2] + arr[-1] + arr[0])
print(f'Максимальное число ягод, которое можно собрать за один заход --> {max(arr_count)}')