a = [int(i) for i in input("Введите элементы массива, разделенные пробелом(ток числа): ").split()]
s = {}
for i in a:
    s[i] = s.get(i,0)+1
print("Неповторяющиеся элементы ")
for i in a:
    if s[i]==1:
        print(i, end='+')
print()
for i in a:
        print(s[i])
