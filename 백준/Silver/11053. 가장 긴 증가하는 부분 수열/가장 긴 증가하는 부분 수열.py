import sys
input = sys.stdin.readline

N = int(input())
dp = [0 for _ in range(N+1)]
st = [0] + list(map(int, input().split()))

for i in range(1, N+1) :
    for j in range(i) :
        if st[j] < st[i] :
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))