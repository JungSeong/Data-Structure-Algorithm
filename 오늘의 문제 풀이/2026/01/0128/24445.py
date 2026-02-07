import sys
from collections import defaultdict, deque
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

cnt = 1
answer = [0]*(N+1)
visited = [False]*(N+1)

def BFS(R) :
    dq = deque()
    dq.append(R)
    global cnt
    visited[R] = True
    answer[R] = cnt

    while dq :
        u = dq.popleft()
        for v in d[u] :
            if not visited[v] :
                cnt += 1
                visited[v] = True
                answer[v] = cnt
                dq.append(v)

BFS(R)
print("\n".join(map(str, answer[1:])))