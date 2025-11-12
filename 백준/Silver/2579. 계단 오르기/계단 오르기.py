import sys
input = sys.stdin.readline

N = int(input())
step = [int(input()) for i in range(N)]
dp = [0 for i in range(N)]

for i in range(N) :
    if i <= 1 : dp[i] = sum(step[:i+1])
    else :
        dp[i] = max(dp[i-3] + step[i-1] + step[i], dp[i-2] + step[i])

print(dp[-1])