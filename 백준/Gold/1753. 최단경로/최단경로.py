import sys, heapq
input = sys.stdin.readline

V, E = map(int, input().split()) # 정점의 수, 간선의 수
K = int(input())
dist = [float('inf')] * (V+1)
graph = [[] for _ in range(V+1)]

for i in range(E) :
    u, v, w = map(int, input().split()) # 시작 정점, 도착 정점, 가중치
    graph[u].append((v,w))

def dijkstra() :
    dist[K] = 0
    pq = []
    heapq.heappush(pq, (0, K)) # 현재까지 거리, 노드

    while pq :
        cur_dist, cur_node = heapq.heappop(pq)
        if dist[cur_node] < cur_dist :
            continue

        for new_node, added_dist in graph[cur_node] :
            if dist[new_node] > cur_dist + added_dist :
                dist[new_node] = cur_dist + added_dist
                heapq.heappush(pq, (cur_dist+added_dist, new_node))

dijkstra()
for i in range(1,V+1) :
    if dist[i] == float('inf') :
        print("INF")
    else :
        print(dist[i])