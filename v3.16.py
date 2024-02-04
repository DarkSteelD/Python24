import random
a = input("Введите строку: ")
a = a.lower()
a1 = a.split()
def order1(c):
    order = {"б": 0, "с": 1, "к" : 2}
    return order.get(c[0], ord(c[0]))
a1.sort(key=order1)

print(' '.join(a1))