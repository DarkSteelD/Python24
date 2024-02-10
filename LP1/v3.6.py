import re
a = input("Введите строку: ")
a1 = re.findall (r'[А-я]{1}', a)

print(len(a1))