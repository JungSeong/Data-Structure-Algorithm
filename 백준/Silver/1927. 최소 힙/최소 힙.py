import sys, heapq
input = sys.stdin.readline

N = int(input())
nums = []
answer = []
for i in range(N) :
    x = int(input())
    if x>=1 :
        heapq.heappush(nums, x)
    elif x == 0 :
        if len(nums) == 0 :
            print(0)
        else :
            n = heapq.heappop(nums)
            print(n)