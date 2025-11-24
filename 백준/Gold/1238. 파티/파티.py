import sys, heapq
input = sys.stdin.readline

N, M, X = map(int, input().split())
dist = [[float('inf')] * (N+1) for _ in range(N+1)]

graph = [[] for _ in range(N+1)]

for i in range(M) :
    s, e, w = map(int, input().split())
    graph[s].append((e,w))

def dijkstra(S) :
    dist[S][S] = 0
    pq = []
    heapq.heappush(pq, (0,S))

    while pq :
        cur_dist, cur_node = heapq.heappop(pq)
        if dist[S][cur_node] < cur_dist :
            continue

        for new_node, added_dist in graph[cur_node] :
            if dist[S][new_node] > cur_dist + added_dist :
                dist[S][new_node] = cur_dist + added_dist
                heapq.heappush(pq, (cur_dist + added_dist, new_node))

for i in range(1, N+1) :
    dijkstra(i)

answer = 0
for i in range(1,N+1) :
    answer = max(answer, dist[i][X]+dist[X][i])

print(answer)