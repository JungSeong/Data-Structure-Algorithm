# 방문한 칸의 수를 최대로
# 4 이상 -> 이동 방법을 모두 한 번씩은 사용 else -> 제약 X

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

if N == 1 :
    print(1)
elif N == 2 :
    if M < 9 :
        print(f"{(M+1)//2}")
    else :
        print(4)
else :
    if M < 5 :
        print(M)
    elif M == 5 or M == 6 :
        print(4)
    else :
        print(M-2)