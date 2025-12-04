import sys
from itertools import combinations
INPUT = sys.stdin.readline

N, M = map(int, INPUT().split())
l = []
for i in range(1, N+1) :
    l.append(i)

comb = combinations(l, M)

for row in comb :
    print(' '.join(map(str, row)))