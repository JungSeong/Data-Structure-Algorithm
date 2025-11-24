import sys
input = sys.stdin.readline

N, T = map(int, input().split())
l = []

for i in range(N) :
    K, S = map(int, input().split())
    l.append((K, S))

dp = [0] * (T+1)

for K, S in l :
    for i in range(T, K-1, -1) :
        dp[i] = max(dp[i], dp[i-K]+S)

print(max(dp))