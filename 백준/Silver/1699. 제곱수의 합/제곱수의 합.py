import sys, math
input = sys.stdin.readline

N = int(input())
dp = [0] * (N+1)

for i in range(1, N+1) :
    si = int(math.sqrt(i))
    l = []
    for j in range(1,si+1) :
        l.append(dp[i-j**2]+1)
    dp[i] = min(l)

print(dp[-1])