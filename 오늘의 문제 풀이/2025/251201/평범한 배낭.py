import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [0] * (K+1)

for i in range(N) :
    W, V = map(int, input().split())
    for j in range(K, W-1, -1) :
        dp[j] = max(dp[j], dp[j-W]+V)

answer = max(dp)
print(answer)