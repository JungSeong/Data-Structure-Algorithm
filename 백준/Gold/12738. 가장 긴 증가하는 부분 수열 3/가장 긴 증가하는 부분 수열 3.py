import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [-float('inf')]
 
for i in range(N) :
    if dp[-1] < A[i] :
        dp.append(A[i])
    else :
        idx = bisect_left(dp, A[i])
        dp[idx] = A[i]

print(len(dp)-1)