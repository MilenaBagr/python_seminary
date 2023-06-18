# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
#    записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# 1. Открыть файл.
# 2. Сохранить файл.
# 3. Пoказать телефонную книжку
# 4. Добавить контакт
# 5. Найти контакт.
# 6. Изменить контакт.
# 7. Удалить контакт
# 8. Выход

import os
from def_file import *

path = 'telephoneDirectory.txt'
clear = lambda: os.system('cls')
lines = viewing_info(path)
flag = True

print('Добро пожаловать в Ваш телефонный справочник!\n')

while flag:

    answer = int(input('Что вы хотите сделать?\n\n'
          '1. Добавить контакт.\n'
          '2. Изменить контакт.\n'
          '3. Удалить контакт.\n'
          '4. Поиск контакта.\n'
          '5. Вывести список всех контактов.\n'
          '6. Очистить телефонную книгу.\n'
          '7. Выйти.\n\n'
          'Выберите нужный пункт: '))
    
    if answer>7 or answer<1:
        clear()
        print('\nВведена неверная команда.\n')

    elif answer == 7:
        flag = False
  
    elif answer == 1:
        clear()
        adding_info(path)
        clear()
        print('\nКонтакт добавлен!\n')

    elif answer == 2:
        clear()
        for line in lines:
            print(line)

        line_numb = int(input('Какую строку вы хотите изменить?\nВведите номер строки: '))
        clear()
        print(f'Изменить строку:\n{lines[line_numb-1]}')
        print('Введите новую строку:')
        if 'Имя' in lines[line_numb-1]:
            new_line = 'Имя: ' + input('Имя: ')
        elif 'Фамилия' in lines[line_numb-1]:
            new_line = 'Фамилия: ' + input('Фамилия: ')
        elif 'Номер' in lines[line_numb-1]:
            new_line = 'Номер телефона: ' + input('Номер телефона: ')
        
        change_info(path, lines, line_numb, new_line)
        clear()
        print('Строка успешно изменена!')

    elif answer == 3:
        clear()
        line_number = int(input('Какую строку вы хотите удалить?\nВведите номер строки: '))
        delete_info(path, line_number)
        print('Строка успешно удалена!')

    elif answer == 4:
        clear()
        word = input('Введите слово для поиска: ')
        search_result = search_info(path, word)
        if search_result != 0:
            print('По Вашему запросу найдено: ')
            print(search_result)
        else:
            print('По Вашему запросу ничего не найдено.')

    elif answer == 5:
        clear()
        contacts = viewing_info(path)

        if len(contacts) < 1:
            print('Телефонная книга пуста.\n')
        else:
            print('\nВсе Ваши контакты: \n')
            for line in contacts:
                print(line, end='\n')

    elif answer == 6:
        clear()
        delete = int(input('Вы действительно хотите очистить Вашу телефонную книгу?\n'
                           '1. Очистить.\n'
                           '2. Отмена.\n'
                           'Выберите нужный пункт: '))
        if 1>delete>2:
            clear()
            print('Введена неверная команда.')

        elif delete == 1:
            clear()
            my_list_cont = ()
            delete_book(path)
            print('Телефонная книга очищена.\n')

        else:
            clear()

