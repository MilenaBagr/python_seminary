def viewing_info(path):
    with open(path, 'r', encoding='UTF-8')  as file:
        data = file.readlines()
        return data
        

def adding_info(path):
    with open(path, 'a', encoding='UTF-8') as file:
        my_dict = dict()
        my_dict['Имя'] = input('Введите имя: ')
        my_dict['Фамилия'] = input('Введите фамилию: ')
        my_dict['Номер телефона'] = input('Введите номер телефона: ')
        for k, v in my_dict.items():
            file.write(f'{k}: {v}\n')
        file.write('\n')

def delete_book(path):
    open(path, 'w').close()


def change_info(path, data, line_number, new_line):
    with open(path, 'r+', encoding='UTF-8') as file:
        data[line_number-1] = new_line + "\n"
        file.seek(0)
        file.truncate()
        file.writelines(data)

def delete_info(path, line_numb):
    with open(path, 'r+', encoding='UTF-8') as file:
        data = file.readlines()
        del data[line_numb-1]
        file.seek(0)
        file.truncate()
        file.writelines(data)

def search_info(path, search_word: str):
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for line in data:
            if search_word.lower() in line.lower():
                return line
        return 0