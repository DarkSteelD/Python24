# Вариант 5 Реализовать функцию, которая будет проверять, является ли
# введенная строка почтовым индексом (Zip Code), возвращаемое значение true
# или False. Дополнительно реализовать функцию, которая выбрасывает
# исключение о некорректном аргументе, иначе возвращает почтовый индекс
# (Zip Code).
import re
def check():
    a = input("Введите строку: ")
    a = re.match(r'\d{5}', a)
    print(True if a!= None else False)