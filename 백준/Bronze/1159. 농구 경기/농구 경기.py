import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
names = [] 
for i in range(N) :
    names.append(input().rstrip()[0])

d = Counter(names)
answer = []

for k, v in d.items() :
    if v>=5 : 
        answer.append(k)
        
if len(answer)>0 :
    print(''.join(sorted(answer)))
else :
    print("PREDAJA")