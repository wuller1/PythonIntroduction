import os
from data_create import name_data, surname_data, phone_data, address_data

file_name = "data.txt"


def print_data():
    if os.path.exists(file_name):
        print("Вывод данных из файла:")
        with open(file_name, 'r', encoding='utf-8') as file:
            list_data = file.readlines()

            for line in list_data:
                print(line)
    else:
        print("Записи отсутствуют")


def input_data():
    print("Введите данные для записи в файл: ")
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()

    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f"{name};{surname};{phone};{address}\n")


def filter_data(filter_string):
    is_found = False

    with open(file_name, 'r', encoding='utf-8') as file:
        list_data = file.readlines()
        list_filter = filter_string.split(";")
        for line in list_data:
            line_array = line.split(";")
            count = 0
            for record in line_array:
                for filter_record in list_filter:
                    if filter_record.lower() in record.lower() and len(filter_record) == len(record):
                        count += 1

            if count == len(list_filter):
                print(line)
                is_found = True

    if not is_found:
        print("Записи с такими параметрами отсутствуют")


def edit_data(name, surname, new_name, new_surname, new_phone, new_address):
    edit_index = get_line_index(name, surname)

    if edit_index != -1:
        with open(file_name, 'r', encoding='utf-8') as file:
            original_data = file.readlines()

        with open(file_name, 'w', encoding='utf-8') as file:
            for i in range(0, len(original_data)):
                if i == edit_index:
                    file.write(f"{new_name};{new_surname};{new_phone};{new_address}")
                else:
                    file.write(original_data[i])


def delete_data(name, surname):
    edit_index = get_line_index(name, surname)

    if edit_index != -1:
        with open(file_name, 'r', encoding='utf-8') as file:
            original_data = file.readlines()

        with open(file_name, 'w', encoding='utf-8') as file:
            for i in range(0, len(original_data)):
                if i != edit_index:
                    file.write(original_data[i])


def get_line_index(name, surname):
    with open(file_name, 'r', encoding='utf-8') as file:
        data = file.readlines()

    for i in range(0, len(data)):
        if name in data[i] and surname in data[i]:
            return i

    return -1


def get_data_by_line_index(index):
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.readlines()[index].split(";")
