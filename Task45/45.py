number = int(input('Введите число:'))

def Summarize(number, sum = 0):
    for i in range(1, number//2+1):
        if number% i ==0:
            sum += i
    return sum

def FriendlyNumber(num):
    for i in range(num):
        if i == Summarize(Summarize(i)) and i != Summarize(i):
            print(i, Summarize(i))    

print(FriendlyNumber(number))