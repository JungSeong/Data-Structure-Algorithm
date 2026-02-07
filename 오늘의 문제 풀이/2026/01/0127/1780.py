import sys
input = sys.stdin.readline

N = int(input())
l = [0]*3
m = list(list(map(int, input().split())) for _ in range(N))

def Paper(cur_r, cur_c, n, comp) :
    isOK = True
    for i in range(cur_r, cur_r + n) :
        for j in range(cur_c, cur_c + n) :
            if comp != m[i][j] :
                isOK = False
                break

    if not isOK :
        for i in range(3) :
            for j in range(3) :
                new_r, new_c = cur_r + i*n//3, cur_c + j*n//3
                Paper(new_r, new_c, n//3, m[new_r][new_c])
    else :
        l[comp+1] += 1

Paper(0, 0, N, m[0][0])

for row in l :
    print(row)