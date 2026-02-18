import sys, heapq
INPUT = sys.stdin.readline

N, M, X = map(int, INPUT().split())
dir = [[] for _ in range(N+1)]

for i in range(M) :
    s, e, t = map(int, INPUT().split())
    dir[s].append((e,t))

def Dijkstra() :
    q = []
    heapq.heappush(q, )