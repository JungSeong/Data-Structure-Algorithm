# 한 번 점프 할 때 방향 바꾸면 안 됨

import sys
INPUT = sys.stdin.readline
N = int(INPUT())
m = [list(map(int, INPUT().split())) for _ in range(N)]

move = [(1,0), (0,1)]
cur_r, cur_c = 0, 0
dp = [[0]*N for _ in range(N)]
dp[cur_r][cur_c] = 1

for i in range(N) :
    for j in range(N) :
        if dp[i][j] == 0 or (i == N-1 and j == N-1) :
            continue
        else :
            jump = m[i][j]
            if 0<=i+jump<N :
                dp[i+jump][j] += dp[i][j]
            if 0<=j+jump<N :
                dp[i][j+jump] += dp[i][j]

print(dp[N-1][N-1])