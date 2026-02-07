import sys, heapq
input = sys.stdin.readline

N = int(input())
cards = []
answer = 0

for i in range(N) :
    cnt = int(input())
    heapq.heappush(cards, cnt)

while len(cards) >= 2 :
    card_1, card_2 = heapq.heappop(cards), heapq.heappop(cards)
    answer += card_1 + card_2
    heapq.heappush(cards, card_1+card_2)

print(answer)