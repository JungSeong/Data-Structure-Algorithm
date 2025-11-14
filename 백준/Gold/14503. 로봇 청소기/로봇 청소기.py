"""
0 : 청소 안됨 + 움직일 수 있음, 1 : 벽, 2 : 청소 됨 + 움직일 수 있음
주변 4칸 중 청소되지 않은 빈칸 X -> 벽 없으면 현재 방향에서 후진, 있으면 멈춤
주변 4칸 중 청소되지 않은 빈칸 O -> 반시계 90도 -> 앞쪽 칸이 드러우면 전진 or 아니면 다시 반시계
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 방의 크기 N, M
r, c, d = map(int, input().split()) # 칸의 좌표 (r, c) + 바라보는 방향 d

move = [[-1,0],[0,1],[1,0],[0,-1]] # 북, 동, 남, 서
m = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N) :
    m[i] = list(map(int, input().split()))

cleaned = 0

while True :
    if m[r][c] == 0 :
        # 현재 칸 청소
        m[r][c] = 2
        cleaned += 1

    # 주변 칸 중 청소되지 않은 빈칸 X
    if m[r-1][c] != 0 and m[r+1][c] != 0 and m[r][c-1] != 0 and m[r][c+1] != 0 :
        new_r = r - move[d][0]
        new_c = c - move[d][1]
        if m[new_r][new_c] != 1 : # 벽이 아니라면
            r, c = new_r, new_c
        else : # 벽이라면
            break
    else : # 주변 칸 중 청소되지 않은 빈칸 O
        while True :
            d = (d-1)%4
            new_r = r + move[d][0]
            new_c = c + move[d][1]
            if m[new_r][new_c] == 0 :
                r, c = new_r, new_c
                break

print(cleaned)