import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().rstrip()
result = 0
dp = [0]*M

for i in range(M) :
    if S[i] == "I" :
        if i == 0 : 
            dp[i] = 1
        else :
            if S[i-1] == "O" :
                dp[i] = dp[i-1]+1
            else :
                dp[i] = 1
    else :
        if i>0 and S[i-1] == "I" :
            dp[i] = dp[i-1]+1

comp = 1+2*N
for i in range(len(dp)) :
    if dp[i] >= comp and dp[i]%2==1 :
        result += 1

print(result)