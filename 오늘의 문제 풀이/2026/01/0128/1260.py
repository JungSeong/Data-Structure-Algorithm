import sys
from collections import deque, defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(200000)

d = defaultdict(list)

N, M, V = map(int, input().split())
for i in range(M) :
    u, v = map(int, input().split())
    d[u].append(v)
    d[v].append(u)

for _, v in d.items() :
    v.sort()

visited_dfs = [False]*(N+1)
visited_bfs = [False]*(N+1)

dfs = []
bfs = []

def DFS(R) :
    dfs.append(R)
    visited_dfs[R] = True

    if d[R] is None :
        return

    for v in d[R] :
        if not visited_dfs[v] :
            DFS(v)

def BFS(R) :
    dq = deque()
    dq.append(R)
    visited_bfs[R] = True
    bfs.append(R)

    while dq :
        u = dq.popleft()
        if d[u] is None :
            return
        for v in d[u] :
            if not visited_bfs[v] :
                visited_bfs[v] = True
                bfs.append(v)
                dq.append(v)

DFS(V)
BFS(V)

print(*dfs)
print(*bfs)