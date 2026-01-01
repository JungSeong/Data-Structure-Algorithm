# k, ti (과목의 수업이 진행되는 교시)
# p, qi (비어 있는 교시)

import sys
input = sys.stdin.readline

N = int(input())
s, bs = [], []
for i in range(N) :
    k_t = list(map(int, input().split()))
    s.append(set(k_t[1:]))

M = int(input())
for j in range(M) :
    p_q = list(map(int, input().split()))
    bs.append(set(p_q[1:]))

answer = [0] * M

for i in range(N) :
    for j in range(M) :
        if s[i] | bs[j] == bs[j] :
            answer[j] += 1

for i in range(M) :
    print(answer[i])