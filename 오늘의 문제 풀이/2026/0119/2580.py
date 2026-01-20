import sys
input = sys.stdin.readline

m = list(list(map(int, input().split())) for _ in range(9))

row_check = [[False]*10 for _ in range(9)]
col_check = [[False]*10 for _ in range(9)]
box_check = [[False]*10 for _ in range(9)]

zeros = []
for i in range(9) :
    for j in range(9) :
        num = m[i][j]
        if num != 0 :
            row_check[i][num] = True
            col_check[j][num] = True
            box_check[i//3*3+j//3][num] = True
        else :
            zeros.append((i, j))

def BackTracking(cur) :
    if cur == len(zeros) :
        for row in m :
            print(*row)
        sys.exit(0)
    r, c = zeros[cur]
    box_idx = r//3*3+c//3
    for num in range(1, 10) :
        if not row_check[r][num] and not col_check[c][num] and not box_check[box_idx][num] :
            row_check[r][num] = col_check[c][num] = box_check[box_idx][num] = True
            m[r][c] = num
            BackTracking(cur+1)
            row_check[r][num] = col_check[c][num] = box_check[box_idx][num] = False
            m[r][c] = 0
            
BackTracking(0)