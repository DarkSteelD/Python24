#v3
def MAXP(a):
    for i in range(a,1,-1):
        if a % i == 0 and ISP(i):
            return i
    return 0
def ISP(a):
    for i in range(2,int(a**0.5)+1):
        if a % i == 0 and a != 2:
            return 0
    return a
# Работает
def P5(a):
    b = 1
    c = str(a)
    for i in c:
        if int(i) % 5 != 0:
            b = b*int(i)
    return b
# Работает

def MAXPNT( a):
    for i in range(2,int(sqrt(a))):
        if a % i == 0 and a % 2 != 0 and MAXP(a) != 0   :
            return a
    return 0
def ATR(a):
    b = string(a)
    a = 1
    for i in range(0,b.size()):
        a *= int(b[i])
    return a

def NOD(a):
    return MAXPNT(a)*ATR(a)

# a = int(input("Введите число: "))
# a = MAXP(a)
# print("Максимальный простой делитель числа: ", a)
# a = int(input("Введите число: "))
# a = P5(a)
# print("Произведение элементов не кратных 5: ", a)

