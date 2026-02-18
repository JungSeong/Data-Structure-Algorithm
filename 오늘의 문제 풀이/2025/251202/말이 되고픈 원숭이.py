import sys
from collections import deque
INPUT = sys.stdin.readline

K = int(INPUT())
W, H = map(int, INPUT().split())
l = [list(map(int, INPUT().split())) for _ in range(H)]
m = [[row[:] for row in l] for _ in range(K+1)]

monkey_move = [(-1,0),(0,1),(1,0),(0,-1)]
horse_move = [(-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2)]

def BFS(cnt, cur_r, cur_c) :
    q = deque()
    q.append([cnt, cur_r, cur_c])
    m[cnt][cur_r][cur_c] = 1

    while q :
        cnt, cur_r, cur_c = q.popleft()
        if cur_r == H-1 and cur_c == W-1 :
            print(m[cnt][cur_r][cur_c]-1)
            return
        if cnt > 0 :
            for dr, dc in horse_move :
                new_r, new_c = cur_r + dr, cur_c +dc
                if 0<=new_r<H and 0<=new_c<W and m[cnt-1][new_r][new_c] == 0 :
                    m[cnt-1][new_r][new_c] = m[cnt][cur_r][cur_c] + 1
                    q.append([cnt-1, new_r, new_c])
        for dr, dc in monkey_move :
            new_r, new_c = cur_r + dr, cur_c + dc
            if 0<=new_r<H and 0<=new_c<W and m[cnt][new_r][new_c] == 0 :
                m[cnt][new_r][new_c] = m[cnt][cur_r][cur_c] + 1
                q.append([cnt, new_r, new_c])

    print(-1)

BFS(K, 0, 0)