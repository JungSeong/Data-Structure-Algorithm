import sys
input = sys.stdin.readline

N = int(input())
col = [0] * N
rd_diag = [0] * (2*N-1)
ld_diag = [0] * (2*N-1)

def NQueen(r) :
    if r == N :
        return 1
    cnt = 0
    for c in range(N) :
        ld_idx = r+c
        rd_idx = r-c+N-1
        if col[c] == 0 and ld_diag[ld_idx] == 0 and rd_diag[rd_idx] == 0 :
            col[c] = ld_diag[ld_idx] = rd_diag[rd_idx] = 1
            cnt += NQueen(r+1)
            col[c] = ld_diag[ld_idx] = rd_diag[rd_idx] = 0
    return cnt

print(NQueen(0))