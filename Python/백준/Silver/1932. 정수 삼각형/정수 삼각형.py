n = int(input())
dp = []

for i in range(1, n + 1):
    s = list(map(int, input().split()))

    if i == 1:
        dp.append(s)
    else:
        for j in range(len(s)):
            if j == 0:
                s[0] += dp[-1][0]
            elif j == len(s) - 1:
                s[len(s) - 1] += dp[-1][-1]
            else:
                s[j] += max(dp[-1][j - 1], dp[-1][j])

        dp.append(s)

print(max(dp[-1]))