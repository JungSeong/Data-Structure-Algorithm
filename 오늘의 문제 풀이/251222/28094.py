import sys
INPUT = sys.stdin.readline

T = int(INPUT())

for i in range(T) :
    N, M = map(int, INPUT().split())
    score_info = [[] for _ in range(N+1)]
    for _ in range(M) :
        v, a, b = map(int, INPUT().split())
        score_info[b].append((v,a))
    
    dp = [-1] * (1 << N)
    count = [0] * (1 << N)

    dp[0] = 0
    count[0] = 1

    for mask in range(1 << N) :
        if dp[mask] == -1 : continue

        for i in range(N) :
            if not (mask & (1 << i)) :
                