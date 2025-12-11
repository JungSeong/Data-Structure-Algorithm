import sys
from itertools import combinations
INPUT = sys.stdin.readline

N, M = map(int, INPUT().split())
possible_combinations = combinations(range(1,N+1),M)
for row in possible_combinations :
    print(*row)