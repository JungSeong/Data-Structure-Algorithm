import sys, heapq
input = sys.stdin.readline

N = int(input())
answer = []
min_heap, max_heap = [], []

for i in range(N) :
    num = int(input())
    if len(min_heap) <= len(max_heap) :
        heapq.heappush(min_heap, num)