import sys
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * (len(A)+1)

cnt = 0
d = defaultdict(int)

for i in range(1, len(A)+1) :
    S[i] = S[i-1] + A[i-1]
    d[S[i]%M] += 1

cnt += d[0]
for k, v in d.items() :
    cnt += v*(v-1)//2

print(cnt)