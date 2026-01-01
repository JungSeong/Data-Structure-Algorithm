import sys
INPUT = sys.stdin.readline

N = int(INPUT())
m = [list(map(int, INPUT().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

move = [(1,0),(0,1)]

for i in range(N) :
    for j in range(N) :
        if dp[i][j] != 0 :
            cur_r, cur_c = i, j
            if cur_r == N-1 and cur_c == N-1 :
                break
            l = m[cur_r][cur_c]
            for dr, dc in move :
                new_r, new_c = cur_r + dr * l, cur_c + dc * l
                if 0<=new_r<N and 0<=new_c<N :
                    dp[new_r][new_c] += dp[cur_r][cur_c]

print(dp[N-1][N-1])