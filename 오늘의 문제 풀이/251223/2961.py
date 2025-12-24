import sys
INPUT = sys.stdin.readline

N = int(INPUT())
taste = []
answer = float('INF')

for i in range(N) :
    s, t = map(int, INPUT().split())
    taste.append((s, t))

def BackTracking(cnt, cur, s, t) :
    if cnt != 0 :
        global answer
        answer = min(answer, abs(s-t))
    for i in range(cur, len(taste)) :
        BackTracking(cnt+1, i+1, s * taste[i][0], t + taste[i][1])

BackTracking(0, 0, 1, 0)
print(answer)