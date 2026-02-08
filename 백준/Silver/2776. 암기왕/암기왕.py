import sys
from bisect import bisect_left
input = sys.stdin.readline

T = int(input())

for i in range(T) :
    N = int(input())
    paper1 = sorted(set(map(int, input().split())))
    M = int(input())
    paper2 = list(map(int, input().split()))

    for num in paper2 :
        idx = bisect_left(paper1, num)
        if not 0<=idx<len(paper1) :
            print(0)
        else :
            if paper1[idx] == num :
                print(1)
            else :
                print(0)