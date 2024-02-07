import re
a = input("Введите строку: ")
a1 = re.findall ('\d{2} \w{4,9} \d{4}', a)

print(" " + str(a1))