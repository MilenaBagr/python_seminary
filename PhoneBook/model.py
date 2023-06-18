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

phone_book: list[dict[str, str]] = []
path = 'telephoneDirectory.txt'

def open_pb():
    global phone_book, path
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        contact = contact.strip().split(':')
        phone_book.append({'name':contact[0], 'phone':contact[1], 'comment':contact[2]})



def save_pb():
    global phone_book, path
    data = []
    for contact in phone_book:
        contact = ':'.join([value for value in contact.values()])
        data.append(contact)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write('\n'.join(data))



def get_pb() -> list[dict[str, str]]:
    global phone_book
    return phone_book



def add_contact(contact: dict[str, str]):
    global phone_book
    phone_book.append(contact)
    return contact.get('name')
    
def del_contact(index: int):
    return phone_book.pop(index-1).get('name')

def search_contact(name: str, contact: list[dict[str, str]]):
    search_cont = []
    for cont in contact:
        if name.upper() in cont.get('name').upper():
            search_cont.append(cont) 
    return search_cont
