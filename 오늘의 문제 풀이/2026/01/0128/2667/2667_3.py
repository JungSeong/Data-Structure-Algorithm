import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(200000)

N = int(input())
m = list(list(map(int, input().strip())) for _ in range(N))
move = [(-1,0), (0,1), (1,0), (0,-1)]

def BFS(cur_r, cur_c) :
    cnt = 0
    dq = deque()
    m[cur_r][cur_c] = 0
    dq.append((cur_r, cur_c))
    cnt += 1

    while dq :
        cur_r, cur_c = dq.popleft()
        for dr, dc in move :
            new_r, new_c = cur_r + dr, cur_c + dc
            if 0<=new_r<N and 0<=new_c<N :
                if m[new_r][new_c] == 1 :
                    m[new_r][new_c] = 0
                    cnt += 1
                    dq.append((new_r, new_c))
    
    return cnt

answer = []

for i in range(N) :
    for j in range(N) :
        if m[i][j] == 1 :
            answer.append(BFS(i, j))

answer.sort()

print(len(answer))
print("\n".join(map(str, answer)))