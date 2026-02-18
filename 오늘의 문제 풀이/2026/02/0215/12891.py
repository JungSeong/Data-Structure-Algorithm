import sys
from collections import Counter
from itertools import combinations

input = sys.stdin.readline

len_S, len_P = map(int, input().split())
DNA = input().rstrip()
d = dict()
d["A"], d["C"], d["G"], d["T"] = map(int, input().split())
cnt = Counter(DNA)
canMake = True

for k, v in d.items() :
    if d[k] > cnt[k] :
        canMake = False

def Factorial(n) :
    if n >= 1 :
        return n * Factorial(n-1)
    else :
        return 1

if canMake :
    for k, v in cnt.items() :
        v -= d[k]
    l = range(sum(d.values()))
    num = len([combinations(l, len_P-sum(d.values()))])
    answer = num * Factorial(len_P)
    print(answer)
else :
    print(0)