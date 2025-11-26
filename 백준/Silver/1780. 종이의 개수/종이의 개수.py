import sys
input = sys.stdin.readline

N = int(input())
m = [list(map(int, input().split())) for _ in range(N)]
cnt = [0,0,0] # -1, 0, 1

def Paper(row, col, N) :
    idx = m[row][col]+1
    if N == 1 :
        cnt[idx] += 1
    else :
        init = m[row][col]
        isOK = True
        for i in range(row, row+N) :
            for j in range(col, col+N) :
                if init != m[i][j] :
                    isOK = False
                    break
        if isOK :
            cnt[idx] += 1
        else :
            for i in range(3) :
                for j in range(3) :
                    Paper(row+i*N//3, col+j*N//3, N//3)

Paper(0, 0, N)
for i in cnt :
    print(i)