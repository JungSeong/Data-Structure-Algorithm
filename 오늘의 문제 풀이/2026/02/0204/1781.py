# 각 초마다 한 문제를 푸는데, 현재 데드라인 기준 가장 많은 개수의 컵라면을 더해나가면 됨

import sys, heapq
input = sys.stdin.readline

N = int(input())
answer = 0
ramyen = []

for i in range(N) :
    deadlines, cup_num = map(int, input().split())
    ramyen.append((deadlines, cup_num))

ramyen.sort(reverse=True)

possible = []
day = ramyen[0][0]
last = 0

for i in range(day, 0, -1) :
    while True :
        if 0<=last<len(ramyen) and ramyen[last][0] >= i :
            cnt = ramyen[last][1]
            heapq.heappush(possible, -cnt)
            last += 1
        else :
            break

    if possible :
        answer += -heapq.heappop(possible)

print(answer)