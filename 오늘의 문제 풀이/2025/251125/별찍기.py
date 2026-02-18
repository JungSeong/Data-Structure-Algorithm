import sys
input = sys.stdin.readline

N = int(input())
m = [[' ']*N for _ in range(N)]

def print_star(row, col, N) :
    if N == 1 :
        m[row][col] = '*'
    else :
        for i in range(3) :
            for j in range(3) :
                if i == 1 and j == 1 :
                    continue
                else :
                    print_star(row+i*N//3, col+j*N//3, N//3)

print_star(0,0,N)

for row in m :
    print(''.join(row))