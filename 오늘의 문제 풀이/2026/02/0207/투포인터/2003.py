import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

sums = [0]*(len(A)+1)
start, end = 0, 1
cnt = 0

for i in range(1, len(sums)) :
    sums[i] = sums[i-1] + A[i-1]

while start <= end and end < len(sums):
    if sums[end]-sums[start] < M :
        end += 1
    elif sums[end]-sums[start] == M :
        cnt += 1
        start += 1
    else :
        start += 1

print(cnt)