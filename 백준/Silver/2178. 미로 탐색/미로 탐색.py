from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
m = [list(map(int, input().strip())) for i in range(N)]
visited = [[False] * M for i in range(N)]

move = [[-1,0],[0,1],[1,0],[0,-1]] # 상,하,좌,우

def BFS(r, c, cnt) :
    q = deque()
    q.append([r, c, cnt])

    while True :
        start_r, start_c, cnt = q.popleft()
        if start_r == N-1 and start_c == M-1 :
            print(cnt)
            break
        for row in move :
            dr, dc = row[0], row[1]
            new_r = start_r+dr
            new_c = start_c+dc
            if 0<=new_r<N and 0<=new_c<M and m[new_r][new_c] == 1 and visited[new_r][new_c] != True:
                visited[new_r][new_c] = True
                q.append([start_r+dr, start_c+dc, cnt+1])

BFS(0,0,1)