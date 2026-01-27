import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
l = list(map(int, input().split()))
A.sort()

for num in l :
    idx = bisect_left(A, num)
    if 0<=idx<=N-1 :
        if A[idx] == num :
            print(1)
        else :
            print(0)
    else :
        print(0)