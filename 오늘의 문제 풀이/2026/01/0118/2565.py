# 없애야 하는 전기줄의 최소 개수 (100이하)
# 위치의 번호 500이하

import sys
input = sys.stdin.readline

N = int(input())
dp_up = [1]*N

l = []
for i in range(N) :
    Ai, Bi = map(int, input().split())
    l.append((Ai, Bi))

l.sort()

for i in range(N) :
    for j in range(i) :
        if l[j][1] < l[i][1] :
            dp_up[i] = max(dp_up[j]+1, dp_up[i])

print(N-max(dp_up))