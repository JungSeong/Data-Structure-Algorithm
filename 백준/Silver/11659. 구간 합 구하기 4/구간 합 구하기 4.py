import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))
S = [0] * (N+1)
for i in range(N) :
    S[i+1] = S[i] + num[i]

answer = [0] * M

for i in range(M) :
    a, b = map(int, input().split())
    answer[i] = str(S[b] - S[a-1])

print('\n'.join(answer))