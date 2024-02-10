a = [int(i) for i in input("Введите элементы массива, разделенные пробелом(ток числа): ").split()]
s = set()
for i in a:
    if i in s:
        print("NO")
    else:
        print("YES")
        s.add(i)