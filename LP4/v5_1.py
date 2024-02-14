with open("C:\\Users\\DarkStell\\Documents\\GitHub\\Python24\\LP4\\27-167a.txt") as file:
    a = list((int(f) for f in file.read().split()))
counter = 0
a1 = {}
for l in range(2,a[0]   ):
    counter %= a[1]
    if counter not in a1:
        a1[counter] = [a[l],0,0]
    elif min(a1[counter]) < a[l]:
        a1[counter][a1[counter].index(min(a1[counter]))] = a[l]
    counter +=1
summer = []
for i in range(a[1]):
    if i in a1:
        summer.append(sum(a1[i]))
    else:
        summer.append(0) 
print(max(summer))
