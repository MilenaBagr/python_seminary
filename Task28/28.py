def Sum(num_a, num_b):
    if num_b == 0:
        return num_a
    elif num_a == 0:
        return num_b
    return num_a + Sum(1, num_b-1)

print(Sum(213, 211))