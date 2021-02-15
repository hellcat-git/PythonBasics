def dev_func(var1, var2):
    try:
        result = var1 / var2
        return result
    except ZeroDivisionError:
        print("Вы ввели ноль! Ничего не получится :(")


print(dev_func(int(input("Введите число 1: ")), int(input("Введите число 2: "))))
