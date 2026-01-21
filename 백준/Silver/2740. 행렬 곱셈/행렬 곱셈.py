import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(list(map(int, input().split())) for _ in range(N))
M, K = map(int, input().split())
B = list(list(map(int, input().split())) for _ in range(M))
B_T = list(zip(*B))

for i in range(N) :
    answer = []
    for j in range(K) :
        C_j = 0
        for k in range(M) :
            C_j += A[i][k] * B_T[j][k]
        answer.append(C_j)
    print(*answer)