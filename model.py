# нужно написать функции:
# - search_contact
# - add_contact
# - delete_contact
# - change_contact
# - get_contacts

# class PhoneBook:
#     def __init__(self, filename):
#         self._filename = filename

# def search_contact(self, name):                                  # Найти контакт по фамилии
#         with open(self._filename, 'r', encoding='utf-8') as file:
#             for line in file.readlines():
#                 surname, phone_number = line.strip().split(' ')
#                 if surname == name:
#                     return phone_number
#         return None

# def add_contact(self, name, phone_number):                       # Добавить контакт
#         with open(self._filename, 'a', encoding='utf-8') as file:
#             file.write(f"{name} {phone_number}\n")

# def delete_contact(self, name):                                  # Удалить контакт
#         with open(self._filename, 'r', encoding='utf-8') as file:
#             lines = file.readlines()
#         with open(self._filename, 'w', encoding='utf-8') as file:
#             for line in lines:
#                 surname, _ = line.strip().split(' ')
#                 if surname != name:
#                     file.write(line)

# def change_contact(self, name, new_phone_number):                # Изменить контакт
#         with open(self._filename, 'r', encoding = 'utf-8') as file:
#             lines = file.readlines()
#         with open(self._filename, 'w', encoding='utf-8') as file:
#             for line in lines:
#                 surname, phone_number = line.strip().split(' ')
#                 if surname == name:
#                     file.write(f"{surname} {new_phone_number}\n")
#                 else:
#                     file.write(line)

# def get_contacts(self):                                          # Посмотреть все контакты
#         with open(self._filename, 'r', encoding='utf-8') as file:
#             return file.read().strip().split('\n')
# class Contact:
#     def __init__(self, surname, phone_number):
#         self.surname = surname
#         self.phone_number = phone_number


# def search_contact(surname):
#     with open('data.txt', 'r') as file:
#         for line in file:
#             contact = Contact(*line.split(','))
#             if surname == contact.surname:
#                 return contact.phone_number

#     return "Контакт не найден"


# def add_contact(surname, phone_number):
#     with open('data.txt', 'a') as file:
#         contact = Contact(surname, phone_number)
#         file.write(f"{contact.surname},{contact.phone_number}\n")


# def delete_contact(surname):
#     contacts = get_contacts()
#     with open('data.txt', 'w') as file:
#         for contact in contacts:
#             if contact.surname != surname:
#                 file.write(f"{contact.surname},{contact.phone_number}\n")


# def update_contact(surname, field, value):
#     contacts = get_contacts()
#     with open('data.txt', 'w') as file:
#         for contact in contacts:
#             if contact.surname == surname:
#                 setattr(contact, field, value)

#             file.write(f"{contact.surname},{contact.phone_number}\n")


# def get_contacts():
#     with open('data.txt', 'r') as file:
#         contacts = []
#         for line in file:
#             contacts.append(Contact(*line.split(',')))

#     return contacts
# class Contact:
#     def __init__(self, surname, phone_number):
#         self.surname = surname
#         self.phone_number = phone_number


# def search_contact(contacts, surname):
#     for contact in contacts:
#         if contact.surname == surname:
#             return contact.phone_number

#     return "Контакт не найден"


# def add_contact(contacts, surname, phone_number):
#     contact = Contact(surname, phone_number)
#     contacts.append(contact)


# def delete_contact(contacts, surname):
#     for contact in contacts:
#         if contact.surname == surname:
#             contacts.remove(contact)


# def update_contact(contacts, surname, field, value):
#     for contact in contacts:
#         if contact.surname == surname:
#             setattr(contact, field, value)


# def get_contacts(contacts):
#     return contacts.copy()

# class Contact:
#     def __init__(self, surname, phone_number):
#         self.surname = surname
#         self.phone_number = phone_number


# def search_contact(contacts, surname):
#     for contact in contacts:
#         if contact.surname == surname:
#             return contact.phone_number

#     return "Контакт не найден"


# def add_contact(contacts, surname, phone_number):
#     contact = Contact(surname, phone_number)
#     contacts.append(contact)


# def delete_contact(contacts, surname):
#     for contact in contacts:
#         if contact.surname == surname:
#             contacts.remove(contact)


# def update_contact(contacts, surname, field, value):
#     for contact in contacts:
#         if contact.surname == surname:
#             setattr(contact, field, value)


# def get_contacts(contacts):
#     return contacts.copy()

import os # Модуль os - библиотека функций для работы с операционной системой


class Contact:
    def __init__(self, surname, phone_number):
        self.surname = surname
        self.phone_number = phone_number


class Phonebook:
    def __init__(self):
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        if not os.path.exists("data.txt"):
            return

        with open("data.txt", "r") as file:
            for line in file:
                surname, phone_number = line.strip().split(",")
                self.add_contact(surname, phone_number)

    def search_contact(self, surname):
        for contact in self.contacts:
            if contact.surname == surname:
                return contact

        return "Контакт не найден"

    def add_contact(self, surname, phone_number):
        contact = Contact(surname, phone_number)
        self.contacts.append(contact)
        self.save_contacts()

    def delete_contact(self, surname):
        for contact in self.contacts:
            if contact.surname == surname:
                self.contacts.remove(contact)
                self.save_contacts()
                return

    def update_contact(self, surname, field, value):
        for contact in self.contacts:
            if contact.surname == surname:
                setattr(contact, field, value)
                self.save_contacts()
                return

    def get_contacts(self):
        return self.contacts

    def save_contacts(self):
        with open("data.txt", "w") as file:
            for contact in self.contacts:
                file.write(f"{contact.surname},{contact.phone_number}\n")