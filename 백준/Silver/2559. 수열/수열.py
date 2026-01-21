import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))

cur_sum = sum(nums[:K])
answer = cur_sum

for i in range(N-K) :
    cur_sum += nums[i+K] - nums[i]
    answer = max(answer, cur_sum)

print(answer)