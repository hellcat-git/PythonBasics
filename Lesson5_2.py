def file_len():
    w = 0
    with open("user_text.txt", 'r', encoding='utf-8') as f:
        for i, l in enumerate(f):
            print(f"Строка {i+1}, слов {len(l.split())}")
            w += len(l.split())
    return f"Всего строк {i+1}, всего слов {w}"


print(file_len())
