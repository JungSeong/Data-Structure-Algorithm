import sys
INPUT = sys.stdin.readline

N, T = map(int, INPUT().split())
dp = [0] * (T+1)
for i in range(N) :
    K, S = map(int, INPUT().split())
    for j in range(T,K-1,-1) :
        dp[j] = max(dp[j], dp[j-K]+S)

print(max(dp))