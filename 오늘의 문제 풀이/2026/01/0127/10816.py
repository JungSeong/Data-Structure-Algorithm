import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
cards.sort()
M = int(input())
myCards = list(map(int, input().split()))
answer = []

for card in myCards :
    l_idx, r_idx = bisect_left(cards, card), bisect_right(cards, card)
    answer.append(r_idx-l_idx)

print(*answer)