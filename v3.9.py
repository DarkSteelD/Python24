import re
b = input("Количество строк : ")
a1 = []
for i in range(0,b):
    a = input("Введите строку: ")
    a1.append(a)
a1.sort()

print(" " + a1)