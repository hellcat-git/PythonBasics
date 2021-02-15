total = 0
is_exit = 0


def sum_func():
    global total, is_exit
    my_arr = input("Введите значения через пробел: ").split()
    res = []
    for y in my_arr:
        try:
            res.append(int(y))
        except ValueError:
            print("Вы ввели текст, а не число! Программа будет завершена :( ")
            is_exit = 1
    sub_total = sum(res)
    total += sub_total

    return f"Подытог: {sub_total}, Общий итог: {total}"


while is_exit == 0:
    print(sum_func())
