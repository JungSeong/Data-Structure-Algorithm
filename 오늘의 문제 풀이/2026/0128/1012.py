import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)

T = int(input())

move = [(-1,0), (0,1), (1,0), (0,-1)]
answer = []

for i in range(T) :
    M, N, K = map(int, input().split())
    m = [[0]*M for _ in range(N)]

    def DFS(cur_r, cur_c) :
        m[cur_r][cur_c] = 0
        answer = 1

        for dr, dc in move :
            new_r, new_c = cur_r + dr, cur_c + dc
            if 0<=new_r<N and 0<=new_c<M :
                if m[new_r][new_c] == 1 :
                    answer += DFS(new_r, new_c)

        return answer

    for j in range(K) :
        x, y = map(int, input().split())
        m[y][x] = 1

    counts = []

    for r in range(N) :
        for c in range(M) :
            if m[r][c] == 1 :
                cnt = DFS(r, c)
                counts.append(cnt)
    
    answer.append(len(counts))

print("\n".join(map(str, answer)))