def fact():
    try:
        n = int(input("Ведите число для подсчета факториала: "))
        a = 1
        for i in range(1, n+1):
            a *= i
            yield a
    except ValueError:
        print("Введено некорректное значение")


for el in fact():
    print(el)
