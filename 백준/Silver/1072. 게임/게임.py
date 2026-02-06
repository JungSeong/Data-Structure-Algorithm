import sys
input = sys.stdin.readline

X, Y = map(int, input().split())
possible = range(1, 1000000001)
Z = 100*Y//X
answer = -1

if possible and Z<99 :
    start, end = possible[0], possible[-1]
    while start<=end :
        mid = (start+end)//2
        if (100*(Y+mid))//(X+mid) == Z :
            start = mid+1
        else :
            answer = mid
            end = mid-1

print(answer)