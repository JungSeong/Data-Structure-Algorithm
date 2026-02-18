import sys
input = sys.stdin.readline

N, M = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
move = [(-1,0), (0,1), (1,0), (0,-1)]

answer1, answer2 = -1, -1

def DFS(cur_r, cur_c, cnt, points) :
    global answer1
    global answer2
    if cnt == 4 :
        return points
    for dr, dc in move :
        new_r, new_c = cur_r+dr, cur_c+dc
        if 0<=new_r<N and 0<=new_c<M and not visited[new_r][new_c] :
            if cnt == 2 :
                visited[new_r][new_c] = True
                answer1 = max(answer1, DFS(cur_r, cur_c, cnt+1, points+m[new_r][new_c]))
                visited[new_r][new_c] = False
            visited[new_r][new_c] = True
            answer2 = max(answer2, DFS(new_r, new_c, cnt+1, points+m[new_r][new_c]))
            visited[new_r][new_c] = False
            
    return max(answer1, answer2)

answer = -1
for i in range(N) :
    for j in range(M) :
        visited[i][j] = True
        answer = max(DFS(i, j, 1, m[i][j]), answer)
        visited[i][j] = False
        
print(answer)