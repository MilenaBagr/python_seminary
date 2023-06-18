string_user = list(input('Введите слово: '))

count_dict = {}

for letter in string_user:
    count_dict[letter] = count_dict.get(letter, 0) + 1
    print(f'{letter}' if count_dict.get(letter) < 2 else f'{letter}_{count_dict.get(letter) -1}', end ='')
