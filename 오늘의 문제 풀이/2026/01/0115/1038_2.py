import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())
num = list()
l = range(0, 10)

for i in range(1, 11) :
    comb = combinations(l, i)
    for row in comb :
        row = list(row)
        row.sort(reverse=True)
        num.append(int("".join(map(str, row))))

num.sort()

if N < len(num) :
    print(num[N])
else :
    print(-1)