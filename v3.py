#v3
def MAXP(a):
    for i in range(2,int(sqrt(a))):
        if a % i == 0:
            return a
    return 0
def P5(a):
    b = 1
    for i in range(2,int(sqrt(a))):
        if a % i == 0 and a % 5 != 0:
            b = b*a
    return b
def MAXPNT( a):
    for i in range(2,int(sqrt(a))):
        if a % i == 0 and a % 2 != 0 and MAXP(a) != 0   :
            return a
    return 0
def ATR(a):
    b = string(a)
    a = 0
    for i in range(0,b.size()):
        

def NOD(a):
    return MAXPNT(a)*ATR(a)