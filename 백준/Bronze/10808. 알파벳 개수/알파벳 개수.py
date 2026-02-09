import sys
from collections import Counter
input = sys.stdin.readline

S = input().rstrip()
cnt = Counter(S)
answer = []

for i in range(ord('a'), ord('z')+1) :
    ch = chr(i)
    answer.append(cnt[ch])

print(' '.join(map(str, answer)))