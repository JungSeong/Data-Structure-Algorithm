# 1<=N<=80

import sys
input = sys.stdin.readline

N = int(input())
answer = []

def isGood(num) :
    for i in range(1, len(num)//2+1) :
        if num[-i:] == num[-2*i:-i] :
            return False
    return True
    
def BackTracking(cur, num) :
    if cur == N :
        print(num)
        sys.exit(0)
    else :
        for i in range(1, 4) :
            if isGood(num+str(i)) :
                BackTracking(cur+1, num+str(i))

BackTracking(0, "")