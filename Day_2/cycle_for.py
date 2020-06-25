for x in ['spam', 'eggs', 'ham']:
    print(x, end=' ')
    # spam eggs ham
print('\n___________________________')

object1 = [{1, 4}, {44, 33}, {12, 45}]

for a, b in object1:
    print(a, b)
# 1 4
# 33 44
# 12 45
print('___________________________')

for i in range(len(object1)):
    print(object1[i])
# {1, 4}
# {33, 44}
# {12, 45}
print('___________________________')

dictionary_1 = {'Semen': 14, 'Gregory': 24, 'Lisa': 20}

for item in dictionary_1:
    print(item)
# Semen
# Gregory
# Lisa
print('___________________________')

for item in dictionary_1.items():
    print(item)
# ('Semen', 14)
# ('Gregory', 24)
# ('Lisa', 20)
print('___________________________')

for a, b in dictionary_1.items():
    print(f'Name: {a}, Old: {b}')
# Name: Semen, Old: 14
# Name: Gregory, Old: 24
# Name: Lisa, Old: 20
