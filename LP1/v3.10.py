import re
def cus(a):
    return len(a.split())
b = int(input("Количество строк : "))
a1 = []
for i in range(0,b):
    a = input("Введите строку: ")
    a1.append(a)
a1.sort(key= cus)

print(" " + str(a1))