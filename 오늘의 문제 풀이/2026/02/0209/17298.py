import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
s = []
answer = [-1]*len(A)

for i in range(len(A)) :
    while s and  A[s[-1]] < A[i] :
        answer[s[-1]] = A[i]
        s.pop()
    s.append(i) 

print(' '.join(map(str, answer)))