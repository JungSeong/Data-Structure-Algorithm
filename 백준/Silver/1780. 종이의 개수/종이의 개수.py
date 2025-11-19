import sys
input = sys.stdin.readline

N = int(input())
m = [list(map(int, input().split())) for _ in range(N)]
cnt = [0,0,0] # -1, 0, 1

def paper(row, col, N) :
    init = m[row][col]
    for i in range(row, row+N) :
        for j in range(col, col+N) :
            if m[i][j] != init :
                h = N//3
                for k in range(3) :
                    for l in range(3) :
                        paper(row+k*h, col+l*h, h)
                return

    if init == -1 :
        cnt[0] += 1
    elif init == 0 :
        cnt[1] += 1
    else :
        cnt[2] += 1

paper(0, 0, N)
for i in cnt : print(i)