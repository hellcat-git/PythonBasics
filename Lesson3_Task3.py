def my_func():
    arg_1 = input("Введите число 1: ")
    arg_2 = input("Введите число 2: ")
    arg_3 = input("Введите число 3: ")
    my_args = [int(arg_1), int(arg_2), int(arg_3)]
    my_args.remove(min(my_args))
    return print(sum(my_args))


my_func()

# решение 2


def my_func_2():
    my_args = input("Введите числа через пробел ").split()
    my_int_array = []
    for y in my_args:
        my_int_array.append(int(y))
    my_int_array.remove(min(my_int_array))
    return print(sum(my_int_array))


my_func_2()
