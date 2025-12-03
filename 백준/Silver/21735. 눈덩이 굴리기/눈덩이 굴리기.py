import sys
INPUT = sys.stdin.readline

N, M = map(int, INPUT().split())
a = [0]
a.extend(list(map(int, input().split())))
move = [1, 2]

def BackTracking(cur, t, s) :
    if cur == N or t == M :
        return s
    answer = s
    for row in move :
        if row == 1 and 0<=cur+1<=N:
            answer = max(answer, BackTracking(cur+1, t+1, s+a[cur+1]))
        elif row == 2 and 0<=cur+2<=N:
            answer = max(answer, BackTracking(cur+2,t+1,s//2+a[cur+2]))
    return answer

print(BackTracking(0,0,1))