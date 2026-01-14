# 항체는 현재 속한 칸과 같은 데이터 가짐 + 인접 칸으로 퍼짐

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
before = list(list(map(int, input().split())) for _ in range(N))
after = list(list(map(int, input().split())) for _ in range(N))
move = [(-1,0), (0,1), (1,0), (0,-1)]

def check(r, c) :
    for dr, dc in move :
        new_r, new_c = r + dr, c + dc
        if 0<=new_r<N and 0<=new_c<M and isVisited[new_r][new_c] is not True :
            if before[r][c] == before[new_r][new_c] :
                isVisited[new_r][new_c] = True
                check(new_r, new_c)

for row in range(N) :
    for col in range(M) :
        r, c = row, col
        isVisited = [[False] * M for _ in range(N)]
        isVisited[r][c] = True
        check(r, c)
        target_val = after[r][c]
        isOK = True

        for i in range(N) :
            for j in range(M) :
                if isVisited[i][j] :
                    if target_val != after[i][j] :
                        isOK = False
                        break
                if not isVisited[i][j] :
                    if before[i][j] != after[i][j] :
                        isOK = False
                        break
            if not isOK :
                break

        if isOK :
            print("YES")
            sys.exit()

print("NO")