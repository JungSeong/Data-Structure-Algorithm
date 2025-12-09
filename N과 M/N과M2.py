import sys
INPUT = sys.stdin.readline

N, M = map(int, INPUT().split())
comb = []
ch = []

def BackTracking(cur, l) :
    if l == M :
        comb.append(ch[:])
        return
    for i in range(cur, N+1) :
        ch.append(i)
        BackTracking(i+1,l+1)
        ch.pop()

BackTracking(1, 0)
print(comb)