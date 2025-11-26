import sys
input = sys.stdin.readline

N, M = map(int, input().split())
comb = []

def BFS(l, cur) :
    if l == M :
        print(' '.join(comb))
        return
    for i in range(cur, N+1) :
        comb.append(str(i))
        BFS(l+1, i+1)
        comb.pop()

BFS(0, 1)