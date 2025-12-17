import sys
INPUT = sys.stdin.readline

N = int(INPUT())
b = list(map(int, INPUT().split()))
a = [0]*N
sum_a = 0
isPossible = True

for i in range(N) :
    if i == 0 :
        a[i] = b[i]
    else :
        sum_a += a[i-1]
        if i*(b[i]+1) < sum_a :
            a[i] = b[i]+1
        elif i*b[i] >= sum_a :
            a[i] = b[i]
        else :
            isPossible = False
            break
    if a[i] == 0 :
        isPossible = False
        break

if isPossible :
    print(*a)
else :
    print("-1")