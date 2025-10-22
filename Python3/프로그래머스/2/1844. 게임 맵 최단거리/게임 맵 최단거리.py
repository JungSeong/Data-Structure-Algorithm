# 최단거리 -> BFS로 풀이할 것

from collections import deque

def BFS(i, j, cnt, maps, visited, m, n) :
    q = deque([(i, j, cnt)])
    move_list = ([1,0], [-1,0], [0,1], [0,-1])
    visited[i][j] = True
    
    while q :
        cur_i, cur_j, cnt = q.popleft()

        if cur_i == n-1 and cur_j == m-1 : return cnt

        for move in move_list :
            dx, dy = move

            nx = cur_i + dx
            ny = cur_j + dy

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False and maps[nx][ny] == 1 :
                q.append([nx, ny, cnt+1])
                visited[nx][ny] = True
                
def solution(maps):
    answer = 0
    i = 0
    j = 0
    cnt = 1
    
    m = len(maps[0])
    n = len(maps)
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    cnt = BFS(i, j, cnt, maps, visited, m, n)
    
    if cnt == None : cnt = -1
    
    return cnt