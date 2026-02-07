import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
m = list(list(input().strip()) for _ in range(N))

case1 = [[0]*(M+1) for _ in range(N+1)] #BWBWBWBW

for i in range(1, N+1) :
    for j in range(1, M+1) :
        if i%2!=0 :
            if j%2!=0 :
                if m[i-1][j-1] == "B" :
                    case1[i][j] += case1[i-1][j] + case1[i][j-1] - case1[i-1][j-1]
                else :
                    case1[i][j] += case1[i-1][j] + case1[i][j-1] - case1[i-1][j-1] + 1
            else :
                if m[i-1][j-1] == "W" :
                    case1[i][j] += case1[i-1][j] + case1[i][j-1] - case1[i-1][j-1]
                else :
                    case1[i][j] += case1[i-1][j] + case1[i][j-1] - case1[i-1][j-1] + 1
        else :
            if j%2!=0 :
                if m[i-1][j-1] == "W" :
                    case1[i][j] += case1[i-1][j] + case1[i][j-1] - case1[i-1][j-1]
                else :
                    case1[i][j] += case1[i-1][j] + case1[i][j-1] - case1[i-1][j-1] + 1
            else :
                if m[i-1][j-1] == "B" :
                    case1[i][j] += case1[i-1][j] + case1[i][j-1] - case1[i-1][j-1]
                else :
                    case1[i][j] += case1[i-1][j] + case1[i][j-1] - case1[i-1][j-1] + 1

answer = float('inf')

for i in range(N-K+1) :
    for j in range(M-K+1) :
        cnt = case1[i+K][j+K]-case1[i+K][j]-case1[i][j+K]+case1[i][j]
        comp = min(cnt, N*M-cnt)
        answer = min(answer, comp)

print(answer)