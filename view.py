def display_menu():
    print("выберите действия для телефонного справочника:", 
          "1 - найти контакт по фамилии", 
          "2 - добавить контакт", 
          "3 - удалить контакт", 
          "4 - изменить контакт", 
          "5 - посмотреть все контакты", 
          "6 - выход из программы", sep="\n")

def display_contact(contact):
    if isinstance(contact, str):
        print(contact)
    else:
        print(f"Фамилия: {contact.surname}")
        print(f"Номер телефона: {contact.phone_number}")

def display_contacts(contacts):
    if not contacts:
        print("Список контактов пуст")
    else:
        print("Контакты:")
        for contact in contacts:
            display_contact(contact)
            print()

def display_message(message):
    print(message)

# def display_menu():
#     print("выберите действия для телефонного справочника:", 
#           "1 - найти контакт по фамилии", 
#           "2 - добавить контакт", 
#           "3 - удалить контакт", 
#           "4 - изменить контакт", 
#           "5 - посмотреть все контакты", 
#           "6 - выход из программы", sep="\n")

# def display_contact(name, phone_number):
#     if phone_number is None:
#         print(f"Контакт {name} не найден")
#     else:
#         print(f"Фамилия: {name}, номер телефона: {phone_number}")

# def display_message(message):
#     print(message)

# def display_contacts(contacts):
#     if not contacts:
#         print("Телефонная книга пуста")
#     else:
#         for contact in contacts:
#             print(contact)