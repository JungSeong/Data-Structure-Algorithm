import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [1] * N

if N > 1 :
    for i in range(N) :
        for j in range(i) :
            if A[j] < A[i] :
                dp[i] = max(dp[j]+1, dp[i])

print(max(dp))