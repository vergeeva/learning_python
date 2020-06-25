import random

# Магический шар
# Постановка задачи: Разработать программу, которая будет как "магически" шар выдавать случайный результат.
# К примеру, вы ей задаете вопрос: "..... . .. ... .. ?", а она выдает вам результат из предложенного:
# Да
# Нет
# Скорее всего да
# Скорее всего нет
# Возможно
# Имеются перспективы
# Вопрос задан неверно
# По желанию дополнить ответами.
answers = ["Да", "Нет", "Скорее всего да", "Скорее всего нет", "Возможно", "Имеются перспективы",
           "Вопрос задан неверно"]
question = input("Введите ваш вопрос: ")
print(answers[random.randrange(0, len(answers))])
