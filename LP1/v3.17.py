a = [int(i) for i in input("Введите элементы массива, разделенные пробелом: ").split()]
a = a[1:] + a[:1]
print( a)