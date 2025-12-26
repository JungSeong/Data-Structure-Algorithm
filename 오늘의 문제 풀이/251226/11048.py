# 사탕 개수의 최댓값?

import sys
INPUT = sys.stdin.readline

N, M = map(int, INPUT().split())
m = [list(map(int, INPUT().split())) for _ in range(N)]
dp = [[0]*M for _ in range(N)]
dp[0][0] = m[0][0]
move = [(1,0), (0,1), (1,1)]

for cur_r in range(N) :
    for cur_c in range(M) :
        for dr, dc in move :
            new_r, new_c = cur_r + dr, cur_c + dc
            if 0<=new_r<N and 0<=new_c<M :
                dp[new_r][new_c] = max(dp[cur_r][cur_c] + m[new_r][new_c], dp[new_r][new_c])

print(dp[N-1][M-1])