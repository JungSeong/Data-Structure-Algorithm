import sys
from itertools import combinations
INPUT = sys.stdin.readline

N, M = map(int, INPUT().split())
l = []

for i in range(1,N+1) :
    l.append(i)

for row in combinations(l, M) :
    print(row)