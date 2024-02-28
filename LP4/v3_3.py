def equal_sum(a,k):
    tot_s = sum(a)
    mas = []
    if tot_s % k != 0:
        return False
    step = tot_s // k
    counter, target_sum = 0,0
    for element in a:
        counter += 1
        if  target_sum + element < step:
            target_sum += element
            
        elif target_sum + element > step:
            return False
        else:
            mas.append(counter)
            counter = 0
           
            target_sum = 0
    return mas

n= [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
ans = equal_sum(a,n[1])
print( "Да" if ans else "Нет")
if ans:
    print(" ".join(str(i) for i in ans))