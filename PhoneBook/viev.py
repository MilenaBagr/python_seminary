import text

def main_menu() -> int:
    print(text.main_menu)
    while True:
        choice = input(text.response_request)
        if choice.isdigit() and 0< int(choice) < 8:
            return int(choice)

def print_messange(messange: str):
    print('\n' + '=' * len(messange))
    print(messange)
    print('=' * len(messange) + '\n')

def print_contact(pb: list[dict[str,str]], error: str):
    if pb:
        print('\n' + '=' * 70)
        for i, contact in enumerate(pb, 1):
            print(f'{i:>3}. {contact.get("name"):<20} | {contact.get("phone"):<15} | {contact.get("comment"):<24}')
        print('=' * 71 + '\n')

    else:
        print_messange(error)


def input_contact(messange: str, cancel: str) -> dict | None:
    contact = {}
    print(messange)
    for key, value in text.input_contact.items():
        data = input(value)
        if data:
            contact[key] = data
        else:
            print_messange(cancel)
            break
 
    return contact


def input_index(messange: str, pb: list, error: str) -> int:
    print_contact(pb, error)
    while True:
        index = input(messange)
        if index :
            if index.isdigit() and 0 < int(index) < len(pb) + 1:
                return int(index)
        else:
            return 0
        

def search_contact_name():
    name = input(text.search_name)
    return name

