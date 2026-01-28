import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)

N = int(input())
m = list(list(map(int, input().strip())) for _ in range(N))
visited = [[False]*N for _ in range(N)]
move = [(-1,0), (0,1), (1,0), (0,-1)]
cnt = 0

def DFS(cur_r, cur_c) :
    global cnt
    visited[cur_r][cur_c] = True
    isOK = False

    for dr, dc in move :
        new_r, new_c = cur_r+dr, cur_c+dc
        if 0<=new_r<N and 0<=new_c<N :
            if m[new_r][new_c] == 1 and not visited[new_r][new_c] :
                cnt += 1
                DFS(new_r, new_c)

answer = []

for i in range(N) :
    for j in range(N) :
        if m[i][j] == 1 and not visited[i][j] :
            cnt = 1
            DFS(i, j)
            answer.append(cnt)

answer.sort()
print(len(answer))
print("\n".join(map(str, answer)))