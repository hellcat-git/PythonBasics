from itertools import count, cycle


def my_func():

    a = int(input("Введите начало списка: "))
    b = int(input("Введите окончание списка: "))

    st = []
    try:
        for el in count(a):
            if el <= b:
                st.append(el)
            elif el > b:
                break
    except TypeError:
        print("Введено некорректное значение одного из параметров")
    return st


def my_loop(n):

    try:
        f = int(input("Введите целое количество повторений списка: "))
        r = len(n)*f-1
        c = 0
        for sets in cycle(n):
            if c > r:
                break
            print(sets)
            c += 1
    except ValueError:
        print("Введено некорректное количество повторений списка")


my_loop(my_func())
