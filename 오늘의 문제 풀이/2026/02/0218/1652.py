import sys
input = sys.stdin.readline

N = int(input())
m = list(list(input().rstrip()) for _ in range(N))
cnt_row, cnt_col = 0, 0

for row in m :
    cnt = 0
    for ch in row :
        if ch == '.' :
            cnt += 1
        else :
            if cnt >= 2 :
                cnt_row += 1
            cnt = 0
    if cnt >= 2 :
        cnt_row += 1
        cnt = 0
        
m_T = list(map(list, zip(*m)))

for col in m_T :
    cnt = 0
    for ch in col :
        if ch == '.' :
            cnt += 1
        else :
            if cnt >= 2 :
                cnt_col += 1
            cnt = 0
    if cnt >= 2 :
        cnt_col += 1
        cnt = 0
        
print(f"{cnt_row} {cnt_col}")