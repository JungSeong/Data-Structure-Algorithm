import sys
input = sys.stdin.readline

N = int(input())
answer = []

def Hanoi(N, start, inter, end) :
    if N == 1 :
        answer.append((start, end))
        return
    Hanoi(N-1, start, end, inter)
    answer.append((start, end))
    Hanoi(N-1, inter, start, end)

K = 2**N-1
if N <= 20 :
    Hanoi(N, 1, 2, 3)

print(K)
if N <= 20 :
    for elem in answer :
        print(*elem)