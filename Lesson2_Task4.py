sting = input("Пожалуйста, введите слова через пробел: ")
for ind, el in enumerate(sting.split(' '), 1):
    print(ind, el[:10])
