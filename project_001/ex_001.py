import json
phonebook = {
    "Иванов Владимир Ильич": {
        "телефон": ["9771478745"],
        "почта": ["ivanovvi@yandex.ru"],
        "дата рождения": "22.05.1990",
        "страна": "Россия"
    },
    "Сидоров Дмитрий Николаевич": {
        "телефон": ["8006564532"],
        "почта": ["siddn@mail.ru", "sid333@rambler.ru"],
        "дата рождения": "19.11.1985",
        "страна": "Россия"
    },
    "Smith John": {
        "телефон": ["7659982004", "6809021445"],
        "почта": ["jsmith@gmail.com"],
        "дата рождения": "30.09.1995",
        "страна": "Австралия"
    }
}


def View_f(tel_dict):
    [print(keys, tel_dict[keys]) for keys in tel_dict]


def Search_f(tel_dict, user_key):
    print(tel_dict.get(user_key, "Такого контакта нет!"))


def Add_f(tel_dict, user_dict):
    tel_dict.update(user_dict)


def Change_f(tel_dict, user_key):
    inner_key = input("Введите, что будем менять: ")
    if inner_key == 'страна':
        tel_dict[user_key][inner_key] = input("Введите новую страну: ")
    elif inner_key == 'телефон' or inner_key == 'почта':
        tel_dict[user_key][inner_key] = input(
            "Введите номера телефонов или адреса почт через пробел: ").split()
    else:
        print('Такого параметра не существует или его нельзя изменить!')


def Delete_f(tel_dict, user_key):
    if user_key in tel_dict:
        del (tel_dict[user_key])


def Save_f(tel_dict):
    with open('phonebook.json', 'w', encoding='utf-8') as f:
        json.dump(tel_dict, f)


while True:
    user_command = int(input('Вас приветствует помощник телефонного справочника.\n'
                             'Список возможных команд:\n'
                             '1. Просмотр\n'
                             '2. Поиск\n'
                             '3. Добавление\n'
                             '4. Изменение\n'
                             '5. Удаление\n'
                             '6. Сохранение\n'
                             '7. Выход\n'
                             'Введите номер команды: '))
    if user_command == 7:
        break
    elif user_command == 1:
        View_f(phonebook)
    elif user_command == 2:
        user_name = input('Введите ФИО контакта: ')
        Search_f(phonebook, user_name)
    elif user_command == 3:
        user_name = input('Введите ФИО нового контакта: ')
        new_dict = {"телефон": input("Введите номера телефонов через пробел: ").split(),
                    "почта": input("Введите адреса почт через пробел: ").split(),
                    "дата рождения": input('Введите дату рождения: '),
                    "страна": input('Введите страну проживания: ')
                    }
        Add_f(phonebook, {user_name: new_dict})
    elif user_command == 4:
        Change_f(phonebook, input('Введите ФИО изменяемого контакта: '))
    elif user_command == 5:
        Delete_f(phonebook, input('Введите ФИО удаляемого контакта: '))
    elif user_command == 6:
        Save_f(phonebook)
