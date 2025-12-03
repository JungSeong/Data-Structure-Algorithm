import sys
INPUT = sys.stdin.readline

N, M = map(int, INPUT().split())
a = [0]
a += list(map(int, input().split()))
move = [1, 2]
answer = 0

def BackTracking(cur, t, s) :
    if cur == N or t == M :
        global answer
        answer = max(answer, s)
        return
    for row in move :
        if row == 1 and 0<=cur+1<=N:
            BackTracking(cur+1, t+1, s+a[cur+1])
        elif row == 2 and 0<=cur+2<=N:
            BackTracking(cur+2,t+1,s//2+a[cur+2])
    return

BackTracking(0,0,1)
print(answer)