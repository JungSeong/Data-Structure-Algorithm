import sys
input = sys.stdin.readline

N, K = map(int, input().split())
S = list(map(int, input().split()))
P = [0] * N
D = list(map(int, input().split()))
D = list(map(lambda x : x-1, D))

for i in range(K) :
    for j in range(N) :
        P[D[j]] = S[j]
    S = P[:]

print(*S)