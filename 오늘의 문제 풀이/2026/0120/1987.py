import sys
from collections import defaultdict
input = sys.stdin.readline

R, C = map(int, input().split())
m = list(list(input().rstrip()) for _ in range(R))
alphabets = defaultdict(bool)

for i in range(R) :
    for j in range(C) :
        alphabets[m[i][j]] = False

move = [(-1,0), (0,1), (1,0), (0,-1)]
answer = []
alphabets[m[0][0]] = True

def isOK(cur_r, cur_c) :
    coordinates = []
    for dr, dc in move :
        new_r, new_c = cur_r + dr, cur_c + dc
        if 0<=new_r<R and 0<=new_c<C :
            alpha = m[new_r][new_c]
            if not alphabets[alpha] :
                coordinates.append((new_r, new_c))
    if len(coordinates) > 0 :
        return True, coordinates
    else :
        return False, []

def DFS(cur_r, cur_c, cnt) :
    isPossible, coordinates = isOK(cur_r, cur_c)
    if not isPossible :
        answer.append(cnt)
        return
    else :
        for new_r, new_c in coordinates : 
            alpha = m[new_r][new_c]
            if not alphabets[alpha] :
                alphabets[alpha] = True
                DFS(new_r, new_c, cnt+1)
                alphabets[alpha] = False

DFS(0, 0, 1)
print(max(answer))