from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
m = [list(map(int, input().strip())) for _ in range(N)]
move = [[-1,0],[0,1],[1,0],[0,-1]] #상,우,하,좌

def BFS(r, c) :
    q = deque()
    q.append([r, c])

    while q :
        cur_r, cur_c = q.popleft()
        if cur_r == N-1 and cur_c == M-1 :
            print(m[cur_r][cur_c])
            break
        for row in move :
            next_r = cur_r + row[0]
            next_c = cur_c + row[1]
            if 0<=next_r<N and 0<=next_c<M and m[next_r][next_c] == 1 :
                m[next_r][next_c] = m[cur_r][cur_c] + 1
                q.append([next_r,next_c])

BFS(0,0)