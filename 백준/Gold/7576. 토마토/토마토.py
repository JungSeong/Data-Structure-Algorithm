import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]
move = [[-1,0],[0,1],[0,-1],[1,0]]

def BFS() :
    q = deque()
    cnt = 0
    for i in range(N) :
        for j in range(M) :
            if m[i][j] == 0 :
                cnt += 1
            elif m[i][j] == 1 :
                q.append([i, j])
    if cnt == 0 :
        print(0)
        return
    while q :
        cur_r, cur_c = q.popleft()
        for row in move :
            new_r = cur_r + row[0]
            new_c = cur_c + row[1]
            if 0<=new_r<N and 0<=new_c<M :
                if m[new_r][new_c] == 0 :
                    m[new_r][new_c] = m[cur_r][cur_c] + 1
                    q.append([new_r, new_c])
                    cnt -= 1

    if cnt > 0 :
        print(-1)
    else :
        max_day = 0
        for row in m :
            max_day = max(max_day, max(row))
        print(max_day-1)

BFS()