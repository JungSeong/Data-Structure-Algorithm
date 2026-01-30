import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = []
record = []
 
for i in range(N) :
    if not dp or dp[-1] < A[i] :
        dp.append(A[i])
        record.append(len(dp)-1)
    else :
        idx = bisect_left(dp, A[i])
        dp[idx] = A[i]
        record.append(idx)

length = len(dp)
result = []
target_idx = length-1

for i in range(N-1, -1, -1) :
    if record[i] == target_idx :
        result.append(A[i])
        target_idx -= 1

print(len(dp))
print(*result[::-1])