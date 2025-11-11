N = int(input())
answer = 0
dp = [0,0,0]

for i in range(1, N + 1):
    s = input().split()
    RGB = list(map(int, s))

    if i > 1 :
        RGB[0] += min(dp[1], dp[2])
        RGB[1] += min(dp[0], dp[2])
        RGB[2] += min(dp[0], dp[1])

    dp = RGB

answer = min(dp)
print(answer)