import sys
from collections import Counter
input = sys.stdin.readline

word = input().rstrip()
cnt = Counter(word)
odd_sum = 0
odd = ""

for k, v in cnt.items() :
    if v%2==1 :   
        odd_sum += 1
        odd = k

if odd_sum >= 2 :
    print("I'm Sorry Hansoo")
    sys.exit(0)
else :
    half, answer = [], []
    for k, v in cnt.items() :
        for j in range(v//2) :
            half.append(k)
        v -= v//2
    half.sort()
    answer.extend(half)
    if odd :
        answer.append(odd)
    answer.extend(reversed(half))

    print(''.join(map(str, answer)))