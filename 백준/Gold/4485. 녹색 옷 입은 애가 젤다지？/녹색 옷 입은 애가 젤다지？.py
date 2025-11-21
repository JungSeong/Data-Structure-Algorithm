import sys, heapq
input = sys.stdin.readline
move = [[-1,0],[0,1],[1,0],[0,-1]]
num = 1

while True :
    N = int(input())
    if N == 0 : break
    else :
        m = [[0] * N for _ in range(N)]
        graph = [[[] for _ in range(N)] for _ in range(N)]
        for i in range(N) :
            row = list(map(int, input().split()))
            for j in range(N) :
                m[i][j] = row[j]

        start_r, start_c = 0, 0
        distances = [[float('inf')] * (N+1) for _ in range(N+1)]

        for cur_r in range(N) :
            for cur_c in range(N) :
                for row in move :
                    new_r, new_c = cur_r+row[0], cur_c+row[1]
                    if 0<=new_r<N and 0<=new_c<N :
                        graph[cur_r][cur_c].append([new_r, new_c,m[cur_r][cur_c]])

        def dijkstra() :
            distances[start_r][start_c] = 0
            pq = []
            heapq.heappush(pq, (0, 0, 0)) # 거리, start_r, start_c

            while pq :
                cur_dist, cur_r, cur_c = heapq.heappop(pq)
                if distances[cur_r][cur_c] < cur_dist :
                    continue

                for new_r, new_c, weight in graph[cur_r][cur_c] :
                    new_cost = cur_dist + weight
                    if new_cost < distances[new_r][new_c] :
                        distances[new_r][new_c] = new_cost
                        heapq.heappush(pq, (new_cost, new_r, new_c))

        dijkstra()
        print("Problem " + str(num) + ": " + str(distances[N-1][N-1]+m[N-1][N-1]))
        num += 1