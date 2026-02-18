import sys
input = sys.stdin.readline

N = int(input())
answer = float('INF')
cnt = 0

while N-5>0 :
    if N % 3 == 0 :
        answer = min(answer, cnt + N//3)
    N -= 5
    cnt += 1
        
if answer == float('INF') :
    print(-1)
else :
    print(answer)