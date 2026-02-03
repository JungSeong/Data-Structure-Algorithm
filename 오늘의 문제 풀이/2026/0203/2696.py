import sys, heapq, math
input = sys.stdin.readline

T = int(input())

for i in range(T) :
    cnt = 0
    answer = []

    M = int(input())
    if M%2 != 0 :
        cnt = M//2+1
    else :
        cnt = M//2

    max_heap, min_heap = [], []
    length = 0

    for i in range(M//10+1) :
        l = list(map(int, input().split()))
        for j in l :
            length += 1
            if len(max_heap) == len(min_heap) :
                heapq.heappush(max_heap, -j)
            else :
                heapq.heappush(min_heap, j)
            if len(min_heap) > 0 and -max_heap[0] > min_heap[0] :
                max_num, min_num = -heapq.heappop(max_heap), heapq.heappop(min_heap)
                heapq.heappush(max_heap, -min_num)
                heapq.heappush(min_heap, max_num)
            if length % 2 == 1 :
                answer.append(-max_heap[0])
    
    print(cnt)
    for i in range(math.ceil(len(answer)/10)) :
        print(*answer[i*10:i*10+10])