import view
import model


def start():
    phonebook = model.Phonebook()
    while True:
        view.display_menu()
        user_choice = input("Введите номер команды: ")
        if user_choice == '1':
            surname = input("Введите фамилию контакта: ")
            contact = phonebook.search_contact(surname)
            view.display_contact(contact)

        elif user_choice == '2':
            surname = input("Введите фамилию: ")
            phone_number = input("Введите номер телефона: ")
            phonebook.add_contact(surname, phone_number)
            view.display_message("Контакт добавлен")

        elif user_choice == '3':
            surname = input("Введите фамилию: ")
            phonebook.delete_contact(surname)
            view.display_message("Контакт удален")

        elif user_choice == '4':
            surname = input("Введите фамилию: ")
            new_phone_number = input("Введите новый номер телефона: ")
            phonebook.update_contact(surname, "phone_number", new_phone_number)
            view.display_message("Контакт изменен")

        elif user_choice == '5':
            contacts = phonebook.get_contacts()
            view.display_contacts(contacts)

        elif user_choice == '6':
            view.display_message("Спасибо, что воспользовались нашим сервисом!")
            break

        else:
            view.display_message("Ошибка, некорректный ввод")

# from view import *
# from model import *

# def start():
#     while True:
#         # В меню нужно вывести список команд "Выберите действия для телефонного справочника, 1 - найти контакт по фамилии, 
#         # 2 - добавить контакт, 3 - удалить контакт, 4 - изменить контакт, 5 - посмотреть все контакты, 6 -выход из программы"
#         view.display_menu()
#         users_choice = input('Введите номер команды: ')

#         if users_choice == '1':                             # 1 - найти контакт по фамилии
#             surname = input("Введите фамилию контакта: ") 
#             contact = model.search_contact(surname)         # найти контакт
#             view.display_contact(surname,contact)           # сделать print фамилии контакта и его номера

#         elif users_choice == '2':                          # 2 - добавить контакт
#             surname = input("Введите фамилию: ")
#             phone_number = input("Введите номер телефона: ")
#             model.add_contact(surname, phone_number)
#             view.display_message("Контакт добавлен")
        
#         elif users_choice == '3':                          # 2 -удалить контакт
            
#             surname = input("Введите фамилию: ")
#             model.delete_contact(surname)
#             view.display_message("Контакт удален")

#         elif users_choice == '4':                        # 4 - изменить контакт
#             surname = input("Введите фамилию: ")
#             new_phone_number = input("Введите номер телефона: ")
#             model.change_contact(surname, new_phone_number)
#             view.display_message("Контакт изменен")

#         elif users_choice == '5':                        # 5 -посмотреть все контакты
#             contacts = model.get_contacts()              # Предлагаю в модуле model сформировать список строк file.read().splitlines() 
#             view.display_contacts(contacts)              # Через цикл выводить каждую строку

#         elif users_choice == '6':
#             view.display_message("Спасибо, что воспользовались нашим сервисом!")
#             break
        
#         else:
#             view.display_message("Ошибка, некорректный ввод")                      

# def controller():
#     while True:
#         view.display_menu()
#         user_choice = input("Введите номер команды: ")
#         if user_choice == '1':
#             surname = input("Введите фамилию контакта: ")
#             contact = model.search_contact(surname)
#             view.display_contact(contact)

#         elif user_choice == '2':
#             surname = input("Введите фамилию: ")
#             phone_number = input("Введите номер телефона: ")
#             model.add_contact(surname, phone_number)
#             view.display_message("Контакт добавлен")

#         elif user_choice == '3':
#             surname = input("Введите фамилию: ")
#             model.delete_contact(surname)
#             view.display_message("Контакт удален")

#         elif user_choice == '4':
#             surname = input("Введите фамилию: ")
#             new_phone_number = input("Введите новый номер телефона: ")
#             model.update_contact(surname, 'phone_number', new_phone_number)
#             view.display_message("Контакт изменен")

#         elif user_choice == '5':
#             contacts = model.get_contacts()
#             view.display_contacts(contacts)

#         elif user_choice == '6':
#             view.display_message("Спасибо, что воспользовались нашим сервисом!")
#             break

#         else:
#             view.display_message("Ошибка, некорректный ввод")

 

# def start():
#     while True:
#         # В меню нужно вывести список команд "Выберите действия для телефонного справочника, 1 - найти контакт по фамилии, 
#         # 2 - добавить контакт, 3 - удалить контакт, 4 - изменить контакт, 5 - посмотреть все контакты, 6 -выход из программы"
#         view.display_menu()
#         users_choice = input('Введите номер команды: ')

#         if users_choice == '1':                             # 1 - найти контакт по фамилии
#             surname = input("Введите фамилию контакта: ") 
#             contact = model.search_contact(surname)         # найти контакт
#             view.display_contact(surname, contact)           # сделать print фамилии контакта и его номера

#         elif users_choice == '2':                          # 2 - добавить контакт
#             surname = input("Введите фамилию: ")
#             phone_number = input("Введите номер телефона: ")
#             model.add_contact(surname, phone_number)
#             view.display_message("Контакт добавлен")
        
#         elif users_choice == '3':                          # 2 -удалить контакт
            
#             surname = input("Введите фамилию: ")
#             model.delete_contact(surname)
#             view.display_message("Контакт удален")

#         elif users_choice == '4':                        # 4 - изменить контакт
#             surname = input("Введите фамилию: ")
#             new_phone_number = input("Введите номер телефона: ")
#             model.change_contact(surname, new_phone_number)
#             view.display_message("Контакт изменен")

#         elif users_choice == '5':                        # 5 -посмотреть все контакты
#             contacts = model.get_contacts()              # Предлагаю в модуле model сформировать список строк file.read().splitlines() 
#             view.display_contacts(contacts)              # Через цикл выводить каждую строку

#         elif users_choice == '6':
#             view.display_message("Спасибо, что воспользовались нашим сервисом!")
#             break
        
#         else:
#             view.display_message("Ошибка, некорректный ввод")    
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
   