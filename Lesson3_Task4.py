def my_func(x, y):
    print(f"{x**y}")


def arg_check(var_1, var_2, var_3):
    try:
        var_1(var_2)
    except ValueError:
        print("Введено некорректное значение")
        exit()
    if var_3 == 1:
        None if var_1(var_2) > 0 else exit()
    if var_3 == -1:
        None if var_1(var_2) < 0 else exit()


arg_1 = input("Введите любое положительное число: ")
arg_check(float, arg_1, 1)
arg_2 = input("Введите целое отрицательное число: ")
arg_check(int, arg_2, -1)

my_func(float(arg_1), int(arg_2))