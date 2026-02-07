import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(list(map(int, input().split())) for _ in range(N))

M, K = map(int, input().split())
B = list(list(map(int, input().split())) for _ in range(M))
B_T = list(map(list, zip(*B)))

answer = []

for row in A :
    l = []
    for col in B_T :
        l.append(sum(map(lambda x,y : x*y, row, col)))
    answer.append(l)

for row in answer :
    print(*row)