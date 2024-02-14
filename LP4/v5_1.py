a = (int(f) for f in input(file="27-166a.txt".split()))
counter = 0
a1 = {}
for l in range(2,a[0]):
    counter %= a[1]
    if a1.get(counter,None) != None:
        a1[counter] = (a[l],0,0)
    elif min(a1[counter]) < a[l]:
        a1[a1.get_index(min(a1[counter]))] = a[l]
sum = ()
for _ in range(a[1]):
    sum[i] = a[_][0]+a[_][1]+a[_][2]
print(sum.index(max(sum)))
