import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
m = [list(map(int, input().strip())) for _ in range(N)]
move = [[-1,0],[0,1],[1,0],[0,-1]]

def BFS() :
    q = deque()
    q.append([0,0])

    while q :
        cur_r, cur_c = q.popleft()
        if cur_r == N-1 and cur_c == M-1 :
            print(m[cur_r][cur_c])
            break
        for row in move :
            new_r, new_c = cur_r + row[0], cur_c + row[1]
            if 0<=new_r<N and 0<=new_c<M :
                if m[new_r][new_c] == 1 :
                    m[new_r][new_c] = m[cur_r][cur_c] + 1
                    q.append([new_r, new_c])

BFS()