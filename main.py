from controller import start

if __name__ == '__main__':
    start()
    # file = 'Phonebook.txt'
    
    # start()
# from controller import controller
# from view import *
# from model import *

# from view import *
# from model import *

# def main():
#     phonebook = PhoneBook('contacts.txt')
#     controller(phonebook)

# if __name__ == '__main__':
#     main()

# import view
# import model


# def start():
#     contacts = []
#     while True:
#         view.display_menu()
#         user_choice = input("Введите номер команды: ")
#         if user_choice == '1':
#             surname = input("Введите фамилию контакта: ")
#             phone_number = model.search_contact(contacts, surname)
#             view.display_contact(phone_number)

#         elif user_choice == '2':
#             surname = input("Введите фамилию: ")
#             phone_number = input("Введите номер телефона: ")
#             model.add_contact(contacts, surname, phone_number)
#             view.display_message("Контакт добавлен")

#         elif user_choice == '3':
#             surname = input("Введите фамилию: ")
#             model.delete_contact(contacts, surname)
#             view.display_message("Контакт удален")

#         elif user_choice == '4':
#             surname = input("Введите фамилию: ")
#             new_phone_number = input("Введите новый номер телефона: ")
#             model.update_contact(contacts, surname, "phone_number", new_phone_number)
#             view.display_message("Контакт изменен")

#         elif user_choice == '5':
#             contacts_list = model.get_contacts(contacts)
#             view.display_contacts(contacts_list)

#         elif user_choice == '6':
#             view.display_message("Спасибо, что воспользовались нашим сервисом!")
#             break

#         else:
#             view.display_message("Ошибка, некорректный ввод")

# start()

