my_list = [1, 3, 7, 4, 7, 3, 5, 3, 5, 7, 2, 9]

transformation = lambda x: x

transformed_my_list = list(map(transformation, my_list))
my_list[2] = 126

print(transformed_my_list)
print(my_list)
