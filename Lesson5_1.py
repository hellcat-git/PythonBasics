def st_input():
    f_obj = open("user_text.txt", 'a', encoding='utf-8')
    i = 0
    print("Форма ввода данных, для выхода введите пустую строку")
    while True:
        st = input(f"Введите строку {i+1}: ")
        if len(st.strip()) == 0:
            print(f"Сохранено {i} строк")
            break
        else:
            print(st, file=f_obj)
            i += 1
    f_obj.close()


st_input()
