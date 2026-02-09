import sys
input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int, input().split())))

start, end = 0, n-1
cnt = 0
x = int(input())

while start < end :
    cur = a[start] + a[end]
    if cur > x :
        end -= 1
    elif cur < x :
        start += 1
    else :
        cnt += 1
        start += 1

print(cnt)