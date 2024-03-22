import sys
sys.set_int_max_str_digits(1000000)
n = int(input())
for i in range (n):
    a,b = list(map(int, input().split()))
    counter,ans = 0,0
    for alpha in range (min(a,b),max(a,b)+1):
        counter = ( alpha**(b-a) - 1) * alpha 
        ans += counter
    print(ans)