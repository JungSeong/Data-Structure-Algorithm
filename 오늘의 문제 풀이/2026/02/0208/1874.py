import sys
input = sys.stdin.readline

s = []
n = int(input())
result = []
nums = list(range(1, n+1))

for i in range(n) :
    result.append(int(input()))

idx = 0
answer = []
for i in range(1, n+1) :
    s.append(i)
    answer.append("+")
    while len(s)>0 and s[-1] == result[idx] :
        s.pop()
        answer.append("-")
        idx += 1

if len(s) != 0 :
    print("NO")
else :
    for row in answer :
        print(row)