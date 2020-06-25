import math

items = ['word', 222, (4, 5), 2.01, 'wow', math.pi]  # Набор объектов
tests = [(4, 5), 2.01, 3.14]  # То, что мы ищем в наборе объектов

for key in tests:
    for item in items:
        if item == key:
            print(key, "was found")
            break
    else:
        print(key, "not found")
# (4, 5) was found
# 2.01 was found
# 3.14 not found

# Запись лучше и короче:

for key in tests:
    if key in items:
        print(key, "was found")
    else:
        print(key, "not found")
# (4, 5) was found
# 2.01 was found
# 3.14 not found

sentence = 'Maybe I call you later'

for i in range(0, len(sentence), 1):
    print(sentence[i], end='')
# MbIa uar -3
# MyeIcl o ae -2
# Maybe I call you later -1
print('\n--------------------------')

for i in sentence[::2]:
    print(i, end='')
# MbIa uar -3
# MyeIcl o ae -2
# Maybe I call you later -1
# Запись разная, но результат один
print('\n--------------------------')

L1 = list(range(5))
L2 = list(range(7, 12))

for x, y in zip(L1, L2):
    print(f'{x} + {y} = {x + y}')
print('--------------------------')

# Тоже самое, что и
for i in range(len(L1)):
    print(f'{L1[i]} + {L2[i]} = {L1[i] + L2[i]}')
# такой вариант использовать не стоит
# Вывод один и тот же
# 0 + 7 = 7
# 1 + 8 = 9
# 2 + 9 = 11
# 3 + 10 = 13
# 4 + 11 = 15
L3 = list(zip(L1, L2))
print(L3)
# [(0, 7), (1, 8), (2, 9), (3, 10), (4, 11)]
print('--------------------------')

# L3 = zip(L1, L2)
# <zip object at 0x01383288>

# for i in L3:
#     print(i, end=' ')
# (0, 7) (1, 8) (2, 9) (3, 10) (4, 11)
# Выводит разные вещи, хотя объект один

# А сейчас фокус:
keys = ['Antony', 'Anastasia', 'Tom']
values = [22, 18, 34]
Old = dict(zip(keys, values))
print(Old)
# {'Antony': 22, 'Anastasia': 18, 'Tom': 34}
print('--------------------------')
str_ = "Hello"
for (offset, item) in enumerate(str_):
    print(f'{item}, имеет номер {offset}')
# H, имеет номер 0
# e, имеет номер 1
# l, имеет номер 2
# l, имеет номер 3
# o, имеет номер 4