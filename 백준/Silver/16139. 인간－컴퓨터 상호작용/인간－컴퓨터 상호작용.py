import sys
from collections import defaultdict, Counter

input = sys.stdin.readline

st = input().rstrip()
S = dict(Counter())
S[0] = Counter()

for i in range(1, len(st)+1) :
    S[i] = Counter(st[:i])

q = int(input())

for i in range(q) :
    ai, li, ri = input().split()
    li, ri = int(li), int(ri)
    print(S[ri+1][ai]-S[li][ai])