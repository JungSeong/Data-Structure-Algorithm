import sys
input = sys.stdin.readline

N, M = map(int, input().split())
m = list(list(map(int, input().split())) for _ in range(N))
S = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N+1) :
    for j in range(1, N+1) :
        S[i][j] = S[i-1][j] + S[i][j-1] -S[i-1][j-1] + m[i-1][j-1]

answer = []

for i in range(M) :
    x1, y1, x2, y2 = map(int, input().split())
    partial_sum = 0
    partial_sum += S[x2][y2] - S[x1-1][y2] - S[x2][y1-1] + S[x1-1][y1-1]
    answer.append(str(partial_sum))

print("\n".join(answer))