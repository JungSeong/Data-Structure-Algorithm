# 안전 영역의 최대 크기, 0의 개수 = 안전 영역의 크기
# 3<=N,M<=8, BackTracking
import sys, copy
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]
start = []
safe_area = []
answer = 0

for i in range(N) :
    for j in range(M) :
        if m[i][j] == 2 :
            start.append((i, j))
        elif m[i][j] == 0 :
            safe_area.append((i,j))

move = [[-1,0],[0,1],[1,0],[0,-1]]

def BackTracking(cnt, start_idx) :
    if cnt == 3 : # 벽이 다 채워짐
        m2 = copy.deepcopy(m)
        safe = 0
        for row in start :
            cur_r, cur_c = row[0], row[1]
            q = deque()
            q.append([cur_r, cur_c])

            while q :
                cur_r, cur_c = q.popleft()
                for row in move :
                    new_r, new_c = cur_r + row[0], cur_c + row[1]
                    if 0<=new_r<N and 0<=new_c<M :
                        if m2[new_r][new_c] == 0 :
                            m2[new_r][new_c] = 2
                            q.append([new_r, new_c])
        for i in range(N) :
            for j in range(M) :
                if m2[i][j] == 0 : safe += 1

        global answer
        answer = max(answer, safe)
        return
    else :
        if start_idx < len(safe_area) :
            for i in range(start_idx, len(safe_area)) :
                r, c = safe_area[i]
                m[r][c] = 1
                BackTracking(cnt+1, i+1)
                m[r][c] = 0

BackTracking(0, 0)
print(answer)