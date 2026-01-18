import sys
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

length1 = len(str1)
length2 = len(str2)
dp = [1]*length2

for i in range(length2) :
    for j in range(length1) :
        if str2[i] == str1[j] :
            dp[i] = max(dp[i]+1,)