unsorted_list = []
sorted_list = []
while True:
    val = [int(input("Введите число ").strip())]
    unsorted_list += val
    unsorted_list_loop = unsorted_list.copy()
    while len(unsorted_list_loop) > 0:
        minimum = unsorted_list_loop[0]
        for item in unsorted_list_loop:
            if item < minimum:
                minimum = item
        sorted_list.append(minimum)
        unsorted_list_loop.remove(minimum)
    print(sorted_list[::-1])
    sorted_list.clear()
    menu = input("Продолжаем? Введите д или н : ").strip()
    if menu == 'д' or menu == 'да':
        continue
    else:
        break
