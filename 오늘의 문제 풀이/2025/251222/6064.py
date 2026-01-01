import sys, math
INPUT = sys.stdin.readline

T = int(INPUT())

for i in range(T) :
    M, N, x, y = map(int, INPUT().split())
    isAvailable = False
    k = x

    while k <= math.lcm(M, N) :
        if (k-y) % N == 0 :
            isAvailable = True
            print(k)
            break
        k += M
    
    if not isAvailable :
        print("-1")