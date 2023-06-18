my_string = '10'
print(my_string)

def Revers(my_list):
    if len(my_list) < 2:
        return my_list
    return my_list[-1] + Revers(my_list[:-1])

print(Revers(my_string))