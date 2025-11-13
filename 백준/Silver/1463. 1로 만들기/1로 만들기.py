from collections import deque

def BFS(N, visited) :
    q = deque()
    q.append([N, 0])

    while q :
        n, cnt = q.popleft()
        if n == 1 :
            print(cnt)
            break
        visited[n] = True

        if n % 3 == 0 and visited[n//3] == False :
            visited[n//3] = True
            q.append([n//3, cnt+1])
        if n % 2 == 0 and visited[n//2] == False :
            visited[n//2] = True
            q.append([n//2, cnt+1])
        q.append([n-1, cnt+1])

N = int(input())
visited = [False] * (N+1)
BFS(N, visited)