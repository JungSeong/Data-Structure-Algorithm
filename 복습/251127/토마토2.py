import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
m = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
move = [(0,-1,0),(0,0,1),(0,1,0),(0,0,-1),(1,0,0),(-1,0,0)]
start = []
cnt = 0

for i in range(H) :
    for j in range(N) :
        for k in range(M) :
            if m[i][j][k] == 1 :
                start.append([i,j,k])
            elif m[i][j][k] == 0 :
                cnt += 1

def BFS() :
    q = deque()
    if cnt > 0 :
        return 0
    for row in start :
        q.append(row)

    while q :
        cur_h, cur_r, cur_c = q.popleft()
        for row in move :
            new_h, new_r, new_c = cur_h + row[0], cur_r + row[1], cur_c + row[2]
            if 0<=new_h<H and 0<=new_r<N and 0<=new_c<M :
                if m[new_h][new_r][new_c] == 0 :
                    m[new_h][new_r][new_c] = m[cur_h][cur_r][cur_c] + 1
                    q.append([new_h,new_r,new_c])

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if m[i][j][k] == 0:
                    return -1

    answer = -1
    for h in m :
        for r in h :
            answer = max(answer, max(r))

    return answer-1

print(BFS())