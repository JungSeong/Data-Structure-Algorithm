import sys, heapq
input = sys.stdin.readline

N = int(input())
arr = []

for i in range(N) :
    l = list(map(int, input().split()))
    for j in l :
        heapq.heappush(arr, j)
        if len(arr)>N :
            heapq.heappop(arr)

print(heapq.heappop(arr))