import sys
input = sys.stdin.readline

N = int(input())
dp = [[0]*2 for _ in range(N)]

dp[0][0] = 2
dp[0][1] = 1

for i in range(1, N) :
    dp[i][0] = 2 * (dp[i-1][0] + dp[i-1][1]) % (10**9+7)
    dp[i][1] = dp[i-1][0] % (10**9+7)

print(sum(dp[-1]) % (10**9+7))