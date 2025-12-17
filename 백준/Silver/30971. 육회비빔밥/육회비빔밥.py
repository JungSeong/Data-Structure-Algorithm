import sys
INPUT = sys.stdin.readline

N, K = map(int, INPUT().split())
A = [0] + list(map(int, INPUT().split()))
B = [0] + list(map(int, INPUT().split()))
C = [0] + list(map(int, INPUT().split()))
answer = -1
isVisited = [False] * (N+1)

def BT(before, cnt, res) :
    if cnt == N :
        global answer
        answer = max(res, answer)
    for i in range(1, N+1) :
        if cnt == 0 :
            isVisited[i] = True
            BT(i, cnt+1, res)
            isVisited[i] = False
        else :
            if not isVisited[i] and C[before] * C[i] <= K :
                isVisited[i] = True
                BT(i, cnt+1, res+A[before]*B[i])
                isVisited[i] = False
    return

BT(1, 0, 0)
print(answer)