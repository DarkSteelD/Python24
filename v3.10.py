import re
def cus(a, b):
    if len(a.spit())> len(b.spit()):
        return 1
    elif len(a.spit()) == len(b.spit()):
        return 0
    return -1
b = int(input("Количество строк : "))
a1 = []
for i in range(0,b):
    a = input("Введите строку: ")
    a1.append(a)
a1.sort(key= lambda b: len(b.split))

print(" " + a1)