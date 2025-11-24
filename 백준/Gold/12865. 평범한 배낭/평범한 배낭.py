import sys

input = sys.stdin.readline
N, K = map(int, input().split())
dp = [0] * (K+1)

items = []
for i in range(N) :
    w, v = map(int, input().split())
    items.append((w,v))

for w, v in items :
    for i in range(K, w-1, -1) :
        dp[i] = max(dp[i], dp[i-w]+v)

print(max(dp))