import sys
input = sys.stdin.readline

N, Z, M = map(int, input().split())
obstacles = set(map(lambda x : x-1, map(int, input().split())))

for k in range(1, Z+1) :
    cur = 0
    isPossible = True
    while True :
        cur += k
        if cur % N in obstacles or cur % N == 0 :
            isPossible = False
            break
        if cur % N == Z-1 :
            print(k)
            break
    if not isPossible :
        continue
    else :
        break