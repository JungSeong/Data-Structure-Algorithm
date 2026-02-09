import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().rstrip()))
answer = []
cnt = 0

for i in range(len(nums)) :
    if i == 0 :
        answer.append(nums[i])
    else :
        while answer and cnt < K and answer[-1] < nums[i] :
            answer.pop()
            cnt += 1
        answer.append(nums[i])

if cnt < K :
    answer = answer[:N-K]

print(''.join(map(str, answer)))