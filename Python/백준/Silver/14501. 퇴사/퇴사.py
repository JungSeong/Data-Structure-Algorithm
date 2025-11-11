"""
1일에 한 경우 & 안 한 경우
2일에 한 경우 & 안 한 경우

해당 날짜 + 해당 날짜의 Ti <= N : 가능
아니면 불가능

day가 해당 배열의 길이를 넘어서면 dfs 종료
"""

import sys
input = sys.stdin.readline

answer = []

def main() :
    N = int(input())
    schedule = [[0,0]] # Ti, Pi
    for i in range(N) :
        s = list(map(int, input().split()))
        schedule.append(s)

    Pi = 0
    day = 1
    dfs(schedule, Pi, day)
    print(max(answer))

def dfs(schedule, Pi, day) :
    if day >= len(schedule) :
        global answer
        answer.append(Pi)
        return
    else :
        dfs(schedule, Pi, day + 1)
        T, P = schedule[day]
        if day + T <= len(schedule) : # 상담을 하는 경우
            dfs(schedule, Pi + P, day+T)

if __name__ == "__main__" :
    main()