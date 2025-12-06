import sys
INPUT = sys.stdin.readline

N, M = map(int, INPUT().split())
l = list(range(1, N+1))
combinations_all = []

def BackTracking(idx, ch) :
    if idx == M :
        combinations_all.append(ch)
        return
    for i in range(1, N+1) :
        BackTracking(idx+1, ch+str(i))

BackTracking(0, '')

for row in combinations_all :
    print(' '.join(row))