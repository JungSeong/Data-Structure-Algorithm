import sys
input = sys.stdin.readline

N = int(input())
col = [0] * N
rd_diag = [0] * (2*N-1)
ld_diag = [0] * (2*N-1)

cnt = 0

def BackTracking(r) :
    if r == N :
        return 1
    cnt = 0
    for i in range(N) :
        rd_idx = i-r+N-1
        ld_idx = i+r
        col_idx = i
        if col[col_idx] != 1 and rd_diag[rd_idx] != 1 and ld_diag[ld_idx] != 1 :
            col[col_idx] = rd_diag[rd_idx] = ld_diag[ld_idx] = 1
            cnt += BackTracking(r+1)
            col[col_idx] = rd_diag[rd_idx] = ld_diag[ld_idx] = 0

    return cnt

cnt = BackTracking(0)
print(cnt)