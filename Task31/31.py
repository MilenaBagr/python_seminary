def fib(num):
    if num == 1 or num == 0:
        return 1
    return fib(num - 2) + fib(num-1)
fibonacci = fib(20)
print(fibonacci)