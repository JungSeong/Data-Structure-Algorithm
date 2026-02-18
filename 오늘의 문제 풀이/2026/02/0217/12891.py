import sys
from collections import defaultdict
input = sys.stdin.readline

S, P = map(int, input().split())
DNA = input().rstrip()
d = dict()
comp = defaultdict(int)
answer = 0

d["A"], d["C"], d["G"], d["T"] = map(int, input().split())
for i in range(P) :
    comp[DNA[i]] += 1

for i in range(len(DNA)-P+1) :
    isOK = True
    if i >= 1 :
        comp[DNA[i-1]] -= 1
        comp[DNA[P-1+i]] += 1

    for k, v in d.items() :
        if v > 0 and k not in d.keys() or d[k] > comp[k] :
            isOK = False
            break

    if isOK :
        answer += 1

print(answer)
