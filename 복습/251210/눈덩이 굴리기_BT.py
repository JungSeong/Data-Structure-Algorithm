import sys
INPUT = sys.stdin.readline

N, M = map(int, INPUT().split())
a = [0] + list(map(int, INPUT().split()))
move = [1,2]

def BackTracking(cur, t, s) :
    if cur == N or t == M :
        return s
    answer = -1
    for i in range(2) :
        if i == 0 and 0<=cur+1<N+1 :
            answer = max(BackTracking(cur+1, t+1, s+a[cur+1]), answer)
        elif i == 1 and 0<=cur+2<N+1 :
            answer = max(BackTracking(cur+2, t+1, s//2+a[cur+2]), answer)
    return answer

print(BackTracking(0, 0, 1))