# нужно написать функции:
# - search_contact
# - add_contact
# - delete_contact
# - change_contact
# - get_contacts

class PhoneBook:
    def __init__(self, filename):
        self._filename = filename

    def search_contact(self, name):                                  # Найти контакт по фамилии
        with open(self._filename, 'r', encoding='utf-8') as file:
            for line in file.readlines():
                surname, phone_number = line.strip().split(' ')
                if surname == name:
                    return phone_number
        return None

    def add_contact(self, name, phone_number):                       # Добавить контакт
        with open(self._filename, 'a', encoding='utf-8') as file:
            file.write(f"{name} {phone_number}\n")

    def delete_contact(self, name):                                  # Удалить контакт
        with open(self._filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        with open(self._filename, 'w', encoding='utf-8') as file:
            for line in lines:
                surname, _ = line.strip().split(' ')
                if surname != name:
                    file.write(line)

    def change_contact(self, name, new_phone_number):                # Изменить контакт
        with open(self._filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        with open(self._filename, 'w', encoding='utf-8') as file:
            for line in lines:
                surname, phone_number = line.strip().split(' ')
                if surname == name:
                    file.write(f"{surname} {new_phone_number}\n")
                else:
                    file.write(line)

    def get_contacts(self):                                          # Посмотреть все контакты
        with open(self._filename, 'r', encoding='utf-8') as file:
            return file.read().strip().split('\n')
