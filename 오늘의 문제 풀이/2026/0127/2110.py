# 가장 인접한 두 공유기 사이의 최대 거리

import sys
input = sys.stdin.readline

N, C = map(int, input().split())
X = []
for i in range(N) :
    X.append(int(input()))
X.sort()

min_len, max_len = 1, X[-1]-X[0]

def get_min_max_length(min_len, max_len) :
    if min_len > max_len :
        return max_len

    before, cnt = 0, 0
    mid = (min_len+max_len)//2
    for i in range(len(X)) :
        if X[i] - X[before] >= mid :
            cnt += 1
            before = i
    if cnt >= C-1 :
        answer = get_min_max_length(mid+1, max_len)
    else :
        answer = get_min_max_length(min_len, mid-1)

    return answer

print(get_min_max_length(min_len, max_len))