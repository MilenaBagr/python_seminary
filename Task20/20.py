scrabble = {'AEIOULNSTRАВЕИНОРСТ': 1,
            'DGДКЛМПУ': 2, 
            'BCMPБГЁЬЯ': 3,
            'FHVWYЙЫ': 4,
            'KЖЗХЦЧ': 5,
            'JXШЭЮ': 8,
            'QZФЩЪ': 10 }

word = input('Введите слово: ')

total = 0

for letter in word.upper():
    for letters in scrabble.keys():
        if letter in letters:
            total += scrabble.get(letters)
            break
print(total)


# Второй вариант решения

# my_dict = {}
# my_dict.update(my_dict.fromkeys('AEIOULNSTRАВЕИНОРСТ', 1))
# my_dict.update(my_dict.fromkeys('DGДКЛМПУ', 2))
# my_dict.update(my_dict.fromkeys('BCMPБГЁЬЯ', 3))
# my_dict.update(my_dict.fromkeys('FHVWYЙЫ', 4))
# my_dict.update(my_dict.fromkeys('KЖЗХЦЧ', 5))
# my_dict.update(my_dict.fromkeys('JXШЭЮ', 8))
# my_dict.update(my_dict.fromkeys('QZФЩЪ', 10))

# word = input('Введите слово: ') 
# total = 0

# for letter in word.upper():
#     total += my_dict.get(letter)
# print(total)