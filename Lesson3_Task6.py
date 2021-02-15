# Задание 6
my_word = input("введите слово в нижнем регистре: ")


def int_func():
    min_char = min(my_word)
    max_char = min(my_word)
    if (min_char >= 'a' and max_char <= 'z') or (min_char >= 'а' and max_char <= 'я'):
        my_word_cap = my_word.capitalize()
    else:
        print(f"Слово '{my_word}' не удовлетворяет условиям ввода")
        my_word_cap = ""
    return my_word_cap


print(int_func())

# Задание 7
my_words = input("Введите слова в нижнем регистре через пробел: ").split()
my_words_cap = []
for my_word in my_words:
    my_words_cap.append(int_func())
my_words_string = " ".join(my_words_cap)

print(my_words_string)
