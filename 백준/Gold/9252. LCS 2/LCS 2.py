import sys
input = sys.stdin.readline

str1 = " " + input().rstrip()
str2 = " " + input().rstrip()
n, m = len(str1), len(str2)
dp = [[0]*m for _ in range(n)]
record = []

for i in range(1, n) :
    for j in range(1, m) :
        if str1[i] == str2[j] :
            dp[i][j] = dp[i-1][j-1] + 1
        else :
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])

if dp[-1][-1] > 0 :
    result = []
    cur_r, cur_c = n-1, m-1

    while dp[cur_r][cur_c] > 0 :
        if dp[cur_r-1][cur_c] == dp[cur_r][cur_c] :
            cur_r -= 1
        elif dp[cur_r][cur_c-1] == dp[cur_r][cur_c] :
            cur_c -= 1
        else :
            result.append(str1[cur_r])
            cur_r -= 1
            cur_c -=1

    print(''.join(reversed(result)))