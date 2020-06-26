# 424
file_name = open("file_.txt", 'a')
file_name.write("\nдобавлено новое слово")
file_name.close()
# It's my first line
# добавлено новое слово

file_name = open("file_.txt")
print(file_name.read())
# Hello, I'm empty file
# It's my second line

# другая запись:
# for line in file_name:
#     print(line)
file_name.close()

file_name = open("file_.txt", 'w')
file_name.write("\nвсе удалилось и записалась эта фраза")
file_name.close()

file_name = open("file_.txt")
print(file_name.read())
file_name.close()
# все удалилось и записалась эта фраза

file_name_2 = open("file_2.txt", 'w')
file_name_2.write("Hello, I'm new file")
file_name_2.close()
# Создали файлик и записали туда надпись
print('-----------------------------')
file_name_2 = open("file_2.txt")
print(file_name_2.read())
file_name_2.close()
# Hello, I'm new file
