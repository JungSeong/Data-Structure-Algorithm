import sys
from collections import Counter, defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())
alphabets = []
for i in range(N) :
    word = input().rstrip()
    if len(word) >= M :
        alphabets.append(word)
    
cnt = Counter(alphabets)
answer = sorted(cnt.items(), key=lambda x : (-x[1],-len(x[0]),x[0]))

for row in answer :
    print(row[0])