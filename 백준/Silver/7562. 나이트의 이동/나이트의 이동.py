import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
move = [[-2,1], [-2,-1], [-1,2], [1,2], [2,1], [2,-1], [-1,-2], [1,-2]]

def BFS(r, c) :
    q = deque()
    q.append([r, c])

    while q :
        cur_r, cur_c = q.popleft()
        if cur_r == goal_r and cur_c == goal_c:
            print(m[cur_r][cur_c])
            break
        for row in move :
            new_r, new_c = cur_r+row[0], cur_c+row[1]
            if 0<=new_r<l and 0<=new_c<l and m[new_r][new_c] == 0 :
                m[new_r][new_c] = m[cur_r][cur_c] + 1
                q.append([new_r,new_c])

for i in range(N) :
    l = int(input())
    m = [[0] * l for _ in range(l)]
    cur_r, cur_c = map(int, input().split())
    goal_r, goal_c = map(int, input().split())

    BFS(cur_r, cur_c)