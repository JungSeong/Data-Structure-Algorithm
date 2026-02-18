import sys
INPUT = sys.stdin.readline

N = int(INPUT())
col = [0]*N
rd_diag = [0]*(2*N-1)
ld_diag = [0]*(2*N-1)

def DFS(cur_r) :
    if cur_r == N :
        return 1
    cnt = 0
    for i in range(N) :
        rd_idx = i-cur_r+N-1
        ld_idx = i+cur_r

        if col[i] == 0 and rd_diag[rd_idx] == 0 and ld_diag[ld_idx] == 0 :
            col[i] = rd_diag[rd_idx] = ld_diag[ld_idx] = 1
            cnt += DFS(cur_r+1)
            col[i] = rd_diag[rd_idx] = ld_diag[ld_idx] = 0

    return cnt

print(DFS(0))