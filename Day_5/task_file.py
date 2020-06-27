import header

# 1. Описать функцию работы со строкой символов,
# которая проверит, начинается ли каждое слово с большой буквы.
str_ = 'Hello, My Name Is Anastasia'
if str_.istitle() == 1:
    print('Все слова начинаются с большой буквы')
else:
    print('Не все слова начинаются с большой буквы')
# Все слова начинаются с большой буквы
str_1 = 'Hello, my name is Anastasia'
if str_1.istitle() == 1:
    print('Все слова начинаются с большой буквы')
else:
    print('Не все слова начинаются с большой буквы')
# Не все слова начинаются с большой буквы


# 2
a = "First.txt"
# Anastasia Olegovna Vergeeva
# Ivan Ivanovich Ivanov
b = "Second.txt"
# header.convert_fio(a, b)
print(str_.rfind(' '))
