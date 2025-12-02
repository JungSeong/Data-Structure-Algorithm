import sys
from collections import deque
INPUT = sys.stdin.readline

N, M = map(int, INPUT().split())
l = [list(map(int, INPUT().strip())) for _ in range(N)]
m = [[row[:] for row in l] for _ in range(2)]
cur_r, cur_c = 0, 0
move = [(-1,0),(0,1),(1,0),(0,-1)]

def BFS(cur_r, cur_c) :
    q = deque()
    m[1][cur_r][cur_c] = 1
    q.append([cur_r, cur_c, 1])

    while q :
        cur_r, cur_c, cnt = q.popleft()
        if cur_r == N-1 and cur_c == M-1 :
            print(m[cnt][cur_r][cur_c])
            return
        for dr, dc in move :
            new_r, new_c = cur_r+dr, cur_c+dc
            if 0<=new_r<N and 0<=new_c<M :
                if cnt == 1 and m[1][new_r][new_c] == 1 :
                    m[0][new_r][new_c] = m[cnt][cur_r][cur_c] + 1
                    q.append([new_r, new_c, cnt-1])
                if m[cnt][new_r][new_c] == 0 :
                    m[cnt][new_r][new_c] = m[cnt][cur_r][cur_c] + 1
                    q.append([new_r, new_c, cnt])
    print(-1)
BFS(cur_r, cur_c)