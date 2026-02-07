# 최대 10^8
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
m = list(list(map(int, input().split())) for _ in range(N))
dp = [[0]*M for _ in range(N)]
dp[0][0] = m[0][0]
H = int(input())

for i in range(N) :
    for j in range(M) :
        if i == 0 :
            if j > 0 :
                dp[i][j] = dp[i][j-1] + m[i][j]
        else :
            if j == 0 :
                dp[i][j] = dp[i-1][j] + m[i][j]
            else :
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + m[i][j]

if dp[i][j] <= H :
    print("YES")
    print(dp[i][j])
else :
    print("NO")
