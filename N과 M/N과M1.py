import sys
INPUT = sys.stdin.readline

N, M = map(int, INPUT().split())
comb = []
isvisited = [0]*(N+1)

def BackTracking(idx, cur) :
    if idx == M :
        comb.append(cur)
        return 
    for i in range(1, N+1) :
        if isvisited[i] == 0 :
            isvisited[i] = 1
            BackTracking(idx+1, cur+str(i))
            isvisited[i] = 0

BackTracking(0, '')
for row in comb :
    print(' '.join(row))