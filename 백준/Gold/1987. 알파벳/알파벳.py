import sys
input = sys.stdin.readline

R, C = map(int, input().split())
m = list(list(input().rstrip()) for _ in range(R))
alphabets = set()
move = [(-1,0),(0,1),(1,0),(0,-1)]

for i in range(R) :
    for j in range(C) :
        alphabets.add(m[i][j])

def BFS() :
    q = set([(0, 0, m[0][0])])
    max_len = 0
    
    while q :
        cur_r, cur_c, cur_alphabets = q.pop()
        max_len = max(len(cur_alphabets), max_len)

        if max_len == len(alphabets) :
            return max_len
        
        for dr, dc in move :
            new_r, new_c = cur_r + dr, cur_c + dc
            if 0<=new_r<R and 0<=new_c<C :
                if m[new_r][new_c] not in cur_alphabets :
                    q.add((new_r, new_c, cur_alphabets + m[new_r][new_c]))

    return max_len

print(BFS())