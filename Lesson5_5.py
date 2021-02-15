def file_sum():

    st = input("Введите несколько чисел, разделенных пробелом: ")

    while any(w.isalpha() for w in st):
        print("Введено текстовое значение. Повторите ввод чисел")
        st = input("Введите несколько чисел, разделенных пробелом: ")

    with open("user_sum.txt", 'w+', encoding='utf-8') as f:
        print(st, file=f)
        f.seek(0)
        arr = sum(map(int, (f.readline().split())))

    return f"Сумма введенных чисел: {arr}"


print(file_sum())
