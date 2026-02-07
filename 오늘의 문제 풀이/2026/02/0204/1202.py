import sys, heapq
input = sys.stdin.readline

N, K = map(int, input().split())
jewels = []

for i in range(N) :
    M, V = map(int, input().split())
    jewels.append((M, V))

jewels.sort()
bags = []

for i in range(K) :
    C = int(input())
    bags.append(C)

bags.sort()
possible = []
answer = [0]*len(bags)

for i in range(len(bags)) :
    while jewels and jewels[0][0] <= bags[i] :
        val = heapq.heappop(jewels)
        heapq.heappush(possible, -val[1])
    if possible :
        answer[i] = -heapq.heappop(possible)

print(sum(answer))