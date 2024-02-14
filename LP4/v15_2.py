# Дан файл целых чисел. Найти количество содержащихся в
# нем серий (то есть наборов последовательно расположенных одинаковых
# элементов). Например, для файла с элементами 1, 5, 5, 5, 4, 4, 5 результат равен
# 4.

with open("C:\\Users\\DarkStell\\Documents\\GitHub\\Python24\\LP4\\A.txt") as file:
    a = list((int(f) for f in file.read().split()))
counter = 1
for i in range(1,len(a)):
    if a[i-1] != a[i]:
        counter +=1
print(counter)