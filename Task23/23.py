list_numbers = [1, 52, 3, 27, 2, 29, 0, 2, 10, 2, 0]
count = 0
for i in range(len(list_numbers)-1):
    if list_numbers[i] < list_numbers[i+1]:
        count +=1
print(list_numbers)
print(count)