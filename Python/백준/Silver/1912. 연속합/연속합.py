"""
하나는 선택
dp[i]는 dp[i-1]까지의 값을 더했을 때와 그렇지 않았을 때 중 더 큰 값을 더해야 함
"""

n = int(input())
dp = list(map(int, input().split()))

for i in range(n):
    if i > 0:
        dp[i] = max(dp[i - 1] + dp[i], dp[i])

print(max(dp))