import sys
input = sys.stdin.readline

N = int(input())
m = [list(map(int, input().split())) for _ in range(N)]
cnt = [0, 0] # 0 = 하얀색, 1 = 파란색

def paper(row, col, N) :
    init = m[row][col]

    for i in range(row, row+N) :
        for j in range(col, col+N) :
            if m[i][j] != init :
                half = N//2
                for k in range(2) :
                    for l in range(2) :
                        paper(row+k*half, col+l*half, half)
                return

    if init == 0 :
        cnt[0] += 1
    else :
        cnt[1] += 1

paper(0, 0, N)
for i in cnt : print(i)