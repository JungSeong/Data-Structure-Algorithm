# 투포인터는 시간 복잡도가 O(N) 수준이다

import sys
input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))
sums = [0]*(len(nums)+1)

for i in range(1, len(nums)+1) :
    sums[i] = sums[i-1] + nums[i-1]

start, end = 0, 1
comp = sums[-1]-sums[0]
length = float('inf')

while start < end and end < len(sums) :
    if sums[end]-sums[start] < S :
        if end == len(sums)-1 and start == 0 :
            print(0)
            sys.exit(0)
        end += 1
    else :
        if end-start < length :
            length = end-start
        start += 1

print(length)