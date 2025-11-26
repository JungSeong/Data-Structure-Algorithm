import sys
input = sys.stdin.readline

N = int(input())
m = [list(map(str, input().strip())) for _ in range(N)]
l = []

def QuadTree(row, col, N) :
    if N == 1 :
        l.append(m[row][col])
        return
    else :
        init = m[row][col]
        isOkay = True
        for i in range(row, row+N) :
            for j in range(col, col+N) :
                if init != m[i][j] :
                    isOkay = False
                    break
        if isOkay :
            l.append(init)
        else :
            l.append('(')
            for i in range(2) :
                for j in range(2) :
                    QuadTree(row+i*N//2, col+j*N//2, N//2)
            l.append(')')

QuadTree(0,0, N)
print(''.join(l))