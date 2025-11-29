import sys
input = sys.stdin.readline
N, M, R = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]
bm = [['S']*M for _ in range(N)]
direction = {'N': (-1,0), 'E': (0,1), 'S': (1,0), 'W' : (0,-1)}
answer = 0

for i in range(R) :
    # 공격수
    X, Y, D = input().split()
    X = int(X)
    Y = int(Y)
    cur_r, cur_c = X-1, Y-1
    dr, dc = direction[D][0], direction[D][1]

    if bm[cur_r][cur_c] == 'S' :
        bm[cur_r][cur_c] = 'F'
        residual_power = m[cur_r][cur_c] - 1
        answer += 1

        while residual_power > 0 :
            new_r, new_c = cur_r + dr, cur_c + dc
            if not (0<=new_r<N and 0<=new_c<M) : break
            residual_power -= 1

            if bm[new_r][new_c] == 'S' :
                answer += 1
                bm[new_r][new_c] = 'F'
                residual_power = max(residual_power, m[new_r][new_c]-1)

            cur_r, cur_c = new_r, new_c

    # 수비수
    X, Y = map(int, input().split())
    if bm[X-1][Y-1] == 'F' :
        bm[X-1][Y-1] = 'S'

print(answer)
for row in bm :
    print(''.join(row))