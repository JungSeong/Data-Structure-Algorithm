import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
m = [list(map(int, input().strip())) for _ in range(N)]
move = [[-1,0], [0,1], [1,0], [0,-1]]

def BFS() :
    q = deque()
    cur_r, cur_c, broken = 0, 0, 0
    q.append([cur_r, cur_c, broken])
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)] # 0열 : 하나도 부수지 않은 세상, 1열 : 하나 부순 세상
    visited[cur_r][cur_c][0] = visited[cur_r][cur_c][1] = 1

    while q :
        cur_r, cur_c, broken = q.popleft()
        if cur_r == N-1 and cur_c == M-1 :
            print(visited[cur_r][cur_c][broken])
            return
        for row in move :
            new_r = cur_r + row[0]
            new_c = cur_c + row[1]
            if 0<=new_r<N and 0<=new_c<M :
                if m[new_r][new_c] == 0 and visited[new_r][new_c][broken] == 0 : # 벽이 아니고 방문 안함
                    visited[new_r][new_c][broken] = visited[cur_r][cur_c][broken] + 1
                    q.append([new_r, new_c, broken])
                if m[new_r][new_c] == 1 and broken == 0 : # 벽이고 하나 더 부술 수 있음
                    visited[new_r][new_c][1] = visited[cur_r][cur_c][broken] + 1
                    q.append([new_r, new_c, 1])

    print(-1)

BFS()