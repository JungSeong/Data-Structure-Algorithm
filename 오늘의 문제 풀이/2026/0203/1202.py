import sys
input = sys.stdin.readline

N, K = map(int, input().split())
jewel = []

for i in range(N) :
    M, V = map(int, input().split())
    jewel.append((M, V))

jewel.sort(key=lambda x : -x[0])
bags = []

for i in range(K) :
    w = int(input())
    bags.append(w)

bags.sort(reverse=True)

while True :
    if jewel[0][0] == 