glas = "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ"
soglas = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZбвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
def pairs(s):
    gs, sg = 0, 0
    for i in range(len(s) - 1):
        if s[i] in glas and s[i+1] in soglas:
            gs += 1
        elif s[i] in soglas and s[i+1] in glas:
            sg += 1
    return gs, sg
def sort(s):
    def difference(c):
        gs, sg = pairs(c)
        return abs(gs - sg)  
    return sorted(s, key=difference)
a = input("Введите строку: ")
a1 = a.split('.')
print(sort(a1))
