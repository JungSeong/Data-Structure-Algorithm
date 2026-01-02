# 1초씩 초록불이 켜짐, 꺼짐과 동시에 다음 신호등의 초록불이 켜짐
# 1번에서 시작, M번이 도착
# 인도, 횡단보도 걷는 시간 무시

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

c_t, cw_t = 0, 0

for i in range(1, M) :
    last_idx = -1
    for j in range(len(A)) :
        if A[j] > last_idx :
            c_t += j
        else :
            c_t += j + len(A)

print(c_t)