import sys
input = sys.stdin.readline

S = input().rstrip()
answer = []

for i in range(len(S)) :
    answer.append(S[i:])

answer.sort()
for row in answer :
    print(row)