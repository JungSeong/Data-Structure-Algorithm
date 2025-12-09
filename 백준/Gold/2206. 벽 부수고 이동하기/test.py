import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]
visited = [[[0]*M for _ in range(N)] for _ in range(2)]
move = [[-1,0],[0,1],[1,0],[0,-1]]

def BFS() :
    cur_r, cur_c, cnt = 0, 0, 1
    q = deque()
    q.append([cur_r, cur_c, cnt])

    while q :
        cur_r, cur_c, cnt = q.popleft()
        # 벽을 부술 수 있을 때
        if cnt == 1 and visited[0][]
