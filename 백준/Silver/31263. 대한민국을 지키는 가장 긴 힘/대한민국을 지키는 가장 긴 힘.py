import sys
input = sys.stdin.readline

N = int(input())
S = input().rstrip()
cnt = 0
st = ""
dp = [float('inf')] * (N+1)
dp[0] = 0

for i in range(1, N+1) :
    for j in range(1, 4) :
        start = i-j
        if start >= 0 :
            ch = S[start:i]
            if ch[0] == "0" :
                continue
            if 1<=int(ch)<=641 :
                dp[i] = min(dp[start]+1, dp[i])

print(dp[-1])