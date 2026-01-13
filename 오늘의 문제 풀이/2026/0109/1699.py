import sys, math
input = sys.stdin.readline

N = int(input())
dp = [float('INF')] * (N+1)
dp[0] = 0

for i in range(1, N+1) :
    si = int(math.sqrt(i))
    for j in range(1,si+1) :
        dp[i] = min(dp[i], dp[i-j*j]+1) 

print(dp[-1])