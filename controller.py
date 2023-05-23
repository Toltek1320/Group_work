from view import *
from model import *

def controller():
    while True:
        # В меню нужно вывести список команд "Выберите действия для телефонного справочника, 1 - найти контакт по фамилии, 
        # 2 - добавить контакт, 3 - удалить контакт, 4 - изменить контакт, 5 - посмотреть все контакты, 6 -выход из программы"
        view.display_menu()
        users_choice = input('Введите номер команды: ')

        if users_choice == '1':                             # 1 - найти контакт по фамилии
            surname = input("Введите фамилию контакта: ") 
            contact = model.search_contact(surname)         # найти контакт
            view.display_contact(surname,contact)           # сделать print фамилии контакта и его номера

        elif users_choice == '2':                          # 2 - добавить контакт
            surname = input("Введите фамилию: ")
            phone_number = input("Введите номер телефона: ")
            model.add_contact(surname, phone_number)
            view.display_message("Контакт добавлен")
        
        elif users_choice == '3':                          # 2 -удалить контакт
            
            surname = input("Введите фамилию: ")
            model.delete_contact(surname)
            view.display_message("Контакт удален")

        elif users_choice == '4':                        # 4 - изменить контакт
            surname = input("Введите фамилию: ")
            new_phone_number = input("Введите номер телефона: ")
            model.change_contact(surname, new_phone_number)
            view.display_message("Контакт изменен")

        elif users_choice == '5':                        # 5 -посмотреть все контакты
            contacts = model.get_contacts()              # Предлагаю в модуле model сформировать список строк file.read().splitlines() 
            view.display_contacts(contacts)              # Через цикл выводить каждую строку

        elif users_choice == '6':
            view.display_message("Спасибо, что воспользовались нашим сервисом!")
            break
        
        else:
            view.display_message("Ошибка, некорректный ввод")                      