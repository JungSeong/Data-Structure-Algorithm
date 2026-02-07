# 계란은 내구도와 무게가 정해짐, 각 계란의 내구도 -= 상대 계란의 무게
# 내구도 <=0 계란 깨짐
# 일렬로 놓인 계란에 대해 왼쪽부터 차례로 들어 한번씩만 다른 계란을 쳐 많은 계란 깨기

import sys
input = sys.stdin.readline

N = int(input())
eggs = list(list(map(int, input().split())) for _ in range(N))

def BackTracking(i) :
    if i == len(eggs) :
        cnt = 0
        for d, w in eggs :
            if d <= 0 : cnt += 1
        return cnt
    answer = 0
    di, wi = eggs[i]
    if di>0 : # 계란이 깨지지 않은 경우
        isPossible = False
        for j in range(N) :
            if j != i :
                dj, wj = eggs[j]
                if dj > 0 : # 깨지지 않은 계란이 있는 경우
                    isPossible = True
                    eggs[i][0] -= eggs[j][1]
                    eggs[j][0] -= eggs[i][1]
                    answer = max(answer, BackTracking(i+1))
                    eggs[i][0] += eggs[j][1]
                    eggs[j][0] += eggs[i][1]
                if not isPossible : # 모든 계란이 깨진 경우
                    answer = max(answer, BackTracking(i+1))
    else : # 계란이 깨진 경우
        answer = max(answer, BackTracking(i+1))

    return answer

print(BackTracking(0))