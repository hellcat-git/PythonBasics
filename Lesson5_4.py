my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четрые'}

file = open('text_4.txt', 'r', encoding='utf-8')
# файл умышленно открывается в режиме w, чтобы повторные запуски скрипта
# полностью перезаписывали его содержимое, а не дописывали его
new_file = open('translate.txt', 'w', encoding='utf-8')


while True:
    line = file.readline().strip()
    if not line:
        break
    arr = line.split()
    new_line = line.replace(arr[0], my_dict.get(arr[0]))
    print(new_line, file=new_file)
    print(f"Считана строка: {line}, Записана строка: {new_line}")

file.close()
