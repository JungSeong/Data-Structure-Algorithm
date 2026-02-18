import sys
from itertools import combinations
INPUT = sys.stdin.readline

N, M = map(int, INPUT().split())
l = list(range(1, N+1))
comb = combinations(l, M)

print(comb)

for row in comb :
    print(' '.join(map(str, row)))