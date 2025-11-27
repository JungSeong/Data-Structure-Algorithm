import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
m = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
move = [[0,-1,0],[0,1,0],[0,0,-1],[0,0,1],[1,0,0],[-1,0,0]]

def BFS() :
    cnt = 0
    q = deque()
    for i in range(H) :
        for j in range(N) :
            for k in range(M) :
                if m[i][j][k] == 0 :
                    cnt += 1
                elif m[i][j][k] == 1 :
                    q.append([i,j,k])
    
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
        answer = 0
        for h in m :
            for r in h :
                answer = max(answer, max(r))
        print(answer-1)

BFS()