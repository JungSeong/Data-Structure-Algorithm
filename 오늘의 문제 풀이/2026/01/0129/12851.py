import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
move = ["jump", "teleport"]
m = [-1]*100001
cnt = 0
arrived = False

def BFS(N) :
    dq = deque()
    dq.append(N)
    m[N] = 0

    while dq :
        cur = dq.popleft()
        if cur == K :
            arrived = True
        for row in move :
            if row == "jump" :
                new = cur * 2
                if 0<=new<len(m) and m[new] == -1 :
                    m[new] = m[cur] + 1
                    dq.append(new)
            else :
                new1, new2 = cur-1, cur+1
                if 0<=new1<len(m) and m[new1] == -1 :
                    m[new1] = m[cur] + 1
                    dq.append(new1)
                if 0<=new2<len(m) and m[new2] == -1 :
                    m[new2] = m[cur] + 1
                    dq.append(new2)

BFS(N)
print(m[K])
print(cnt)