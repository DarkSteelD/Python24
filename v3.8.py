import random
a = input("Введите строку: ")
a1 = a.split()
i = 0
for b in a1:
    if(len(b)%2==0):
         i+=1


print(i)