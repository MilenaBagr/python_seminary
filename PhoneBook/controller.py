import text
import viev
import model


def start():
    while True:
        choice = viev.main_menu()
        match choice:
            case 1:
                model.open_pb()
                viev.print_messange(text.load_successful)
            case 2:
                model.save_pb()
                viev.print_messange(text.save_successful)
            case 3:
                pb = model.get_pb()
                viev.print_contact(pb, text.load_error)
            case 4:
                contact = viev.input_contact(text.new_contact, text.input_error)
                if contact:
                    name = model.add_contact(contact)
                    viev.print_messange(text.new_contact_succesful(name))
            case 5:
                name = viev.search_contact_name()
                pb = model.get_pb()
                search = model.search_contact(name, pb)

                viev.print_contact(search, text.error_search_name(name))
            case 6:
                pb = model.get_pb()
                index = viev.input_index(text.index_del_contact, pb, text.load_error)
                if index != 0:
                    name = model.del_contact(index)
                    viev.print_messange(text.del_contact(name))
                else:
                    viev.print_messange(text.input_error)
            case 7:
                break