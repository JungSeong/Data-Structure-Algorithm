import sys
from collections import defaultdict
input = sys.stdin.readline

sys.setrecursionlimit(200000)
N, M, R = map(int, input().split())

d = defaultdict(list)

for i in range(M) :
    u, v = map(int, input().split())
    d[u].append(v)
    d[v].append(u)

for _, v in d.items() :
    v.sort(reverse=True)

visited = [False] * (N+1)
answer = [0] * (N+1)
cnt = 0

def DFS(R) :
    global cnt
    cnt += 1
    answer[R] = cnt
    visited[R] = True
    for v in d[R] :
        if not visited[v] :
            DFS(v)

DFS(R)
print("\n".join(map(str, answer[1:])))