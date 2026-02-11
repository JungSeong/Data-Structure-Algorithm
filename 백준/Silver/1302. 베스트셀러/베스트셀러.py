import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
titles = [input().rstrip() for _ in range(N)]

cnt = Counter(titles)
high_val = max(cnt.values())

answer = []

for k, v in cnt.items() :
    if v == high_val : answer.append(k)

print(sorted(answer)[0]) 