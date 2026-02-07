import sys
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

len1, len2 = len(str1), len(str2)
LCS = [[0]*(len2+1) for _ in range(len1+1)]

for i in range(1, len1+1) :
    for j in range(1, len2+1) :
        if str1[i-1] == str2[j-1] :
            LCS[i][j] = LCS[i-1][j-1] + 1
        else :
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

answer = 0
for row in LCS :
    comp = max(row)
    answer = max(answer, comp)

print(answer)