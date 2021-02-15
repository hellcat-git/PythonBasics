my_users_attr = ['Имя', 'Фамилия', 'Год рождения', 'Город проживания', 'email', 'Телефон']


def collect_data():
    new_user_data = []
    for i in my_users_attr:
        a = input(f"Введите значение атрибута '{i}': ")
        new_user_data += [(i, a)]
    new_user_dict = dict(new_user_data)
    return new_user_dict


def new_user(**kwargs):
    return print(f"Вы ввели параметры пользователя: {kwargs}")


# Решение 1 - собираем значения аттрибутов в цикле
new_user(**collect_data())


# Решение 2 - вводим значения аттрибутов вручную через input
new_user(Имя=input("Введите Имя: "), Фамилия=input("Введите Фамилию: "))
