import sys, math
input = sys.stdin.readline

K, N = map(int, input().split())
wires = []
for i in range(K) :
    wires.append(int(input()))

wires.sort()
min_len, max_len = 1, wires[-1]

while min_len <= max_len :
    mid = (max_len + min_len)//2
    cnt = 0
    for wire in wires :
        cnt += wire // mid
    if cnt >= N :
        min_len, max_len = mid+1, max_len
    else :
        min_len, max_len = min_len, mid-1

print(max_len)