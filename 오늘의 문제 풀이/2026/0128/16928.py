import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
ladder, snake = dict(), dict()
board = [-1]*101

for i in range(N) :
    u, v = map(int, input().split())
    ladder[u] = v

for i in range(M) :
    u, v = map(int, input().split())
    snake[u] = v

def BFS(cur) :
    dq = deque()
    dq.append(cur)
    board[cur] = 0

    while dq :
        cur = dq.popleft()
        if cur == 100 :
            print(board[cur])
            sys.exit(0)
        for i in range(1, 7) :
            new = cur + i
            if 1<=new<=100 :
                if new in ladder.keys() and board[ladder[new]] == -1 :
                    board[ladder[new]] = board[cur] + 1
                    dq.append(ladder[new])
                if new in snake.keys() and board[snake[new]] == -1 :
                    board[snake[new]] = board[cur] + 1
                    dq.append(snake[new])
                if new not in ladder.keys() and new not in snake.keys() and board[new] == -1 :
                    board[new] = board[cur] + 1
                    dq.append(new)

BFS(1)