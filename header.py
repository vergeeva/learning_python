import math


# 1. Описать функцию работы со строкой символов, которая найдет,
# сколько раз входит в строку некоторый произвольный символ (задать как параметр функции).
def find_count(symbol, str_):
    count_ = 0
    for symbols in str_:
        if symbol == symbols:
            count_ += 1
    return count_


# 2. Дан текст (2-3 строки) в файле F1.
# Описать функцию преобразования строки,
# которая вносит изменения в строку текста, повторяя дважды каждую букву строки.
# (знаки препинания и прочие символы не изменять).
# Преобразовать все строки текста, и новый текст записать в файл F2.
def convert_text(file_1, file_2):
    a = open(file_1)
    b = open(file_2, 'w')
    for line in a:
        for i in range(0, len(line)):
            if 65 <= ord(line[i]) <= 90 or 97 <= ord(line[i]) <= 122 or 1040 <= ord(line[i]) <= 1103:
                b.write(line[i] * 2)
            else:
                b.write(line[i])
    b.close()
    a.close()


# 2. Дан текст в файле F1 в виде:
# ИМЯ ОТЧЕСТВО ФАМИЛИЯ_1
# ИМЯ ОТЧЕСТВО ФАМИЛИЯ_2
# …
# Описать функцию, которая формирует текстовую строку в формате:
# ФАМИЛИЯ И.О.
# Сохранить преобразованный текст в файле F2.
# def convert_fio(a, b):
#     aa = open(a)
#     bb = open(b, 'w')
#     c = list()
#     counter = 0
#     for line in aa:
#         # bb.write(line[(line.rfind(' ') + 1):len(line)])
#         # bb.write(line[0])
#         # bb.write('. ')
#         # bb.write(line[line.find('')+1])
#         # bb.write('.')
#     #     for i in range(len(line)):
#     #         if line[i] == ' ':
#     #             bb.write(line[i + 1])
#     #             bb.write('. ')
#     #             counter += 1
#     #             if counter == 2:
#     #                 print(i)
#     #                 bb.write(line[i + 1:len(line)])
#     #                 i -= 1
#     #                 counter = 0
#     #                 continue
#     #         c.append(line[i])
#     # print(c)
#     aa.close()
#     bb.close()
