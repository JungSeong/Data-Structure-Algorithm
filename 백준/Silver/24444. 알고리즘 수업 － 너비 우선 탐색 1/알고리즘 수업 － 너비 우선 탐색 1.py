import sys
from collections import deque, defaultdict
input = sys.stdin.readline

sys.setrecursionlimit(200000)
N, M, R = map(int, input().split())
d = defaultdict(list)

for i in range(M) :
    u, v = map(int, input().split())
    d[u].append(v)
    d[v].append(u)

for _, v in d.items() :
    v.sort()

visited = [False]*(N+1)
answer = [0]*(N+1)
cnt = 1

def BFS(R) :
    global cnt
    q = deque()
    visited[R] = True
    answer[R] = cnt
    q.append(R)

    while q :
        u = q.popleft()
        
        for v in d[u] :
            if not visited[v] :
                q.append(v)
                cnt += 1
                visited[v] = True
                answer[v] = cnt

BFS(R)
print("\n".join(map(str, answer[1:])))