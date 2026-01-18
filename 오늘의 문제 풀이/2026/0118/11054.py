# LIS : 왼쪽에서 오른쪽으로 가면서, 각 인덱스 $i$에서 끝나는 가장 긴 증가하는 부분 수열의 길이
# LDS : 오른쪽에서 왼쪽으로 오면서, 각 인덱스 $i$에서 시작하는 가장 긴 감소하는 부분 수열의 길이

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp_up = [1]*N
dp_down = [1]*N

for i in range(N) :
    for j in range(i) :
        if A[j] < A[i] :
            dp_up[i] = max(dp_up[j]+1, dp_up[i])

for i in range(N-1,-1,-1) :
    for j in range(N-1,i-1,-1) :
        if A[j] < A[i] :
            dp_down[i] = max(dp_down[j]+1, dp_down[i])

answer = 0

for i in range(N) :
    answer = max(answer, dp_up[i]+dp_down[i]-1)

print(answer)