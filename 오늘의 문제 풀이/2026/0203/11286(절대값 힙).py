import sys, heapq
input = sys.stdin.readline

N = int(input())
arr = []
answer = []

for i in range(N) :
    x = int(input())
    if x != 0 :
        if x > 0 :
            heapq.heappush(arr, (x, 'p'))
        else :
            heapq.heappush(arr, (-x, 'm'))
    else :
        if len(arr) == 0 :
            answer.append(0)
        else :
            elem = heapq.heappop(arr)
            if elem[1] == 'm' :
                answer.append(-elem[0])
            else :
                answer.append(elem[0])

for row in answer :
    print(row)