import sys
from collections import deque
input = sys.stdin.readline

A, B = input().split()
opers = ['*', '+']
d = deque()

def BFS() :
    d.append([A, 0])
    
    while d :
        cur_A, cnt = d.popleft()
        if cur_A == B :
            print(cnt+1)
            break
        if int(cur_A) <= int(B) :
            for oper in opers :
                if oper == '*' :
                    temp = str(int(cur_A)*2)
                else :
                    temp = cur_A+"1"
                d.append([temp, cnt+1])

BFS()

if len(d) == 0 :
    print(-1)