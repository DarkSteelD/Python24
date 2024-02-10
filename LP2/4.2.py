inputer = int(input("Введите количество : "))
d = {}
for _ in range(inputer):
    a,b = input("Пара ключ значение : ").split()
    d[a]=b
    d[b]=a
inputer = input("Ваше слово : ")
print(d[inputer])