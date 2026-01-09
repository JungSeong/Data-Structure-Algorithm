# 학생이 현재 위치 (r, c)에서 세 번 이하의 이동으로 사과를 2개 이상 -> 1 아니면 0

import sys
input = sys.stdin.readline

m = [list(map(int, input().split())) for _ in range(5)]
move = [(-1,0), (0,1), (1,0), (0,-1)]
r, c = map(int, input().split())
isOK = False

def DFS(r, c, moved, eaten) :
    if moved <= 3 and eaten >= 2 :
        global isOK
        isOK = True
        return
    for dr, dc in move :
        new_r, new_c = r+dr, c+dc
        temp = m[r][c]
        if 0<=new_r<5 and 0<=new_c<5 :
            if m[new_r][new_c] == 1 :
                m[r][c] = -1
                DFS(new_r, new_c, moved+1, eaten+1)
                m[r][c] = temp
            elif m[new_r][new_c] == 0 :
                m[r][c] = -1
                DFS(new_r, new_c, moved+1, eaten)
                m[r][c] = temp

DFS(r, c, 0, 0)
if isOK : print(1)
else : print(0)