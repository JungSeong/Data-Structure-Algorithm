# 매일 각 부품 a, b, c개
# 매일 부품 검사, 하나라도 고장나면 오작동

import sys
from collections import defaultdict, deque

input = sys.stdin.readline
a, b, c = map(int, input().split())
N = int(input())
cases = deque()

for i in range(N) :
    i, j, k, r = map(int, input().split())
    if r == 1 :
        cases.appendleft((i, j, k, r))
    else :
        cases.append((i, j, k, r))

d = defaultdict(int)
for i in range(1, a+b+c+1) :
    d[i] = 2
d = dict(sorted(d.items()))

for i, j, k, r in cases :
    if r == 1 :
        d[i] = d[j] = d[k] = 1
    else :
        if d[i] == d[j] == 1 and d[k] == 2 :
            d[k] = 0
        elif d[i] == d[k] == 1 and d[j] == 2 :
            d[j] = 0
        elif d[j] == d[k] == 1 and d[i] == 2 :
            d[i] = 0

for k, v in d.items() :
    print(v)