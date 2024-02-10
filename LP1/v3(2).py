import random
a = input("Введите строку: ")
a1 = a.split()
a = ""
while len(a1) > 0:
    l = random.randint(0, len(a1) -1 )
    a += " " + a1[l]
    a1.remove(a1[l])

print(a)