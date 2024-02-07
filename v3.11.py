# Вариант 3. Задачи 3, 5, 7, 12\
#  В порядке увеличения разницы между частотой наиболее часто
# встречаемого символа в строке и частотой его появления в алфавите.
order = {}
def order1(k):
    
    if not order:
        for i in a:
            c = order.get(i, 0)
            if c == 0:
                order[i]=1
            else:
                order[i] =  order[i]+1
    return order.get(k[0], ord(k[0]))
d = {}
a = input("Введите строку: ")
order1(a)
a1 = a.split()
a1.sort(key = order1)
print(str(a1))