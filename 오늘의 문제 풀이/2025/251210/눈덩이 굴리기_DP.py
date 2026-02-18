import sys
INPUT = sys.stdin.readline

N, M = map(int, INPUT().split())
a = [0]
a.extend(list(map(int, INPUT().split())))
max_snowball = 0

dp = [[-1]*(N+1) for _ in range(M+1)]
dp[0][0] = 1

for i in range(1, M+1) :
    for j in range(1, N+1) :
        if j-1 >= 0 and dp[i-1][j-1] != -1 :
            dp[i][j] = max(dp[i-1][j-1]+a[j], dp[i][j])
        if j-2 >= 0 and dp[i-1][j-2] != -1 :
            dp[i][j] = max(dp[i-1][j-2]//2+a[j], dp[i][j])
        
        max_snowball = max(max_snowball, dp[i][j])

print(max_snowball)