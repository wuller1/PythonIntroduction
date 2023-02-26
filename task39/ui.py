from logger import print_data, input_data, filter_data, edit_data, delete_data, get_data_by_line_index, get_line_index


def interface():
    print("""
    Выберете режим работы:
        1 - запись данных
        2 - вывод данных
        3 - поиск данных по параметрам
        4 - редактировать запись
        5 - удалить запись
    """)

    command = int(input("Введите номер команды: "))

    while command < 1 or command > 5:
        print("Введите корректный номер команды: ")
        command = int(input("Введите номер команды: "))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        filter_parameters = input("Введите параметры поиска через точку с запятой: ")
        filter_data(filter_parameters)
    elif command == 4:
        print("""
            Введите данные для редактирования.
            При вводе пустой строки в изменяемые поля, данные будут оставлены без изменения.
        """)

        name = input("Введите имя для редактирования: ")
        surname = input("Введите фамилию для редактирования: ")

        if get_line_index(name, surname) != -1:
            new_name = input("Введите новое имя: ")
            new_surname = input("Введите новую фамилию: ")
            new_phone = input("Введите новый номер телефона: ")
            new_address = input("Введите новый адрес: ")

            original_data = get_data_by_line_index(get_line_index(name, surname))

            if new_name == "":
                new_name = original_data[0]

            if new_surname == "":
                new_surname = original_data[1]

            if new_phone == "":
                new_phone = original_data[2]

            if new_address == "":
                new_address = original_data[3]

            edit_data(name, surname, new_name, new_surname, new_phone, new_address)
        else:
            print("Запись отсутствует")

    elif command == 5:
        name = input("Введите имя для удаления: ")
        surname = input("Введите фамилию для удаления: ")
        delete_data(name, surname)
