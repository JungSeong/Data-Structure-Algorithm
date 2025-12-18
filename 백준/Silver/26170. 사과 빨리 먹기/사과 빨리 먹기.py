import sys
from collections import deque
INPUT = sys.stdin.readline

m = [list(map(int, INPUT().split())) for _ in range(5)]
cur_r, cur_c = map(int, INPUT().split())
move = ((-1,0), (0,1), (1,0), (0,-1))
answer = float('INF')

def BackTracking(cnt, moved, cur_r, cur_c) :
    if cnt == 3 :
        global answer
        answer = min(answer, moved)
        return
    for dr, dc in move :
        new_r, new_c = cur_r + dr, cur_c + dc
        temp = m[cur_r][cur_c]
        if 0<=new_r<5 and 0<=new_c<5 and m[new_r][new_c] != -1 :
            m[cur_r][cur_c] = -1
            if m[new_r][new_c] == 1 :
                BackTracking(cnt+1, moved+1, new_r, new_c)
            elif m[new_r][new_c] == 0 :
                BackTracking(cnt, moved+1, new_r, new_c)
            m[cur_r][cur_c] = temp
    return

BackTracking(0, 0, cur_r, cur_c)
if answer == float('INF') :
    print("-1")
else :
    print(answer)