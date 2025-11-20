import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
m = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)] # H, N, M 순으로 나옴
move = [[0,-1,0],[0,0,1],[0,1,0],[0,0,-1],[1,0,0],[-1,0,0]]

def BFS() :
    q = deque()
    cnt = 0
    for h in range(H) :
        for r in range(N) :
            for c in range(M) :
                if m[h][r][c] == 0 :
                    cnt += 1
                if m[h][r][c] == 1 :
                    q.append([h,r,c])
    if cnt == 0 :
        print(0)
        return
    while q :
        cur_h, cur_r, cur_c = q.popleft()
        for row in move :
            new_h, new_r, new_c = cur_h + row[0], cur_r + row[1], cur_c + row[2]
            if 0<=new_h<H and 0<=new_r<N and 0<=new_c<M :
                if m[new_h][new_r][new_c] == 0 :
                    m[new_h][new_r][new_c] = m[cur_h][cur_r][cur_c] + 1
                    q.append([new_h,new_r,new_c])
                    cnt -= 1

    if cnt > 0 :
        print(-1)
    else :
        min_day = 0
        for h in m :
            for row in h :
                min_day = max(min_day, max(row))
        print(min_day-1)

BFS()