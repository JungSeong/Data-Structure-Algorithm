import sys
input = sys.stdin.readline

N = int(input())
m = [[' ' for _ in range(N)] for _ in range(N)]

def print_star(x, y, N) :
    if N == 1 :
        m[x][y] = "*"
        return
    n = N // 3
    for i in range(3) :
        for j in range(3) :
            if i == 1 and j == 1 :
                continue
            else :
                print_star(x+n*i, y+n*j, N//3)

print_star(0, 0, N)

for row in m :
    print(''.join(row))