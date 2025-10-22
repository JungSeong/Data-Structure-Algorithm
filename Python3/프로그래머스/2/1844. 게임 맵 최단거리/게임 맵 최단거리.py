# 최단거리 문제 -> BFS (큐로 구현)

from collections import deque

def bfs(i, j, n, m, cnt, maps, visited) :
    q = deque([(cnt, i, j)])
    visited[i][j] = True
    
    delta = [(1,0), (-1,0), (0,1), (0,-1)]
    
    while q :
        cnt, x, y = q.popleft()
        
        if x == n-1 and y == m-1 : return cnt
        
        for dx, dy in delta :
            nx = x + dy
            ny = y + dx
            
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] is False and maps[nx][ny] == 1 :
                q.append((cnt+1, nx, ny))
                visited[nx][ny] = True

def solution(maps):
    answer = -1
    i = 0
    j = 0
    
    n = len(maps) # 행의 크기
    m = len(maps[0]) # 열의 크기
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    result = bfs(i,j,n,m,1,maps,visited)
    if result is None : answer = -1
    else : answer = result
    
    return answer