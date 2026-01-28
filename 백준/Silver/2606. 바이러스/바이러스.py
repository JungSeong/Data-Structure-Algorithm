import sys
from collections import defaultdict
input = sys.stdin.readline

sys.setrecursionlimit(200000)

N = int(input())
M = int(input())

d = defaultdict(list)

for i in range(M) :
    u, v = map(int, input().split())
    d[u].append(v)
    d[v].append(u)

visited = [False]*(N+1)

def DFS(R) :
    visited[R] = True

    for v in d[R] :
        if not visited[v] :
            DFS(v)

DFS(1)
print(sum(visited)-1)