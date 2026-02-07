import sys
from bisect import bisect_left # 시간 복잡도 O(logN) ~= 6정도 밖에 되지 않음
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [0]

for i in range(N) :
    if dp[-1] < A[i] :
        dp.append(A[i])
    else :
        idx = bisect_left(dp, A[i])
        dp[idx] = A[i]

print(len(dp)-1)