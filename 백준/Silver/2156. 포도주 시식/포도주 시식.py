n = int(input())
dp = [[0 for i in range(3)] for j in range(n+1)]

for i in range(1, n+1) :
    p = int(input())
    if i == 1 :
        dp[i][0] = 0
        dp[i][1] = p
        dp[i][2] = 0
    else :
        dp[i][0] = max(dp[i-1][1], dp[i-1][2])
        dp[i][1] = max([dp[i-2][0], dp[i-2][1], dp[i-2][2]]) + p
        dp[i][2] = dp[i-1][1] + p

answer = -1

for i in range(1, n+1) :
    p = max(dp[i])
    answer = max(answer, p)

print(answer)