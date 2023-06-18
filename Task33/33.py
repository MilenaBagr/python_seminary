import random
number = 19
evaluations = [random.randint(1, 5) for _ in range(number)]
print(evaluations)

# # а-ля тренировка, расписываю все сама без встроенные функций min м max, знаю об их существовании, если что
# def ReplacMaxWithTheMin(my_list):
#     min_num = my_list[0] 
#     max_num = my_list[0]
#     for i in range(len(my_list)):
#         if my_list[i] < min_num:
#             min_num = my_list[i]
#         elif my_list[i] > max_num:
#             max_num = my_list[i]

#     for i in range(len(my_list)):
#         if my_list[i] == max_num:
#             my_list[i] = min_num
#     return my_list

# ReplacMaxWithTheMin(evaluations)
# print(evaluations)

# Второй вариант в одну строку: чери чери леди, гоинг троуз эмоушен, лов ис ве ю файнд ит, лисен ту ю хар
evaluations = [min(evaluations) if i == max(evaluations) else i for i in evaluations]
print(evaluations)